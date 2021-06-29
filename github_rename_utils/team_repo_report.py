from github_rename_utils.team_repo_report_utils import build_team_report_query, \
    build_team_report_variables, map_repository_data_list


def get_team_repo_report(endpoint, org, team, include_read=False, include_archived=False):

    # we assume the unwanted branch name is 'master'
    unwanted_branch_name = "master"
    repo_page_cursor = ''

    mapped_repo_list = []

    op = build_team_report_query()
    variables = build_team_report_variables(org, team, repo_page_cursor, unwanted_branch_name)
    data = endpoint(op, variables)

    while (data.organization.team.repositories.page_info.has_next_page):
        mapped_repo_list.extend(map_repository_data_list(data, include_read=include_read, include_archived=include_archived))
        repo_page_cursor = data.organization.team.repositories.page_info.end_cursor
        variables = build_team_report_variables(org, team, repo_page_cursor, unwanted_branch_name)
        data = endpoint(op, variables)
    
    # last data batch
    mapped_repo_list.extend(map_repository_data_list(data, include_read=include_read, include_archived=include_archived))

    return mapped_repo_list
