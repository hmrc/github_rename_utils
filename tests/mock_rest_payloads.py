org_result = """
{
  "login": "github",
  "id": 1,
  "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
  "url": "https://api.github.com/orgs/github",
  "repos_url": "https://api.github.com/orgs/github/repos",
  "events_url": "https://api.github.com/orgs/github/events",
  "hooks_url": "https://api.github.com/orgs/github/hooks",
  "issues_url": "https://api.github.com/orgs/github/issues",
  "members_url": "https://api.github.com/orgs/github/members{/member}",
  "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
  "avatar_url": "https://github.com/images/error/octocat_happy.gif",
  "description": "A great organization",
  "name": "github",
  "company": "GitHub",
  "blog": "https://github.com/blog",
  "location": "San Francisco",
  "email": "my-org@github.com",
  "twitter_username": "github",
  "is_verified": true,
  "has_organization_projects": true,
  "has_repository_projects": true,
  "public_repos": 2,
  "public_gists": 1,
  "followers": 20,
  "following": 0,
  "html_url": "https://github.com/my-org",
  "created_at": "2008-01-14T04:33:35Z",
  "updated_at": "2014-03-03T18:58:10Z",
  "type": "Organization",
  "total_private_repos": 100,
  "owned_private_repos": 100,
  "private_gists": 81,
  "disk_usage": 10000,
  "collaborators": 8,
  "billing_email": "mona@github.com",
  "plan": {
    "name": "Medium",
    "space": 400,
    "private_repos": 20,
    "filled_seats": 4,
    "seats": 5
  },
  "default_repository_permission": "read",
  "members_can_create_repositories": true,
  "two_factor_requirement_enabled": true,
  "members_allowed_repository_creation_type": "all",
  "members_can_create_public_repositories": false,
  "members_can_create_private_repositories": false,
  "members_can_create_internal_repositories": false,
  "members_can_create_pages": true
}

"""


repos_body = """
    [
  {
    "name": "my-repo",
    "full_name": "tess/my-repo",
    "default_branch": "master",
    "teams_url": "http://not-shared.com"
  },
  {
    "name": "Hello-New-World",
    "full_name": "tess/Hello-New-World",
    "default_branch": "main",
    "teams_url": "http://not-shared.com"
  },
  {
    "name": "Hello-Shared-World",
    "full_name": "tess/Hello-Shared-World",
    "default_branch": "main",
    "teams_url": "http://shared.com"
  }
]
    """

my_empty_search_result = """
{
  "total_count": 0,
  "incomplete_results": false,
  "items": 
  []}
"""

def my_repo(expected_default_branch):
  return """
      {
      "id": 3081286,
      "node_id": "MDEwOlJlcG9zaXRvcnkzMDgxMjg2",
      "name": "my-repo",
      "full_name": "my-org/my-repo",
      "owner": {
        "login": "dtrupenn",
        "id": 872147,
        "node_id": "MDQ6VXNlcjg3MjE0Nw==",
        "avatar_url": "https://secure.gravatar.com/avatar/e7956084e75f239de85d3a31bc172ace?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png",
        "gravatar_id": "",
        "url": "https://api.github.com/users/my-org",
        "received_events_url": "https://api.github.com/users/my-org/received_events",
        "type": "User",
        "html_url": "https://github.com/my-org",
        "followers_url": "https://api.github.com/users/my-org/followers",
        "following_url": "https://api.github.com/users/my-org/following{/other_user}",
        "gists_url": "https://api.github.com/users/my-org/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/my-org/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/my-org/subscriptions",
        "organizations_url": "https://api.github.com/users/my-org/orgs",
        "repos_url": "https://api.github.com/users/my-org/repos",
        "events_url": "https://api.github.com/users/my-org/events{/privacy}",
        "site_admin": true
      },
      "private": false,
      "html_url": "https://github.com/my-org/my-repo",
      "description": "My awesome repo",
      "fork": false,
      "url": "https://api.github.com/repos/my-org/my-repo",
      "created_at": "2012-01-01T00:31:50Z",
      "updated_at": "2013-01-05T17:58:47Z",
      "pushed_at": "2012-01-01T00:37:02Z",
      "homepage": "https://github.com",
      "size": 524,
      "stargazers_count": 1,
      "watchers_count": 1,
      "language": "Assembly",
      "forks_count": 0,
      "open_issues_count": 0,
      """ + f"""
      "master_branch": "{expected_default_branch}",
      "default_branch": "{expected_default_branch}",
      """ + """
      "score": 1,
      "archive_url": "https://api.github.com/repos/my-org/my-repo/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/my-org/my-repo/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/my-org/my-repo/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/my-org/my-repo/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/my-org/my-repo/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/my-org/my-repo/comments{/number}",
      "commits_url": "https://api.github.com/repos/my-org/my-repo/commits{/sha}",
      "compare_url": "https://api.github.com/repos/my-org/my-repo/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/my-org/my-repo/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/my-org/my-repo/contributors",
      "deployments_url": "https://api.github.com/repos/my-org/my-repo/deployments",
      "downloads_url": "https://api.github.com/repos/my-org/my-repo/downloads",
      "events_url": "https://api.github.com/repos/my-org/my-repo/events",
      "forks_url": "https://api.github.com/repos/my-org/my-repo/forks",
      "git_commits_url": "https://api.github.com/repos/my-org/my-repo/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/my-org/my-repo/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/my-org/my-repo/git/tags{/sha}",
      "git_url": "git:github.com/my-org/my-repo.git",
      "issue_comment_url": "https://api.github.com/repos/my-org/my-repo/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/my-org/my-repo/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/my-org/my-repo/issues{/number}",
      "keys_url": "https://api.github.com/repos/my-org/my-repo/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/my-org/my-repo/labels{/name}",
      "languages_url": "https://api.github.com/repos/my-org/my-repo/languages",
      "merges_url": "https://api.github.com/repos/my-org/my-repo/merges",
      "milestones_url": "https://api.github.com/repos/my-org/my-repo/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/my-org/my-repo/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/my-org/my-repo/pulls{/number}",
      "releases_url": "https://api.github.com/repos/my-org/my-repo/releases{/id}",
      "ssh_url": "git@github.com:my-org/my-repo.git",
      "stargazers_url": "https://api.github.com/repos/my-org/my-repo/stargazers",
      "statuses_url": "https://api.github.com/repos/my-org/my-repo/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/my-org/my-repo/subscribers",
      "subscription_url": "https://api.github.com/repos/my-org/my-repo/subscription",
      "tags_url": "https://api.github.com/repos/my-org/my-repo/tags",
      "teams_url": "https://api.github.com/repos/my-org/my-repo/teams",
      "trees_url": "https://api.github.com/repos/my-org/my-repo/git/trees{/sha}",
      "clone_url": "https://github.com/my-org/my-repo.git",
      "mirror_url": "git:git.example.com/my-org/my-repo",
      "hooks_url": "https://api.github.com/repos/my-org/my-repo/hooks",
      "svn_url": "https://svn.github.com/my-org/my-repo",
      "forks": 1,
      "open_issues": 1,
      "watchers": 1,
      "has_issues": true,
      "has_projects": true,
      "has_pages": true,
      "has_wiki": true,
      "has_downloads": true,
      "archived": true,
      "disabled": true,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "url": "https://api.github.com/licenses/mit",
        "spdx_id": "MIT",
        "node_id": "MDc6TGljZW5zZW1pdA==",
        "html_url": "https://api.github.com/licenses/mit"
      }
    }"""

