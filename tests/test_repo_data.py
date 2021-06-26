import os
import json
import github_rename_utils.team_repo_report as utils
from github_rename_utils.github_graphql_api import create_graphql_endpoint


def integration_test_can_get_repo_data():
    token = os.environ['GH_TOKEN']

    assert token is not None

    org = 'hmrc'
    team = 'ddcops'

    endpoint = create_graphql_endpoint(token)
    data = utils.get_repo_data(org, team, endpoint)
    print(data)

    assert len(data) > 0

    with open('./repo_data.json', 'w', encoding='utf-8') as fh:
        json.dump(data, fh, indent=4, sort_keys=True)

    assert 1 == 2
