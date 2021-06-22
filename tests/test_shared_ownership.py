from github_rename_utils.shared_ownership import get_shared_ownership_report
import responses


@responses.activate
def test_get_ownership_ignores_expected_ignore_teams():
    def custom_callback(request):
        from tests.expected_queries import team_names_page1, team_repo_names_page1, team_repo_names_admin_page1
        from tests.mock_payloads import team_name_list, team_repo_owner_list, team_repo_owner_admin_list

        if team_names_page1 == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c13'}
            return (200, headers, team_name_list)

        if team_repo_names_page1 == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c14'}
            return (200, headers, team_repo_owner_list)

        elif team_repo_names_admin_page1 == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c15'}
            return (200, headers, team_repo_owner_admin_list)

        else:
            print(request.body)
            raise Exception('Unexpected payload received')

    responses.add_callback(
        responses.POST,
        'https://api.github.com/graphql',
        callback=custom_callback,
        content_type='application/json',
    )

    token = '__dummy__'
    org_name = 'my-org'
    ignored_teams = ['justice-league']

    expected_shared_ownership_report = {
        'repo1': ['my-team', 'my-admin-team'],
        'repo2': ['my-team', 'my-admin-team'],
        'repo3': ['my-team', 'my-admin-team'],
        'repo4': ['my-admin-team']
    }

    actual_report = get_shared_ownership_report(token, org_name, ignored_teams)

    assert expected_shared_ownership_report == actual_report
