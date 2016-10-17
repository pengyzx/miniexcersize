# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights

elements = []
with open('filtered_words.txt', 'r') as f:
	for word in f.readlines():
		elements.append(word.strip('\n'))
print(elements)


while True:
	filename = "filtered_words.txt"
	inputword = str(input("Enter your word:"))
	if inputword in elements:
		print('Freedom')
	elif inputword == 'exit':
		break
	else:
		print('Human Rights')
