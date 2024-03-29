import lib

uLim, lLim = 1000, -999

primes = filter(lambda x: lib.isPrime(abs(x)), range(lLim, uLim))


def quad(a, b, n):
    return n**2 + a*n + b


pair = [0, 0]
best = 0

for a in range(lLim, uLim):
    for b in range(lLim, uLim):
        n = 0
        while abs(quad(a, b, n)) in primes:
            n += 1
        if n > best:
            pair = [a, b]
            best = n

print(pair[0] * pair[1])
