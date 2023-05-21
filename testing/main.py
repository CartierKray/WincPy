
# 1
def get_none():
    return None 


# 2
def flatten_dict(dictionary):
    flattened = []
    for value in dictionary.values():
        if isinstance(value, list):
            flattened.extend(value)
        else:
            flattened.append(value)
    return flattened



