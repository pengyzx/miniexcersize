'''
 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
'''
import xlwt

with open('city.txt', 'r') as f:
	content = f.read()


citydict = eval(content)
print(citydict)
citytable = xlwt.Workbook(encoding='utf-8')
cityinfo = citytable.add_sheet('city', cell_overwrite_ok=False)

for key, value in citydict.items():
	cityinfo.write(int(key)-1, 0, key)
	cityinfo.write(int(key)-1, 1, value)

citytable.save('city.xls')