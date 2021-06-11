import responses
from github_rename_utils.github_wrapper import get_github_client
from github_rename_utils.rest_report_utils import get_sharing_teams, \
    get_active_webhook_urls
from tests.mock_rest_payloads import org_result, hook_data, \
    owning_teams, shared_teams, shared_teams_admin_only

def setup_org(org_name="my-org"):
    responses.add(responses.GET, f"https://api.github.com/orgs/{org_name}",
                            body=org_result,
                            status=200,
                            content_type='text/json')
                            

@responses.activate
def test_get_sharing_teams_never_returns_own_team():
    org = "my-org"
    token = "__dummy__"
    team = "my-team"
    repo_name = "my-repo"
    setup_org()

    responses.add(responses.GET, 'https://api.github.com/repos/my-org/my-repo/teams',
                    content_type='application/json',
                    body=owning_teams)

    client = get_github_client(org, team, token)
    sharing_teams = get_sharing_teams(client, repo_name)

    assert 0 == len(sharing_teams)

@responses.activate  
def test_get_sharing_teams_with_ignored_teams_returns_zero_teams():

    org = "my-org"
    token = "__dummy__"
    team = "my-team"
    repo_name = "my-repo"
    setup_org()

    responses.add(responses.GET, 'https://api.github.com/repos/my-org/my-repo/teams',
                    content_type='application/json',
                    body=shared_teams_admin_only)

    client = get_github_client(org, team, token)
    ignore_these = ["known-admin-team"]
    sharing_teams = get_sharing_teams(client, repo_name, ignore_these)

    assert 0 == len(sharing_teams)

@responses.activate
def test_get_sharing_teams_on_shared_repo_returns_shared():
    
    org = "my-org"
    token = "__dummy__"
    team = "my-team"
    repo_name = "my-repo"
    setup_org()

    responses.add(responses.GET, 'https://api.github.com/repos/my-org/my-repo/teams',
                    content_type='application/json',
                    body=shared_teams)

    client = get_github_client(org, team, token)
    ignore_these = ["known-admin-team"]
    sharing_teams = get_sharing_teams(client, repo_name, ignore_these)
    
    assert 1 == len(sharing_teams)
    assert 'justice-league' in shared_teams

@responses.activate
def test_get_webhooks_returns_expected_list_of_active_urls():
    org = "my-org"
    token = "__dummy__"
    team = "my-team"
    repo_name = "my-repo"
    setup_org()

    responses.add(responses.GET, 'https://api.github.com/repos/my-org/my-repo/hooks',
                    content_type='application/json',
                    body=hook_data)

    client = get_github_client(org, team, token)
    webhooks = get_active_webhook_urls(client, repo_name)
    
    assert 2 == len(webhooks)
    assert 'https://example.com/webhook' in webhooks
