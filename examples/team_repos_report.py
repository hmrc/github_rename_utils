import os
from github_rename_utils.github_graphql_api import GithubGraphqlEndpoint
from github_rename_utils.github_rate_limit import InMemoryRateLimitStore
from github_rename_utils.team_repo_report import get_team_repo_report
from pprint import pprint


org_name = "my-org"
team_name = "my-team"
branch_name = "old-branch"

token = os.getenv("GH_TOKEN")

rate_limit_store = InMemoryRateLimitStore()
endpoint = GithubGraphqlEndpoint(token, rate_limit_store=rate_limit_store)

report = get_team_repo_report(endpoint, org_name, team_name, branch_name)

pprint(report)
pprint(rate_limit_store.values)
