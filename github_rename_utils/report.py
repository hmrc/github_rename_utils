from sgqlc.endpoint.requests import RequestsEndpoint
from sgqlc.operation import Operation
from sgqlc.types import Variable
from github_rename_utils.schema import github_schema as schema

def initialise_endpoint(token):
    url = 'https://api.github.com/graphql'
    headers = {'Authorization': f'bearer {token}'}
    endpoint = RequestsEndpoint(url, headers)
    return endpoint

def get_repo_data(org, team, name, endpoint, include_read=False, include_archived=False):

    # we assume the unwanted branch name is 'master'
    unwanted_branch_name = "master"
    repo_page_cursor = ''


    responses = [] # map at end? this will not allow gap between calls. Each call for 100 repos can take around 5 seconds
    mapped_repo_list = []

    op = build_team_report_operation_query()
    variables = build_team_report_variables(org, team, repo_page_cursor, unwanted_branch_name)
    data = endpoint(op, variables)

    interpreted_response = (op + data)
    while (interpreted_response.organization.team.repositories.page_info.has_next_page):
        mapped_repo_list.extend(map_repository_data_list(interpreted_response, include_read=include_read, include_archived=include_archived))
        repo_page_cursor = interpreted_response.organization.team.repositories.page_info.end_cursor
        variables = build_team_report_variables(org, team, repo_page_cursor, unwanted_branch_name)
        data = endpoint(op, variables)
        interpreted_response = (op + data)
    
    # last data batch
    mapped_repo_list.extend(map_repository_data_list(interpreted_response, include_read=include_read, include_archived=include_archived))

    return mapped_repo_list

def build_team_report_variables(org, team, repo_page_cursor, unwanted_branch_name):
    return {'teamSlug': team, 'org': org, 'reposCursor': repo_page_cursor, 'unwantedBranchName': unwanted_branch_name, 'unwantedBranchQuery': f'name: "refs/heads/{unwanted_branch_name}"'}

def build_team_report_operation_query():
    variables= {'teamSlug': str, 'org': str, 'reposCursor': str, 'unwantedBranchName': str, 'unwantedBranchQuery': str}
    
    op = Operation(schema.Query, name='Team_Repos', variables=variables)

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
    branches = repos.edges.node.refs(__alias__='branches', ref_prefix='refs/heads/')
    branches.total_count()
    old_default = repos.edges.node.refs(__alias__='unwanted_branch', query=Variable('unwanted_branch_query'))
    old_default.nodes.name()

    return op

def map_repository_data_list(interpreted_response, include_read, include_archived):
    mapped_objects = []

    valid_permissions = ['ADMIN', 'MAINTAIN', 'WRITE', 'TRIAGE', 'READ']
    if not include_read:
        valid_permissions.remove('READ')
        valid_permissions.remove('TRIAGE')

    for edge in interpreted_response.organization.team.repositories.edges:
        if edge.permission not in valid_permissions:
            continue
        
        if (not include_archived) and edge.node.is_archived == True:
            continue
        
        repo = edge.node
        bp = [edge.node for edge in repo.branch_protection_rules.edges if repo.default_branch_ref in [node.name for node in edge.node.matching_refs.nodes]]
        checks = []
        if bp is not None and len(bp) > 0:
            checks = bp[0].required_status_check_contexts
        
        map = {
            "name": repo.name,
            "default_branch": repo.default_branch_ref,
            "open_prs": repo.pull_requests.total_count,
            "branches": repo.branches.total_count,
            "default_branch_protection": (bp is not None),
            "default_branch_protection_checks" : checks,
            "old_term_branch": "to be calculated"
        }
        mapped_objects.append(map)

    return mapped_objects