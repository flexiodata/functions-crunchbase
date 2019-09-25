
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

    flex.output.content_type = 'application/json'
    flex.output.write(content)

