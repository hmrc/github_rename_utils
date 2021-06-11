import requests
import json

'''
This is the REST approach for reporting which will not be efficient to scale
This is left in as a reference for business process for future code 
written against the github4 endpoint
'''

def request_headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json,application/vnd.github.luke-cage-preview+json,application/vnd.github.zzzax-preview+json"
    }

def get_webhooks(git_accessor, repo_name):
    url = f'https://api.github.com/repos/{git_accessor.org_name}/{repo_name}/hooks'
    response = requests.get(url, headers=request_headers(git_accessor.token))
    return response.json()

def get_active_webhook_urls(git_accessor, repo_name):
    webhooks = get_webhooks(git_accessor, repo_name)
    return [hook['config']['url'] for hook in webhooks if hook['active']]

def get_first_100_teams_for_repo(git_accessor, repo_name):
    url =f"https://api.github.com/repos/{git_accessor.org_name}/{repo_name}/teams"

    response = requests.get(url, headers=request_headers(git_accessor.token))
    return response.json()

def get_sharing_teams(git_accessor, repo_name, ignore_team_slugs = []):
    first_100_teams = get_first_100_teams_for_repo(git_accessor, repo_name)
    ignore_team_slugs.append(git_accessor.team)
    sharing_teams = [team['slug'] for team in first_100_teams if team['slug'] not in ignore_team_slugs]
    return sharing_teams
