from sgqlc.endpoint.requests import RequestsEndpoint


def graphql_endpoint(token):
    url = 'https://api.github.com/graphql'
    headers = { 'Authorization': f'bearer {token}' }

    endpoint = RequestsEndpoint(url, headers)

    def do_request(op, vars):
        data = endpoint(op, vars)

        return (op + data)

    return do_request

def monitor_graphql_endpoint(endpoint, rate_limit_store):
    def do_request(op, vars):
        rate_limit = op.rate_limit()
        rate_limit.limit()
        rate_limit.cost()
        rate_limit.remaining()
        rate_limit.reset_at()

        data = endpoint(op, vars)

        rate_limit_store.put(
            'graphql',
            data.rate_limit.cost,
            data.rate_limit.reset_at
        )

        return data

    return do_request

valid_permissions = ['ADMIN', 'MAINTAIN', 'WRITE', 'TRIAGE', 'READ']
