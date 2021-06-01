'''
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

'''
import os
from pprint import pprint
from github_rename_utils.github_wrapper import get_github_client
from github_rename_utils.github_requests import copy_branch_protection, \
    delete_old_branch_protection, delete_branch
from github_rename_utils.rename_utils import get_repository, is_repository_shared, \
    copy_branch, update_pull_requests, \
    get_webhook_report, update_default_branch

def convert_repo(client, org_name, repo_name, desired_branch_name):
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

    new_branch = copy_branch(repo, repo.default_branch, desired_branch_name)
    attempted,failed = update_pull_requests(repo, repo.default_branch, desired_branch_name)
    report_lines.append(f"{attempted} pull request rebases attempted, {failed} failed.")

    copy_success = copy_branch_protection(client, repo.name, repo.default_branch, desired_branch_name)
    if not copy_success:
        report_lines.append(f"Unable to copy branch protection for {repo_name}. Escaping before finishing!!")
        return False,report_lines
    else:
        report_lines.append("Branch protection copied")
        updated_repo = update_default_branch(client, org_name, repo, desired_branch_name)
        report_lines.append(f"New default branch set to {desired_branch_name}")
        report_lines.append(f"Deleting protection on old default branch {old_branch_name}")
        update_success = delete_old_branch_protection(client, repo.name, old_branch_name)
        report_lines.append(f"Deleting old default branch {old_branch_name}")
        delete_success = delete_branch(client, repo_name, old_branch_name)
        if not delete_success:
            report_lines.append(f"Unable to delete old default branch {old_branch_name}. stopping!")
            return False,report_lines
        else:
            report_lines.append(f"Successfully deleted old default branch {old_branch_name}")

    return (True, report_lines)


if __name__ == "__main__":

    """
    import argparse

    parser = argparse.ArgumentParser(description='Arguments for github branch renamer.')
    parser.add_argument('-r','--repositories', nargs='+', help='<Required> Set flag', required=True)
    parser.add_argument('-n','--new-name', help='<Required> Set flag', required=True)
    # python test.py -n "main" -r "repo1 repo2 repo3"

    """

    desired = "main"
    repos = []
    
    token = os.getenv("GH_TOKEN")
    org = "my-org"
    client = get_github_client(org, None, token)
    report = []

    for repo_name in repos:
        success, repo_report = convert_repo(client, org, repo_name, desired)
        report.extend(repo_report)
        pprint(success)

    pprint(report)
