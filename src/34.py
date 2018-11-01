import lib

a = 0
for x in xrange(3,100000):
	s = sum(map(lambda x: lib.factorial(x), lib.getNums(x)))
	if s == x:
		a += s
print a