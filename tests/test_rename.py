from unittest.mock import Mock

class StubClient():

    org_name = 'dummy_org'
    team = 'dummy_team'
    token = '__dummy__'

    github = {
        'repository': Mock()
    }

class StubRepoSameBranch():
    def __init__(self, expected_branch):
        self.default_branch = expected_branch


def test_skip_existing_desired_default_branch(monkeypatch):
    """
    Repo will be skipped if default branch is already desired branch
    """

    expected_branch = 'main'
    expected_report = "default branch is already desired branch name"
    def mock_get_repo(client, org_name, repo_name):
        return StubRepoSameBranch(expected_branch)

    client = StubClient()
    import github_rename_utils.rename as rename
    monkeypatch.delattr("requests.sessions.Session.request")
    with monkeypatch.context() as m:
        # monkey patch out get_repository call in rename, this returns a simple object with only one property (default_branch)
        m.setattr(rename, 'get_repository', mock_get_repo)

        success, report = rename.convert_repo(client, 'dummy', 'repo', "main")

        assert success == True
        assert expected_report in report
