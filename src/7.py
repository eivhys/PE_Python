import lib

primes = 0
n = 0
while primes != 10001:
	n = n + 1
	if lib.isPrime(n):
		primes = primes + 1
	print(primes)
print(n)