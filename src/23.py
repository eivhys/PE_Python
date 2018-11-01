import math
import bisect
numbers = list(range(1, 28123))
abundant = set()

for n in numbers:
    m = 2
    divisorsum = 1
    while m <= math.sqrt(n):
        if n % m == 0:
            divisorsum += m + (n / m)
        m += 1
    if math.sqrt(n) % 1 == 0:
        divisorsum -= math.sqrt(n)
    if divisorsum > n:
        abundant.add(n)
#print(sorted(abundant))
nonabundantsum = 0
for i in numbers:
    issumoftwoabundants = False
    for k in abundant:
        if k > i / 2:
            break

        if i - k in abundant:
            issumoftwoabundants = True
            break

    if not issumoftwoabundants:
        nonabundantsum += i

print(nonabundantsum)