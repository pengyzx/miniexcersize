import re

wordlist = []
wordfrequence = {}


with open("article.txt", 'r') as f:
	word = f.read().split(' ')  #以空格作为分格符
	for i in word:
		if i not in wordfrequence:
			wordfrequence[i] = 1
		else:
			wordfrequence[i] += 1

print(wordfrequence)
