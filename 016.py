'''
纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中
'''
import xlwt

with open('numbers.txt', 'r') as f:
	content = f.read()

numlist = eval(content)
print(numlist)


numtable = xlwt.Workbook(encoding='utf-8')
numinfo = numtable.add_sheet('number', cell_overwrite_ok=True)

for i in range(len(numlist)):
	#	遍历整个numlist，获取子列表
	for j in range(len(numlist[i])):
		#   遍历子列表，获取里面的元素
		numinfo.write(i, j, numlist[i][j])

numtable.save('numbers.xls')
