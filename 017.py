'''
将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如下所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
    "1" : ["张三", 150, 120, 100],
    "2" : ["李四", 90, 99, 95],
    "3" : ["王五", 60, 66, 68]
}
</students>
</root>
'''

import xlrd
import json

content = '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n<students>\n<!--\n    学生信息表\n    "id" : [名字, 数学, 语文, 英文]\n-->\n'
studict = {}
data = xlrd.open_workbook('student.xls')
table = data.sheet_by_index(0)
nrows = table.nrows      #获取表的行
for row in range(nrows):
	stulist = []
#   print(table.row_values(row))
#获取表格每行的值
	stuinfo = table.row_values(row)
	for x in range(len(stuinfo)-1):
#将每行第二个及以后的元素加入列表
		stulist.append(stuinfo[x+1])
	studict[stuinfo[0]] = stulist   #表格每行第一个元素作为键
print(studict)

#将字典转为json格式
info = json.dumps(studict, indent=4, ensure_ascii=False)
content = content + info + '\n</students>\n</root>'

with open('student.xml', 'w') as f:
	f.write(content)
