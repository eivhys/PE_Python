import itertools

a = '0123456789'
k = len(a)
c = 0
for p in itertools.permutations(a, k):
    c += 1
    if c == 1000000:
    	print "".join(p),
    	break