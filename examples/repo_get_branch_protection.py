import os
from github_rename_utils.github_rest_api import create_rest_client
from github_rename_utils.branch_rename_utils import get_branch_protection

token = os.getenv("GH_TOKEN")
client = create_rest_client(token)

res = get_branch_protection(client, 'hmrc', 'github_rename_utils', 'main')
print(res)
