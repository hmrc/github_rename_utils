import os
import json
import examples.repo_shared_ownership as utils

def integration_test_can_get_ownership_report():
    # integration test! may use 250 points against rate limiting on graphql endpoint
    token = os.environ['GH_TOKEN']

    assert token is not None

    org = 'hmrc'
    ignored_teams = ['my-admin-team']

    report = utils.get_shared_ownership_report(token, org, ignored_teams)
    print(report)

    assert len(report) > 0

    with open('./shared_ownership.json', 'w', encoding='utf-8') as fh:
        json.dump(report, fh, indent=4, sort_keys=True)

    assert 1 == 2
