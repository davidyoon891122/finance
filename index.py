from bs4 import BeautifulSoup
from selenium import webdriver
import driver


class Index:
	def __init__(self, driver_path=None):
		self.driver_path = driver_path
		self.driver = driver.Driver(self.driver_path)

	def parse_index_tags(self):
		bs = self.driver.get_soup()
		index_tags = bs.select('div.heading_area a span.num')
		return index_tags



	def parse_time(self):
		bs = self.driver.get_soup()
		date_tags = bs.find('div', {'class':'ly_realtime'})
		time = bs.find('span', {'id':'time'})
		return time


	def index_information(self):
		index_tags = self.parse_index_tags()
		time_tags = self.parse_time()
		datetime = time_tags.text
		kospi = index_tags[0].text
		kosdaq = index_tags[1].text
		kospi200 = index_tags[2].text
		return datetime, kospi, kosdaq, kospi200


	def print_index(self):
		datetime, kospi, kosdaq, kospi200 = self.index_information()
		print('DateTime is : {}'.format(datetime))
		print('KOSPI is : {}'.format(kospi))
		print('KOSDAQ is : {}'.format(kosdaq))
		print('KOSPI200 is : {}'.format(kospi200))


	

