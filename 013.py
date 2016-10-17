'''用 Python 写一个爬图片的程序，网址：http://tieba.baidu.com/p/2166231880
'''


import requests
from bs4 import BeautifulSoup

url = 'http://tieba.baidu.com/p/2166231880'
response = requests.get(url).content  #content转化为字节
data = BeautifulSoup(response, 'html.parser')
datacontent = data.find_all('img', class_="BDE_Image")  #抓取img标签，class="BED_Image"
count = 1


def download(img):
	global count
	imgdir = "D:\\Efile\\"  #文件保存路径
	filename = str(count) + '.jpg'
	imglink = requests.get(img).content
	#注：open只能打开文件，不能打开文件夹
	with open(imgdir+filename, 'wb') as f:
		f.write(imglink)
	count += 1


for img in datacontent:
	download(img.get('src')) # 下载img标签下的图片链接





