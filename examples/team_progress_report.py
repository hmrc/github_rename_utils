import os
from github_wrapper import get_github_client
from github_requests import get_default_branch_report

'''
The final version will accept arguments of 
- org name
- team name
- output path
- expected owning teams (list)

For performance reasons, the final version will call utility methods related to GitHub v4 api (graphql)

For each repo where the team has push access we should look if the repo is shared
which will use team(s) 'owning' the code (the team name(s) in an array) 
 and repo admins (the repositories owners team name in an array)
We should report 
 - number of other teams shared with 
 - the current default branch name
 - if the current default branch name is protected to ensure
   that there is no corrupt data or bad branches
 - if there is a 'master' branch even if the default branch has a different name
We can also optionally report on
 - the webhooks attached to the repo which will reflect the required checks for the current default branch
'''

def report_specific_team_repos_if_not_migrated():
  """Real call prototyping report script: report_specific_team_repos"""
  import os
  org = "my-org"
  team = "my-team"
  token = os.getenv("GH_TOKEN")

  client = get_github_client(org, team, token)
  owners = ['my-team', 'my-team-read-only']
  admins = ['my-admin-team']
  data = get_default_branch_report(client, owners, admins)

  accepted_default_branches = ['main', 'ubuntu-1804']

  with open('./report.txt', 'w', encoding='utf-8') as fh:
    fh.write("full_name,default_branch,open_prs,hooks,shared_with\n")
    for repo in data:
      if repo['default_branch'] in accepted_default_branches:
        continue

      fh.write(f"{repo['full_name']},{repo['default_branch']},{repo['open_prs']},{repo['hooks']},{repo['shared']}\n")

  assert 0 < len(data)