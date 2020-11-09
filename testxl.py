import xlrd
data = xlrd.open_workbook('./excel.xlsx')
table = data.sheets()[0]
table2 = data.sheet_by_index(0)
table3 = data.sheet_by_name('Sheet1')
print(table.cell_value(1,2))
print(table2.cell(1,2).value)
print(table3.row(1)[2].value)

import xlwt
new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet('new_test')
worksheet.write(0,0,'hello')
new_workbook.save('./excel_w.xls')
