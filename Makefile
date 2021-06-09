.PHONY: load_schema

load_schema:
	poetry install && \
	cd ./github_rename_utils/schema && \
	python3 -m sgqlc.introspection \
     --exclude-deprecated \
     --exclude-description \
     -H "Authorization: bearer ${GH_TOKEN}" \
     https://api.github.com/graphql \
     github_schema.json && \
	 sgqlc-codegen schema github_schema.json github_schema.py && \
	 cd -