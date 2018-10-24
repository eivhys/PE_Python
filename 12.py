import math

def divisors(n):
    m = 0
    for i in xrange(1, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            m +=2
        if i*i==n:
            m -=1
    return m

for n in xrange(1,1000000):
    Tn=(n*(n+1))/2
    if n%2==0:
        cnt=divisors(n/2)*divisors(n+1)
    else:
        cnt=divisors(n)*divisors((n+1)/2)
    if cnt >= 500:
        print Tn
        break