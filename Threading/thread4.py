import time
import threading

def calc_square(arr):
	for i in arr:
		print("Square",i*i)

	return

def calc_cube(arr):
	for i in arr:
		print("Cube",i*i*i)
	return

arr = [2349,42348,562342,728723]

t1 = threading.Thread(target=calc_square,args=(arr,))
t2 = threading.Thread(target=calc_cube,args=(arr,))

t = time.time()

"""
calc_square(arr)
calc_cube(arr)
"""

t1.start()
t2.start()

t1.join()
t2.join()

print("Program completed at:",time.time()-t)

