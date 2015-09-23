import sys
import random
from csv import DictReader, DictWriter
from fractions import gcd
import time

#Algorithm directly adapted from lecture slides
def maxSubArray(a, low, high):
	if high==low:
		return (low, high, a[low])
	else:
		mid = (low+high)/2
		left_low, left_high, left_sum    = maxSubArray(a, low, mid)
		right_low, right_high, right_sum = maxSubArray(a, mid + 1, high)
		cross_low, cross_high, cross_sum = maxCrossSubarray(a, low, mid,  high)

        if left_sum > right_sum:
        	if left_sum > cross_sum:
        		return (left_low, left_high, left_sum)
        	else:
        		return (cross_low, cross_high, cross_sum)
        else:
			if right_sum > cross_sum:
				return (right_low, right_high, right_sum)
			else:
				return (cross_low, cross_high, cross_sum)

# Inspired by online implementations
def maxCrossSubarray(A, low, mid,  high):
    left_sum = float(-10000)
    sum = 0
    i = mid
    max_left = 0
    for i in range (mid, low, -1):
        sum = sum + A[i]
        if sum > left_sum:
             left_sum = sum
             max_left = i

    right_sum = float(-10000)
    sum = 0
    j = mid + 1
    max_right = 0
    for j in range (mid + 1, high):
        sum = sum + A[j]
        if sum > right_sum:
             right_sum = sum
             max_right = j
    return (max_left, max_right, left_sum + right_sum)

def test (f):
	fname=f+".csv"
	data = list(DictReader(open(fname, 'r')))
	stockprices= []
	diffarr=[]
	print f
	print 'from: ', data[1]['date'], ' to ', data[-1]['date']
	for x in data:
		stockprices.append(float(x['close']))
	i=0
	for x in stockprices:
		if i==0:
			i+=1
		else:
			diffarr.append(x-stockprices[i-1])
			i+=1

	sell, buy, profit =  maxSubArray(diffarr, 0, len(diffarr)-1)
	print 'Buy Date: ', data[buy+1]['date'] #We essentially skipped the first element in data when building our diffarray, 
	print 'Sell Date: ', data[sell+1]['date'] #so there's a -1 difference
	print 'Profit: ', profit
	print '****'

# main function
def main(argv):
	test("GOOG")
	test("FNMA")
	test("AAPL")

# main entry point
if __name__ == "__main__":
	main(sys.argv)