import lib

p = []
for x in range(10, 1000000):
    if lib.isPrime(x):
        n = lib.getNums(x)
        flag = True
        nl, nr = n, n
        while len(nl) > 1:
            nl = nl[:-1]
            nr = nr[1:]
            if not lib.isPrime(lib.listToNum(nr)) or not lib.isPrime(lib.listToNum(nl)):
                flag = False
        if flag:
            p.append(x)
print(sum(p))
