import os
from github_rename_utils.rate_limit import InMemoryRateLimitStore
from github_rename_utils.github_graphql_api import create_graphql_endpoint
from github_rename_utils.shared_ownership_report import get_shared_ownership_report
from pprint import pprint


org_name = "my-org"
ignored_team_names = ["my-admin-team"]

token = os.getenv("GH_TOKEN")

def rate_limit_callback(values):
  pprint(values)

with InMemoryRateLimitStore(rate_limit_callback) as rate_limit_store:
  endpoint = create_graphql_endpoint(token)

  report = get_shared_ownership_report(endpoint, org_name, ignored_team_names)
  pprint(report)
