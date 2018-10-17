#! -*-coding=utf-8 -*-

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

s_file = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'

def parse_stock(s_file):
	code_df = pd.read_html(s_file, header=0)[0]
	code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
	code_df = code_df[['회사명', '종목코드']]
	code_df = code_df.rename(columns={'회사명':'name', '종목코드':'code'})
	return code_df



def get_url(item_name, code):
	url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)

	print('요청 ULR = {}'.format(url))
	
	try:
		df = pd.DataFrame()
		for page in range(1,20):
			pg_url = '{url}&page={page}'.format(url=url, page=page)
			df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)
		df = df.dropna()
		df.head()
		print(df.head())
	except Exception as e:
		print(e)
		print('There is not {}\n'.format(item_name))



def draw_graph(item_name, code):
	item = web.DataReader(code+'.KS','yahoo')
	
	plt.plot(item.index, item['Adj Close'], label=item_name)
	plt.legend(loc=1)

	plt.show()

def code_query(item_name, code_df):
	code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
	return code

def financial_statement(item_name, code):
	pass



def run():
	code_data = parse_stock(s_file)
	stock = input('조회하고 싶은 종목을 써주세요. : ')
	
	code = code_query(stock, code_data)
	print(code)
	get_url(stock, code)
	draw_graph(stock, code)
	
