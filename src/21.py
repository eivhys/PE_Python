import lib

ans = 0
for x in range(1, 10000):
    if lib.isAmicable(x):
        ans = ans + x
print(ans)
