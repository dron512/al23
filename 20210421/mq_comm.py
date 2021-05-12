import Queue
import threading
import time

HOW_MANY_MESSAGES = 10
mq = Queue.Queue(HOW_MANY_MESSAGES)

flag_exit = False
def t1():
	value = 0
	
	while True:
		value = value + 1
		mq.put(value)
		time.sleep(0.1)
		if flag_exit: break
		
thread = threading.Thread(target=t1)
thread.start()

try:
	while True:
		value = mq.get()
		print("Read Data %d" %(value))

except KeyboardInterrupt:
	pass
flag_exit = True
thread.join()