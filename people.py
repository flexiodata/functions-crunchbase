
# ---
# name: cb-people
# deployed: true
# title: Crunchbase People
# description: Returns information about people satisfying a search term
# params:
# - name: query
#   type: string
#   description: Query string to use when searching for people
#   required: true
# examples:
# - '"Steve Jobs"'
# - '"Bill Gates"'
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
    url = 'https://api.crunchbase.com/v3.1/people'
    url += '?user_key=' + auth_token
    url += '&query=' + query

    response = requests.get(url)
    content = response.json()

    items = content.get('data',{}).get('items')
    columns = [
        'permalink','first_name','last_name','gender',
        'title','organization_permalink','profile_image_url',
        'homepage_url','facebook_url','twitter_url','linkedin_url',
        'city_name','region_name','country_code'
    ]

    result = []
    result.append(columns)

    for i in items:
        props = []
        for c in columns:
            props.append(i.get('properties').get(c,''))
        result.append(props)

    flex.output.content_type = 'application/json'
    flex.output.write(result)

