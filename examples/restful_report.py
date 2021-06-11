"""
This is the REST approach for reporting which will not be efficient to scale
This is left in as a reference for business process for future code 
written against the github4 endpoint
"""

import requests
import json
from github_rename_utils.rest_report_utils import get_sharing_teams


def request_headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json,application/vnd.github.luke-cage-preview+json,application/vnd.github.zzzax-preview+json"
    }


def get_team_repos_full_data(git_accessor, owners, admins):

    team_resp = requests.get(f'https://api.github.com/orgs/{git_accessor.org_name}/teams/{git_accessor.team}',
                            headers=request_headers(git_accessor.token))
    team = team_resp.json()
    base_url = f"{team['repositories_url']}?per_page=100&page="

    data_left = True
    page=1
    repos = []
    ignore_teams = owners
    ignore_teams.extend(admins)

    while data_left:
        repos_url = f'{base_url}{page}'
        response = requests.get(repos_url, headers=request_headers(git_accessor.token))

        if response.status_code != 200:
            data_left = False

        data = response.json()
        if len(data) == 0:
            data_left = False

        for repo in data:
            sharing_teams = get_sharing_teams(git_accessor=git_accessor, 
                repo_name=repo['name'],
                ignore_team_slugs=ignore_teams)
            repo["number_teams_sharing"] = len(sharing_teams)
            repos.append(repo)
        page += 1

    return repos

def get_open_pull_requests(git_accessor, repo_name):
    pr_url = f'https://api.github.com/repos/{git_accessor.org_name}/{repo_name}/pulls?state=open'
    response = requests.get(pr_url, headers=request_headers(git_accessor.token))
    return response.json()

def get_default_branch_report(git_accessor, expected_owners, expected_admins):
    report_entries = []
    repos = get_team_repos_full_data(git_accessor, expected_owners, expected_admins)
    for repo in repos:
        entry = {"full_name": repo["full_name"], "default_branch": repo["default_branch"]}
        pr_list_data = get_open_pull_requests(git_accessor,repo["name"])
        entry["open_prs"] = len(pr_list_data)
        entry["shared"] = repo["number_teams_sharing"]
        report_entries.append(entry)
    return report_entries