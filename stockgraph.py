#! -*-coding=utf-8 -*-

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

s_file = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'

def parse_stock(s_file):
	code_df = pd.read_html(s_file, header=0)[0]
	code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
	code_df = code_df[['회사명', '종목코드']]
	code_df = code_df.rename(columns={'회사명':'name', '종목코드':'code'})
	return code_df



def get_url(item_name, code_df):
	code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
	url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)

	print('요청 ULR = {]'.format(url))
	return url



def draw_graph(item_name, code_df):
	code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
	item = web.DataReader(code+'.KS','yahoo')
	
	plt.plot(item.index, item['Adj Close'], label=item_name)
	plt.legend(loc=1)

	plt.show()


if __name__ =='__main__':
	code_data = parse_stock(s_file)
	stock = input('조회하고 싶은 종목을 써주세요. : ')
	draw_graph(stock, code_data)

	
