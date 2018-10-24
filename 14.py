def collatz(n):
	c = 1
	while n > 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = n * 3 + 1
		c = c + 1
	return c
max = 0
a = 0
for x in xrange(1,1000000):
	c = collatz(x)
	if c > max:
		max = c
		a = x
print a