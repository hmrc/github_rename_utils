# Github Rename Utils

## Why rename?

The default name for a branch has, until recently, been 'master' which is a word deemed inappropriate for use in this context. Changing 5k repositories overnight is not a manual task so this utility code is provided to help.

## Why not use what github provides?

There is an api call which github has provided to make this easier but it doesn't work well with the 5k hmrc repos. We use branch protection to (amongst other things) ensure that all code commits are signed and default branches do not get deleted by mistake. This gets in the way of the provided 'easy rename'. The utility code provided here handles the branch protection.

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
