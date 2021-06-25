from sgqlc.endpoint.requests import RequestsEndpoint


def initialise_endpoint(token):
    url = 'https://api.github.com/graphql'
    headers = { 'Authorization': f'bearer {token}' }

    endpoint = RequestsEndpoint(url, headers)

    return endpoint

def query_add_rate_limiting_data(op):
    rate_limit = op.rate_limit()
    rate_limit.limit()
    rate_limit.cost()
    rate_limit.remaining()
    rate_limit.reset_at()

valid_permissions = ['ADMIN', 'MAINTAIN', 'WRITE', 'TRIAGE', 'READ']
