import threading 
import ctypes
import time


def print_num():
	for i in range(100):
		print('threading {}'.format(threading.currentThread().getName()))
		time.sleep(3)


def terminate_thread(thread):
	if not threading.Thread.isAlive():
		return

	exe = ctypes.py_object(SystemExit)
	res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
	
	if res == 0:
		raise ValueError('nonexistent thread id')
	elif res > 1:
		ctypes.pythonapi.PyThreadState_SetAsyncExc(threading.Thread.ident, None)
		raise SystemError('PyThreadState_SetAsyncExc failed')




if __name__ =='__main__':
	for i in range(3):
		t1 = threading.Thread(target=print_num)
		t1.daemon = True
		t1.start()


