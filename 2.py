import lib

sum = 0
for n in lib.fibonacci(4000000):
    if n % 2 == 0:
        sum += n
print(sum)