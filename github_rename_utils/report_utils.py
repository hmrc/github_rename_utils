from sgqlc.operation import Operation
from sgqlc.types import Variable, non_null
from github_rename_utils.schema import github_schema as schema

def query_add_rate_limiting_data(op):
    rate_limit = op.rate_limit()
    rate_limit.limit()
    rate_limit.cost()
    rate_limit.remaining()
    rate_limit.reset_at()


def build_team_name_query(first_page=False):
    if first_page:
        variables = {'org': non_null(str)}
    else:
        variables= {'org': non_null(str), 'teamsCursor': str }
    
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
    return {'org': org, 'team': team, 'reposCursor': repos_cursor}

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
    
    repo_names = [edge.repo.name for edge.repo in interpreted_response.organization.team.repositories.edges
                                        if edge.permission in expected_permissions and (not edge.repo.is_archived)]
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
        repo_list_variables = build_team_repo_name_variables(org, page_cursor)
        data = endpoint(op, repo_list_variables)
        interpreted_response = (op + data)
    
    # last data batch
    repos.extend(map_repo_name_data(interpreted_response))

    return repos


def build_team_report_variables(org, team, repo_page_cursor, unwanted_branch_name):
    return {'teamSlug': team, 'org': org, 'reposCursor': repo_page_cursor, 'unwantedBranchName': unwanted_branch_name, 'unwantedBranchQualifiedName': f"refs/heads/{unwanted_branch_name}"}

def build_team_report_query():
    variables= {'teamSlug': non_null(str), 'org': non_null(str), 'reposCursor': str, 'unwantedBranchName': non_null(str), 'unwantedBranchQuery': non_null(str)}
    
    op = Operation(schema.Query, name='Team_Repos', variables=variables)
    query_add_rate_limiting_data(op)

    org = op.organization(login=Variable('org'))
    org.id()
    org.name()
    team = org.team(slug=Variable('team_slug'))
    team.name()
    repos = team.repositories(first=100, after=Variable('repos_cursor'))
    repos.total_count()
    repos.page_info.end_cursor()
    repos.page_info.has_next_page()
    repos.edges.permission()
    repos.edges.node.is_archived()
    repos.edges.node.id()
    repos.edges.node.name()
    repos.edges.node.default_branch_ref.id()
    repos.edges.node.default_branch_ref.name()
    rules = repos.edges.node.branch_protection_rules(first=5)
    rules.edges.node.required_status_check_contexts()
    rule_branches = rules.edges.node.matching_refs(first=5)
    rule_branches.total_count()
    rule_branches.nodes.name()
    prs = repos.edges.node.pull_requests(base_ref_name=Variable('unwanted_branch_name'), states=['OPEN'])
    prs.total_count()
    old_default = repos.edges.node.ref(qualified_name=Variable('unwanted_branch_qualified_name'))
    old_default.name()

    return op

valid_permissions = ['ADMIN', 'MAINTAIN', 'WRITE', 'TRIAGE', 'READ']

def map_repository_data_list(interpreted_response, include_read, include_archived):
    mapped_objects = []

    expected_pemissions = valid_permissions
    if not include_read:
        expected_pemissions = [permission for permission in valid_permissions if permission not in ['READ', 'TRIAGE']]

    for edge in interpreted_response.organization.team.repositories.edges:
        if edge.permission not in expected_pemissions:
            continue
        
        if (not include_archived) and edge.node.is_archived == True:
            continue
        
        repo = edge.node
        bp = [edge.node for edge in repo.branch_protection_rules.edges if repo.default_branch_ref in [node.name for node in edge.node.matching_refs.nodes]]
        checks = []
        if bp is not None and len(bp) > 0:
            checks = bp[0].required_status_check_contexts
        
        unwanted_branch = None
        if repo.ref:
            unwanted_branch = repo.ref.name

        map = {
            "name": repo.name,
            "default_branch": repo.default_branch_ref.name,
            "open_prs": repo.pull_requests.total_count,
            "default_branch_protection": (bp is not None),
            "default_branch_protection_checks" : checks,
            "old_term_branch": unwanted_branch
        }
        mapped_objects.append(map)

    return mapped_objects