def my_repo_search_result(expected_default_branch):
  return """
{
  "total_count": 1,
  "incomplete_results": false,
  "items": 
  [
    """ + my_repo(expected_default_branch) + """
  ]
}

"""

my_repo_branch = """
{
"_links": {"html": "https://github.com/my-org/my-repo/tree/main",
          "self": "https://api.github.com/repos/my-org/my-repo/branches/main"},
"commit": {"author": {"avatar_url": "https://avatars.githubusercontent.com/u/7059542?v=4",
                      "events_url": "https://api.github.com/users/my-user/events{/privacy}",
                      "followers_url": "https://api.github.com/users/my-user/followers",
                      "following_url": "https://api.github.com/users/my-user/following{/other_user}",
                      "gists_url": "https://api.github.com/users/my-user/gists{/gist_id}",
                      "gravatar_id": "",
                      "html_url": "https://github.com/my-user",
                      "id": 7059542,
                      "login": "my-user",
                      "node_id": "MDQ6VXNlcjcwNTk1NDI=",
                      "organizations_url": "https://api.github.com/users/my-user/orgs",
                      "received_events_url": "https://api.github.com/users/my-user/received_events",
                      "repos_url": "https://api.github.com/users/my-user/repos",
                      "site_admin": false,
                      "starred_url": "https://api.github.com/users/my-user/starred{/owner}{/repo}",
                      "subscriptions_url": "https://api.github.com/users/my-user/subscriptions",
                      "type": "User",
                      "url": "https://api.github.com/users/my-user"},
          "comments_url": "https://api.github.com/repos/my-org/my-repo/commits/b0b1530db19173902babba3a645e1c1be995aa44/comments",
          "commit": {"author": {"date": "2019-04-03T15:21:53Z",
                                "email": "my-user@users.noreply.github.com",
                                "name": "My User"},
                      "comment_count": 0,
                      "committer": {"date": "2019-04-03T15:21:53Z",
                                    "email": "my-user@users.noreply.github.com",
                                    "name": "My User"},
                      "message": "Commit message",
                      "tree": {"sha": "2c090c7134e5e819ec7b0a2c0da752c56a80a7ec",
                              "url": "https://api.github.com/repos/my-org/my-repo/git/trees/2c090c7134e5e819ec7b0a2c0da752c56a80a7ec"},
                      "url": "https://api.github.com/repos/my-org/my-repo/git/commits/b0b1530db19173902babba3a645e1c1be995aa44",
                      "verification": {"payload": null,
                                      "reason": "unsigned",
                                      "signature": null,
                                      "verified": false}},
          "committer": {"avatar_url": "https://avatars.githubusercontent.com/u/111?v=4",
                        "events_url": "https://api.github.com/users/my-user/events{/privacy}",
                        "followers_url": "https://api.github.com/users/my-user/followers",
                        "following_url": "https://api.github.com/users/my-user/following{/other_user}",
                        "gists_url": "https://api.github.com/users/my-user/gists{/gist_id}",
                        "gravatar_id": "",
                        "html_url": "https://github.com/my-user",
                        "id": 7059542,
                        "login": "my-user",
                        "node_id": "MDQ6VXNlcjcwNTk1NDI=",
                        "organizations_url": "https://api.github.com/users/my-user/orgs",
                        "received_events_url": "https://api.github.com/users/my-user/received_events",
                        "repos_url": "https://api.github.com/users/my-user/repos",
                        "site_admin": false,
                        "starred_url": "https://api.github.com/users/my-user/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/my-user/subscriptions",
                        "type": "User",
                        "url": "https://api.github.com/users/my-user"},
          "html_url": "https://github.com/my-org/my-repo/commit/b0b1530db19173902babba3a645e1c1be995aa44",
          "node_id": "MDY6Q29tbWl0MTIxMzg0NDg2OmIwYjE1MzBkYjE5MTczOTAyYmFiYmEzYTY0NWUxYzFiZTk5NWFhNDQ=",
          "parents": [{"html_url": "https://github.com/my-org/my-repo/commit/b4e1fffafd1b6b01ff30639604b6f66b0e501c6b",
                        "sha": "b4e1fffafd1b6b01ff30639604b6f66b0e501c6b",
                        "url": "https://api.github.com/repos/my-org/my-repo/commits/b4e1fffafd1b6b01ff30639604b6f66b0e501c6b"}],
          "sha": "b0b1530db19173902babba3a645e1c1be995aa44",
          "url": "https://api.github.com/repos/my-org/my-repo/commits/b0b1530db19173902babba3a645e1c1be995aa44"},
"name": "main",
"protected": true,
"protection": {"enabled": true,
              "required_status_checks": {"contexts": [],
                                          "enforcement_level": "off"}},
"protection_url": "https://api.github.com/repos/my-org/my-repo/branches/main/protection"
}
"""
pr_body = """
  {
    "url": "https://api.github.com/repos/my-org/my-repo/pulls/1347",
    "id": 1,
    "node_id": "MDExOlB1bGxSZXF1ZXN0MQ==",
    "html_url": "https://github.com/my-org/my-repo/pull/1347",
    "diff_url": "https://github.com/my-org/my-repo/pull/1347.diff",
    "patch_url": "https://github.com/my-org/my-repo/pull/1347.patch",
    "issue_url": "https://api.github.com/repos/my-org/my-repo/issues/1347",
    "commits_url": "https://api.github.com/repos/my-org/my-repo/pulls/1347/commits",
    "review_comments_url": "https://api.github.com/repos/my-org/my-repo/pulls/1347/comments",
    "review_comment_url": "https://api.github.com/repos/my-org/my-repo/pulls/comments{/number}",
    "comments_url": "https://api.github.com/repos/my-org/my-repo/issues/1347/comments",
    "statuses_url": "https://api.github.com/repos/my-org/my-repo/statuses/6dcb09b5b57875f334f61aebed695e2e4193db5e",
    "number": 1347,
    "state": "open",
    "locked": true,
    "title": "Amazing new feature",
    "user": {
      "login": "my-org",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/my-org",
      "html_url": "https://github.com/my-org",
      "followers_url": "https://api.github.com/users/my-org/followers",
      "following_url": "https://api.github.com/users/my-org/following{/other_user}",
      "gists_url": "https://api.github.com/users/my-org/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/my-org/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/my-org/subscriptions",
      "organizations_url": "https://api.github.com/users/my-org/orgs",
      "repos_url": "https://api.github.com/users/my-org/repos",
      "events_url": "https://api.github.com/users/my-org/events{/privacy}",
      "received_events_url": "https://api.github.com/users/my-org/received_events",
      "type": "User",
      "site_admin": false
    },
    "body": "Please pull these awesome changes in!",
    "body_html": "<div>Please pull these awesome changes in!</div>",
    "body_text": "",
    "labels": [
      {
        "id": 208045946,
        "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
        "url": "https://api.github.com/repos/my-org/my-repo/labels/bug",
        "name": "bug",
        "description": "Something isn't working",
        "color": "f29513",
        "default": true
      }
    ],
    "milestone": {
      "url": "https://api.github.com/repos/my-org/my-repo/milestones/1",
      "html_url": "https://github.com/my-org/my-repo/milestones/v1.0",
      "labels_url": "https://api.github.com/repos/my-org/my-repo/milestones/1/labels",
      "id": 1002604,
      "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
      "number": 1,
      "state": "open",
      "title": "v1.0",
      "description": "Tracking milestone for version 1.0",
      "creator": {
        "login": "my-org",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "gravatar_id": "",
        "url": "https://api.github.com/users/my-org",
        "html_url": "https://github.com/my-org",
        "followers_url": "https://api.github.com/users/my-org/followers",
        "following_url": "https://api.github.com/users/my-org/following{/other_user}",
        "gists_url": "https://api.github.com/users/my-org/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/my-org/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/my-org/subscriptions",
        "organizations_url": "https://api.github.com/users/my-org/orgs",
        "repos_url": "https://api.github.com/users/my-org/repos",
        "events_url": "https://api.github.com/users/my-org/events{/privacy}",
        "received_events_url": "https://api.github.com/users/my-org/received_events",
        "type": "User",
        "site_admin": false
      },
      "open_issues": 4,
      "closed_issues": 8,
      "created_at": "2011-04-10T20:09:31Z",
      "updated_at": "2014-03-03T18:58:10Z",
      "closed_at": "2013-02-12T13:22:01Z",
      "due_on": "2012-10-09T23:39:01Z"
    },
    "active_lock_reason": "too heated",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:01:12Z",
    "closed_at": "2011-01-26T19:01:12Z",
    "merged_at": "2011-01-26T19:01:12Z",
    "merge_commit_sha": "e5bd3914e2e596debea16f433f57875b5b90bcd6",
    "assignee": {
      "login": "my-org",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/my-org",
      "html_url": "https://github.com/my-org",
      "followers_url": "https://api.github.com/users/my-org/followers",
      "following_url": "https://api.github.com/users/my-org/following{/other_user}",
      "gists_url": "https://api.github.com/users/my-org/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/my-org/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/my-org/subscriptions",
      "organizations_url": "https://api.github.com/users/my-org/orgs",
      "repos_url": "https://api.github.com/users/my-org/repos",
      "events_url": "https://api.github.com/users/my-org/events{/privacy}",
      "received_events_url": "https://api.github.com/users/my-org/received_events",
      "type": "User",
      "site_admin": false
    },
    "assignees": [
      {
        "login": "my-org",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "gravatar_id": "",
        "url": "https://api.github.com/users/my-org",
        "html_url": "https://github.com/my-org",
        "followers_url": "https://api.github.com/users/my-org/followers",
        "following_url": "https://api.github.com/users/my-org/following{/other_user}",
        "gists_url": "https://api.github.com/users/my-org/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/my-org/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/my-org/subscriptions",
        "organizations_url": "https://api.github.com/users/my-org/orgs",
        "repos_url": "https://api.github.com/users/my-org/repos",
        "events_url": "https://api.github.com/users/my-org/events{/privacy}",
        "received_events_url": "https://api.github.com/users/my-org/received_events",
        "type": "User",
        "site_admin": false
      },
      {
        "login": "hubot",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://github.com/images/error/hubot_happy.gif",
        "gravatar_id": "",
        "url": "https://api.github.com/users/hubot",
        "html_url": "https://github.com/hubot",
        "followers_url": "https://api.github.com/users/hubot/followers",
        "following_url": "https://api.github.com/users/hubot/following{/other_user}",
        "gists_url": "https://api.github.com/users/hubot/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/hubot/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/hubot/subscriptions",
        "organizations_url": "https://api.github.com/users/hubot/orgs",
        "repos_url": "https://api.github.com/users/hubot/repos",
        "events_url": "https://api.github.com/users/hubot/events{/privacy}",
        "received_events_url": "https://api.github.com/users/hubot/received_events",
        "type": "User",
        "site_admin": true
      }
    ],
    "requested_reviewers": [
      {
        "login": "other_user",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://github.com/images/error/other_user_happy.gif",
        "gravatar_id": "",
        "url": "https://api.github.com/users/other_user",
        "html_url": "https://github.com/other_user",
        "followers_url": "https://api.github.com/users/other_user/followers",
        "following_url": "https://api.github.com/users/other_user/following{/other_user}",
        "gists_url": "https://api.github.com/users/other_user/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/other_user/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/other_user/subscriptions",
        "organizations_url": "https://api.github.com/users/other_user/orgs",
        "repos_url": "https://api.github.com/users/other_user/repos",
        "events_url": "https://api.github.com/users/other_user/events{/privacy}",
        "received_events_url": "https://api.github.com/users/other_user/received_events",
        "type": "User",
        "site_admin": false
      }
    ],
    "requested_teams": [
      {
        "id": 1,
        "node_id": "MDQ6VGVhbTE=",
        "url": "https://api.github.com/teams/1",
        "html_url": "https://github.com/orgs/github/teams/justice-league",
        "name": "Justice League",
        "slug": "justice-league",
        "description": "A great team.",
        "privacy": "closed",
        "permission": "admin",
        "members_url": "https://api.github.com/teams/1/members{/member}",
        "repositories_url": "https://api.github.com/teams/1/repos"
      }
    ],
    "head": {
      "label": "my-org:new-topic",
      "ref": "new-topic",
      "sha": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "user": {
        "login": "my-org",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "gravatar_id": "",
        "url": "https://api.github.com/users/my-org",
        "html_url": "https://github.com/my-org",
        "followers_url": "https://api.github.com/users/my-org/followers",
        "following_url": "https://api.github.com/users/my-org/following{/other_user}",
        "gists_url": "https://api.github.com/users/my-org/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/my-org/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/my-org/subscriptions",
        "organizations_url": "https://api.github.com/users/my-org/orgs",
        "repos_url": "https://api.github.com/users/my-org/repos",
        "events_url": "https://api.github.com/users/my-org/events{/privacy}",
        "received_events_url": "https://api.github.com/users/my-org/received_events",
        "type": "User",
        "site_admin": false
      },
      "repo": {
        "id": 1296269,
        "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
        "name": "my-repo",
        "full_name": "my-org/my-repo",
        "owner": {
          "login": "my-org",
          "id": 1,
          "node_id": "MDQ6VXNlcjE=",
          "avatar_url": "https://github.com/images/error/octocat_happy.gif",
          "gravatar_id": "",
          "url": "https://api.github.com/users/my-org",
          "html_url": "https://github.com/my-org",
          "followers_url": "https://api.github.com/users/my-org/followers",
          "following_url": "https://api.github.com/users/my-org/following{/other_user}",
          "gists_url": "https://api.github.com/users/my-org/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/my-org/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/my-org/subscriptions",
          "organizations_url": "https://api.github.com/users/my-org/orgs",
          "repos_url": "https://api.github.com/users/my-org/repos",
          "events_url": "https://api.github.com/users/my-org/events{/privacy}",
          "received_events_url": "https://api.github.com/users/my-org/received_events",
          "type": "User",
          "site_admin": false
        },
        "private": false,
        "html_url": "https://github.com/my-org/my-repo",
        "description": "This your first repo!",
        "fork": false,
        "url": "https://api.github.com/repos/my-org/my-repo",
        "archive_url": "https://api.github.com/repos/my-org/my-repo/{archive_format}{/ref}",
        "assignees_url": "https://api.github.com/repos/my-org/my-repo/assignees{/user}",
        "blobs_url": "https://api.github.com/repos/my-org/my-repo/git/blobs{/sha}",
        "branches_url": "https://api.github.com/repos/my-org/my-repo/branches{/branch}",
        "collaborators_url": "https://api.github.com/repos/my-org/my-repo/collaborators{/collaborator}",
        "comments_url": "https://api.github.com/repos/my-org/my-repo/comments{/number}",
        "commits_url": "https://api.github.com/repos/my-org/my-repo/commits{/sha}",
        "compare_url": "https://api.github.com/repos/my-org/my-repo/compare/{base}...{head}",
        "contents_url": "https://api.github.com/repos/my-org/my-repo/contents/{+path}",
        "contributors_url": "https://api.github.com/repos/my-org/my-repo/contributors",
        "deployments_url": "https://api.github.com/repos/my-org/my-repo/deployments",
        "downloads_url": "https://api.github.com/repos/my-org/my-repo/downloads",
        "events_url": "https://api.github.com/repos/my-org/my-repo/events",
        "forks_url": "https://api.github.com/repos/my-org/my-repo/forks",
        "git_commits_url": "https://api.github.com/repos/my-org/my-repo/git/commits{/sha}",
        "git_refs_url": "https://api.github.com/repos/my-org/my-repo/git/refs{/sha}",
        "git_tags_url": "https://api.github.com/repos/my-org/my-repo/git/tags{/sha}",
        "git_url": "git:github.com/my-org/my-repo.git",
        "issue_comment_url": "https://api.github.com/repos/my-org/my-repo/issues/comments{/number}",
        "issue_events_url": "https://api.github.com/repos/my-org/my-repo/issues/events{/number}",
        "issues_url": "https://api.github.com/repos/my-org/my-repo/issues{/number}",
        "keys_url": "https://api.github.com/repos/my-org/my-repo/keys{/key_id}",
        "labels_url": "https://api.github.com/repos/my-org/my-repo/labels{/name}",
        "languages_url": "https://api.github.com/repos/my-org/my-repo/languages",
        "merges_url": "https://api.github.com/repos/my-org/my-repo/merges",
        "milestones_url": "https://api.github.com/repos/my-org/my-repo/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/my-org/my-repo/notifications{?since,all,participating}",
        "pulls_url": "https://api.github.com/repos/my-org/my-repo/pulls{/number}",
        "releases_url": "https://api.github.com/repos/my-org/my-repo/releases{/id}",
        "ssh_url": "git@github.com:my-org/my-repo.git",
        "stargazers_url": "https://api.github.com/repos/my-org/my-repo/stargazers",
        "statuses_url": "https://api.github.com/repos/my-org/my-repo/statuses/{sha}",
        "subscribers_url": "https://api.github.com/repos/my-org/my-repo/subscribers",
        "subscription_url": "https://api.github.com/repos/my-org/my-repo/subscription",
        "tags_url": "https://api.github.com/repos/my-org/my-repo/tags",
        "teams_url": "https://api.github.com/repos/my-org/my-repo/teams",
        "trees_url": "https://api.github.com/repos/my-org/my-repo/git/trees{/sha}",
        "clone_url": "https://github.com/my-org/my-repo.git",
        "mirror_url": "git:git.example.com/my-org/my-repo",
        "hooks_url": "https://api.github.com/repos/my-org/my-repo/hooks",
        "svn_url": "https://svn.github.com/my-org/my-repo",
        "homepage": "https://github.com",
        "language": null,
        "forks_count": 9,
        "stargazers_count": 80,
        "watchers_count": 80,
        "size": 108,
        "default_branch": "master",
        "open_issues_count": 0,
        "is_template": true,
        "topics": [
          "my-org",
          "atom",
          "electron",
          "api"
        ],
        "has_issues": true,
        "has_projects": true,
        "has_wiki": true,
        "has_pages": false,
        "has_downloads": true,
        "archived": false,
        "disabled": false,
        "visibility": "public",
        "pushed_at": "2011-01-26T19:06:43Z",
        "created_at": "2011-01-26T19:01:12Z",
        "updated_at": "2011-01-26T19:14:43Z",
        "permissions": {
          "admin": false,
          "push": false,
          "pull": true
        },
        "allow_rebase_merge": true,
        "template_repository": null,
        "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
        "allow_squash_merge": true,
        "delete_branch_on_merge": true,
        "allow_merge_commit": true,
        "subscribers_count": 42,
        "network_count": 0,
        "license": {
          "key": "mit",
          "name": "MIT License",
          "url": "https://api.github.com/licenses/mit",
          "spdx_id": "MIT",
          "node_id": "MDc6TGljZW5zZW1pdA==",
          "html_url": "https://github.com/licenses/mit"
        },
        "forks": 1,
        "open_issues": 1,
        "watchers": 1
      }
    },
    "base": {
      "label": "my-org:master",
      "ref": "master",
      "sha": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "user": {
        "login": "my-org",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "gravatar_id": "",
        "url": "https://api.github.com/users/my-org",
        "html_url": "https://github.com/my-org",
        "followers_url": "https://api.github.com/users/my-org/followers",
        "following_url": "https://api.github.com/users/my-org/following{/other_user}",
        "gists_url": "https://api.github.com/users/my-org/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/my-org/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/my-org/subscriptions",
        "organizations_url": "https://api.github.com/users/my-org/orgs",
        "repos_url": "https://api.github.com/users/my-org/repos",
        "events_url": "https://api.github.com/users/my-org/events{/privacy}",
        "received_events_url": "https://api.github.com/users/my-org/received_events",
        "type": "User",
        "site_admin": false
      },
      "repo": {
        "id": 1296269,
        "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
        "name": "my-repo",
        "full_name": "my-org/my-repo",
        "owner": {
          "login": "my-org",
          "id": 1,
          "node_id": "MDQ6VXNlcjE=",
          "avatar_url": "https://github.com/images/error/octocat_happy.gif",
          "gravatar_id": "",
          "url": "https://api.github.com/users/my-org",
          "html_url": "https://github.com/my-org",
          "followers_url": "https://api.github.com/users/my-org/followers",
          "following_url": "https://api.github.com/users/my-org/following{/other_user}",
          "gists_url": "https://api.github.com/users/my-org/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/my-org/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/my-org/subscriptions",
          "organizations_url": "https://api.github.com/users/my-org/orgs",
          "repos_url": "https://api.github.com/users/my-org/repos",
          "events_url": "https://api.github.com/users/my-org/events{/privacy}",
          "received_events_url": "https://api.github.com/users/my-org/received_events",
          "type": "User",
          "site_admin": false
        },
        "private": false,
        "html_url": "https://github.com/my-org/my-repo",
        "description": "This your first repo!",
        "fork": false,
        "url": "https://api.github.com/repos/my-org/my-repo",
        "archive_url": "https://api.github.com/repos/my-org/my-repo/{archive_format}{/ref}",
        "assignees_url": "https://api.github.com/repos/my-org/my-repo/assignees{/user}",
        "blobs_url": "https://api.github.com/repos/my-org/my-repo/git/blobs{/sha}",
        "branches_url": "https://api.github.com/repos/my-org/my-repo/branches{/branch}",
        "collaborators_url": "https://api.github.com/repos/my-org/my-repo/collaborators{/collaborator}",
        "comments_url": "https://api.github.com/repos/my-org/my-repo/comments{/number}",
        "commits_url": "https://api.github.com/repos/my-org/my-repo/commits{/sha}",
        "compare_url": "https://api.github.com/repos/my-org/my-repo/compare/{base}...{head}",
        "contents_url": "https://api.github.com/repos/my-org/my-repo/contents/{+path}",
        "contributors_url": "https://api.github.com/repos/my-org/my-repo/contributors",
        "deployments_url": "https://api.github.com/repos/my-org/my-repo/deployments",
        "downloads_url": "https://api.github.com/repos/my-org/my-repo/downloads",
        "events_url": "https://api.github.com/repos/my-org/my-repo/events",
        "forks_url": "https://api.github.com/repos/my-org/my-repo/forks",
        "git_commits_url": "https://api.github.com/repos/my-org/my-repo/git/commits{/sha}",
        "git_refs_url": "https://api.github.com/repos/my-org/my-repo/git/refs{/sha}",
        "git_tags_url": "https://api.github.com/repos/my-org/my-repo/git/tags{/sha}",
        "git_url": "git:github.com/my-org/my-repo.git",
        "issue_comment_url": "https://api.github.com/repos/my-org/my-repo/issues/comments{/number}",
        "issue_events_url": "https://api.github.com/repos/my-org/my-repo/issues/events{/number}",
        "issues_url": "https://api.github.com/repos/my-org/my-repo/issues{/number}",
        "keys_url": "https://api.github.com/repos/my-org/my-repo/keys{/key_id}",
        "labels_url": "https://api.github.com/repos/my-org/my-repo/labels{/name}",
        "languages_url": "https://api.github.com/repos/my-org/my-repo/languages",
        "merges_url": "https://api.github.com/repos/my-org/my-repo/merges",
        "milestones_url": "https://api.github.com/repos/my-org/my-repo/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/my-org/my-repo/notifications{?since,all,participating}",
        "pulls_url": "https://api.github.com/repos/my-org/my-repo/pulls{/number}",
        "releases_url": "https://api.github.com/repos/my-org/my-repo/releases{/id}",
        "ssh_url": "git@github.com:my-org/my-repo.git",
        "stargazers_url": "https://api.github.com/repos/my-org/my-repo/stargazers",
        "statuses_url": "https://api.github.com/repos/my-org/my-repo/statuses/{sha}",
        "subscribers_url": "https://api.github.com/repos/my-org/my-repo/subscribers",
        "subscription_url": "https://api.github.com/repos/my-org/my-repo/subscription",
        "tags_url": "https://api.github.com/repos/my-org/my-repo/tags",
        "teams_url": "https://api.github.com/repos/my-org/my-repo/teams",
        "trees_url": "https://api.github.com/repos/my-org/my-repo/git/trees{/sha}",
        "clone_url": "https://github.com/my-org/my-repo.git",
        "mirror_url": "git:git.example.com/my-org/my-repo",
        "hooks_url": "https://api.github.com/repos/my-org/my-repo/hooks",
        "svn_url": "https://svn.github.com/my-org/my-repo",
        "homepage": "https://github.com",
        "language": null,
        "forks_count": 9,
        "stargazers_count": 80,
        "watchers_count": 80,
        "size": 108,
        "default_branch": "master",
        "open_issues_count": 0,
        "is_template": true,
        "topics": [
          "my-org",
          "atom",
          "electron",
          "api"
        ],
        "has_issues": true,
        "has_projects": true,
        "has_wiki": true,
        "has_pages": false,
        "has_downloads": true,
        "archived": false,
        "disabled": false,
        "visibility": "public",
        "pushed_at": "2011-01-26T19:06:43Z",
        "created_at": "2011-01-26T19:01:12Z",
        "updated_at": "2011-01-26T19:14:43Z",
        "permissions": {
          "admin": false,
          "push": false,
          "pull": true
        },
        "allow_rebase_merge": true,
        "template_repository": null,
        "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
        "allow_squash_merge": true,
        "delete_branch_on_merge": true,
        "allow_merge_commit": true,
        "subscribers_count": 42,
        "network_count": 0,
        "license": {
          "key": "mit",
          "name": "MIT License",
          "url": "https://api.github.com/licenses/mit",
          "spdx_id": "MIT",
          "node_id": "MDc6TGljZW5zZW1pdA==",
          "html_url": "https://github.com/licenses/mit"
        },
        "forks": 1,
        "open_issues": 1,
        "watchers": 1
      }
    },
    "_links": {
      "self": {
        "href": "https://api.github.com/repos/my-org/my-repo/pulls/1347"
      },
      "html": {
        "href": "https://github.com/my-org/my-repo/pull/1347"
      },
      "issue": {
        "href": "https://api.github.com/repos/my-org/my-repo/issues/1347"
      },
      "comments": {
        "href": "https://api.github.com/repos/my-org/my-repo/issues/1347/comments"
      },
      "review_comments": {
        "href": "https://api.github.com/repos/my-org/my-repo/pulls/1347/comments"
      },
      "review_comment": {
        "href": "https://api.github.com/repos/my-org/my-repo/pulls/comments{/number}"
      },
      "commits": {
        "href": "https://api.github.com/repos/my-org/my-repo/pulls/1347/commits"
      },
      "statuses": {
        "href": "https://api.github.com/repos/my-org/my-repo/statuses/6dcb09b5b57875f334f61aebed695e2e4193db5e"
      }
    },
    "author_association": "OWNER",
    "auto_merge": null,
    "draft": false
  }
"""

