repo_branches_large_query = b"""{"query": "query {\\nrepository(owner: \\"my-org\\", name: \\"my-repo\\") {\\nrefs(refPrefix: \\"refs/heads/\\", first: 10) {\\nnodes {\\nname\\n}\\ntotalCount\\n}\\n}\\n}", "variables": null, "operationName": null}"""