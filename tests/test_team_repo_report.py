import github_rename_utils.team_repo_report as utils
from github_rename_utils.github_graphql_wrapper import initialise_endpoint
import responses
from unittest import TestCase

expected_repos_all = [
    {
        "name": "repo1",
        "default_branch": "master",
        "open_prs": 8,
        "default_branch_protection": True,
        "default_branch_protection_checks" : ['some-check-pr-builder'],
        "old_term_branch": "master"
    },
    {
        "name": "repo2",
        "default_branch": "master",
        "open_prs": 4,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": "master"
    },
    {
        "name": "repo3",
        "default_branch": "master",
        "open_prs": 4,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": "master"
    },
    {
        "name": "repo-fhddjksfhk",
        "default_branch": "main",
        "open_prs": 0,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": None
    },
    {
        "name": "repo-saderwkrhs",
        "default_branch": "main",
        "open_prs": 0,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": None
    },
    {
        "name": "repo-thjrecvix",
        "default_branch": "master",
        "open_prs": 0,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": "master"
    },
    {
        "name": "repo-fdhiob",
        "default_branch": "main",
        "open_prs": 0,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": None
    },
]

expected_repos_no_archived_no_read = [
    expected_repos_all[0],
    expected_repos_all[1],
    expected_repos_all[2],
    expected_repos_all[4],
    expected_repos_all[6],
]
expected_repos_no_archived = [
    expected_repos_all[0],
    expected_repos_all[1],
    expected_repos_all[2],
    expected_repos_all[4],
    expected_repos_all[5],
    expected_repos_all[6],
]
expected_repos_no_read = [
    expected_repos_all[0],
    expected_repos_all[1],
    expected_repos_all[2],
    expected_repos_all[3],
    expected_repos_all[4],
    expected_repos_all[6],
]

def compare_response_vs_expected(data, expected):
    test_util = TestCase()
    test_util.maxDiff = None
    test_util.assertCountEqual(expected, data)

def request_callback(request):
        from tests.expected_queries import team_repos_query_page1, team_repos_query_page2
        from tests.mock_payloads import repo_list_page_1, repo_list_page_2

        if team_repos_query_page1 == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c13'}
            return (200, headers, repo_list_page_1)
        
        elif team_repos_query_page2 == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c14'}
            return (200, headers, repo_list_page_2)

        else:
            print(request.body)
            raise Exception('Unexpected payload received')

@responses.activate
def test_get_active_owned_repo_data_for_team():

    responses.add_callback(
        responses.POST,
        'https://api.github.com/graphql',
        callback=request_callback,
        content_type='application/json',
    )

    team_name = 'my-team'
    org_name = 'my-org'
    '''
    # in integration and production usage we would normally recommend that token is loaded 
    # from an enironment variable for security
    # e.g. token = os.environ.get('GH_TOKEN', '')
    '''
    token = 'dummy_token'

    endpoint = initialise_endpoint(token)

    data = utils.get_repo_data(org_name, team_name, endpoint)

    assert data is not None
    compare_response_vs_expected(data, expected_repos_no_archived_no_read)

@responses.activate
def test_get_repo_data_on_all_repos_for_team():
    
    responses.add_callback(
        responses.POST,
        'https://api.github.com/graphql',
        callback=request_callback,
        content_type='application/json',
    )

    team_name = 'my-team'
    org_name = 'my-org'
    token = 'dummy_token'

    endpoint = initialise_endpoint(token)

    data = utils.get_repo_data(org_name, team_name, endpoint, include_read=True, include_archived=True)

    assert data is not None
    compare_response_vs_expected(data, expected_repos_all)
    
@responses.activate
def test_get_repo_data_on_all_active_repos_for_team():
    
    responses.add_callback(
        responses.POST,
        'https://api.github.com/graphql',
        callback=request_callback,
        content_type='application/json',
    )

    team_name = 'my-team'
    org_name = 'my-org'
    token = 'dummy_token'

    endpoint = initialise_endpoint(token)

    data = utils.get_repo_data(org_name, team_name, endpoint, include_read=True)

    assert data is not None
    compare_response_vs_expected(data, expected_repos_no_archived)

@responses.activate
def test_get_repo_data_on_all_owned_repos_for_team():
    
    responses.add_callback(
        responses.POST,
        'https://api.github.com/graphql',
        callback=request_callback,
        content_type='application/json',
    )

    team_name = 'my-team'
    org_name = 'my-org'
    token = 'dummy_token'

    endpoint = initialise_endpoint(token)

    data = utils.get_repo_data(org_name, team_name, endpoint, include_archived=True)

    assert data is not None
    compare_response_vs_expected(data, expected_repos_no_read)

