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
    r = min(float(sub) for sub in data)
    return numberHelper(r)


## max
def maximalus(data):
    r = max(float(sub) for sub in data)
    return numberHelper(r)


## 1 kvantilis
def kvantilis_pirmas(data, kiekis):
    kvantilis = kiekis * 0.25
    return numberHelper(data[round(kvantilis)])


## 3 kvantilis
def kvantilis_trecias(data, kiekis):
    kvantilis = kiekis * 0.75
    return numberHelper(data[round(kvantilis)])


## vidurkis
def vidurkis(data, kiekis):
    sum_num = 0.0
    avg = 0
    for t in data:
        if float(t) > 0:
            sum_num = sum_num + float(t)
            avg = sum_num / kiekis
    return round(avg, 2)


## mediana
def kvantilis_mediana(data, kiekis):
    kvantilis = kiekis * 0.50
    return numberHelper(data[round(kvantilis)])


## stand nuokrypis
def standartinis_nuokrypis():
    return


def numberHelper(r):
    if type(r) == int:
        return r
    else:
        return round(float(r), 2)
