def get_repository(github_client, org, name):
    results = github_client.github.search_repositories(f"repo:{org}/{name}")
    result = results.next()
    return result.repository

def is_repository_shared(repo, owners):
    teams = repo.teams()
    ownership_threshold = len(owners)

    count_teams = 0
    for team in teams:
        count_teams += 1
        if count_teams > ownership_threshold:
            break

    return ownership_threshold < count_teams

def copy_branch(repo, source_branch_name, dest_branch_name):
    source_sha = repo.branch(source_branch_name).commit.sha

    ref = repo.create_ref(f"refs/heads/{dest_branch_name}", source_sha)
    new_branch = repo.branch(dest_branch_name)

    return new_branch

def update_pull_requests(repo, old_base_name, new_base_name):
    prs = repo.pull_requests(state='open', base=old_base_name)

    failures = 0
    count = 0
    for pr in prs:
        count += 1
        try:
            # Modified = false where it is an idempotent success
            modified = pr.update(base=new_base_name)
        except Exception:
            failures +=1

    return (count, failures)

def get_webhook_report(repo):
    hooks = repo.hooks()

    results = [hook.config['url'] for hook in hooks if hook.active]

    return results

def update_default_branch(github_client, org, repo, new_branch_name):
    success = repo.edit(repo.name, default_branch=new_branch_name)

    updated_repo = get_repository(github_client, org, repo.name)

    return updated_repo