# 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

filename = "filtered_words.txt"
elements = []

with open(filename, 'r') as f:
		#用read会一个一个字的读取，字会拆开
		for word in f.readlines():
			#去除换行
			elements.append(word.strip('\n'))


def wordreplace(inputword):
	result = inputword
	for x in elements:
		if result.find(x) != -1:
			#不等于-1表示输入的字符串中含敏感字符，然后将敏感字符替换
			result = result.replace(x, '**')
	return result

while True:
	inputwords = str(input('Enter your word:'))
	if inputwords.lower() == 'exit':
		break
	else:
		print(wordreplace(inputwords))

