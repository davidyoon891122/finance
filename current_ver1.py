import requests
from bs4 import BeautifulSoup
import lxml


def get_current_price(code):
	url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(code)
	rs = requests.get(url)
	soup = BeautifulSoup(rs.text, 'lxml')
	price = soup.find('strong', {'class':'tah p11'}).text
	rate_parent = soup.find('strong', {'id':'_rate'})
	rate = rate_parent.find('span', {'class':'tah p11 nv01'}).text
	time = soup.find('span', {'id':'time'}).text
	m_time = time.replace('\n', '')
	m_rate = rate.replace('\t', '').replace('\n','')

	
	return [m_time, price, m_rate]


	

if __name__ == '__main__':
	rt = get_current_price('034730')
	print(rt)
