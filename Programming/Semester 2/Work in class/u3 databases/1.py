import pandas

excelDataDF = pandas.read_excel('vegetable.xlsx', sheet_name='summer')

print(excelDataDF)