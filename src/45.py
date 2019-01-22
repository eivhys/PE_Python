import lib

found = False
p = 157 + 1
while not found:
		for h in xrange(1, p):
			n = lib.pentagonal(p) + lib.hexagonal(h)
			if not n == 40755 and lib.isHexagonal(n) and lib.isPentagonal(n) and lib.isTriangle(n):
				found = True
				print n
	p += 1