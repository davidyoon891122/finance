from bs4 import BeautifulSoup
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable_gpu')
driver = webdriver.Chrome('/home/david/python/chromedriver', chrome_options=options)


main_url = 'http://finance.naver.com'


def get_soup(url):
	driver.get(url)
	return BeautifulSoup(driver.page_source, 'lxml')



def parse_index_tags():
	bs = get_soup(main_url)
	index_tags = bs.select('div.heading_area a span.num')
	return index_tags



def parse_time():
	bs = get_soup(main_url)
	date_tags = bs.find('div', {'class':'ly_realtime'})
	time = bs.find('span', {'id':'time'})
	return time


def index_information():
	index_tags = parse_index_tags()
	time_tags = parse_time()
	datetime = time_tags.text
	kospi = index_tags[0].text
	kosdaq = index_tags[1].text
	kospi200 = index_tags[2].text
	return datetime, kospi, kosdaq, kospi200


def print_index():
	datetime, kospi, kosdaq, kospi200 = index_information()
	print('DateTime is : {}'.format(datetime))
	print('KOSPI is : {}'.format(kospi))
	print('KOSDAQ is : {}'.format(kosdaq))
	print('KOSPI200 is : {}'.format(kospi200))


	

