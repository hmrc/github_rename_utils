from sgqlc.endpoint.requests import RequestsEndpoint

def initialise_endpoint(token):
    url = 'https://api.github.com/graphql'
    headers = {'Authorization': f'bearer {token}'}
    endpoint = RequestsEndpoint(url, headers)
    return endpoint