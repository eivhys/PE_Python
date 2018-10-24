def fibonacci(limit):
    n = 1
    m = 2
    fib = [1, 2]
    while m <= limit:
        tmp = n
        n = m
        m += tmp
        fib.append(m)
    return fib

def isPrime(n):
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False

def amicableHelpF(n):
    s = 0
    for x in xrange(1, n):
        if n % x == 0:
            s = s + x
    return s

def properDivs(n):
    divs = []
    for x in xrange(1,n):
        if n % x == 0:
            divs.append(x)
    return divs

def isAmicable(n):
    a = sum(properDivs(n))
    b = sum(properDivs(a))
    return n == b and a != n


def max(m, n):
    if m > n:
        return m
    else:
        return n

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def rotate90(l):
    return [list(reversed(x)) for x in zip(*l)]

def listMirror(n):
    m = []
    for x in xrange(0,len(n)):
        row = []
        for y in xrange(len(n[x]) - 1, -1, -1):
            row.append(n[x][y])
        m.append(row)
    return m

def factorial(n):
    l = 1
    for x in xrange(1,n+1):
        l = l * x
    return l