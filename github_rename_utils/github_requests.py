import requests


def request_headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json,application/vnd.github.luke-cage-preview+json,application/vnd.github.zzzax-preview+json"
    }

def get_branch_protection(git_accessor, repo_name, branch):
    branch_url = f'https://api.github.com/repos/{git_accessor.org_name}/{repo_name}/branches/{branch}/protection'
    response = requests.get(branch_url, headers=request_headers(git_accessor.token))
    return response.json()

def get_protection_template():

    return {
        "required_status_checks": {
            "strict": True,
            "contexts": []
        },
        "enforce_admins": None,
        "allow_force_pushes": False,
        "allow_deletions": False,
        "required_linear_history": False,
        "required_signatures": True,
        "required_pull_request_reviews": {
            "dismissal_restrictions": {
                "users": [],
                "teams": []
            },
            "dismiss_stale_reviews": True,
            "require_code_owner_reviews": True,
            "required_approving_review_count": 1
        },
        "restrictions": {
            "users": [],
            "teams": [],
            "apps": []
        }
    }

def map_branch_protection_payload(existing_protection, data):
        # map specifics onto template
    if existing_protection.get('required_status_checks', None) is not None:
        data['required_status_checks']['contexts'] = existing_protection['required_status_checks']['contexts']
    else:
        data['required_status_checks'] = None 

    if existing_protection.get('enforce_admins', None) is not None and existing_protection['enforce_admins']['enabled'] == True:
        data['enforce_admins'] = True

    if existing_protection.get("required_pull_request_reviews", None) is None:
        data['required_pull_request_reviews'] = None
    else:
        existing_reviews = existing_protection['required_pull_request_reviews']
        data['required_pull_request_reviews']['dismiss_stale_reviews'] = existing_reviews['dismiss_stale_reviews']
        data['required_pull_request_reviews']['require_code_owner_reviews'] = existing_reviews['require_code_owner_reviews']

        if existing_reviews.get('required_approving_review_count', None) is not None:
            data['required_pull_request_reviews']['required_approving_review_count'] = existing_reviews['required_approving_review_count']
        else:
            data['required_pull_request_reviews']['required_approving_review_count'] = 0

        if existing_reviews.get('dismissal_restrictions', None) is not None:
            users = [user['login'] for user in existing_reviews['dismissal_restrictions']['users']]
            data['required_pull_request_reviews']['dismissal_restrictions']['users'] = users
            teams = [team['slug'] for team in existing_reviews['dismissal_restrictions']['teams']]
            data['required_pull_request_reviews']['dismissal_restrictions']['teams'] = teams

    if existing_protection.get('restrictions', None) is not None:
        users = [user['login'] for user in existing_protection['restrictions']['users']]
        data['restrictions']['users'] = users
        teams = [team['slug'] for team in existing_protection['restrictions']['teams']]
        data['restrictions']['teams'] = teams
        apps = [app['slug'] for app in existing_protection['restrictions']['apps']]
        data['restrictions']['apps'] = apps
    else: 
         data['restrictions'] = None

    if existing_protection.get('required_linear_history', None) is not None:
        data['required_linear_history'] = existing_protection['required_linear_history']['enabled']
    if existing_protection.get('required_signatures', None) is not None:
        data['required_signatures'] = existing_protection['required_signatures']['enabled']
    if existing_protection.get('allow_force_pushes', None) is not None:
        data['allow_force_pushes'] = existing_protection['allow_force_pushes']['enabled']
    if existing_protection.get('allow_deletions', None) is not None:
        data['allow_deletions'] = existing_protection['allow_deletions']['enabled']

    return data


def copy_branch_protection(git_accessor,repo_name, old_branch, new_branch):

    # assumes that new branch exists but protection has not yet been added
    # - protection is only available on public repos for free account
    data = get_protection_template()

    data['owner'] = git_accessor.org_name
    data['repo'] = repo_name
    data['branch'] = new_branch

    existing_protection = get_branch_protection(git_accessor, repo_name, old_branch)

    data = map_branch_protection_payload(existing_protection, data)

    update_url = f'https://api.github.com/repos/{git_accessor.org_name}/{repo_name}/branches/{new_branch}/protection'
    response = requests.put(url=update_url, json=data, headers=request_headers(git_accessor.token))

    return response.status_code == 200

def delete_old_branch_protection(git_accessor, repo_name, branch_name):
    update_url = f'https://api.github.com/repos/{git_accessor.org_name}/{repo_name}/branches/{branch_name}/protection'
    response = requests.delete(url=update_url, headers=request_headers(git_accessor.token))

    return response.status_code == 204

def delete_branch(git_accessor, repo_name, branch_name):
    ref = f"refs/heads/{branch_name}"
    ref_url = f'https://api.github.com/repos/{git_accessor.org_name}/{repo_name}/git/{ref}'
    response = requests.delete(ref_url, headers=request_headers(git_accessor.token))

    return response.status_code == 204

