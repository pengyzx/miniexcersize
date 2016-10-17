# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）


import random
import string


def randomcode(n):
	randomletters = string.ascii_letters  #随机字母
	randomdigits = string.digits          #随机数字
	randomkey = ''.join(random.choice(randomletters+randomdigits) for i in range(n))
	#产生n位随机码字符串，由数字和字母组成
	return randomkey

if __name__ == "__main__":
		a = random.sample(randomcode(8), 200)
		print(a)
# 产生200个8位数的随机码