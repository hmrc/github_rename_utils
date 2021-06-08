import requests
import json

def request_headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json,application/vnd.github.luke-cage-preview+json,application/vnd.github.zzzax-preview+json"
    }

def get_team_repos(git_accessor, owners, admins):

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
            teams_response = requests.get(repo['teams_url'], headers=request_headers(git_accessor.token))
            teams = teams_response.json()
            sharing_teams = [team for team in teams if team['slug'] not in ignore_teams]
            repo["number_teams_sharing"] = len(sharing_teams)
            repos.append(repo)
        page += 1

    return repos

def get_default_branch_report(git_accessor, expected_owners, expected_admins):
    report_entries = []
    repos = get_team_repos(git_accessor, expected_owners, expected_admins)
    for repo in repos:
        entry = {"full_name": repo["full_name"], "default_branch": repo["default_branch"]}
        pr_list_data = get_open_pull_requests(git_accessor,repo["name"])
        entry["open_prs"] = len(pr_list_data)
        entry["shared"] = repo["number_teams_sharing"]
        report_entries.append(entry)
    return report_entries

def get_webhooks(git_accessor, repo_name):
    url = f'https://api.github.com/repos/{git_accessor.org_name}/{repo_name}/hooks'
    response = requests.get(url, headers=request_headers(git_accessor.token))
    return response.json()

def get_open_pull_requests(git_accessor, repo_name):
    pr_url = f'https://api.github.com/repos/{git_accessor.org_name}/{repo_name}/pulls?state=open'
    response = requests.get(pr_url, headers=request_headers(git_accessor.token))
    return response.json()
    
def get_branch_details(git_accessor, repo_name, branch):
    branch_url = f'https://api.github.com/repos/{git_accessor.org_name}/{repo_name}/branches/{branch}'
    response = requests.get(branch_url, headers=request_headers(git_accessor.token))
    return response.json()

def get_repos(git_accessor):
    # in this example the org and the user are the same 
    # - will not be so in prod, we will expect a team in prod
    # user repos: 'https://api.github.com/user/repos'
    # org team repos: '/orgs/{org}/teams/{team_slug}/repos'
    repos_url = f'https://api.github.com/orgs/{git_accessor.org_name}/repos'
    if git_accessor.team:
        repos_url = f'https://api.github.com/orgs/{git_accessor.org_name}/teams/{git_accessor.team}/repos'
    
    response = requests.get(repos_url, headers=request_headers(git_accessor.token))
    return response.json()