ps = 0
tris = 0
for p in xrange(30, 1000, 30):
	tri = []
	print p
	for a in xrange(1, p / 2):
		for b in xrange(a, p / 2):
			for c in xrange(b, p / 2):
				if a + b + c == p:
					if a**2 + b**2 == c**2:
						tri.append({a, b, c})
	if len(tri) > tris:
		ps = p
		tris = len(tri)
print ps