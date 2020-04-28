
# ---
# name: crunchbase-lead-investor
# deployed: true
# title: Crunchbase Lead Investor
# description: Returns information about the lead investor for a company for a particular round
# params:
#   - name: domain
#     type: string
#     description: The domain name of the organization for which you want to retrieve information. For example, "google.com". If no domain is specified, the function returns the properties names.
#     required: true
#   - name: round
#     type: string
#     description: The type of round to find the lead investor for; options include "Seed", "Angel", "Venture", "A", "B", etc. and are case-insensitive.
#     required: true
#   - name: properties
#     type: array
#     description: The properties to return (defaults to all properties). See "Returns" for a listing of the available properties.
#     required: false
# returns:
#   - name: permalink
#     type: string
#     description: The Crunchbase permalink identifier for the investor
#   - name: name
#     type: string
#     description: The name of the investor
#   - name: stock_exchange
#     type: string
#     description: The stock exchange for the investor
#   - name: stock_symbol
#     type: string
#     description: The stock ticker for the investor
#   - name: primary_role
#     type: string
#     description: The primary role of the investor
#   - name: short_description
#     type: string
#     description: A short description of the investor
#   - name: profile_image_url
#     type: string
#     description: The profile image URL for the investor
#   - name: homepage_url
#     type: string
#     description: The homepage URL for the investor
#   - name: funding_type
#     type: string
#     description: The funding type
#   - name: series
#     type: string
#     description: The series type
#   - name: series_qualifier
#     type: string
#     description: The series type qualifier
#   - name: announced_on
#     type: string
#     description: The date the investment was announced
#   - name: money_raised
#     type: string
#     description: The total amount raised in the funding round
#   - name: money_raised_currency_code
#     type: string
#     description: The currency of the total amount raised in the funding round
# examples:
#   - '"spacex.com", "venture"'
#   - '"g2.com", "angel"'
#   - '"g2.com", "A"'
#   - '"g2.com", "B", "name, announced_on, money_raised"'
#   - '"", "", "*"'
# ---

import json
import urllib
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import itertools
from datetime import *
from cerberus import Validator
from collections import OrderedDict

