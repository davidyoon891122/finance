import requests
import pandas as pd


def get_financial_statements(code):
	url = 'http://media.kisline.com/highlight/mainHighlight.nice?nav=1&paper_stock={}'.format(code)
	df_list = pd.read_html(url)
	df = df_list[4]
	print(type(df))
	print(df.keys())
	


if __name__=='__main__':
	get_financial_statements('034730')
