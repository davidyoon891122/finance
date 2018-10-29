import requests
from bs4 import BeautifulSoup
import lxml
import os
import time
import threading
import pandas as pd

s_file = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'


def parse_stock(s_file):
	code_df = pd.read_html(s_file, header=0)[0]
	code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
	code_df = code_df[['회사명', '종목코드']]
	code_df = code_df.rename(columns={'회사명':'name', '종목코드':'code'})
	
	return code_df



def code_query(item_name, code_df):
	try:
		code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
		return code
	except Exception as e:
		print(e)
		print('존재하지 않는 종목입니다.\n')




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
		m_rate = rate.replace('\t', '').replace('\n','')
	else:
		rate = None
		m_rate = None

	time_tag = soup.find('span', {'id':'time'})

	if time_tag != None:
		time = time_tag.text
		m_time = time.replace('\n','')

	return [m_time, price, m_rate]




def run():
	code_data = parse_stock(s_file)
	stock = input('조회하고 싶은 종목을 써주세요.:')

	code = code_query(stock, code_data)

	if code:
		while True:
			t = time.localtime()
			try:
				result = get_current_price(code)
				print(result)
				time.sleep(5)
				if t.tm_hour >= 15:
					print('장이 마감되어 프로그램을 종류합니다.\n')
					break
			except KeyboardInterrupt:
				print('프로그램 정지 신호 포착! 정지합니다.\n')
				break
				
		
		




if __name__=='__main__':
	num_of_thread = input('확인하고 싶은 종목 수를 써주세요')
	
	for i in range(int(num_of_thread)):
		thread = threading.Thread(target=run)
		print(thread)
		thread.start()



	


