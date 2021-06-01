import github3

def get_github_client(org_name, team, token):
    connection = HMRCGithubClient(org_name, team, token)
    return connection

class HMRCGithubClient:
    '''
    This client can work in two modes, 
    1. calls on self.github and returned wrapped objects
    invoke logic from the github3 library
    2. we can use the stored org name to build raw urls to call 
    github api direct with auth from the user and pa token
    This is useful as the github3 library does not handle everything
    '''
    def __init__(self, org_name, team, token):
        self.org_name = org_name
        self.team = team
        self.token = token

        self.github = github3.login(token=token)

        if not self.github:
            raise Exception("Can't connect to github")

        self.org = self.github.organization(org_name)
        if not self.org:
            raise Exception("Can't get github org")