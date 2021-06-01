from sgqlc.operation import Operation
from sgqlc.endpoint.requests import RequestsEndpoint
from github_rename_utils.schema import github_schema as schema

def initialise_endpoint(token):
    url = 'https://api.github.com/graphql'
    headers = {'Authorization': f'bearer {token}'}
    endpoint = endpoint = RequestsEndpoint(url, headers)
    return endpoint

def get_repo_data(org, team, name, endpoint):
    op = Operation(schema.Query)  # note 'schema.'

    # -- code below follows as the original usage example:

    # select a field, here with selection arguments, then another field:
    branches = op.repository(owner=org, name=name).refs(ref_prefix='refs/heads/', first=10)
    # select sub-fields explicitly: { nodes { number title } }
    branches.nodes.name()
    branches.total_count()

    # you can print the resulting GraphQL
    # print(op)

    # Call the endpoint:
    data = endpoint(op)

    # Interpret results into native objects
    repo = (op + data).repository
    # for branch in repo.refs.nodes:
    #     print(branch.name)

    return repo