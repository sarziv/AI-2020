import CVSFileHelper
import Tol_calcs as tolyginis
import Kat_calcs as kategorinis

TOTAL_LINES = 6367


def generavimas(show):
    general_list = []
    tol_list = []
    kat_list = []
    for cols in range(13):
        if cols > 0:  ##ignoring id line
            cvs = CVSFileHelper.getInformation(cols)
            general_list.append(cvs)
    for col_list in general_list:
        colValue = col_list[1:][:1][0]
        if colValue.isalpha() == False:
            tol_list.append(col_list)
        else:
            kat_list.append(col_list)
    for tol_each in tol_list:
        tol_name = tol_each[:1]
        tol_data = tol_each[1:]
        tolydinisTipas(tol_name[0], tol_data)
    if (show == True):
        print(tol_each)

    for kat_each in kat_list:
        kat_name = kat_each[:1]
        kat_data = kat_each[1:]
        kategorijosTipas(kat_name[0], kat_data)
        if (show == True):
            print(kat_each)


## Tolydinio tipo reikšmėms
def tolydinisTipas(name, data):
    sarasas = ['Pavadinimas', 'kiekis', 'truksta', 'kardinalumas', 'min', 'max', 'kvantilis pirmas',
               'kvantilis trecias', 'mediana', 'vidurkis']
    result = []
    result.append(name)
    kiekis = tolyginis.kiekis(data)
    result.append(kiekis)
    truksta = tolyginis.truksta(TOTAL_LINES, kiekis)
    result.append(truksta)
    kardinalumas = tolyginis.kardinalumas(data)
    result.append(kardinalumas)
    minimalus = tolyginis.minimalus(data)
    result.append(minimalus)
    maximalus = tolyginis.maximalus(data)
    result.append(maximalus)
    sorted_list = sorted(data)
    pirmas = tolyginis.kvantilis_pirmas(sorted_list, kiekis)
    result.append(pirmas)
    trecias = tolyginis.kvantilis_trecias(sorted_list, kiekis)
    result.append(trecias)
    mediana = tolyginis.kvantilis_mediana(sorted_list, kiekis)
    result.append(mediana)
    vidurkis = tolyginis.vidurkis(data, kiekis)
    result.append(vidurkis)
    print(sarasas)
    print(result)


## Kategorinio tipo reikšmėms
def kategorijosTipas(name, data):
    print()


generavimas(False)