prs_body = f"""
[
{pr_body}
]
"""

hook_data = """
    [
  {
    "type": "Repository",
    "id": 12345678,
    "name": "web",
    "active": true,
    "updated_at": "2019-06-03T00:57:16Z",
    "created_at": "2019-06-03T00:57:16Z"    
  },
    {
    "type": "Repository",
    "id": 12345679,
    "name": "web",
    "active": false,
    "updated_at": "2019-06-03T00:57:16Z",
    "created_at": "2019-06-03T00:57:16Z"    
  }
]
  """

owning_team = """
   {
    "id": 1,
    "node_id": "MDQ6VGVhbTE=",
    "url": "https://api.github.com/teams/2",
    "html_url": "https://github.com/orgs/my-org/teams/my-team",
    "name": "my-team",
    "slug": "my-team",
    "description": "A great team.",
    "privacy": "closed",
    "permission": "admin",
    "members_url": "https://api.github.com/teams/2/members{/member}",
    "repositories_url": "https://api.github.com/teams/2/repos",
    "parent": null
  }
"""

owning_teams = """
[
   {
    "id": 1,
    "node_id": "MDQ6VGVhbTE=",
    "url": "https://api.github.com/teams/2",
    "html_url": "https://github.com/orgs/my-org/teams/my-team",
    "name": "my-team",
    "slug": "my-team",
    "description": "A great team.",
    "privacy": "closed",
    "permission": "admin",
    "members_url": "https://api.github.com/teams/2/members{/member}",
    "repositories_url": "https://api.github.com/teams/2/repos",
    "parent": null
  }
]
"""

