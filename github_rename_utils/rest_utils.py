import github3


def create_rest_client(token):
    client = github3.login(token=token)
    if not client:
        raise Exception("Can't connect to github")

    client.session.headers.update({
        "Accept": "application/vnd.github.v3.full+json,application/vnd.github.v3+json,application/vnd.github.luke-cage-preview+json,application/vnd.github.zzzax-preview+json" 
    })

    return client
