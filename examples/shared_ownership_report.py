import os
from github_rename_utils.github_graphql_api import GithubGraphqlEndpoint
from github_rename_utils.github_rate_limit import InMemoryRateLimitStore
from github_rename_utils.shared_ownership_report import get_shared_ownership_report
from pprint import pprint


org_name = "my-org"
ignored_team_names = ["my-admin-team"]

token = os.getenv("GH_TOKEN")

rate_limit_store = InMemoryRateLimitStore()
endpoint = GithubGraphqlEndpoint(token, rate_limit_store=rate_limit_store)

report = get_shared_ownership_report(endpoint, org_name, ignored_team_names)

pprint(report)
pprint(rate_limit_store.values)
