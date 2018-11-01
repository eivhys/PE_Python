s = ""
n = 1
while len(s) <= 1000000:
	s += str(n)
	n += 1
m = 1
for x in [1, 10, 100, 1000, 10000, 100000, 1000000]:
	m *= int(s[x - 1])
print m