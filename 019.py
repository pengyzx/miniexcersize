'''
将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下
所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!--
    数字信息
-->
[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
</numbers>
</root>
'''

import xlrd
import json

numdict = []
numdata = xlrd.open_workbook('numbers.xls')
numtable = numdata.sheet_by_index(0)
nrows = numtable.nrows

for row in range(nrows):
    #	print(numtable.row_values(row))
    # 输出的值变成小数?
    numdict.append(numtable.row_values(row))

s = json.dumps(numdict, indent=4, ensure_ascii=False)

content = '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n<numbers>\n<!--\n    数字信息\n-->\n'
content = content + s + '\n</numbers>\n</root>'

with open('numbers.xml', 'w') as f:
    f.write(content)
