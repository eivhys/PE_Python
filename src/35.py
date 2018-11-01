import itertools
import lib

p = []
for x in xrange(1,1000000):
	flag = True
	if lib.isPrime(x):
		for n in lib.circulars(x):
			if flag:
				if not lib.isPrime(lib.listToNum(n)):
					flag = False
		if flag:
			p.append(x)
print len(p), p