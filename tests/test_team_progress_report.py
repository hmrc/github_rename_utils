import os
from github_rename_utils.github_wrapper import get_github_client
from github_rename_utils.rename_utils import get_repository, get_webhook_report

'''
This is the REST approach for reporting which will not be efficient to scale
This is left in as a reference for business process for future code 
written against the github4 endpoint
'''

def integration_test_repo_hooks_can_be_checked():
    """Real call and will break with example org and repo"""
    token = os.getenv("GH_TOKEN")
    if not token:
        raise Exception("Token is needed for integration tests.")
    org = "my-org"
    client = get_github_client(org, None, token)
    repo = get_repository(client, "my-org", "my-repo")

    targets = get_webhook_report(repo)

    assert 3 == len(targets)
