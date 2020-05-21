
# ---
# name: crunchbase-people
# deployed: true
# config: index
# title: Crunchbase People
# description: Returns a list of people from Crunchbase
# params:
#   - name: properties
#     type: array
#     description: The properties to return, given as a string or array; defaults to all properties; see "Returns" for available properties
#     required: false
#   - name: filter
#     type: array
#     description: Search query to determine the rows to return, given as a string or array
#     required: false
# returns:
#   - name: uuid
#     type: string
#     description: The UUID for the person
#   - name: permalink
#     type: string
#     description: The permalink of the person
#   - name: name
#     type: string
#     description: The full name of the person
#   - name: first_name
#     type: string
#     description: The first name of the person
#   - name: middle_name
#     type: string
#     description: The middle name of the person
#   - name: last_name
#     type: string
#     description: The last name of the person
#   - name: gender
#     type: string
#     description: The gender of the person
#   - name: primary_job_title
#     type: string
#     description: The primary job title for the person
#   - name: primary_organization_uuid
#     type: string
#     description: The UUID of the organization associated with the primary job for the person
#   - name: primary_organization_permalink
#     type: string
#     description: The permalink of the organization associated with the primary job for the person
#   - name: primary_organization_name
#     type: string
#     description: The name of the organization associated with the primary job for the person
#   - name: created_at
#     type: string
#     description: The date the person was created in the system
#   - name: updated_at
#     type: string
#     description: The date the information for the person was last updated in the system
#   - name: facet_ids
#     type: string
#     description: A delimited list of facet ids for the person
#   - name: short_description
#     type: string
#     description: A short description of the person
#   - name: description
#     type: string
#     description: A description of the person
#   - name: permalink_aliases
#     type: string
#     description: A delimited list of alternate permalinks for the person
#   - name: aliases
#     type: string
#     description: A delimited list of alternate names for the person
#   - name: location_group_names
#     type: string
#     description: A delimited list of the names of the areas where the person is located
#   - name: location_names
#     type: string
#     description: A delimited list of the names of the places where the person is located
#   - name: image_url
#     type: string
#     description: The cloudinary url of the profile image
#   - name: website_url
#     type: string
#     description: Link to the homepage for the person
#   - name: linkedin_url
#     type: string
#     description: Link to the LinkedIn page for the person
#   - name: facebook_url
#     type: string
#     description: Link to the Facebook page for the person
#   - name: twitter_url
#     type: string
#     description: Link to the Twitter page for the person
#   - name: born_on
#     type: string
#     description: The date the person was born
#   - name: died_on
#     type: string
#     description: The date the person died
#   - name: rank
#     type: integer
#     description: Algorithmic rank assigned to the top 100,000 most active profiles on Crunchbase
#   - name: rank_delta_d7
#     type: integer
#     description: Movement in rank over the last 7 days using a score from -10 to 10
#   - name: rank_delta_d30
#     type: integer
#     description: Movement in rank over the last 30 days using a score from -10 to 10
#   - name: rank_delta_d90
#     type: integer
#     description: Movement in rank over the last 90 days using a score from -10 to 10
#   - name: rank_person
#     type: integer
#     description: Algorithmic rank assigned to the top 100,000 most active people
#   - name: rank_principal
#     type: integer
#     description: Algorithmic rank assigned to the top 100,000 most active organizations and people
#   - name: rank_principal_investor
#     type: integer
#     description: Algorithmic rank assigned to the top 100,000 most active investors
#   - name: num_articles
#     type: integer
#     description: The number of news articles that reference the person
#   - name: num_current_advisor_jobs
#     type: integer
#     description: Total number of current advisors and board roles the person has
#   - name: num_current_positions
#     type: integer
#     description: Total number of current Jobs the person has
#   - name: num_event_appearances
#     type: integer
#     description: Total number of events a person appeared in
#   - name: num_exits
#     type: integer
#     description: Total number of exits
#   - name: num_exits_ipo
#     type: integer
#     description: Total number of exits (IPO)
#   - name: num_founded_organizations
#     type: integer
#     description: Number of organizations that the person founded
#   - name: num_investments
#     type: integer
#     description: Number of investments the person has participated in
#   - name: num_investments_funding_rounds
#     type: integer
#     description: Total number of investment funding rounds
#   - name: num_jobs
#     type: integer
#     description: Total number of jobs the person has
#   - name: num_lead_investments
#     type: integer
#     description: Total number of lead investments made
#   - name: num_partner_investments
#     type: integer
#     description: Total number of investments the person has partnered in
#   - name: num_past_advisor_jobs
#     type: integer
#     description: Total number of past board and advisor roles the person has
#   - name: num_past_jobs
#     type: integer
#     description: Total number of past jobs the person has
#   - name: num_portfolio_organizations
#     type: integer
#     description: Total number of portfolio companies associated to the person
#   - name: num_relationships
#     type: integer
#     description: Total number of relationships a profile has
#   - name: investor_type
#     type: string
#     description: A delimited list of the type of investors this person is
#   - name: investor_stage
#     type: string
#     description: A delimited list of the stage of investments made by this person
# examples:
#   - '"*"'
# ---

