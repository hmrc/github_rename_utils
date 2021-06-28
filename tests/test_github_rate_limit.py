from datetime import datetime
from github_rename_utils.github_rate_limit import InMemoryRateLimitStore


def test_in_memory_rate_limit_store_can_put_rate_limits():
    rate_limits = [
        {
            "resource": "resource-1",
            "cost": 3,
            "reset_at": datetime(2021, 6, 27, 10)
        },
        {
            "resource": "resource-1",
            "cost": 5,
            "reset_at": datetime(2021, 6, 27, 11)
        },
        {
            "resource": "resource-2",
            "cost": 7,
            "reset_at": datetime(2021, 6, 27, 12)
        }
    ]

    store = InMemoryRateLimitStore()

    for rate_limit in rate_limits:
        store.put(
            rate_limit["resource"],
            rate_limit["cost"],
            rate_limit["reset_at"]
        )

    actual_values = store.values
    expected_values = {
        "resource-1": {
            "cost": 8,
            "reset_at": datetime(2021, 6, 27, 11)
        },
        "resource-2": {
            "cost": 7,
            "reset_at": datetime(2021, 6, 27, 12)
        }
    }

    assert expected_values == actual_values

def test_in_memory_rate_limit_store_can_be_reset():
    store = InMemoryRateLimitStore()

    store.put("resource-1", 1, datetime(2021, 6, 27, 12))
    store.reset()

    actual_values = store.values
    expected_values = {}

    assert expected_values == actual_values
