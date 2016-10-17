'''
 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：
<?xmlversion="1.0" encoding="UTF-8"?>
<root>
<citys>
<!--
    城市信息
-->
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
</citys>
</root>
'''

import xlrd
import json

citydic = {}
citydata = xlrd.open_workbook('city.xls')  # 也可以用with...as操作
citytable = citydata.sheet_by_index(0)
nrows = citytable.nrows

for row in range(nrows):
    # print(row) 会输出0，1，2，故后面会+1
    # print(citytable.row_values(row))
    citydic[str(row + 1)] = citytable.row_values(row)[1]  # 每一行的第一个元素，作为字典的值

cityjson = json.dumps(citydic, indent=4, ensure_ascii=False)

content = '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n<citys>\n<!--\n    城市信息\n-->\n'
content = content + cityjson + '\n</citys>\n</root>'

with open('city.xml', 'w') as f:
    f.write(content)
