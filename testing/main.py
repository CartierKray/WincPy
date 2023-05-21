
# 1
def get_none():
    return None 


# 2
def flatten_dict(dictionary):
    result = []
    for value in dictionary.values():
        if isinstance(value, dict):
            result.extend(flatten_dict(value))
        elif isinstance(value, list):
            result.extend(flatten_list(value))
        else:
            result.append(value)
    return result

def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, (dict, list)):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


