import xlsxwriter


def create(katPavadinimas, katResult, tolPavadinimas, tolResult):
    workbook = xlsxwriter.Workbook('./Result/Result.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for kat_pav in katPavadinimas:
        worksheet.write(row, col, kat_pav)
        col += 1
    col = 0

    row = 1
    for kat_x in katResult:
        for kat_each in kat_x:
            worksheet.write(row, col, kat_each)
            col += 1
        row += 1
        col = 0

    row += 1
    for tol_pav in tolPavadinimas:
        worksheet.write(row, col, tol_pav)
        col += 1
    col = 0

    row += 1
    for tol_x in tolResult:
        for tol_each in tol_x:
            worksheet.write(row, col, tol_each)
            col += 1
        row += 1
        col = 0

    workbook.close()
