import os
import json
import github_rename_utils.shared_ownership_report as utils
from github_rename_utils.github_graphql_api import create_graphql_endpoint


def integration_test_can_get_ownership_report():
    # integration test! may use 250 points against rate limiting on graphql endpoint
    token = os.environ['GH_TOKEN']

    assert token is not None

    org = 'hmrc'
    ignored_teams = ['my-admin-team']

    endpoint = create_graphql_endpoint(token)
    report = utils.get_shared_ownership_report(endpoint, org, ignored_teams)
    print(report)

    assert len(report) > 0

    with open('./shared_ownership.json', 'w', encoding='utf-8') as fh:
        json.dump(report, fh, indent=4, sort_keys=True)

    assert 1 == 2
