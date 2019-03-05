import lib
sum = 0
for x in range(1, 2000000):
    if lib.isPrime(x):
        sum = sum + x
print(sum)
