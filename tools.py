import pandas as pd


s_file = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'


def parse_stock():
	code_df = pd.read_html(s_file, header=0)[0]
	code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
	code_df = code_df[['회사명', '종목코드']]
	code_df = code_df.rename(columns={'회사명':'name', '종목코드':'code'})
	
	return code_df.replace(' ', '')