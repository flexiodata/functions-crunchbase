
# ---
# name: crunchbase-organizations
# deployed: true
# config: index
# title: Crunchbase Organizations
# description: Returns a list of organizations from Crunchbase
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
#     description: The UUID for the organization
#   - name: permalink
#     type: string
#     description: The permalink of the organization
#   - name: name
#     type: string
#     description: The name of the organization
#   - name: legal_name
#     type: string
#     description: The legal name of the organization
#   - name: created_at
#     type: string
#     description: The date the organization was created in the system
#   - name: updated_at
#     type: string
#     description: Date the information for the organization was last updated in the system
#   - name: category_names
#     type: string
#     description: A delimited list of the names of the categories for the organization
#   - name: category_group_names
#     type: string
#     description: A delimited list of the names of the category groups for the organization
#   - name: facet_ids
#     type: string
#     description: A delimited list of facet ids for the organization
#   - name: hub_tags
#     type: string
#     description: A delimited list of hub tags for the organization
#   - name: company_type
#     type: string
#     description: The type of the organization
#   - name: short_description
#     type: string
#     description: A short description of the organization
#   - name: description
#     type: string
#     description: A description of the organization
#   - name: permalink_aliases
#     type: string
#     description: A delimited list of alternate permalinks for the organization
#   - name: aliases
#     type: string
#     description: A delimited list of alternate names for the organization
#   - name: location_group_names
#     type: string
#     description: A delimited list of the names of the areas where the organization is headquartered
#   - name: location_names
#     type: string
#     description: A delimited list of the names of the places where the organization is headquartered
#   - name: phone_number
#     type: string
#     description: The general phone number of the organization
#   - name: contact_email
#     type: string
#     description: The general contact email for the organization
#   - name: image_url
#     type: string
#     description: The cloudinary url of the profile image
#   - name: website_url
#     type: string
#     description: Link to the homepage for the organization
#   - name: linkedin_url
#     type: string
#     description: Link to the LinkedIn page for the organization
#   - name: facebook_url
#     type: string
#     description: Link to the Facebook page for the organization
#   - name: twitter_url
#     type: string
#     description: Link to the Twitter page for the organization
#   - name: founded_on
#     type: string
#     description: The date the organization was founded
#   - name: exited_on
#     type: string
#     description: The date the organization was acquired or went public
#   - name: went_public_on
#     type: string
#     description: The date when the organization went public
#   - name: delisted_on
#     type: string
#     description: The date when the organization removed its stock from the stock exchange
#   - name: status
#     type: string
#     description: The status of the organization
#   - name: operating_status
#     type: string
#     description: The operating status of the organization
#   - name: ipo_status
#     type: string
#     description: The current public status of the organization
#   - name: stock_exchange_symbol
#     type: string
#     description: The stock exchange where the organization is listed
#   - name: stock_symbol
#     type: string
#     description: Stock ticker symbol
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
#   - name: rank_org
#     type: integer
#     description: Algorithmic rank assigned to the top 100,000 most active organizations
#   - name: rank_org_company
#     type: integer
#     description: Algorithmic rank assigned to the top 100,000 most active companies
#   - name: rank_org_school
#     type: integer
#     description: Algorithmic rank assigned to the top 100,000 most active schools
#   - name: rank_principal
#     type: integer
#     description: Algorithmic rank assigned to the top 100,000 most active organizations and people
#   - name: rank_principal_investor
#     type: integer
#     description: Algorithmic rank assigned to the top 100,000 most active investors
#   - name: revenue_range
#     type: string
#     description: Estimated revenue range for organization
#   - name: num_acquisitions
#     type: integer
#     description: The total number of acquisitions
#   - name: num_alumni
#     type: integer
#     description: Total number of alumni
#   - name: num_articles
#     type: integer
#     description: The number of news articles that reference the organization
#   - name: num_current_advisor_positions
#     type: integer
#     description: Total number of current board members and advisors an organization has
#   - name: num_current_positions
#     type: integer
#     description: Total number of current team members an organization has on Crunchbase
#   - name: num_employees_enum
#     type: string
#     description: Total number of employees range
#   - name: num_enrollments
#     type: string
#     description: Total number of enrollments range
#   - name: num_event_appearances
#     type: integer
#     description: Total number of events an organization appeared in
#   - name: num_exits
#     type: integer
#     description: Total number of exits
#   - name: num_exits_ipo
#     type: integer
#     description: Total number of exits (IPO)
#   - name: num_founder_alumni
#     type: integer
#     description: Total number of alumni that are founders
#   - name: num_founders
#     type: integer
#     description: Total number of founders
#   - name: num_funding_rounds
#     type: integer
#     description: Total number of funding rounds
#   - name: num_funds
#     type: integer
#     description: Total number of funds raised
#   - name: num_investments_funding_rounds
#     type: integer
#     description: Total number of investment funding rounds
#   - name: num_investors
#     type: integer
#     description: Total number of investment firms and individual investors
#   - name: num_lead_investments
#     type: integer
#     description: Total number of lead investments made
#   - name: num_lead_investors
#     type: integer
#     description: Total number of lead investment firms and individual investors
#   - name: num_past_positions
#     type: integer
#     description: Total number of past team members of an organization
#   - name: num_portfolio_organizations
#     type: integer
#     description: Total number of portfolio organizations
#   - name: num_relationships
#     type: integer
#     description: Total number of relationships a profile has
#   - name: num_sub_organizations
#     type: integer
#     description: Total number of sub-organizations that belongs to a parent organization
#   - name: investor_type
#     type: string
#     description: A delimited list of the type of investors this organization is
#   - name: investor_stage
#     type: string
#     description: A delimited list of the stage of investments made by this organization
#   - name: funding_stage
#     type: string
#     description: The most recent funding status of the organization
#   - name: funds_currency
#     type: string
#     description: Currency type of the total funding amount raised across all fund raises
#   - name: funds_total
#     type: integer
#     description: Total funding amount raised across all fund raises in the specified currency
#   - name: funds_total_usd
#     type: integer
#     description: Total funding amount raised across all fund raises in USD
#   - name: funding_currency
#     type: string
#     description: Currency type of the total amount raised across all funding rounds
#   - name: funding_total
#     type: integer
#     description: Total amount raised across all funding rounds in the specified currency
#   - name: funding_total_usd
#     type: integer
#     description: Total amount raised across all funding rounds in USD
#   - name: equity_funding_currency
#     type: string
#     description: Currency type of the total funding amount raised across all funding rounds excluding debt
#   - name: equity_funding_total
#     type: integer
#     description: Total funding amount raised across all funding rounds excluding debt in the specified currency
#   - name: equity_funding_total_usd
#     type: integer
#     description: Total funding amount raised across all funding rounds excluding debt in USD
#   - name: last_funding_total_currency
#     type: string
#     description: Currency type of the most recent funding round
#   - name: last_funding_total
#     type: integer
#     description: Total funding amount of the most recent funding round
#   - name: last_funding_total_total_usd
#     type: integer
#     description: Total funding amount of the most recent funding round in USD
#   - name: last_equity_funding_currency
#     type: string
#     description: Currency type of the most recent funding round excluding debt
#   - name: last_equity_funding_total
#     type: integer
#     description: Total funding amount of the most recent funding round excluding debt
#   - name: last_equity_funding_total_usd
#     type: integer
#     description: Total funding amount of the most recent funding round excluding debt in USD
#   - name: last_funding_at
#     type: string
#     description: Date of most recent funding round
#   - name: last_funding_type
#     type: string
#     description: Last funding round type
#   - name: last_equity_funding_type
#     type: string
#     description: The most recent funding round excluding debt
#   - name: owner_uuid
#     type: string
#     description: UUID of the parent organization of the sub-organization
#   - name: owner_permalink
#     type: string
#     description: Permalink of the parent organization of the sub-organization
#   - name: owner_name
#     type: string
#     description: Name of the parent organization of the sub-organization
#   - name: acquirer_uuid
#     type: string
#     description: UUID of the organization that made the acquisition
#   - name: acquirer_permalink
#     type: string
#     description: Permalink of the organization that made the acquisition
#   - name: acquirer_name
#     type: string
#     description: Name of the organization that made the acquisition
#   - name: founder_uuids
#     type: string
#     description: A delimited list of the UUIDs of the founders
#   - name: founder_permalinks
#     type: string
#     description: A delimited list of the permalinks of the founders
#   - name: founder_names
#     type: string
#     description: A delimited list of the names of the founders
#   - name: investor_uuids
#     type: string
#     description: A delimited list of the UUIDs of the top 5 investors with investments in this company, ordered by Crunchbase rank
#   - name: investor_permalinks
#     type: string
#     description: A delimited list of the permalinks of the top 5 investors with investments in this company, ordered by Crunchbase rank
#   - name: investor_names
#     type: string
#     description: A delimited list of the names of the top 5 investors with investments in this company, ordered by Crunchbase rank
#   - name: program_type
#     type: integer
#     description: The type of accelerator program
#   - name: program_duration
#     type: integer
#     description: The duration of the acceleration program in number of weeks
#   - name: program_application_deadline
#     type: string
#     description: The deadline for applying to the accelerator program
#   - name: school_type
#     type: string
#     description: The type of school
#   - name: school_program
#     type: string
#     description: The type of school program
#   - name: school_method
#     type: string
#     description: The type of school method
#   - name: demo_days
#     type: boolean
#     description: Whether an accelerator hosts any demo days
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
    # https://app.swaggerhub.com/apis-docs/Crunchbase/crunchbase-enterprise_api/1.0.1#/Search/post_searches_organizations

    query = {
        "field_ids": get_available_properties(),
        "limit": 1000 # page size
    }
    headers = {
        'Content-Type': 'application/json',
        'X-cb-user-key': auth_token
    }
    url = 'https://api.crunchbase.com/api/v4/searches/organizations'

    page_idx = 1
    max_pages = 5 # TODO: temporariliy limit number of pages; set to large value to get all pages
    while True:

        page_url = url
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
    status_forcelist=(429, 500, 502, 503, 504),
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
    info['legal_name'] = item.get('legal_name')
    info['created_at'] = to_date(item.get('created_at'))
    info['updated_at'] = to_date(item.get('updated_at'))
    info['category_names'] = ", ".join([i.get('value') for i in item.get('categories',[])])
    info['category_group_names'] = ", ".join([i.get('value') for i in item.get('category_groups',[])])
    info['facet_ids'] = ", ".join(item.get('facet_ids',[]))
    info['hub_tags'] = ", ".join(item.get('hub_tags',[]))
    info['company_type'] = item.get('company_type')
    info['short_description'] = item.get('short_description')
    info['description'] = item.get('description')
    info['permalink_aliases'] = ", ".join(item.get('permalink_aliases',[]))
    info['aliases'] = ", ".join(item.get('aliases',[]))
    info['location_group_names'] = ", ".join([i.get('value') for i in item.get('location_group_identifiers',[])])
    info['location_names'] = ", ".join([i.get('value') for i in item.get('location_identifiers',[])])
    info['phone_number'] = item.get('phone_number')
    info['contact_email'] = item.get('contact_email')
    info['image_url'] = item.get('image_url')
    info['website_url'] = item.get('website',{}).get('value')
    info['linkedin_url'] = item.get('linkedin',{}).get('value')
    info['facebook_url'] = item.get('facebook',{}).get('value')
    info['twitter_url'] = item.get('twitter',{}).get('value')
    info['founded_on'] = to_date(item.get('founded_on',{}).get('value'))
    info['exited_on'] = to_date(item.get('exited_on',{}).get('value'))
    info['went_public_on'] = to_date(item.get('went_public_on'))
    info['delisted_on'] = to_date(item.get('delisted_on',{}).get('value'))
    info['status'] = item.get('status')
    info['operating_status'] = item.get('operating_status')
    info['ipo_status'] = item.get('ipo_status')
    info['stock_exchange_symbol'] = item.get('stock_exchange_symbol')
    info['stock_symbol'] = item.get('listed_stock_symbol')
    info['rank'] = item.get('rank')
    info['rank_delta_d7'] = item.get('rank_delta_d7')
    info['rank_delta_d30'] = item.get('rank_delta_d30')
    info['rank_delta_d90'] = item.get('rank_delta_d90')
    info['rank_org'] = item.get('rank_org')
    info['rank_org_company'] = item.get('rank_org_company')
    info['rank_org_school'] = item.get('rank_org_school')
    info['rank_principal'] = item.get('rank_principal')
    info['rank_principal_investor'] = item.get('rank_principal_investor')
    info['revenue_range'] = item.get('revenue_range')
    info['num_acquisitions'] = item.get('num_acquisitions')
    info['num_alumni'] = item.get('num_alumni')
    info['num_articles'] = item.get('num_articles')
    info['num_current_advisor_positions'] = item.get('num_current_advisor_positions')
    info['num_current_positions'] = item.get('num_current_positions')
    info['num_employees_enum'] = item.get('num_employees_enum')
    info['num_enrollments'] = item.get('num_enrollments')
    info['num_event_appearances'] = item.get('num_event_appearances')
    info['num_exits'] = item.get('num_exits')
    info['num_exits_ipo'] = item.get('num_exits_ipo')
    info['num_founder_alumni'] = item.get('num_founder_alumni')
    info['num_founders'] = item.get('num_founders')
    info['num_funding_rounds'] = item.get('num_funding_rounds')
    info['num_funds'] = item.get('num_funds')
    info['num_investments_funding_rounds'] = item.get('num_investments_funding_rounds')
    info['num_investors'] = item.get('num_investors')
    info['num_lead_investments'] = item.get('num_lead_investments')
    info['num_lead_investors'] = item.get('num_lead_investors')
    info['num_past_positions'] = item.get('num_past_positions')
    info['num_portfolio_organizations'] = item.get('num_portfolio_organizations')
    info['num_relationships'] = item.get('num_relationships')
    info['num_sub_organizations'] = item.get('num_sub_organizations')
    info['investor_type'] = ", ".join(item.get('investor_type',[]))
    info['investor_stage'] = ", ".join(item.get('investor_stage',[]))
    info['funding_stage'] = item.get('funding_stage')
    info['funds_currency'] = item.get('funds_total',{}).get('currency')
    info['funds_total'] = item.get('funds_total',{}).get('value')
    info['funds_total_usd'] = item.get('funds_total',{}).get('value_usd')
    info['funding_currency'] = item.get('funding_total',{}).get('currency')
    info['funding_total'] = item.get('funding_total',{}).get('value')
    info['funding_total_usd'] = item.get('funding_total',{}).get('value_usd')
    info['equity_funding_currency'] = item.get('equity_funding_total',{}).get('currency')
    info['equity_funding_currency'] = item.get('equity_funding_total',{}).get('value')
    info['equity_funding_currency'] = item.get('equity_funding_total',{}).get('value_usd')
    info['last_equity_funding_currency'] = item.get('last_funding_total',{}).get('currency')
    info['last_equity_funding_total'] = item.get('last_funding_total',{}).get('value')
    info['last_equity_funding_total_usd'] = item.get('last_funding_total',{}).get('value_usd')
    info['last_equity_funding_currency'] = item.get('last_equity_funding_total',{}).get('currency')
    info['last_equity_funding_total'] = item.get('last_equity_funding_total',{}).get('value')
    info['last_equity_funding_total_usd'] = item.get('last_equity_funding_total',{}).get('value_usd')
    info['last_funding_at'] = to_date(item.get('last_funding_at'))
    info['last_funding_type'] = item.get('last_funding_type')
    info['last_equity_funding_type'] = item.get('last_equity_funding_type')
    info['owner_uuid'] = item.get('owner_identifier',{}).get('uuid')
    info['owner_permalink'] = item.get('owner_identifier',{}).get('permalink')
    info['owner_name'] = item.get('owner_identifier',{}).get('value')
    info['acquirer_uuid'] = item.get('acquirer_identifier',{}).get('uuid')
    info['acquirer_permalink'] = item.get('acquirer_identifier',{}).get('permalink')
    info['acquirer_name'] = item.get('acquirer_identifier',{}).get('value')
    info['founder_uuids'] = ", ".join([i.get('uuid') for i in item.get('founder_identifiers',[])])
    info['founder_permalinks'] = ", ".join([i.get('permalink') for i in item.get('founder_identifiers',[])])
    info['founder_names'] = ", ".join([i.get('value') for i in item.get('founder_identifiers',[])])
    info['investor_uuids'] = ", ".join([i.get('uuid') for i in item.get('investor_identifiers',[])])
    info['investor_permalinks'] = ", ".join([i.get('permalink') for i in item.get('investor_identifiers',[])])
    info['investor_names'] = ", ".join([i.get('value') for i in item.get('investor_identifiers',[])])
    info['program_type'] = item.get('program_type')
    info['program_duration'] = item.get('program_duration')
    info['program_application_deadline'] = to_date(item.get('program_application_deadline'))
    info['school_type'] = item.get('school_type')
    info['school_program'] = item.get('school_program')
    info['school_method'] = item.get('school_method')
    info['demo_days'] = item.get('demo_days')

    return info

