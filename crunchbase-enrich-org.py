
# ---
# name: crunchbase-enrich-org
# deployed: true
# title: Crunchbase Organization Enrichment
# description: Return information about an organization based on domain name.
# params:
#   - name: domain
#     type: string
#     description: The domain name of the organization from which you want to retrieve information. For example, "apple.com". If no domain is specified, the function returns the properties names.
#     required: true
#   - name: properties
#     type: array
#     description: The properties to return (defaults to all properties). See "Returns" for a listing of the available properties.
#     required: false
# returns:
#   - name: permalink
#     type: string
#     description: The Crunchbase permalink identifier for the organization
#   - name: name
#     type: string
#     description: The name of the organization
#   - name: stock_exchange
#     type: string
#     description: The stock exchange for the organization
#   - name: stock_symbol
#     type: string
#     description: The stock ticker for the organization
#   - name: primary_role
#     type: string
#     description: The primary role of the organization
#   - name: short_description
#     type: string
#     description: A short description of the organization
#   - name: profile_image_url
#     type: string
#     description: A profile image URL for the organization
#   - name: domain
#     type: string
#     description: The domain for the organization
#   - name: homepage_url
#     type: string
#     description: The homepage URL for the organization
#   - name: facebook_url
#     type: string
#     description: The Facebook URL for the organization
#   - name: twitter_url
#     type: string
#     description: The Twitter URL for the organization
#   - name: linkedin_url
#     type: string
#     description: The LinkedIn URL for the organization
#   - name: city_name
#     type: string
#     description: The city name for the organization
#   - name: region_name
#     type: string
#     description: The region name for the organization
#   - name: country_code
#     type: string
#     description: The country code for the organization
#   - name: rank
#     type: string
#     description: The Crunchbase organization rank
#   - name: contact_email
#     type: string
#     description: The contact email for the organization
#   - name: phone_number
#     type: string
#     description: The phone number for the organization
#   - name: founded_on
#     type: string
#     description: The date the organization was founded on
#   - name: total_funding_usd
#     type: string
#     description: The total funding dollars for the organization in USD
#   - name: number_of_investments
#     type: string
#     description: The number of investments made in the organization
#   - name: num_employees_min
#     type: string
#     description: The minimum number of employees in the organization
#   - name: num_employees_max
#     type: string
#     description: The maximum number of employees in the organization
#   - name: role_company
#     type: string
#     description: Whether or not the organization is a company
#   - name: role_investor
#     type: string
#     description: Whether or not the organization is an investor
#   - name: role_group
#     type: string
#     description: Whether or not the organization is a group
#   - name: role_school
#     type: string
#     description: Whether or not the organization is a school
#   - name: investor_type
#     type: string
#     description: The investor type
#   - name: founded_on_trust_code
#     type: string
#     description: The founded_on trust code
#   - name: is_closed
#     type: string
#     description: Whether or not the organization is closed
#   - name: closed_on
#     type: string
#     description: The date the organization closed, if applicable
#   - name: closed_on_trust_code
#     type: string
#     description: The closed-on trust code
# examples:
#   - '"spacex.com"'
#   - '"apple.com"'
#   - '"https://www.apple.com"'
#   - '"apple.com", "permalink, name, short_description, founded_on"'
#   - '"apple.com", "short_description, region_name, founded_on, num_employees_min, num_employees_max, contact_email, linkedin_url"'
#   - '"", "*"'
# ---

import json
import requests
import urllib
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
    params['properties'] = {'required': False, 'validator': validator_list, 'coerce': to_list, 'default': '*'}
    input = dict(zip(params.keys(), input))

    # validate the mapped input against the validator
    v = Validator(params, allow_unknown = True)
    input = v.validated(input)
    if input is None:
        raise ValueError

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
    property_map['domain'] = 'domain'
    property_map['homepage_url'] = 'homepage_url'
    property_map['facebook_url'] = 'facebook_url'
    property_map['twitter_url'] = 'twitter_url'
    property_map['linkedin_url'] = 'linkedin_url'
    property_map['city_name'] = 'city_name'
    property_map['region_name'] = 'region_name'
    property_map['country_code'] = 'country_code'

    # additional properties from secondary api call
    property_map['rank'] = 'rank'
    property_map['contact_email'] = 'contact_email'
    property_map['phone_number'] = 'phone_number'
    property_map['founded_on'] = 'founded_on'
    property_map['total_funding_usd'] = 'total_funding_usd'
    property_map['number_of_investments'] = 'number_of_investments'
    property_map['num_employees_min'] = 'num_employees_min'
    property_map['num_employees_max'] = 'num_employees_max'
    property_map['role_company'] = 'role_company'
    property_map['role_investor'] = 'role_investor'
    property_map['role_group'] = 'role_group'
    property_map['role_school'] = 'role_school'
    property_map['investor_type'] = 'investor_type'
    property_map['founded_on_trust_code'] = 'founded_on_trust_code'
    property_map['is_closed'] = 'is_closed'
    property_map['closed_on'] = 'closed_on'
    property_map['closed_on_trust_code'] = 'closed_on_trust_code'

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
        response = requests.get(url)
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
        url_query_params = {'user_key': auth_token}
        url_query_str = urllib.parse.urlencode(url_query_params)

        url = 'https://api.crunchbase.com/v3.1/organizations/' + organization_permalink + '/?' + url_query_str
        response = requests.get(url)
        response.raise_for_status()
        content = response.json()
        organization_information_additional = content.get('data',{}).get('properties')

        # merge the organization information and return the information for this item
        organization_information = {**organization_information_base, **organization_information_additional}
        result = [[organization_information.get(property_map.get(p,''),'') or '' for p in properties]]
        result = json.dumps(result, default=to_string)
        flex.output.content_type = 'application/json'
        flex.output.write(result)

    except:
        flex.output.content_type = 'application/json'
        flex.output.write([['']])

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
