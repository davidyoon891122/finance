from index import *
from stock import *
from rate import *



def print_menu():
	print('1. show Index information')
	print('2. show Stock Price')
	print('3. show Exchange Rate')
	print('4. exit')



def run():
	while 1:
		print_menu()
		menu = int(input('which information do you want to know'))
		if menu == 1:
			print_index()
		elif menu == 2:
			print_stock()
		elif menu == 3:
			print_rate()
		elif menu == 4:
			import sys
			sys.exit()
		else:
			print('invalid number!! write valid number')
	


if __name__ == '__main__':
	run()