def get_available_properties():

    return [
        "uuid",
        "permalink",
        "name",
        "legal_name",
        "created_at",
        "updated_at",
        "categories",
        "category_groups",
        "facet_ids",
        "hub_tags",
        "company_type",
        "short_description",
        "description",
        "permalink_aliases",
        "aliases",
        "location_group_identifiers",
        "location_identifiers",
        "phone_number",
        "contact_email",
        "image_url",
        "website",
        "linkedin",
        "facebook",
        "twitter",
        "founded_on",
        "exited_on",
        "went_public_on",
        "delisted_on",
        "status",
        "operating_status",
        "ipo_status",
        "stock_exchange_symbol",
        "listed_stock_symbol",
        "rank",
        "rank_delta_d7",
        "rank_delta_d30",
        "rank_delta_d90",
        "rank_org",
        "rank_org_company",
        "rank_org_school",
        "rank_principal",
        "rank_principal_investor",
        "revenue_range",
        "num_acquisitions",
        "num_alumni",
        "num_articles",
        "num_current_advisor_positions",
        "num_current_positions",
        "num_employees_enum",
        "num_enrollments",
        "num_event_appearances",
        "num_exits",
        "num_exits_ipo",
        "num_founder_alumni",
        "num_founders",
        "num_funding_rounds",
        "num_funds",
        "num_investments_funding_rounds",
        "num_investors",
        "num_lead_investments",
        "num_lead_investors",
        "num_past_positions",
        "num_portfolio_organizations",
        "num_relationships",
        "num_sub_organizations",
        "investor_type",
        "investor_stage",
        "funding_stage",
        "funds_total",
        "funds_total",
        "funds_total",
        "funding_total",
        "funding_total",
        "funding_total",
        "equity_funding_total",
        "equity_funding_total",
        "equity_funding_total",
        "last_funding_total",
        "last_funding_total",
        "last_funding_total",
        "last_equity_funding_total",
        "last_equity_funding_total",
        "last_equity_funding_total",
        "last_funding_at",
        "last_funding_type",
        "last_equity_funding_type",
        "owner_identifier",
        "owner_identifier",
        "owner_identifier",
        "acquirer_identifier",
        "acquirer_identifier",
        "acquirer_identifier",
        "founder_identifiers",
        "founder_identifiers",
        "founder_identifiers",
        "investor_identifiers",
        "investor_identifiers",
        "investor_identifiers",
        "program_type",
        "program_duration",
        "program_application_deadline",
        "school_type",
        "school_program",
        "school_method",
        "demo_days"
    ]
