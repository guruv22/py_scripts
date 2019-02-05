#!/usr/bin/python

import threading
import time
import Queue

def func(count, q_msg):
	try:
		for i in range(count):
			if (i == 7):
				assert 0, ('Failure in thread')
			print("In thread: {}".format(i))
			time.sleep(1)
	except Exception as e:
		q.put(e)

q=Queue.Queue()
test_thread = threading.Thread(
	target=func, args=(10,q,))
test_thread.start()    
time.sleep(3)
for j in range(100,110):
	print("In main:{}".format(j))
	time.sleep(1)
	
test_thread.join()
while not q.empty():
	print ("###Raise assertion in main program: Start###\n")
	str = str(q.get())
	print (str+"\n")
		
print("Success")
