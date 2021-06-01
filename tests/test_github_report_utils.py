import github_rename_utils.report as utils
import json
import os
import responses


@responses.activate
def test_get_repo_data():

    def request_callback(request):
        from tests.expected_queries import repo_branches_large_query
        from tests.mock_payloads import repo_with_64_branches

        payload = json.loads(request.body)

        if repo_branches_large_query == request.body:
            headers = {'request-id': '728d329e-0e86-11e4-a748-0c84dc037c13'}
            return (200, headers, repo_with_64_branches)
        
        else:
            print(payload)
            raise Exception('Unexpected payload received')

    responses.add_callback(
        responses.POST,
        'https://api.github.com/graphql',
        callback=request_callback,
        content_type='application/json',
    )

    team_name = 'my-team'
    org_name = 'my-org'
    repo_name = 'my-repo'
    # token = os.environ.get('GH_TOKEN', '')
    token = 'dummy_token'

    endpoint = utils.initialise_endpoint(token)

    data = utils.get_repo_data(org_name, team_name, repo_name, endpoint)

    assert data.refs.total_count == 64
