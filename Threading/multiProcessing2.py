import time
import multiprocessing

def calc_square_n_cube(arr,sqr,val,cube):
	for idx, i in enumerate(arr):
		print("Square",i*i)
		sqr[idx] = i*i
		val.value += 1
		cube.put(i*i*i)
		time.sleep(0.1)

	return

arr = [2349,42348,562342,728723]

sqr = multiprocessing.Array('i',len(arr))
val = multiprocessing.Value('i',5)
cube = multiprocessing.Queue()

p1 = multiprocessing.Process(target=calc_square_n_cube, args=(arr,sqr,val,cube))

t = time.time()

p1.start()

p1.join()

print(sqr[:],val.value)

while cube.empty() is False:
	print(cube.get())

print("Done at: ", time.time()-t)

