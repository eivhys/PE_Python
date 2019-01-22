import lib
from itertools import permutations

divs = [17, 13, 11, 7, 5, 3, 2]

total = 0

for i in permutations('0123456789'):
	if i[0] == '0':
		continue
	n = ''.join(list(i))
	valid = True
	for j in xrange(0, len(divs)):
		x = n[len(divs) - j:len(divs) - j + 3]
		if int(x) % divs[j]:
			valid = False
			break
	if valid:
		total += int(n)

print total