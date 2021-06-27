import os
from github_rename_utils.rate_limit import InMemoryRateLimitStore
from github_rename_utils.github_graphql_api import create_graphql_endpoint
from github_rename_utils.team_repo_report import get_team_repo_report
from pprint import pprint


org_name = "my-org"
team_name = "my-team"

token = os.getenv("GH_TOKEN")

def rate_limit_callback(values):
  pprint(values)

with InMemoryRateLimitStore(rate_limit_callback) as rate_limit_store:
  endpoint = create_graphql_endpoint(token, rate_limit_store)

  report = get_team_repo_report(endpoint, org_name, team_name)
  pprint(report)
