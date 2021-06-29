from github3 import GitHub
from github3.session import GitHubSession
from datetime import datetime


class GithubSessionWrapper:
    def __init__(self, session, rate_limit_store=None):
        self._wrapped = session
        self.rate_limit_store = rate_limit_store

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        return getattr(self._wrapped, attr)

    def request(self, method, url, headers={}, **kwargs):
        headers = {
            **headers,
            "Accept": "application/vnd.github.v3.full+json,application/vnd.github.v3+json,application/vnd.github.luke-cage-preview+json,application/vnd.github.zzzax-preview+json" 
        }

        response = self._wrapped.request(method, url, headers=headers, **kwargs)

        if self.rate_limit_store is not None:
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

class GithubRestClient(GitHub):
    def __init__(self, token, session=GitHubSession(), rate_limit_store=None):
        wrapped_session = GithubSessionWrapper(session, rate_limit_store=rate_limit_store)

        super(GithubRestClient, self).__init__(token=token, session=wrapped_session)
