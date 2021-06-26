import os
from github_rename_utils.github_graphql_api import create_graphql_endpoint
from github_rename_utils.team_repo_report import get_repo_data
from pprint import pprint


org_name = "my-org"
team_name = "my-team"

token = os.getenv("GH_TOKEN")
endpoint = create_graphql_endpoint(token)

report = get_repo_data(endpoint, org_name, team_name)
pprint(report)
