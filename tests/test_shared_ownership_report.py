import github_rename_utils.shared_ownership_utils as report_utils
from github_rename_utils.github_graphql_wrapper import initialise_endpoint
import responses
from unittest import TestCase

@responses.activate
def test_get_team_names_for_org_single_page():
    def custom_callback(request):
        from tests.expected_queries import team_names_page1
        from tests.mock_payloads import team_name_list

        if team_names_page1 == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c13'}
            return (200, headers, team_name_list)
        else:
            print(request.body)
            raise Exception('Unexpected payload received')

    responses.add_callback(
        responses.POST,
        'https://api.github.com/graphql',
        callback=custom_callback,
        content_type='application/json',
    )

    expected_team_name_list = ["my-team", "my-admin-team", "justice-league"]

    org_name = 'my-org'
    token = '__dummy__'

    endpoint = initialise_endpoint(token)
    actual_list = report_utils.get_team_names(endpoint, org_name)

    TestCase().assertCountEqual(expected_team_name_list, actual_list)

@responses.activate
def test_get_team_names_for_org_multipage():
    def custom_callback(request):
        from tests.expected_queries import team_names_page1, team_names_page2
        from tests.mock_payloads import team_name_list_page_1, team_name_list_page_2

        if team_names_page1 == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c13'}
            return (200, headers, team_name_list_page_1)

        elif team_names_page2 == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c14'}
            return (200, headers, team_name_list_page_2)

        else:
            print(request.body)
            raise Exception('Unexpected payload received')

    responses.add_callback(
        responses.POST,
        'https://api.github.com/graphql',
        callback=custom_callback,
        content_type='application/json',
    )

    expected_team_name_list = ["my-team", "my-admin-team", "justice-league", "my-additional-team"]

    org_name = 'my-org'
    token = '__dummy__'

    endpoint = initialise_endpoint(token)
    actual_list = report_utils.get_team_names(endpoint, org_name)

    TestCase().assertCountEqual(expected_team_name_list, actual_list)

@responses.activate
def test_get_repo_names_for_team_single_page():
    def custom_callback(request):
        from tests.expected_queries import team_repo_names_page1
        from tests.mock_payloads import team_repo_owner_list

        if team_repo_names_page1 == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c13'}
            return (200, headers, team_repo_owner_list)
        else:
            print(request.body)
            raise Exception('Unexpected payload received')

    responses.add_callback(
        responses.POST,
        'https://api.github.com/graphql',
        callback=custom_callback,
        content_type='application/json',
    )

    expected_repo_name_list = ["repo1", "repo2", "repo3"]

    token = '__dummy__'
    org_name = 'my-org'
    team_slug = 'my-team'

    endpoint = initialise_endpoint(token)
    actual_list = report_utils.get_repo_names_for_team(endpoint, team_slug, org_name)

    TestCase().assertCountEqual(expected_repo_name_list, actual_list)

# @responses.activate
# def test_get_repo_names_for_team_multipage():
#     assert 1 == 2

# @responses.activate
# def test_get_ownership_ignores_expected_ignore_teams():
#     assert 1 == 2
