
# ---
# name: crunchbase-list-people
# deployed: true
# title: Crunchbase People Search
# description: Returns a list of people profiles that match a search term.
# params:
#   - name: search
#     type: string
#     description: Search string for the person's name.
#     required: true
#   - name: properties
#     type: array
#     description: The properties to return (defaults to all properties). See "Returns" for a listing of the available properties.
#     required: false
# returns:
#   - name: permalink
#     type: string
#     description: The Crunchbase permalink identifier for the person
#   - name: first_name
#     type: string
#     description: The first name of the person
#   - name: last_name
#     type: string
#     description: The last name of the person
#   - name: gender
#     type: string
#     description: The gender of the person
#   - name: title
#     type: string
#     description: The title of the person
#   - name: organization_permalink
#     type: string
#     description: The Crunchbase permalink identifier of the organization of which the person is a member
#   - name: profile_image_url
#     type: string
#     description: The profile image for the person
#   - name: homepage_url
#     type: string
#     description: The homepage URL for the person
#   - name: facebook_url
#     type: string
#     description: The Facebook URL for the person
#   - name: twitter_url
#     type: string
#     description: The Twitter URL for the person
#   - name: linkedin_url
#     type: string
#     description: The LinkedIn URL for the person
#   - name: city_name
#     type: string
#     description: The city name where the person is located
#   - name: region_name
#     type: string
#     description: The region name where the person is located
#   - name: country_code
#     type: string
#     description: The country code where the person is located
# examples:
#   - '"Steve Jobs"'
#   - '"Bill Gates"'
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
    params['name'] = {'required': True, 'type': 'string'}
    params['properties'] = {'required': False, 'validator': validator_list, 'coerce': to_list, 'default': '*'}
    input = dict(zip(params.keys(), input))

    # validate the mapped input against the validator
    v = Validator(params, allow_unknown = True)
    input = v.validated(input)
    if input is None:
        raise ValueError

    # map this function's property names to the API's property names
    property_map = OrderedDict()
    property_map['permalink'] = 'permalink'
    property_map['first_name'] = 'first_name'
    property_map['last_name'] = 'last_name'
    property_map['gender'] = 'gender'
    property_map['title'] = 'title'
    property_map['organization_permalink'] = 'organization_permalink'
    property_map['profile_image_url'] = 'profile_image_url'
    property_map['homepage_url'] = 'homepage_url'
    property_map['facebook_url'] = 'facebook_url'
    property_map['twitter_url'] = 'twitter_url'
    property_map['linkedin_url'] = 'linkedin_url'
    property_map['city_name'] = 'city_name'
    property_map['region_name'] = 'region_name'
    property_map['country_code'] = 'country_code'

    # make the api request
    # see here for more info: https://data.crunchbase.com/reference
    url_query_params = {'user_key': auth_token, 'name': input['name']}
    url_query_str = urllib.parse.urlencode(url_query_params)

    url = 'https://api.crunchbase.com/v3.1/people?' + url_query_str
    response = requests.get(url)
    content = response.json()

    # get the properties to return and the property map
    properties = [p.lower().strip() for p in input['properties']]

    # if we have a wildcard, get all the properties
    if len(properties) == 1 and properties[0] == '*':
        properties = list(property_map.keys())

    # build up the result
    result = []

    result.append(properties)
    items = content.get('data',{}).get('items')
    for person in items:
        row = [person.get('properties',{}).get(property_map.get(p,''),'') or '' for p in properties]
        result.append(row)

    result = json.dumps(result, default=to_string)
    flex.output.content_type = "application/json"
    flex.output.write(result)

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
