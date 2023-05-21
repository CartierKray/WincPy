import main

# 1
def test_get_none():
    result = main.get_none()
    assert result is None
    print('Test #1 Passed!')

test_get_none()



# 2
def test_flatten_dict():
    dictionary = {'a': [42, 350], 'b': 3.14 }
    expected_output = [[42, 350], 3.14]
    result = main.flatten_dict(dictionary)
    assert result == expected_output, f"Expected: {expected_output}, Got: {result}"
    print('Test #2 Passed!')

test_flatten_dict()