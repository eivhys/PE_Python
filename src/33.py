from __future__ import division
import lib

fracts = []
for x in xrange(10,100):
	for y in xrange(x,100):
		xn, yn = lib.getNums(x), lib.getNums(y)
		fract = x / y
		if xn[1] == yn[0] and yn[1] > 0:
			if fract == xn[0] / yn[1] and fract < 1:
				fracts.append(fract)
				print x, y

a = 1
for f in fracts:
	a /= f

print a