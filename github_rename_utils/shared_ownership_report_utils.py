from sgqlc.operation import Operation
from sgqlc.types import Variable, non_null
from github_rename_utils.schema import github_schema as schema
from github_rename_utils.github_graphql_api import query_add_rate_limiting_data, valid_permissions


def build_team_name_query(first_page=False):
    if first_page:
        variables = {'org': non_null(str)}
    else:
        variables = {'org': non_null(str), 'teamsCursor': str }
    
    op = Operation(schema.Query, name='Teams', variables=variables)
    query_add_rate_limiting_data(op)
    org = op.organization(login=Variable('org'))
    org.name()
    if first_page:
        teams = org.teams(first=100)
    else:
        teams = org.teams(first=100, after=Variable('teams_cursor'))
    teams.total_count()
    teams.page_info.has_next_page()
    teams.page_info.end_cursor()
    teams.nodes.slug()

    return op

def build_team_repo_name_query():
    variables= {'org': non_null(str), 'teamSlug': non_null(str),'reposCursor': str }
    
    op = Operation(schema.Query, name='Per_Team_Repos', variables=variables)
    query_add_rate_limiting_data(op)

    org = op.organization(login=Variable('org'))
    org.name()
    
    team = org.team(slug=Variable('team_slug'))
    team.name()
    repos = team.repositories(first=100, after=Variable('repos_cursor'))
    repos.total_count()
    repos.page_info.end_cursor()
    repos.page_info.has_next_page()
    repos.edges.permission()
    repos.edges.node.is_archived()
    repos.edges.node.name()

    return op

def build_team_repo_name_variables(org, team, repos_cursor):
    return {'org': org, 'teamSlug': team, 'reposCursor': repos_cursor}

def build_team_name_variables(org, teams_cursor):
    return {'org': org, 'teamsCursor': teams_cursor}

def map_team_name_data(intepreted_response):
    data = [team.slug for team in
        intepreted_response.organization.teams.nodes]
    return data

def map_repo_name_data(interpreted_response, include_read=False):
    expected_permissions = valid_permissions
    if not include_read:
        expected_permissions = [permission for permission in valid_permissions if permission not in ['READ', 'TRIAGE']]
    
    repo_names = [edge.node.name for edge in interpreted_response.organization.team.repositories.edges
                                        if edge.permission in expected_permissions and (not edge.node.is_archived)]
    return repo_names

def get_team_names(endpoint, org):
    
    team_data = []
    
    team_variables = build_team_name_variables(org, '')

    # githubV4 organization.teams endpoint will not allow empty string for end_cursor
    op_first_page = build_team_name_query(first_page=True)
    op = build_team_name_query()

    data = endpoint(op_first_page, team_variables)
    interpreted_response = (op_first_page + data)

    while (interpreted_response.organization.teams.page_info.has_next_page):
        team_data.extend(map_team_name_data(interpreted_response))
        page_cursor = interpreted_response.organization.teams.page_info.end_cursor
        team_variables = build_team_name_variables(org, page_cursor)
        data = endpoint(op, team_variables)
        interpreted_response = (op + data)
    
    # last data batch
    team_data.extend(map_team_name_data(interpreted_response))

    return team_data

def get_repo_names_for_team(endpoint, team_slug, org):

    repos = []

    # only get active repos, not archived ones, 
    # this will have to be post processed in mapping as
    # the query 'archived:false' doesn't work in graphql
    repo_list_variables = build_team_repo_name_variables(org, team_slug, '')

    op = build_team_repo_name_query()
    data = endpoint(op, repo_list_variables)
    interpreted_response = (op + data)

    while (interpreted_response.organization.team.repositories.page_info.has_next_page):
        repos.extend(map_repo_name_data(interpreted_response))
        page_cursor = interpreted_response.organization.team.repositories.page_info.end_cursor
        repo_list_variables = build_team_repo_name_variables(org, team_slug, page_cursor)
        data = endpoint(op, repo_list_variables)
        interpreted_response = (op + data)
    
    # last data batch
    repos.extend(map_repo_name_data(interpreted_response))

    return repos
