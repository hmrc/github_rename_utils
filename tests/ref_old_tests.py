import responses
from github_rename_utils.github_wrapper import get_github_client
from github_rename_utils.github_requests import get_default_branch_report
from tests.mock_rest_payloads import owning_team, repos_body, \
  prs_body, hook_data, owning_teams, shared_teams


@responses.activate
def test_get_report_returns_three_complete_entries():
    org = "my-org"
    user = "app"
    token = "__dummy__"
    team = "my-team"

    responses.add(responses.GET, "https://api.github.com/orgs/my-org/teams/my-team",
                            body=owning_team,
                            content_type='text/json')

    responses.add(responses.GET, "https://api.github.com/teams/2/repos?per_page=100&page=1",
                            body=repos_body,
                            content_type='text/json', 
                            match_querystring=True)

    responses.add(responses.GET, "https://api.github.com/teams/2/repos?per_page=100&page=2",
                            body='[]',
                            content_type='text/json', 
                            match_querystring=True)

    responses.add(responses.GET, 'https://api.github.com/repos/my-org/Hello-World/pulls?state=open',
                            body='[]',
                            content_type='text/json')

    responses.add(responses.GET, 'https://api.github.com/repos/my-org/Hello-New-World/pulls?state=open',
                            body=prs_body,
                            content_type='text/json')

    responses.add(responses.GET, 'https://api.github.com/repos/my-org/Hello-Shared-World/pulls?state=open',
                            body=prs_body,
                            content_type='text/json')

    responses.add(responses.GET, 'https://api.github.com/repos/my-org/Hello-World/hooks',
                          body='[]',
                          content_type='text/json')

    responses.add(responses.GET, 'https://api.github.com/repos/my-org/Hello-New-World/hooks',
                          body=hook_data,
                          content_type='text/json')

    responses.add(responses.GET, 'https://api.github.com/repos/my-org/Hello-Shared-World/hooks',
                          body=hook_data,
                          content_type='text/json')

    responses.add(responses.GET, "http://not-shared.com",
                            body=owning_teams,
                            content_type='text/json')

    responses.add(responses.GET, "http://shared.com",
                            body=shared_teams,
                            content_type='text/json')

    client = get_github_client(org, team, user, token)
    data = get_default_branch_report(client, ["my-team"],[])

    assert 3 == len(data)
    assert 1 == data[1]['open_prs']
    assert 'main' == data[1]['default_branch']
    assert 'tess/Hello-World' == data[0]['full_name']
    assert 0 == data[0]['open_prs']