shared_teams = """
[
  {
    "id": 1,
    "node_id": "MDQ6VGVhbTE=",
    "url": "https://api.github.com/teams/1",
    "html_url": "https://github.com/orgs/github/teams/justice-league",
    "name": "Justice League",
    "slug": "justice-league",
    "description": "A great team.",
    "privacy": "closed",
    "permission": "admin",
    "members_url": "https://api.github.com/teams/1/members{/member}",
    "repositories_url": "https://api.github.com/teams/1/repos",
    "parent": null
  },
    {
    "id": 1,
    "node_id": "MDQ6VGVhbTE=",
    "url": "https://api.github.com/teams/2",
    "html_url": "https://github.com/orgs/my-org/teams/my-team",
    "name": "my-team",
    "slug": "my-team",
    "description": "A great team.",
    "privacy": "closed",
    "permission": "admin",
    "members_url": "https://api.github.com/teams/2/members{/member}",
    "repositories_url": "https://api.github.com/teams/2/repos",
    "parent": null
  }
]

  """

my_new_ref = """
{
  "ref": "refs/heads/featureA",
  "node_id": "MDM6UmVmcmVmcy9oZWFkcy9mZWF0dXJlQQ==",
  "url": "https://api.github.com/repos/my-org/my-repo/git/refs/heads/main",
  "object": {
    "type": "commit",
    "sha": "aa218f56b14c9653891f9e74264a383fa43fefbd",
    "url": "https://api.github.com/repos/my-org/my-repo/git/commits/aa218f56b14c9653891f9e74264a383fa43fefbd"
  }
}
"""

