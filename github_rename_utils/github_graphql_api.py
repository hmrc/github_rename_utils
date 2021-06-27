from sgqlc.endpoint.requests import RequestsEndpoint


def create_graphql_endpoint(token):
    url = 'https://api.github.com/graphql'
    headers = { 'Authorization': f'bearer {token}' }

    endpoint = RequestsEndpoint(url, headers)

    def do_request(op, vars):
        data = endpoint(op, vars)

        return (op + data)

    return do_request

valid_permissions = ['ADMIN', 'MAINTAIN', 'WRITE', 'TRIAGE', 'READ']
