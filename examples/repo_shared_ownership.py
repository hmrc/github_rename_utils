from collections import defaultdict
from github_rename_utils.graphql_utils import initialise_endpoint
from github_rename_utils.shared_ownership_utils import get_team_names, get_repo_names_for_team


def get_shared_ownership_report(token, org, ignored_teams):
 
    endpoint = initialise_endpoint(token)
    teams = get_team_names(endpoint, org) # 7 seconds

    report = defaultdict(list)

    for team in teams:
        if team in ignored_teams:
            continue
        repos = get_repo_names_for_team(endpoint, team, org)
        for repo in repos:
            report[repo].append(team)

    return report
