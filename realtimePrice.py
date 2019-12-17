import requests
from bs4 import BeautifulSoup
import lxml
import os
import time
import threading
import pandas as pd
from tools import *


def code_query(item_name, code_df):
	try:
		code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False).replace(' ', '')
		return code
	except Exception as e:
		print(e)
		print('존재하지 않는 종목입니다.\n')




def get_current_price(code):
	url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(code)
	rs = requests.get(url)
	soup = BeautifulSoup(rs.text, 'lxml')
	
	today = soup.find('div', {'class':'today'})

	price_tag = today.find('p', {'class':'no_today'})
	price = price_tag.find('span', {'class':'blind'})
	if price != None:
		price = price.text
	else:
		price = None

	rate_tag = today.find('p', {'class':'no_exday'})
	rate = rate_tag.find_all('span', {'class':'blind'})[1]
	if rate != None:
		rate = rate.text
	else:
		rate = None
	time_tag = soup.find('span', {'id':'time'})
	if time_tag != None:
		time = time_tag.text
		time = time.replace('\n', '')


	return [time, price, rate]




def run(name):
	code_data = parse_stock()
	stock = name
	code = code_query(stock, code_data)
	if code:
		while True:
			t = time.localtime()
			try:
				result = get_current_price(code)
				print('종목: {}'.format(stock),  result)
				time.sleep(5)
				if t.tm_hour >= 15:
					print('장이 마감되어 프로그램을 종류합니다.\n')
					break
			except KeyboardInterrupt:
				print('프로그램 정지 신호 포착! 정지합니다.\n')
				break
				
		
		
def select_stock():
	number = input("실시간으로 확인 하실 종목의 개수를 정해주세요 :")
	number = int(number)
	name_list = []
	for i in range(number):
		name = input("{} 번째 종목 : ".format(i+1))
		name_list.append(name)

	return name_list



def run_mystock():
	name_list = select_stock()

	for i in range(len(name_list)):
		thread = threading.Thread(target=run, args=(name_list[i],))
		thread.daemon = True
		print(thread)
		thread.start()