branch_protection = """
{
  "url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection",
  "required_status_checks": {
    "url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/required_status_checks",
    "contexts": [
      "continuous-integration/travis-ci"
    ],
    "contexts_url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/required_status_checks/contexts",
    "enforcement_level": "non_admins"
  },
  "enforce_admins": {
    "url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/enforce_admins",
    "enabled": true
  },
  "required_pull_request_reviews": {
    "url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/required_pull_request_reviews",
    "dismissal_restrictions": {
      "url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/dismissal_restrictions",
      "users_url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/dismissal_restrictions/users",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/dismissal_restrictions/teams",
      "users": [
        {
          "login": "octocat",
          "id": 1,
          "node_id": "MDQ6VXNlcjE=",
          "avatar_url": "https://github.com/images/error/octocat_happy.gif",
          "gravatar_id": "",
          "url": "https://api.github.com/users/octocat",
          "html_url": "https://github.com/octocat",
          "followers_url": "https://api.github.com/users/octocat/followers",
          "following_url": "https://api.github.com/users/octocat/following{/other_user}",
          "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
          "organizations_url": "https://api.github.com/users/octocat/orgs",
          "repos_url": "https://api.github.com/users/octocat/repos",
          "events_url": "https://api.github.com/users/octocat/events{/privacy}",
          "received_events_url": "https://api.github.com/users/octocat/received_events",
          "type": "User",
          "site_admin": false
        }
      ],
      "teams": [
        {
          "id": 1,
          "node_id": "MDQ6VGVhbTE=",
          "url": "https://api.github.com/teams/1",
          "html_url": "https://github.com/orgs/github/teams/justice-league",
          "name": "Justice League",
          "slug": "justice-league",
          "description": "A great team.",
          "privacy": "closed",
          "permission": "admin",
          "members_url": "https://api.github.com/teams/1/members{/member}",
          "repositories_url": "https://api.github.com/teams/1/repos",
          "parent": null
        }
      ]
    },
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true,
    "required_approving_review_count": 2
  },
  "restrictions": {
    "url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/restrictions",
    "users_url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/restrictions/users",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/restrictions/teams",
    "apps_url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/restrictions/teams",
    "users": [
      {
        "login": "octocat",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "gravatar_id": "",
        "url": "https://api.github.com/users/octocat",
        "html_url": "https://github.com/octocat",
        "followers_url": "https://api.github.com/users/octocat/followers",
        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
        "organizations_url": "https://api.github.com/users/octocat/orgs",
        "repos_url": "https://api.github.com/users/octocat/repos",
        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
        "received_events_url": "https://api.github.com/users/octocat/received_events",
        "type": "User",
        "site_admin": false
      }
    ],
    "teams": [
      {
        "id": 1,
        "node_id": "MDQ6VGVhbTE=",
        "url": "https://api.github.com/teams/1",
        "html_url": "https://github.com/orgs/github/teams/justice-league",
        "name": "Justice League",
        "slug": "justice-league",
        "description": "A great team.",
        "privacy": "closed",
        "permission": "admin",
        "members_url": "https://api.github.com/teams/1/members{/member}",
        "repositories_url": "https://api.github.com/teams/1/repos",
        "parent": null
      }
    ],
    "apps": [
      {
        "id": 1,
        "slug": "octoapp",
        "node_id": "MDExOkludGVncmF0aW9uMQ==",
        "owner": {
          "login": "github",
          "id": 1,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
          "url": "https://api.github.com/orgs/github",
          "repos_url": "https://api.github.com/orgs/github/repos",
          "events_url": "https://api.github.com/orgs/github/events",
          "hooks_url": "https://api.github.com/orgs/github/hooks",
          "issues_url": "https://api.github.com/orgs/github/issues",
          "members_url": "https://api.github.com/orgs/github/members{/member}",
          "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
          "avatar_url": "https://github.com/images/error/octocat_happy.gif",
          "description": "A great organization"
        },
        "name": "Octocat App",
        "description": "",
        "external_url": "https://example.com",
        "html_url": "https://github.com/apps/octoapp",
        "created_at": "2017-07-08T16:18:44-04:00",
        "updated_at": "2017-07-08T16:18:44-04:00",
        "permissions": {
          "metadata": "read",
          "contents": "read",
          "issues": "write",
          "single_file": "write"
        },
        "events": [
          "push",
          "pull_request"
        ]
      }
    ]
  },
  "required_linear_history": {
    "enabled": true
  },
  "allow_force_pushes": {
    "enabled": true
  },
  "allow_deletions": {
    "enabled": true
  },
  "required_conversation_resolution": {
    "enabled": true
  }
}
"""