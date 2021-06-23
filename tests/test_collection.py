from github_rename_utils.collection import AddingDict


def test_adding_dict_can_add_integers():
  rate_limits_1 = AddingDict({ 'a': 1, 'b': 2 })
  rate_limits_2 = AddingDict({ 'b': 3, 'c': 4 })

  expected = AddingDict({ 'a': 1, 'b': 5, 'c': 4 })

  actual = rate_limits_1 + rate_limits_2

  assert expected == actual

def test_adding_dict_can_add_string():
  rate_limits_1 = AddingDict({ 'a': 'a', 'b': 'b' })
  rate_limits_2 = AddingDict({ 'b': 'b', 'c': 'c' })

  expected = AddingDict({ 'a': 'a', 'b': 'bb', 'c': 'c' })

  actual = rate_limits_1 + rate_limits_2

  assert expected == actual
