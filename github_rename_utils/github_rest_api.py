import github3
from datetime import datetime


def rest_client(token):
    client = github3.login(token=token)
    if not client:
        raise Exception("Can't connect to github")

    client.session.headers.update({
        "Accept": "application/vnd.github.v3.full+json,application/vnd.github.v3+json,application/vnd.github.luke-cage-preview+json,application/vnd.github.zzzax-preview+json" 
    })

    return client

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

    return github3.GitHub(session=session)
