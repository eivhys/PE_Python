import lib

n = 0
for x in range(1, 10000000):
    if lib.isPandigital(x):
        if lib.isPrime(x):
            n = lib.max(x, n)
print(n)
