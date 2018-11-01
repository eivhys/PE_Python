terms = []
lim = 100
for x in xrange(2,lim+1):
	for y in xrange(2,lim+1):
		terms.append(x**y)
print len(set(sorted(terms)))