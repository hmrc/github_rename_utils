import os
from github_rename_utils.github_rest_api import GithubRestClient
from github_rename_utils.github_rate_limit import InMemoryRateLimitStore
from github_rename_utils.branch_rename import rename_default_branch
from pprint import pprint


org_name = "my-org"
repo_name = "my-repo"
desired_branch_name = "main"

token = os.getenv("GH_TOKEN")

rate_limit_store = InMemoryRateLimitStore()
client = GithubRestClient(token, rate_limit_store=rate_limit_store)

_, report = rename_default_branch(client, org_name, repo_name, desired_branch_name)

pprint(report)
pprint(rate_limit_store.values)
