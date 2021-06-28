import os
from github_rename_utils.github_graphql_api import graphql_endpoint, monitor_graphql_endpoint
from github_rename_utils.github_rate_limit import InMemoryRateLimitStore
from github_rename_utils.shared_ownership_report import get_shared_ownership_report
from pprint import pprint


org_name = "my-org"
ignored_team_names = ["my-admin-team"]

token = os.getenv("GH_TOKEN")

endpoint = graphql_endpoint(token)
rate_limit_store = InMemoryRateLimitStore()
monitored_endpoint = monitor_graphql_endpoint(endpoint, rate_limit_store)

report = get_shared_ownership_report(monitored_endpoint, org_name, ignored_team_names)

pprint(report)
pprint(rate_limit_store.values)
