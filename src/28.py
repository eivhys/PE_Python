spiral = xrange(1, 1001**2 + 1)
sum = 0
curlW = 1 # width of "curl"
skipper = 0 # how many entried should be skipped 
for x in spiral:
	if skipper == 0:
		sum += x
		tmp = x**0.5
		if int(tmp) == tmp:
			curlW = tmp
		skipper = curlW
	else:
		skipper -= 1
print sum