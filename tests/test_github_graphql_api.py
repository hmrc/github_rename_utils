import responses
import json
from dateutil import parser
from unittest.mock import MagicMock
from sgqlc.operation import Operation
from github_rename_utils.schema import github_schema as schema
from github_rename_utils.github_graphql_api import graphql_endpoint, monitor_graphql_endpoint

@responses.activate
def test_graphql_client_can_be_monitored():
    token = "__dummy__"
    cost = 12
    reset_at = "2021-06-28T10:00:00Z"

    endpoint = graphql_endpoint(token)
    store = MagicMock()
    monitored_endpoint = monitor_graphql_endpoint(endpoint, store)

    responses.add(responses.POST, "https://api.github.com/graphql",
        body=json.dumps({
            "data": {
                "rateLimit": {
                    "cost": cost,
                    "resetAt": reset_at
                }
            }
        }),
        content_type='application/json',
        status=200
    )

    op = Operation(schema.Query, name='Test')
    monitored_endpoint(op, {})

    store.put.assert_called_with(
        "graphql",
        cost,
        parser.parse(reset_at)
    )
