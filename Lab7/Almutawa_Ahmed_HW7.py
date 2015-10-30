import sys
import itertools

filename   = sys.argv[-2]
outputname = sys.argv[-1]
# filename   = "sample.txt"
# outputname = "output.txt"
x, y, n, abc = -1, -1, -1, []

def parser():
	#Input and formatting
	file      = open(filename)
	xy        = file.next().split()
	(x, y, n) = (int(xy[0]), int(xy[1]), int(file.next()))
	abc       = []
	for i in file:
		j = i.split()
		j[0], j[1], j[2] = int(j[0]), int(j[1]), int(j[2]) #String to int on a, b, c vals
		abc.append(j)
	return (x,y,n,abc)

def rectangle(cloth, piece, x, y, x2, y2):
	area = int(piece)
	d = 0
	#k=i,
	for i in range (0,y):
		for j in range (0,x):
			for k in range (i, y2):
				if(cloth[k][j] == '1'):
					d = d + 1
					if(d == area):
						for a in range (k-y2+1, k+1):
							for b in range (j-x2+1, j+1):
								cloth[a][b] = '0'
						return True, (a, b)
						break
				else:
					d = 0
	return False, (0,0)

def priceCalculate(x, y, n, abc):
	rows         = []
	cloth        = []
	prices       = []
	cuts         = []
	areap        = []
	combinations = []
	curatedcuts  = []
	area         = x*y
	max_profit   = 0

	# creating a grid of 1's the size of the cloth
	for i in range(0, x):
		rows.append('1')
	for i in range(0, y):
		cloth.append(rows)

	for i in range(0, len(abc)):
		cuts.append(abc[i][0] * abc[i][1])
		prices.append(abc[i][2])
		areap = cuts[i], prices[i]
	
	for i in range(0, len(abc)):
		pcuts = list(itertools.combinations(cuts,i))
		for q in range(0, len(pcuts)):
			total = 0
			for v in range(0, len(pcuts[q])):
				total += int(pcuts[q][v])
			if(total < area):
				z = 0
				for w in range(0, len(pcuts[q])):
					if(pcuts[q][w] == cuts[w]):
						a = int(abc[w][0])
						b = int(abc[w][1])
					valid = rectangle(cloth,pcuts[q][w],x,y,a,b)
					if(valid[0] == True):
						curatedcuts.append((a, b, z, valid[1]))
						z += 1
				if(z == len(pcuts[q])):
					combinations.append(pcuts[q])

	for i in range(0, len(combinations)):
		acc = 0
		for j in range(0, len(combinations[i])):
			tmp = int(combinations[i][j])
			acc = acc + tmp
		if(acc > max_profit):
			max_profit = acc

	output = open(outputname, 'w')
	sys.stdout = output
	print "Max profit is", "$" + str(max_profit), "with", str(len(curatedcuts)), "cuts"
	t = 1
	for i in curatedcuts:
		print str(t)+ ':-', '\tx= '+str(i[0]), '|', 'y= '+str(i[1]), '|', 'orientation= '+str(i[2]), '|', 'cutting point= '+str(i[3])
		t+=1

def main(argv):
	x, y, n, abc = parser()
	priceCalculate(x, y, n, abc)

if __name__ == '__main__':
  main(sys.argv)