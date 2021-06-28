import github_rename_utils.shared_ownership_report_utils as report_utils
from github_rename_utils.github_graphql_api import graphql_endpoint
import responses
from unittest import TestCase


token = '__dummy__'
org = 'my-org'
team_slug = 'my-team'
teams_cursor = 'fd3kle2jkKLfdsklswHTjk=='
repos_cursor = "fd3kle2jkKLfdsklswHTjk=="

@responses.activate
def test_get_team_names_for_org_single_page():
    def custom_callback(request):
        from tests.mock_graphql_queries import team_names_query
        from tests.mock_graphql_payloads import team_name_list_single_page

        if team_names_query(org) == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c13'}
            return (200, headers, team_name_list_single_page)
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

    endpoint = graphql_endpoint(token)
    actual_list = report_utils.get_team_names(endpoint, org)

    TestCase().assertCountEqual(expected_team_name_list, actual_list)

@responses.activate
def test_get_team_names_for_org_multipage():
    def custom_callback(request):
        from tests.mock_graphql_queries import team_names_query
        from tests.mock_graphql_payloads import team_name_list_multi_page_1, team_name_list_multi_page_2

        if team_names_query(org) == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c13'}
            return (200, headers, team_name_list_multi_page_1)

        elif team_names_query(org, teams_cursor) == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c14'}
            return (200, headers, team_name_list_multi_page_2)

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

    endpoint = graphql_endpoint(token)
    actual_list = report_utils.get_team_names(endpoint, org)

    TestCase().assertCountEqual(expected_team_name_list, actual_list)

@responses.activate
def test_get_repo_names_for_team_single_page():
    def custom_callback(request):
        from tests.mock_graphql_queries import team_repo_name_query
        from tests.mock_graphql_payloads import team_repo_list_single_page

        if team_repo_name_query(org, team_slug) == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c13'}
            return (200, headers, team_repo_list_single_page)
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

    endpoint = graphql_endpoint(token)
    actual_list = report_utils.get_repo_names_for_team(endpoint, team_slug, org)

    TestCase().assertCountEqual(expected_repo_name_list, actual_list)

@responses.activate
def test_get_repo_names_for_team_multipage():
    def custom_callback(request):
        from tests.mock_graphql_queries import team_repo_name_query
        from tests.mock_graphql_payloads import team_repo_list_multi_page_1, team_repo_list_multi_page_2

        if team_repo_name_query(org, team_slug) == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c13'}
            return (200, headers, team_repo_list_multi_page_1)

        elif team_repo_name_query(org, team_slug, repos_cursor) == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c14'}
            return (200, headers, team_repo_list_multi_page_2)

        else:
            print(request.body)
            raise Exception('Unexpected payload received')

    responses.add_callback(
        responses.POST,
        'https://api.github.com/graphql',
        callback=custom_callback,
        content_type='application/json',
    )

    expected_repo_name_list = ["repo1", "repo2", "repo3", "repo4"]

    endpoint = graphql_endpoint(token)
    actual_list = report_utils.get_repo_names_for_team(endpoint, team_slug, org)

    TestCase().assertCountEqual(expected_repo_name_list, actual_list)
