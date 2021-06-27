import os
from github_rename_utils.github_graphql_api import create_graphql_endpoint
from github_rename_utils.github_rate_limit import InMemoryRateLimitStore, monitor_graphql_endpoint
from github_rename_utils.team_repo_report import get_team_repo_report
from pprint import pprint


org_name = "my-org"
team_name = "my-team"

token = os.getenv("GH_TOKEN")

endpoint = create_graphql_endpoint(token)
rate_limit_store = InMemoryRateLimitStore()
monitored_endpoint = monitor_graphql_endpoint(endpoint, rate_limit_store)

report = get_team_repo_report(monitored_endpoint, org_name, team_name)

pprint(report)
pprint(rate_limit_store.values)
