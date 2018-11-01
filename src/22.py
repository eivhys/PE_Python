with open('../misc/22.txt', 'r') as problem:
    data=problem.read().replace('\n', '').replace('"','')

names = sorted(data.split(","))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def namePoints(s):
	for x in xrange(0,len(alphabet)):
		if s == alphabet[x]:
			return x + 1
	return 0

m = 0
for n in xrange(0,len(names)):
	s = sum(map(lambda x : namePoints(x), names[n]))
	m = m + (s * (n + 1))
print m