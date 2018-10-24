import lib

num = 600851475143
for n in range(int(num**0.5)+1, 1, -1):
    if num % n == 0 and lib.isPrime(n):
        print(n)
        break