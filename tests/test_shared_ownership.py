from github_rename_utils.shared_ownership import get_shared_ownership_report
import responses


@responses.activate
def test_get_ownership_ignores_expected_ignore_teams():
    org = 'my-org'
    team_slug = 'my-team'
    admin_team_slug = 'my-admin-team'

    def custom_callback(request):
        from tests.expected_queries import team_names_query, team_repo_name_query
        from tests.mock_payloads import team_name_list, team_repo_owner_list, team_repo_owner_admin_list

        if team_names_query(org) == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c13'}
            return (200, headers, team_name_list)

        if team_repo_name_query(org, team_slug) == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c14'}
            return (200, headers, team_repo_owner_list)

        elif team_repo_name_query(org, admin_team_slug) == request.body:
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
    ignored_teams = ['justice-league']

    expected_shared_ownership_report = {
        'repo1': [team_slug, admin_team_slug],
        'repo2': [team_slug, admin_team_slug],
        'repo3': [team_slug, admin_team_slug],
        'repo4': [admin_team_slug]
    }

    actual_report = get_shared_ownership_report(token, org, ignored_teams)

    assert expected_shared_ownership_report == actual_report
