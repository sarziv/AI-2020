import xlsxwriter

workbook = xlsxwriter.Workbook('file.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
data = (
    tolySar,
    tolyData,
    katSar,
    katData,
)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in data:
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1


workbook.close()