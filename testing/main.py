
# 1
def get_none():
    return None 


# 2
def flatten_dict(dictionary):
    result = []

    def flatten_helper(obj):
        if isinstance(obj, dict):
            for value in obj.values():
                flatten_helper(value)
        elif isinstance(obj, list):
            for item in obj:
                flatten_helper(item)
        else:
            result.append(obj)

    flatten_helper(dictionary)
    return result



