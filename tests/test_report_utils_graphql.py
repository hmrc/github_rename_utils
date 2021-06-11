import github_rename_utils.report as utils
import json
import os
import responses


expected_repos_all = [
    {
        "name": "repo1",
        "default_branch": "master",
        "open_prs": 8,
        "branches": 17,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": "master"
    },
    {
        "name": "repo2",
        "default_branch": "master",
        "open_prs": 4,
        "branches": 34,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": "master"
    },
    {
        "name": "repo3",
        "default_branch": "master",
        "open_prs": 4,
        "branches": 34,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": "master"
    },
    {
        "name": "repo-fhddjksfhk",
        "default_branch": "main",
        "open_prs": 0,
        "branches": 2,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": None
    },
    {
        "name": "repo-saderwkrhs",
        "default_branch": "main",
        "open_prs": 0,
        "branches": 1,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": None
    },
    {
        "name": "repo-thjrecvix",
        "default_branch": "master",
        "open_prs": 0,
        "branches": 2,
        "default_branch_protection": True,
        "default_branch_protection_checks" : [],
        "old_term_branch": "master"
    },
    {
        "name": "repo-fdhiob",
        "default_branch": "main",
        "open_prs": 0,
        "branches": 1,
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

def request_callback(request):
        from tests.expected_queries import team_repos_query_page1, team_repos_query_page2
        from tests.mock_payloads import repo_list_page_1, repo_list_page_2

        payload = json.loads(request.body)

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
    repo_name = 'my-repo'
    '''
    # in integration and production usage we would normally recommend that token is loaded 
    # from an enironment variable for security
    # e.g. token = os.environ.get('GH_TOKEN', '')
    '''
    token = 'dummy_token'

    endpoint = utils.initialise_endpoint(token)

    data = utils.get_repo_data(org_name, team_name, repo_name, endpoint)

    assert data is not None
    assert len(data) == len(expected_repos_no_archived_no_read)
    # todo deep comparison of returned objects

@responses.activate
def test_get_repo_data_on_all_repos_for_team():
    assert False

@responses.activate
def test_get_repo_data_on_all_active_repos_for_team():
    assert False

@responses.activate
def test_get_repo_data_on_all_owned_repos_for_team():
    assert False
