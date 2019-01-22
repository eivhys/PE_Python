import lib

def isPentagonal(n):
	p = 0
	c = 0
	while p < n:
		p = lib.pentagonal(c)
		c += 1
	return p == n
pk = 0
found = False
while not found:
	for pj in xrange(1,pk):
		p1 = lib.pentagonal(pk)
		p2 = lib.pentagonal(pj)
		pAdd = p1 + p2
		pDiff = p1 - p2
		if isPentagonal(pAdd) and isPentagonal(pDiff):
			print p1 - p2
			found = True
	pk += 1