def flex_handler(flex):

    # get the api key from the variable input
    auth_token = dict(flex.vars).get('crunchbase_api_key')
    if auth_token is None:
        flex.output.content_type = "application/json"
        flex.output.write([[""]])
        return

    # get the input
    input = flex.input.read()
    try:
        input = json.loads(input)
        if not isinstance(input, list): raise ValueError
    except ValueError:
        raise ValueError

    # define the expected parameters and map the values to the parameter names
    # based on the positions of the keys/values
    params = OrderedDict()
    params['domain'] = {'required': True, 'type': 'string'}
    params['round'] = {'required': True, 'type': 'string'}
    params['properties'] = {'required': False, 'validator': validator_list, 'coerce': to_list, 'default': '*'}
    input = dict(zip(params.keys(), input))

    # validate the mapped input against the validator
    v = Validator(params, allow_unknown = True)
    input = v.validated(input)
    if input is None:
        raise ValueError

    # get the round to return information for
    funding_round_requested = input['round'].lower().strip()

    # map this function's property names to the API's property names
    property_map = OrderedDict()

    # primary properties from first api call
    property_map['permalink'] = 'permalink'
    property_map['name'] = 'name'
    property_map['stock_exchange'] = 'stock_exchange'
    property_map['stock_symbol'] = 'stock_symbol'
    property_map['primary_role'] = 'primary_role'
    property_map['short_description'] = 'short_description'
    property_map['profile_image_url'] = 'profile_image_url'
    property_map['homepage_url'] = 'homepage_url'
    property_map['funding_type'] = 'funding_type'
    property_map['series'] = 'series'
    property_map['series_qualifier'] = 'series_qualifier'
    property_map['announced_on'] = 'announced_on'
    property_map['money_raised'] = 'money_raised'
    property_map['money_raised_currency_code'] = 'money_raised_currency_code'

    # get the properties to return and the property map
    properties = [p.lower().strip() for p in input['properties']]

    # if we have a wildcard, get all the properties
    if len(properties) == 1 and properties[0] == '*':
        properties = list(property_map.keys())

    try:

        # see here for more info about using the api:
        # https://data.crunchbase.com/reference
        # https://data.crunchbase.com/docs/organization

        search_domain = input['domain'].lower().strip().strip("/")

        # if no domain is specified, echo the properties
        if search_domain == '':
            flex.output.content_type = 'application/json'
            flex.output.write([properties])
            return

        # trim off leading https://www, etc
        search_domain = search_domain.replace('https://www.', '')
        search_domain = search_domain.replace('http://www.', '')
        search_domain = search_domain.replace('https://', '')
        search_domain = search_domain.replace('http://', '')
        search_domain = search_domain.replace('www.', '')

        # make the initial api request to get
        url_query_params = {'user_key': auth_token, 'domain_name': search_domain}
        url_query_str = urllib.parse.urlencode(url_query_params)

        url = 'https://api.crunchbase.com/v3.1/organizations?' + url_query_str
        response = requests_retry_session().get(url)
        response.raise_for_status()
        content = response.json()

        organization_information_base = {}
        organization_permalink = None

        # get the permalink for the item that matches the domain
        items = content.get('data',{}).get('items')
        for organization in items:
            item_properties = organization.get('properties',{})
            item_domain = item_properties.get('domain','').lower().strip().strip("/")
            if item_domain == search_domain:
                organization_information_base = item_properties
                organization_permalink = item_properties.get('permalink','')
                break

        # if we didn't find an organization, fall through to empty result
        if organization_permalink is None:
            raise ValueError('Unable to find domain')

        # using the permalink, get additional information about the company
        url_query_params = {'user_key': auth_token, 'sort_order': 'announced_on'}
        url_query_str = urllib.parse.urlencode(url_query_params)

        url = 'https://api.crunchbase.com/v3.1/organizations/' + organization_permalink + '/funding_rounds?' + url_query_str
        response = requests_retry_session().get(url)
        response.raise_for_status()
        content = response.json()

        # funding rounds are sorted in ascending order; iterate over the investors for all
        # the funding rounds until we find the first lead investor; then return the information
        investment_info = {}
        is_lead_investor = False
        items = content.get('data',{}).get('items')

        for funding_round in items:

            # see if the requested funding type matchees; if not, move on
            funding_type = funding_round.get('properties',{}).get('funding_type','') or ''
            funding_series = funding_round.get('properties',{}).get('series','') or ''
            funding_type = funding_type.lower().strip()
            funding_series = funding_series.lower().strip()

            funding_round_requested_valid = False
            if funding_type == 'angel' and funding_round_requested == funding_type:
                funding_round_requested_valid = True
            if funding_type == 'seed' and funding_round_requested == funding_type:
                funding_round_requested_valid = True
            if funding_type == 'venture' and funding_round_requested == funding_type and funding_series == '':
                funding_round_requested_valid = True
            if funding_type == 'venture' and funding_round_requested == funding_series:
                funding_round_requested_valid = True

            if funding_round_requested_valid is False:
                continue

            # we're have the requested funding round; populate the funding information and find the lead investor if available
            investment_info['funding_type'] = funding_round.get('properties').get('funding_type')
            investment_info['series'] = funding_round.get('properties').get('series')
            investment_info['series_qualifier'] = funding_round.get('properties').get('series_qualifier')
            investment_info['announced_on'] = funding_round.get('properties').get('announced_on')
            investment_info['money_raised'] = funding_round.get('properties').get('money_raised')
            investment_info['money_raised_currency_code'] = funding_round.get('properties').get('money_raised_currency_code')

            investments = funding_round.get('relationships',{}).get('investments',[])
            for i in investments:

                # if we have only one investor, they're the lead investor; if we have multiple
                # investors, find the first investor listed as the lead investor and merge
                # the information into the investment_info
                is_lead_investor = len(investments) == 1 or i.get('properties',{}).get('is_lead_investor',False)
                if is_lead_investor is True:
                    investor_info = i.get('relationships',{}).get('investors',{}).get('properties',{})
                    investment_info = {**investment_info, **investor_info}
                    break

            # the requested round matches, so we're done
            break

        result = [[investment_info.get(property_map.get(p,''),'') or '' for p in properties]]
        result = json.dumps(result, default=to_string)
        flex.output.content_type = 'application/json'
        flex.output.write(result)

    except:
        flex.output.content_type = 'application/json'
        flex.output.write([['']])

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def validator_list(field, value, error):
    if isinstance(value, str):
        return
    if isinstance(value, list):
        for item in value:
            if not isinstance(item, str):
                error(field, 'Must be a list with only string values')
        return
    error(field, 'Must be a string or a list of strings')

def to_string(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, (Decimal)):
        return str(value)
    return value

def to_list(value):
    # if we have a list of strings, create a list from them; if we have
    # a list of lists, flatten it into a single list of strings
    if isinstance(value, str):
        return value.split(",")
    if isinstance(value, list):
        return list(itertools.chain.from_iterable(value))
    return None
