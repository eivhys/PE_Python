toNineteen = {
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
	10:"ten",
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	14:"fourteen",
	15:"fifteen",
	16:"sixteen",
	17:"seventeen",
	18:"eighteen",
	19:"nineteen"
}

toNinety = {
	2:"twenty",
	3:"thirty",
	4:"forty",
	5:"fifty",
	6:"sixty",
	7:"seventy",
	8:"eighty",
	9:"ninety",
}

sum = 0

for x in xrange(999,0,-1):
	date = ""
	h = x // 100
	t = (x % 100) // 10
	s = x % 10
	if h > 0:
		date = date + toNineteen.get(h)
		date = date + "hundred"
		if x % 100 != 0:
			date = date + "and"
	if t > 1:
		date = date + toNinety.get(t)
		if s > 0:
			date = date + toNineteen.get(s)
	elif x % 100 > 0:
		date = date + toNineteen.get(x%100)
	#print (x, " ",date)
	sum = sum + len(date)
print sum + len("onethousand")