for a in xrange(1,500):
	for b in xrange(a + 1,500):
		for c in xrange(b + 1,500):
			if a**2 + b**2 == c**2 and a + b + c == 1000:
				print(a*b*c)