import responses
from unittest.mock import MagicMock
from github_rename_utils.github_rest_api import rest_client, monitor_rest_client
from datetime import datetime

@responses.activate
def test_rest_client_can_be_monitored():
    token = "__dummy__"
    resource = "test"
    reset_at = 1624874400

    client = rest_client(token)
    store = MagicMock()
    monitored_client = monitor_rest_client(client, store)

    responses.add(responses.GET, "https://api.github.com/test",
        body=b'{ "message": "success" }',
        content_type='text/json',
        headers={
            "X-RateLimit-Resource": resource,
            "X-RateLimit-Reset": str(reset_at)
        },
        status=200
    )

    url = monitored_client.session.build_url("test")
    monitored_client.session.get(url)

    store.put.assert_called_with(
        "test",
        1,
        datetime.fromtimestamp(reset_at)
    )
