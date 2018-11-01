import lib

max = 0
for x in range(1,1000):
	for y in range(1,1000):
		if x*y > max and lib.isPalindrome(x*y):
			max = x*y
print(max)