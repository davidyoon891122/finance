from bs4 import BeautifulSoup
from selenium import webdriver
options = webdriver.ChromeOptions() 
options.add_argument('headless')
options.add_argument('disable_gpu')
driver = webdriver.Chrome('/chromedriver', chrome_options=options)

main_url = 'http://finance.naver.com'


def get_soup(url):
	driver.get(url)
	return BeautifulSoup(driver.page_source, 'lxml')


def parse_rate_tags():
	bs = get_soup(main_url)
	rate_tags = bs.select('div.group1 table.tbl_home tbody tr td')
	return rate_tags


def rate_information():
	rate_tags = parse_rate_tags()
	
	US = rate_tags[0].text
	JP = rate_tags[2].text
	EU = rate_tags[4].text
	CN = rate_tags[6].text	
	return US, JP, EU, CN


def print_rate():
	US, JP, EU, CN = rate_information()
	print('US rate is : {}'.format(US))
	print('JP rate is : {}'.format(JP))
	print('EU rate is : {}'.format(EU))
	print('CN rate is : {}'.format(CN))


def calculate_rate():
	US, JP, EU, CN = rate_information()
	amount_kor = input("How much money do you want to change : ")
	
	amount = int(amount_kor.replace(",", ""))
	US = float(US.replace(",", ""))
	JP = float(JP.replace(",", ""))
	EU = float(EU.replace(",", ""))
	CN = float(CN.replace(",", ""))
	US_result = amount / US
	JP_result = amount / (JP * 0.01)	
	EU_result = amount / EU
	CN_result = amount / CN

	print("{} WON : {:0.2f} USD".format(amount_kor, US_result))
	print("{} WON : {:0.2f} JPY".format(amount_kor, JP_result))
	print("{} WON : {:0.2f} EUR".format(amount_kor, EU_result))
	print("{} WON : {:0.2f} CNY".format(amount_kor, CN_result))







