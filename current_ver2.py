import requests
from bs4 import BeautifulSoup
import lxml
import os
import time


def get_current_price():
	url = 'https://finance.naver.com/item/main.nhn?code=034730'
	rs = requests.get(url)
	soup = BeautifulSoup(rs.text, 'lxml')
	parent = soup.find('div', {'class':'today'})
	price = parent.find('span', {'class':'blind'})
	print(price.text)

if __name__ =='__main__':
	t = time.localtime()

	if t.tm_hour <= 17:
		while True:
			get_current_price()
			time.sleep(5)
			if t.tm_hour == 17:
				print('장 마감\n')
				break


