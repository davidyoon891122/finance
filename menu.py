from index import *
from stock import *
from rate import *
import stockgraph



def print_menu():
	print('1. show Index information')
	print('2. show Stock Price')
	print('3. show Exchange Rate')
	print('4. exit')
	



def run():
	while True:
		try:
			print_menu()
			menu = int(input('which information do you want to know'))
			if menu == 1:
				print_index()
			elif menu == 2:
				stockgraph.run()
			elif menu == 3:
				print_rate()
			elif menu == 4:
				import sys
				sys.exit()
			else:
				print('invalid number!! write valid number')
		except KeyboardInterrupt as e:
			print('시스템이 강제로 종류 되었습니다.\n')
			break


if __name__ == '__main__':
	run()
