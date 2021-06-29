def get_repository(client, org_name, repo_name):
    results = client.search_repositories(f"repo:{org_name}/{repo_name}")
    result = results.next()
    return result.repository

def is_repository_shared(repo, owners):
    teams = repo.teams()
    ownership_threshold = len(owners)

    count_teams = 0
    for _ in teams:
        count_teams += 1
        if count_teams > ownership_threshold:
            break

    return ownership_threshold < count_teams

def copy_branch(repo, source_branch_name, dest_branch_name):
    source_sha = repo.branch(source_branch_name).commit.sha

    repo.create_ref(f"refs/heads/{dest_branch_name}", source_sha)
    new_branch = repo.branch(dest_branch_name)

    return new_branch

def update_pull_requests(repo, old_base_name, new_base_name):
    prs = repo.pull_requests(state='open', base=old_base_name)

    failures = 0
    count = 0
    for pr in prs:
        count += 1
        try:
            pr.update(base=new_base_name)
        except Exception:
            failures +=1

    return (count, failures)

def get_webhook_report(repo):
    hooks = repo.hooks()

    results = [hook.config['url'] for hook in hooks if hook.active]

    return results

def update_default_branch(client, org_name, repo, new_branch_name):
    repo.edit(repo.name, default_branch=new_branch_name)

    updated_repo = get_repository(client, org_name, repo.name)

    return updated_repo

def get_branch_protection(client, org_name, repo_name, branch_name):
    url = client.session.build_url('repos', org_name, repo_name, 'branches', branch_name, 'protection')
    response = client.session.get(url)

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


def copy_branch_protection(client, org_name, repo_name, old_branch, new_branch):
    # assumes that new branch exists but protection has not yet been added
    # - protection is only available on public repos for free account
    data = get_protection_template()

    data['owner'] = org_name
    data['repo'] = repo_name
    data['branch'] = new_branch

    existing_protection = get_branch_protection(client, org_name, repo_name, old_branch)

    data = map_branch_protection_payload(existing_protection, data)

    url = client.session.build_url('repos', org_name, repo_name, 'branches', new_branch, 'protection')
    response = client.session.put(url, json=data)

    return response.status_code == 200

def delete_old_branch_protection(client, org_name, repo_name, branch_name):
    url = client.session.build_url('repos', org_name, repo_name, 'branches', branch_name, 'protection')
    response = client.session.delete(url)

    return response.status_code == 204

def delete_branch(client, org_name, repo_name, branch_name):
    url = client.session.build_url('repos', org_name, repo_name, 'git', 'refs', 'heads', branch_name)
    response = client.session.delete(url)

    return response.status_code == 204
