from datetime import datetime
from github_rename_utils.rate_limit import RateLimit


def test_rate_limit_can_be_added():
  rate_limit_1 = RateLimit(3, datetime(2021, 6, 23, 12))
  rate_limit_2 = RateLimit(6, datetime(2021, 6, 23, 11))

  expected = RateLimit(9, datetime(2021, 6, 23, 12))

  actual = rate_limit_1 + rate_limit_2

  assert expected == actual
