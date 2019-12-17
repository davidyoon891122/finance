from bs4 import BeautifulSoup
from selenium import webdriver
import driver



class Rate:
	def __init__(self, driver_path=None):
		self.driver_path = driver_path
		self.driver = driver.Driver(self.driver_path)

	def parse_rate_tags(self):
		bs = self.driver.get_soup()
		rate_tags = bs.select('div.group1 table.tbl_home tbody tr td')
		return rate_tags


	def rate_information(self):
		rate_tags = self.parse_rate_tags()
		
		US = rate_tags[0].text
		JP = rate_tags[2].text
		EU = rate_tags[4].text
		CN = rate_tags[6].text	
		return US, JP, EU, CN


	def print_rate(self):
		US, JP, EU, CN = self.rate_information()
		print('US rate is : {}'.format(US))
		print('JP rate is : {}'.format(JP))
		print('EU rate is : {}'.format(EU))
		print('CN rate is : {}'.format(CN))


	def calculate_rate(self):
		US, JP, EU, CN = self.rate_information()
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







