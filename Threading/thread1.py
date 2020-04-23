#tutorial : https://realpython.com/intro-to-python-threading/
#docs : https://docs.python.org/3/library/threading.html
#Python 3.6.9

import logging as log
import time
import threading


def thread_func(name):
	log.info("Thread %s: starting", name)
	time.sleep(2)
	log.info("Thread %s: finishing", name)

if __name__ == "__main__":
	format = "%(asctime)s: %(message)s"
	log.basicConfig(format=format, level=log.INFO,
					 datefmt="%H:%M:%S")
	log.info("Main  : before creating thread")
	x = threading.Thread(target=thread_func, args=(1,),
						 daemon=None)
	log.info("Main  : before running thread")
	x.start()
	time.sleep(0.1)
	log.info("Main  : waiting for the thread to finish")
	x.join()
	log.info("Main  : all done")

