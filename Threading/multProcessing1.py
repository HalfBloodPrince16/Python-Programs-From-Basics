import time
import multiprocessing


squares = []

def calc_square(arr):
	global squares
	for i in arr:
		print("Square",i*i)
		squares.append(i*i)
		time.sleep(0.1)

	return

def calc_cube(arr):
	for i in arr:
		print("Cube",i*i*i)
		time.sleep(0.1)
		
	return

arr = [2349,42348,562342,728723]

p1 = multiprocessing.Process(target=calc_square, args=(arr,))
p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

t = time.time()

p1.start()
p2.start()

p1.join()
p2.join()

print(squares)
print("Done at: ", time.time()-t)

