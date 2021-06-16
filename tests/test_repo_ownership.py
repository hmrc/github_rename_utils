import os
import examples.repo_shared_ownership as utils

def integration_test_can_get_ownership_report():
    # integration test! may use 250 points against rate limiting on graphql endpoint
    token = os.environ['GH_TOKEN']
    org = 'hmrc'
    ignored_teams = ['my-admin-team']

    assert token is not None

    report = utils.get_shared_ownership_report(token, org, ignored_teams)
    print(report)
    assert len(report) > 0

    printable_report = [f'{line[0]},{line[1]}\n' for line in report]

    with open('./ownership.txt', 'w', encoding='utf-8') as fh:
        fh.writelines(printable_report)

    assert 1 == 2
