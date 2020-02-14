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


## min
def minimalus(data):
    return min(data)


## max
def maximalus(data):
    return max(data)


## 1 kvantilis
def kvantilis_pirmas(data, kiekis):
    kvantilis = kiekis * 0.25
    return data[round(kvantilis)]


## 3 kvantilis
def kvantilis_trecias(data, kiekis):
    kvantilis = kiekis * 0.75
    return data[round(kvantilis)]


## vidurkis
def vidurkis(data, kiekis):
    results = list(map(int, data))
    visaSuma = sum(results)
    vid = visaSuma / kiekis
    return round(vid, 2)


## mediana
def kvantilis_mediana(data, kiekis):
    kvantilis = kiekis * 0.50
    return data[round(kvantilis)]


## stand nuokrypis
def standartinis_nuokrypis():
    return
