
# ---
# name: crunchbase-search-org
# deployed: true
# title: Crunchbase Organization Enrichment
# description: Returns profile information based on an organization's name
# params:
#   - name: name
#     type: string
#     description: The name of the organization
#     required: true
# examples:
#   - '"Crunchbase"'
#   - '"SpaceX"'
# notes: |
#   See https://www.crunchbase.com/ for more information
# ---


import json
import requests
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
    input = dict(zip(params.keys(), input))

    # validate the mapped input against the validator
    v = Validator(params, allow_unknown = True)
    input = v.validated(input)
    if input is None:
        raise ValueError

    query = input['name']

    # api reference: https://data.crunchbase.com/reference
    url = 'https://api.crunchbase.com/v3.1/organizations'
    url += '?user_key=' + auth_token
    url += '&query=' + query

    response = requests.get(url)
    content = response.json()

    items = content.get('data',{}).get('items')
    columns = [
        'permalink','name','stock_exchange','stock_symbol',
        'primary_role','short_description','profile_image_url',
        'domain','homepage_url','facebook_url','twitter_url',
        'linkedin_url','city_name','region_name','country_code'
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

