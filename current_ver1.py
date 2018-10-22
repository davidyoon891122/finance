import requests
from bs4 import BeautifulSoup
import lxml
import os
import time




def get_current_price(code):
	url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(code)
	rs = requests.get(url)
	soup = BeautifulSoup(rs.text, 'lxml')
	price_tag = soup.find('strong', {'class':'tah p11'})
	if price_tag != None:
		price = price_tag.text
	else:
		price = None
	rate_parent = soup.find('strong', {'id':'_rate'})
	rate_tag = rate_parent.find('span', {'class':'tah p11 nv01'})
	if rate_tag != None:
		rate = rate_tag.text
		m_rate = rate.replace('\t','').replace('\n','')
	else:
		rate = None
		m_rate = None

	time_tag = soup.find('span', {'id':'time'})

	if time_tag != None:
		time = time_tag.text
		m_time = time.replace('\n', '')
	return [m_time, price, m_rate]




if __name__ == '__main__':
	while True:
		t = time.localtime()
		if t.tm_hour <= 16:
				try:
					rt = get_current_price('034730')
					time.sleep(5)
					print(rt)
					if t.tm_hour == 16:
						print('장 마감\n')
						break
				except KeyboardInterrupt:
					print('프로그램 정지')
					break
