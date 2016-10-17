'''
纯文本文件 student.txt为学生信息
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
'''
import xlwt


with open('student.txt', 'r') as f:
	content = f.read()
# eval可以执行字符串的内容，切记
studentdict = eval(content)


print(studentdict)


studenttable = xlwt.Workbook(encoding='utf-8')
studentinfo = studenttable.add_sheet('student', cell_overwrite_ok=False)


def writesheet(key, value):
# 行从0开始计算，故用字典的值-1
	studentinfo.write(int(key)-1, 0, key)
	for x in range(len(value)):
# range中x初始值为0，从第1列开始写入，故x+1，字典中的值为列表，从0开始，故value[x]
		studentinfo.write(int(key)-1, x+1, str(value[x]))

for key, value in studentdict.items():
	writesheet(key, value)

studenttable.save('student.xls')

