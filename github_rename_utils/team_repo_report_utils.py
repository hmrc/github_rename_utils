from sgqlc.operation import Operation
from sgqlc.types import Variable, non_null
from github_rename_utils.schema import github_schema as schema
from github_rename_utils.graphql_utils import query_add_rate_limiting_data, valid_permissions


def build_team_report_variables(org, team, repo_page_cursor, unwanted_branch_name):
    return {'teamSlug': team, 'org': org, 'reposCursor': repo_page_cursor, 'unwantedBranchName': unwanted_branch_name, 'unwantedBranchQualifiedName': f"refs/heads/{unwanted_branch_name}"}

def build_team_report_query():
    variables= {'teamSlug': non_null(str), 'org': non_null(str), 'reposCursor': str, 'unwantedBranchName': non_null(str), 'unwantedBranchQualifiedName': non_null(str)}
    
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
        bp = [edge.node for edge in repo.branch_protection_rules.edges if repo.default_branch_ref.name in [node.name for node in edge.node.matching_refs.nodes]]
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