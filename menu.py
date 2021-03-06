import index
import rate 
import stockgraph
import realtimePrice
import config 


def print_menu():
	print('1. show Index information')
	print('2. show Stock Price')
	print('3. show Exchange Rate')
	print('4. Rate calculator')
	print('5. Real-Time current price check')
	print('6. exit')
	



def run(driver_path=None):
	while True:
		try:
			print_menu()
			menu = input('Which information do you want to know : ')
			if menu == '1':
				i = index.Index(driver_path)
				i.print_index()
			elif menu == '2':
				stockgraph.run()
			elif menu == '3':
				r = rate.Rate(driver_path)
				r.print_rate()
			elif menu == '4':
				r = rate.Rate(driver_path)
				r.calculate_rate()
			elif menu == '5':
				realtimePrice.run_mystock()
				break
			elif menu == '6':
				import sys
				sys.exit()
			else:
				print('invalid number!! write valid number')
		except KeyboardInterrupt as e:
			print('시스템이 강제로 종류 되었습니다.\n')
			break


if __name__ == '__main__':

	conf = config.Config('./fin.conf')
	driver = conf.fallback['driver']['path']
	run(driver)
