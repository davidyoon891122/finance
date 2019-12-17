#! -*-coding=utf-8 -*-

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from tools import *

#font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
#rc('font', family=font_name)



def get_url(item_name, code):
	url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)

	print('요청 ULR = {}'.format(url))
	
	try:
		df = pd.DataFrame()
		for page in range(1,50):
			pg_url = '{url}&page={page}'.format(url=url, page=page)
			print(pg_url)
			df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)
		df = df.dropna()
		df.head()
		print(df.head())
	except Exception as e:
		print(e)
		print('There is not {}\n'.format(item_name))



def draw_graph(item_name, code):
	try:
		item = web.DataReader(code+'.KS','yahoo')
		
		plt.plot(item.index, item['Adj Close'], label=item_name)
		plt.legend(loc=1)

		plt.show()
	except Exception as e:
		print(e)
		print('Yahoo에서 존재하지 않는 데이터 입니다.')

def code_query(item_name, code_df):
	try:
		code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False).replace(' ', '')
		return code
	except Exception as e:
		print('존재하지 않는 종목입니다.\n')

def financial_statement(item_name, code):
	pass



def run():
	code_data = parse_stock()
	stock = input('조회하고 싶은 종목을 써주세요. : ')
	
	code = code_query(stock, code_data)
	if code:
		print(code)
		get_url(stock, code)
		draw_graph(stock, code)
	
