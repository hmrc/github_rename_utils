"""
wrapper example has main entrypoint
this takes arguments: desired default branch name, list of repo names 
the wrapper expects the pa token of the user to have enough permissions
the wrapper gets the token from an environment variable

for each repo name in the list we will 
- perform the steps 
- report
-- whether the repo is shared outside the owning team (out of scope - relies on team name)
-- how many PRs have been rebased (and how many failed)
-- what web hooks are in play
-- that conversion was successful

! currently we will assume that repos should be changed even if shared.
! as there is no delete method on branch protection, we end up with a branch protection rule orphaned!


import argparse

parser = argparse.ArgumentParser(description='Arguments for github branch renamer.')
parser.add_argument('-r','--repositories', nargs='+', help='<Required> Set flag', required=True)
parser.add_argument('-n','--new-name', help='<Required> Set flag', required=True)
# python test.py -n "main" -r "repo1 repo2 repo3"

"""
import os
from github_rename_utils.rest_utils import create_rest_client
from github_rename_utils.rename import convert_repo
from pprint import pprint

desired = "main"
repos = []

token = os.getenv("GH_TOKEN")
org = "my-org"
client = create_rest_client(token)
report = []

for repo_name in repos:
    success, repo_report = convert_repo(client, org, repo_name, desired)
    report.extend(repo_report)
    pprint(success)

pprint(report)