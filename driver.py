from selenium import webdriver
from bs4 import BeautifulSoup



class Driver():
    def __init__(self, driver_path=None):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable_gpu')
        self.driver = webdriver.Chrome(driver_path, chrome_options=options)
        self.url = 'http://finance.naver.com'


    def get_soup(self):
        self.driver.get(self.url)
        return BeautifulSoup(self.driver.page_source, 'lxml')


