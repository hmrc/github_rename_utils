from github_rename_utils.branch_rename_utils import get_repository, \
    copy_branch, update_pull_requests, \
    get_webhook_report, update_default_branch, \
    copy_branch_protection, delete_old_branch_protection, \
    delete_branch


def rename_default_branch(client, org_name, repo_name, desired_branch_name):
    report_lines = []
    report_lines.append(f"Converting {repo_name} to default branch name {desired_branch_name}")
    repo = get_repository(client, org_name, repo_name)
    old_branch_name = repo.default_branch
    if old_branch_name == desired_branch_name:
        report_lines.append("default branch is already desired branch name")
        return True,report_lines
 
    # don't check that repository is shared as we expect the list to be vetted

    targets = get_webhook_report(repo)
    report_lines.append("Webhooks attached to repo:")
    report_lines.extend(targets)

    copy_branch(repo, repo.default_branch, desired_branch_name)
    attempted,failed = update_pull_requests(repo, repo.default_branch, desired_branch_name)
    report_lines.append(f"{attempted} pull request rebases attempted, {failed} failed.")

    copy_success = copy_branch_protection(client, repo.name, repo.default_branch, desired_branch_name)
    if not copy_success:
        report_lines.append(f"Unable to copy branch protection for {repo_name}. Escaping before finishing!!")
        return False,report_lines
    else:
        report_lines.append("Branch protection copied")
        update_default_branch(client, org_name, repo, desired_branch_name)
        report_lines.append(f"New default branch set to {desired_branch_name}")
        report_lines.append(f"Deleting protection on old default branch {old_branch_name}")
        delete_old_branch_protection(client, repo.name, old_branch_name)
        report_lines.append(f"Deleting old default branch {old_branch_name}")
        delete_success = delete_branch(client, repo_name, old_branch_name)
        if not delete_success:
            report_lines.append(f"Unable to delete old default branch {old_branch_name}. stopping!")
            return False,report_lines
        else:
            report_lines.append(f"Successfully deleted old default branch {old_branch_name}")

    return (True, report_lines)
