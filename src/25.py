m = 1
n = 1
i = 1
while True:
    i += 1
    if len(str(m)) >= 1000:
        break
    tmp = m
    m += n
    n = tmp
print(i)
