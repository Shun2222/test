import xlrd
import pprint
import numpy as np
print('パスの記入をしてください')
x = input()
wb = xlrd.open_workbook(x)
sheets = wb.sheets()
sheet = wb.sheet_by_name('Sheet1')
print('行の入力(0から始まる)')
start_row = input()
end_row = input()
print('列の入力(0から始まる)')
start_col = input()
end_col = input()
c = 'c'*(int(end_col) + 1 - int(start_col))
caption = input('Enter caption: ')
print('latex(表用)')
print('\\begin{table}[H]')
print('\\begin{center}')
print('\\caption{%s}'% caption)
print('\\begin{tabular}{%s}\\hline'% c)
data = np.array([sheet.row_values(row, int(start_col), int(end_col) + 1) for row in range(int(start_row), int(end_row) + 1)])
data2 = ''
for i in data:
	data2 = ''
	for j in i:
		data2 += str(j)+'&'
	print(data2[0:len(data2)-1]+'\\\\')
print('\\end{tabular}')
print('\\end{center}')
print('\\end{table}')
