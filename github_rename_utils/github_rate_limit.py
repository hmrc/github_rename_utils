from datetime import datetime
from github3 import GitHub


class InMemoryRateLimitStore:
    def __init__(self):
        self.values = {}

    def put(self, resource, cost, reset_at):
        self.values[resource] = {
            "cost": self.values[resource]["cost"] + cost,
            "reset_at": max([self.values[resource]["reset_at"], reset_at])
        } if resource in self.values else {
            "cost": cost,
            "reset_at": reset_at
        }

    def reset(self):
        self.values = {}


class GithubSessionWrapper:
    def __init__(self, session, rate_limit_store):
        self._wrapped = session
        self.rate_limit_store = rate_limit_store

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        return getattr(self._wrapped, attr)

    def request(self, method, url, **kwargs):
        response = self._wrapped.request(method, url, **kwargs)

        self.rate_limit_store.put(
            response.headers["X-RateLimit-Resource"],
            1,
            datetime.fromtimestamp(int(response.headers["X-RateLimit-Reset"]))
        )

        return response

    def get(self, url, params=None, **kwargs):
        return self.request('get', url, params=params, **kwargs)
    
    def options(self, url, **kwargs):
        return self.request('options', url, **kwargs)

    def head(self, url, **kwargs):
        kwargs.setdefault('allow_redirects', False)
        return self.request('head', url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request('post', url, data=data, json=json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request('put', url, data=data, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request('patch', url, data=data, **kwargs)
    
    def delete(self, url, **kwargs):
        return self.request('delete', url, **kwargs)


def monitor_rest_client(client, rate_limit_store):
    session = GithubSessionWrapper(client.session, rate_limit_store)

    return GitHub(session=session)


def monitor_graphql_endpoint(endpoint, rate_limit_store):
    def do_request(op, vars):
        rate_limit = op.rate_limit()
        rate_limit.limit()
        rate_limit.cost()
        rate_limit.remaining()
        rate_limit.reset_at()

        data = endpoint(op, vars)

        if rate_limit_store:
            rate_limit_store.put(
                'graphql',
                data.rate_limit.cost,
                data.rate_limit.reset_at
            )

        return data

    return do_request
