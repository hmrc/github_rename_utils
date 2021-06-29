from sgqlc.endpoint.requests import RequestsEndpoint


class GithubGraphqlEndpoint:
    def __init__(self, token, session=None, rate_limit_store=None):
        url = 'https://api.github.com/graphql'
        self.base_headers = { 'Authorization': f'bearer {token}' }

        self.endpoint = RequestsEndpoint(url, session=session)
        self.session = self.endpoint.session
        self.rate_limit_store = rate_limit_store

    def __call__(self, op, vars):
        if self.rate_limit_store is not None:
            rate_limit = op.rate_limit()
            rate_limit.limit()
            rate_limit.cost()
            rate_limit.remaining()
            rate_limit.reset_at()

        data = self.endpoint(op, vars, extra_headers=self.base_headers)
        interpreted_data = (op + data)

        if self.rate_limit_store is not None:
            self.rate_limit_store.put(
                'graphql',
                interpreted_data.rate_limit.cost,
                interpreted_data.rate_limit.reset_at
            )

        return interpreted_data

valid_permissions = ['ADMIN', 'MAINTAIN', 'WRITE', 'TRIAGE', 'READ']
