from collections import Counter


## eil sk
def kiekis(data):
    return len(data)


## missing values
def truksta(total_lines, kiekis):
    proc_value = kiekis / total_lines
    result = round(proc_value, 2) * 100 - 100
    return round(abs(result))


## uniqe
def kardinalumas(data):
    my_set = set(data)
    my_new_list = list(my_set)
    return len(my_new_list)


def moda1(data):
    dict = Counter(data)
    value = sorted(dict.values(), reverse=True)
    largest = value[0]
    for (key, val) in dict.items():
        if val == largest:
            print(key,largest)
            return [key,largest]


def moda2(data):
    dict = Counter(data)
    value = sorted(dict.values(), reverse=True)
    secondLarge = value[1]
    for (key, val) in dict.items():
        if val == secondLarge:
            return [key,secondLarge]


def moda_proc(moda2, total_lines):
    proc_value = moda2 / total_lines
    result = round(proc_value, 2) * 100 - 100
    return round(abs(result))
