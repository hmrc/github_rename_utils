import json
import pytest
import responses

from github_rename_utils.github_rest_api import GithubRestClient
from github_rename_utils.branch_rename_utils import get_repository, \
    copy_branch, update_pull_requests, \
    update_default_branch, copy_branch_protection, \
    get_branch_protection, delete_old_branch_protection, \
    delete_branch
from tests.mock_rest_payloads import my_repo, my_repo_search_result, \
    org_result, my_repo_branch, my_new_ref, \
    prs_body, pr_body, branch_protection


# Tests that call in gh_rerequests (responses)
# Tests that call methods in branch_rename_utils (mockclient)

class StubClient():

    org_name = 'dummy_org'
    team = 'dummy_team'
    token = '__dummy__'

    github = None

def setup_org(org_name="my-org"):
    responses.add(responses.GET, f"https://api.github.com/orgs/{org_name}",
                            body=org_result,
                            status=200,
                            content_type='text/json')

def setup_repo(org_name='my-org', repo_name='my-repo', expected_default_branch='master'):
    url = f"https://api.github.com/search/repositories?q=repo%3A{org_name}"+r"%2F"+f"{repo_name}&per_page=100"
    responses.add(responses.GET, url,
                            body=my_repo_search_result(expected_default_branch),
                            content_type='text/json',
                            status=200)

@responses.activate
def test_client_can_get_repo_from_search():

    setup_org()
    setup_repo()

    org = "my-org"
    token = '__dummy__'
    repo_name = "my-repo"

    # create the client using dummy token
    # Subsequent calls using the client need to be intercepted.

    client = GithubRestClient(token)
    repo = get_repository(client, org, repo_name)
    assert repo is not None

    assert "master" == repo.default_branch

@responses.activate
def test_branch_can_be_copied():
    """ Intercept http and mock client (get_repo) """

    setup_org()
    setup_repo()

    responses.add(responses.GET, "https://api.github.com/repos/my-org/my-repo/branches/master",
                            body=my_repo_branch,
                            content_type='text/json',
                            status=200)

    responses.add(responses.POST, "https://api.github.com/repos/my-org/my-repo/git/refs",
                            body=my_new_ref,
                            content_type='text/json',
                            status=201)

    responses.add(responses.GET, "https://api.github.com/repos/my-org/my-repo/branches/main",
                            body=my_repo_branch,
                            content_type='text/json',
                            status=200)

    token = '__dummy__'
    org = "my-org"
    client = GithubRestClient(token)
    new_branch_name = "main"

    repo = get_repository(client, org, "my-repo")
    new_branch = copy_branch(repo, repo.default_branch, new_branch_name)
    assert None is not new_branch


@pytest.mark.parametrize("status,expected_failures", [(200, 0), (401, 1)])
@responses.activate
def test_can_handle_pr_rebase_correctly(status, expected_failures):
    """
    library client
    """
    
    setup_org()
    setup_repo()

    url = "https://api.github.com/repos/my-org/my-repo/pulls?state=open&base=master&sort=created&direction=desc&per_page=100"

    responses.add(responses.GET, url, 
                    status=200,
                    body=prs_body,
                    content_type="text/json")

    patch_url = "https://api.github.com/repos/my-org/my-repo/pulls/1347"

    responses.add(responses.PATCH, 
                        url=patch_url,
                        status=status,
                        content_type="text/json",
                        body=pr_body)

    token = '__dummy__'
    org = "my-org"
    client = GithubRestClient(token)
    new_branch_name = "main"

    repo = get_repository(client, org, "my-repo")
    attempted,failed = update_pull_requests(repo, repo.default_branch, new_branch_name)

    assert 1 == attempted
    assert expected_failures == failed

@responses.activate
def test_can_retrieve_branch_protection():
    protection_url = "https://api.github.com/repos/octocat/Hello-World/branches/master/protection"
    responses.add(responses.GET, protection_url, status=200, content_type='text/json', body=branch_protection)

    token = '__dummy__'
    org = 'octocat'
    client = GithubRestClient(token)

    protection = get_branch_protection(client, org, "Hello-World", 'master')

    assert None is not protection
    assert True == protection['enforce_admins']['enabled']

@responses.activate
def test_protection_can_be_copied():
    """ Intercept http and mock client (get_repo) """

    setup_org("octocat")
    protection_url = "https://api.github.com/repos/octocat/Hello-World/branches/master/protection"
    responses.add(responses.GET, protection_url, status=200, content_type='text/json', body=branch_protection)

    put_url = "https://api.github.com/repos/octocat/Hello-World/branches/main/protection"
    responses.add(responses.PUT, put_url)

    token = '__dummy__'
    org = "octocat"
    repo = "Hello-World"
    client = GithubRestClient(token)

    success = copy_branch_protection(client, org, repo, 'master', 'main')

    assert True == success

    last_request = json.loads(responses.calls[-1].request.body)
    assert True == last_request['enforce_admins']

@responses.activate
def test_update_repo_default_branch():
    setup_org()
    setup_repo()
    setup_repo(expected_default_branch='main')

    responses.add(responses.PATCH, 'https://api.github.com/repos/my-org/my-repo',
                    status=200,
                    content_type='text/json',
                    body=my_repo('main'))

    token = '__dummy__'
    org = "my-org"

    client = GithubRestClient(token)
    repo = get_repository(client, org, "my-repo")
    new_branch_name = "main"

    updated_repo = update_default_branch(client, org, repo, new_branch_name)

    assert updated_repo is not None
    assert new_branch_name == updated_repo.default_branch

@responses.activate
def test_delete_branch():
    url = "https://api.github.com/repos/dummy_org/test/git/refs/heads/master"

    responses.add(responses.DELETE, url, status=204)

    token = '__dummy__'

    client = GithubRestClient(token)
    success = delete_branch(client, "dummy_org", "test", "master")

    assert success == True

@responses.activate
def test_delete_branch_protection():
    url = "https://api.github.com/repos/dummy_org/test/branches/master/protection"

    responses.add(responses.DELETE, url, status=204)

    token = '__dummy__'

    client = GithubRestClient(token)
    success = delete_old_branch_protection(client, "dummy_org", "test", "master")
    assert success == True
