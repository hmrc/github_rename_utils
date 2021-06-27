from sgqlc.endpoint.requests import RequestsEndpoint

def create_graphql_endpoint(token, rate_limit_store=None):
    url = 'https://api.github.com/graphql'
    headers = { 'Authorization': f'bearer {token}' }

    endpoint = RequestsEndpoint(url, headers)

    def do_request(op, vars):
        rate_limit = op.rate_limit()
        rate_limit.limit()
        rate_limit.cost()
        rate_limit.remaining()
        rate_limit.reset_at()

        data = endpoint(op, vars)
        interpreted_response = (op + data)

        if rate_limit_store:
            rate_limit = interpreted_response.rate_limit
            rate_limit_store.put(
                'graphql',
                rate_limit.cost,
                rate_limit.reset_at
            )

        return interpreted_response

    return do_request

valid_permissions = ['ADMIN', 'MAINTAIN', 'WRITE', 'TRIAGE', 'READ']
