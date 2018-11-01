power = 5

def addNums(n):
	return sum(map(lambda x:x**power,n))

def getNums(n):
	nums = []
	while n > 0:
		nums.append(n % 10)
		n = n // 10
	return nums[::-1]

s = 0

for num in xrange(2,200000):
	if addNums(getNums(num)) == num:
		s += num
print s
