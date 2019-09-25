
# ---
# name: cb-organizations
# deployed: true
# title: Crunchbase Organizations
# description: Returns information about organizations satisfying a search term
# params:
# - name: query
#   type: string
#   description: Query string to use when searching for organizations
#   required: true
# examples:
# - '"Crunchbase"'
# - '"SpaceX"'
# notes: |-
#   See https://www.crunchbase.com/ for more information
# ---


import json
import requests
from cerberus import Validator
from collections import OrderedDict

CONST_CRUNCHBASE_API_CONNECTION_NAME = '' # TODO: fill out

def flex_handler(flex):

    # get the authorization token
    auth_token = flex.connections[CONST_CRUNCHBASE_API_CONNECTION_NAME].description

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
    params['query'] = {'required': True, 'type': 'string'}
    input = dict(zip(params.keys(), input))

    # validate the mapped input against the validator
    v = Validator(params, allow_unknown = True)
    input = v.validated(input)
    if input is None:
        raise ValueError

    query = input['query']

    # api reference: https://data.crunchbase.com/reference
    url = 'https://api.crunchbase.com/v3.1/organizations'
    url += '?user_key=' + auth_token
    url += '&query=' + query

    response = requests.get(url)
    content = response.json()

    items = content.get('data',{}).get('items')

    result = []
    for i in items:
        p = i.get('properties')

        props = OrderedDict()
        props['permalink'] = p.get('permalink','')
        props['name'] = p.get('name','')
        props['stock_exchange'] = p.get('stock_exchange','')
        props['stock_symbol'] = p.get('stock_symbol','')
        props['primary_role'] = p.get('primary_role','')
        props['short_description'] = p.get('short_description','')
        props['profile_image_url'] = p.get('profile_image_url','')
        props['domain'] = p.get('domain','')
        props['homepage_url'] = p.get('homepage_url','')
        props['facebook_url'] = p.get('facebook_url','')
        props['twitter_url'] = p.get('twitter_url','')
        props['linkedin_url'] = p.get('linkedin_url','')
        props['city_name'] = p.get('city_name','')
        props['region_name'] = p.get('region_name','')
        props['country_code'] = p.get('country_code','')

        result.append(props)

    flex.output.content_type = 'application/json'
    flex.output.write(content)