import json
import urllib
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from collections import OrderedDict

# main function entry point
def flexio_handler(flex):

    flex.vars['crunchbase_api_key'] = flex.connections['crunchbase-api-key'].get_credentials().get('api_key')

    flex.output.content_type = 'application/x-ndjson'
    for data in get_data(flex.vars):
        flex.output.write(data)

def get_data(params):

    # get the api key from the variable input
    auth_token = dict(params).get('crunchbase_api_key')
    if auth_token is None:
        raise ValueError

    # see here for more info:
    # https://data.crunchbase.com/docs/using-the-api
    # https://data.crunchbase.com/docs/using-search-apis
    # https://app.swaggerhub.com/apis-docs/Crunchbase/crunchbase-enterprise_api/1.0.1#/Search/post_searches_people

    query = {
        "field_ids": get_available_properties(),
        "limit": 1000 # page size
    }
    headers = {
        'Content-Type': 'application/json'
    }
    url = 'https://api.crunchbase.com/api/v4/searches/people'

    page_idx = 1
    max_pages = 5 # TODO: temporariliy limit number of pages; set to large value to get all pages
    while True:

        url_query_params = {'user_key': auth_token}
        url_query_str = urllib.parse.urlencode(url_query_params)

        page_url = url + '?' + url_query_str
        response = requests_retry_session().post(page_url, data=json.dumps(query), headers=headers)
        response.raise_for_status()
        content = response.json()

        data = content.get('entities')
        if data is None:
            break
        if len(data) == 0:
            break

        after_id = None
        buffer = ''
        for item in data:
            item = get_item_info(item.get('properties',{}))
            buffer = buffer + json.dumps(item, default=to_string) + "\n"
            after_id = item.get('uuid')
        yield buffer

        if after_id is None:
            break

        # get the next page of data
        query['after_id'] = after_id
        page_idx = page_idx + 1

        if page_idx > max_pages:
            break

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

def to_date(value):
    return value

def to_string(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, (Decimal)):
        return str(value)
    return value

