import main
from main import flatten_dict

# 1
def test_get_none():
    result = main.get_none()
    assert result is None
    print('Test #1 Passed!')

test_get_none()



# 2
def test_flatten_dict():
    # Test with a simple dictionary
    assert flatten_dict({'a': 42, 'b': 3.14}) == [42, 3.14]

    # Test with a dictionary containing a list
    assert flatten_dict({'a': [42, 350], 'b': 3.14}) == [[42, 350], 3.14]

    # Test with a dictionary containing nested dictionaries
    assert flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 350}) == [{'inner_a': 42, 'inner_b': 350}, 350]


