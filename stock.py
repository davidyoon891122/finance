import pandas as pd


def get_url(item_name, code_df):
	code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
	url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)

	print('요청 URL = {}'.format(url))
	return url



def main():
	item_name = input('write stock name which wants to know current price: ')
	code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
	code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
	code_df = code_df[['회사명', '종목코드']]
	code_df = code_df.rename(columns={'회사명':'name', '종목코드':'code'})
	code_df.head()

	url = get_url(item_name, code_df)

	df = pd.DataFrame()
	for page in range(1,5):
		pg_url = '{url}&page={page}'.format(url=url, page=page)
		df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)
	df = df.dropna()
	df.head()
	print(df.head())


def print_stock():
	main()


if __name__ =='__main__':
	main()
