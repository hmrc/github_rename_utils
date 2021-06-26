from collections import defaultdict
from github_rename_utils.shared_ownership_report_utils import get_team_names, get_repo_names_for_team


def get_shared_ownership_report(endpoint, org, ignored_teams):
    teams = get_team_names(endpoint, org) # 7 seconds

    report = defaultdict(list)

    for team in teams:
        if team in ignored_teams:
            continue
        repos = get_repo_names_for_team(endpoint, team, org)
        for repo in repos:
            report[repo].append(team)

    return report
