def get_value(obj, key):
    keys = key.split("/")
    value = obj
    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            return None
    return value

object = {'a': {'b':{'c':'d'}}}
result = get_value(object,'a/b/c')
print(result)
