import lib


def is_pandigital(n, s=9): n = str(n); return len(
    n) == s and not '1234567890'[:s].strip(n)


pan = 0
p = 1
while True:
    p += 1
    if p > 10000 + 1 / 2:
        break
    muls = []
    prods = []
    for x in range(1, 10):
        muls.append(x)
        prods.append(x * p)
        concat = ""
        for prod in prods:
            concat += str(prod)
        if is_pandigital(int(concat)) and int(concat) > pan:
            pan = int(concat)

print(pan)
