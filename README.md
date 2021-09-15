# Github Rename Utils

[![Brought to you by TeamDDCOps](https://img.shields.io/badge/MDTP-DDCOps-40D9C0?style=flat&labelColor=000000&logo=gov.uk)](https://confluence.tools.tax.service.gov.uk/display/Tools) **owned with pride by DDCOps**

## Why rename?

The default name for a branch has, until recently, been 'master' which is a word deemed inappropriate for use in this context. Changing 5k repositories overnight is not a manual task so this utility code is provided to help.

## Why not use what Github provides?

There is an api call which github has provided to make this easier but it doesn't work well with the 5k hmrc repos. We use branch protection to (amongst other things) ensure that all code commits are signed and default branches do not get deleted by mistake. This gets in the way of the provided 'easy rename'. The utility code provided here handles the branch protection.

## Usage

### Utilities

#### Default branch renaming

The following example shows how to rename a branch and generate the associated report:

```python
from github_rename_utils.github_rest_api import GithubRestClient
from github_rename_utils.branch_rename import rename_default_branch

client = GithubRestClient("my-token")
success, report = rename_default_branch(client, "my-org", "my-repo", "new-default-branch")
```

#### Shared ownership reporting

The following example shows how to generate a report showing the ownership of repositories:

```python
from github_rename_utils.github_graphql_api import GithubGraphqlEndpoint
from github_rename_utils.shared_ownership_report import get_shared_ownership_report

endpoint = GithubGraphqlEndpoint("my-token")
report = get_shared_ownership_report(endpoint, "my-org", ["my-ignored-team"])
```

#### Team repositories reporting

The following example shows how to generate a report of team repositories:

```python
from github_rename_utils.github_graphql_api import GithubGraphqlEndpoint
from github_rename_utils.team_repo_report import get_team_repo_report

endpoint = GithubGraphqlEndpoint("my-token")
report = get_team_repo_report(endpoint, "my-org", "my-team")
```

### Monitoring

Monitoring of the Github API rate limits can be enabled if required:

```python
from github_rename_utils.github_rest_api import GithubRestClient
from github_rename_utils.github_rate_limit import InMemoryRateLimitStore

rate_limit_store = InMemoryRateLimitStore()
client = GithubRestClient("my-token", rate_limit_store=rate_limit_store)
```

The module provides the `InMemoryRateLimitStore` but an alternative implementation for the store can be used. For example, you may want a store that submits metrics based on the rate limiting data to your chosen monitoring stack.

## Useful dev commands

Even this code cannot update a clone in another github instance so engineers will find these commands useful to run after a rename:

```bash
git branch -m OLD-BRANCH-NAME NEW-BRANCH-NAME
git fetch origin
git branch -u origin/NEW-BRANCH-NAME NEW-BRANCH-NAME
git remote prune origin
git remote set-head origin --auto
```

## What else?

In a world where migration is self-service (our teams will be empowered to trigger this when it suits them best) it's good to know how far through the 5k repositories we have got. This collection of utils also includes reporting methods to help gather data for that purpose.

## How to build and consume

This utils package is managed by poetry and may (depending on your poetry config) use a virtual environment

- Getting set up with poetry: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)
- install dependencies: `poetry install`
- run tests: `poetry run pytest`
- build the package: `poetry build`
- consume the wheel in your app: `pip install <path to this clone>/dist/github-rename-utils-0.2.0.tar.gz` (or use your favourite --find-links syntax)

## Docs for dependent libraries

For expedience, some rest calls have been wrapped with [github3.py](https://github3py.readthedocs.io/en/master/narrative/index.html) and graphql calls are managed in code via [sgqlc](https://sgqlc.readthedocs.io/en/latest/index.html)
