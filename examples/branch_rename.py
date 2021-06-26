import os
from github_rename_utils.github_rest_api import create_rest_client
from github_rename_utils.branch_rename import rename_default_branch
from pprint import pprint


org_name = "my-org"
repo_name = "my-repo"
desired_branch_name = "main"

token = os.getenv("GH_TOKEN")
client = create_rest_client(token)

_, report = rename_default_branch(client, org_name, repo_name, desired_branch_name)

pprint(report)
