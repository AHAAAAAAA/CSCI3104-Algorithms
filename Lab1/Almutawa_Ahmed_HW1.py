# imports
import sys
import itertools
import time
import random

def randgen (n):
	i=0
	j=[]
	for i in range(0,n):
		j.append(random.randint(0,10*n))
	return j

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

def running(n):
	i=0
	times=[]
	min=0
	max=0
	print (n, ':')
	for i in range(0, 10):
		j=randgen(n)
		start_time = time.time()
		selectionSort(j)
		end_time = time.time()
		timez=end_time-start_time
		times.append(timez)
		if(i==0):
			min=timez
			max=timez
		if (timez < min):
			min=timez
		if (timez > max):
			max=timez
	i=0
	avg=0
	for i in range(0,10):
		avg += times[i]
	avg /= 10
	print ('Minimum is ', min)
	print ('Maximum is ', max)
	print ('Average is ', avg)
	return

# main function
def main(argv):
	running(100)
	running(1000)
	running(10000)
	return

# main entry point
if __name__ == "__main__":
	main(sys.argv)
