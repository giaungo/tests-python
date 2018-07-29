

def store(arr_of_map):
    """
    Store an array of map (dict) in a string type variable
    :param arr_of_map: array of map data
    :return: string
    """
    itms = []

    for itm in arr_of_map:
        kv = []
        for k, v in itm.items():
            kv.append("{}={}".format(k, v))
        itms.append(";".join(kv))

    return "\n".join(itms)


def load(str_from_arra_of_map):
    """
    Store an array of map (dict) in a string type variable
    :param arr_of_map: array of map data
    :return: string
    """
    arr = []

    itms = str_from_arra_of_map.split("\n")
    for itm in itms:
        dct = {}
        kvs = itm.split(";")
        for kv in kvs:
            k, v = kv.split("=")
            dct[k] = v
        arr.append(dct)

    return arr
