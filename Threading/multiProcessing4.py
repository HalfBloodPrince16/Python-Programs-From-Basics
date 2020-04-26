import time
from multiprocessing import Pool

def f(n):
	sum = 0
	for i in range(1000):
		sum += i*i*i
	return sum


if __name__  ==  "__main__":
	
	t1 = time.time()
	p = Pool()
	result = p.map(f,range(10000))
	p.close()
	p.join()

	print("Pool took : ", time.time()-t1)

	t2 = time.time()
	result = []
	for i in range(10000):
		result.append(f(i))

	print("serial process took : ",time.time()-t2)