def get_item_info(item):

    info = OrderedDict()

    info['uuid'] = item.get('uuid')
    info['permalink'] = item.get('permalink')
    info['name'] = item.get('name')
    info['first_name'] = item.get('first_name')
    info['middle_name'] = item.get('middle_name')
    info['last_name'] = item.get('last_name')
    info['gender'] = item.get('gender')
    info['primary_job_title'] = item.get('primary_job_title')
    info['primary_organization_uuid'] = item.get('primary_organization',{}).get('uuid')
    info['primary_organization_permalink'] = item.get('primary_organization',{}).get('permalink')
    info['primary_organization_name'] = item.get('primary_organization',{}).get('value')
    info['created_at'] = to_date(item.get('created_at'))
    info['updated_at'] = to_date(item.get('updated_at'))
    info['facet_ids'] = ", ".join(item.get('facet_ids',[]))
    info['short_description'] = item.get('short_description')
    info['description'] = item.get('description')
    info['permalink_aliases'] = ", ".join(item.get('permalink_aliases',[]))
    info['aliases'] = ", ".join(item.get('aliases',[]))
    info['location_group_names'] = ", ".join([i.get('value') for i in item.get('location_group_identifiers',[])])
    info['location_names'] = ", ".join([i.get('value') for i in item.get('location_identifiers',[])])
    info['image_url'] = item.get('image_url')
    info['website_url'] = item.get('website',{}).get('value')
    info['linkedin_url'] = item.get('linkedin',{}).get('value')
    info['facebook_url'] = item.get('facebook',{}).get('value')
    info['twitter_url'] = item.get('twitter',{}).get('value')
    info['born_on'] = to_date(item.get('born_on'))
    info['died_on'] = to_date(item.get('died_on'))
    info['rank'] = item.get('rank')
    info['rank_delta_d7'] = item.get('rank_delta_d7')
    info['rank_delta_d30'] = item.get('rank_delta_d30')
    info['rank_delta_d90'] = item.get('rank_delta_d90')
    info['rank_person'] = item.get('rank_person')
    info['rank_principal'] = item.get('rank_principal')
    info['rank_principal_investor'] = item.get('rank_principal_investor')
    info['num_articles'] = item.get('num_articles')
    info['num_current_advisor_jobs'] = item.get('num_current_advisor_jobs')
    info['num_current_jobs'] = item.get('num_current_jobs')
    info['num_event_appearances'] = item.get('num_event_appearances')
    info['num_exits'] = item.get('num_exits')
    info['num_exits_ipo'] = item.get('num_exits_ipo')
    info['num_founded_organizations'] = item.get('num_founded_organizations')
    info['num_investments'] = item.get('num_investments')
    info['num_investments_funding_rounds'] = item.get('num_investments_funding_rounds')
    info['num_jobs'] = item.get('num_jobs')
    info['num_lead_investments'] = item.get('num_lead_investments')
    info['num_partner_investments'] = item.get('num_partner_investments')
    info['num_past_advisor_jobs'] = item.get('num_past_advisor_jobs')
    info['num_past_jobs'] = item.get('num_past_jobs')
    info['num_portfolio_organizations'] = item.get('num_portfolio_organizations')
    info['num_relationships'] = item.get('num_relationships')
    info['investor_type'] = ", ".join(item.get('investor_type',[]))
    info['investor_stage'] = ", ".join(item.get('investor_stage',[]))

    return info

def get_available_properties():

    return [
        "uuid",
        "permalink",
        "name",
        "first_name",
        "middle_name",
        "last_name",
        "gender",
        "primary_job_title",
        "primary_organization",
        "primary_organization",
        "primary_organization",
        "created_at",
        "updated_at",
        "facet_ids",
        "short_description",
        "description",
        "permalink_aliases",
        "aliases",
        "location_group_identifiers",
        "location_identifiers",
        "image_url",
        "website",
        "linkedin",
        "facebook",
        "twitter",
        "born_on",
        "died_on",
        "rank",
        "rank_delta_d7",
        "rank_delta_d30",
        "rank_delta_d90",
        "rank_person",
        "rank_principal",
        "rank_principal_investor",
        "num_articles",
        "num_current_advisor_jobs",
        "num_current_jobs",
        "num_event_appearances",
        "num_exits",
        "num_exits_ipo",
        "num_founded_organizations",
        "num_investments",
        "num_investments_funding_rounds",
        "num_jobs",
        "num_lead_investments",
        "num_partner_investments",
        "num_past_advisor_jobs",
        "num_past_jobs",
        "num_portfolio_organizations",
        "num_relationships",
        "investor_type",
        "investor_stage"
    ]
