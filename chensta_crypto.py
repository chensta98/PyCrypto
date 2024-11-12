import math
import secrets

# Greatest Common Divisor using Euclid Algo
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Extended Euclid
def extendedEuclid(a, b):
    x, y = 0, 1
    u, v = 1, 0 
    while a != 0:
        q = b // a
        r = b % a
        m = x - u * q
        n = y - v * q
        b, a = a,r
        x,y = u,v
        u,v = m,n        
    return b, x, y

# Fast Exponenentiation (y should start as 1 always)
def fastExpo(x, e, m, y=1):
    if e == 0:
        return y
    elif e % 2 == 0:
        x2 = (x ** 2) % m
        e2 = e / 2
        return fastExpo(x2, e2, m, y)
    else:
        y2 = (x * y) % m
        e2 = e - 1
        return fastExpo(x, e2, m, y2)

# Prime Factorization
def primeFactors(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    for x in range(3,math.ceil(math.sqrt(n))+2, 2):
        while n % x == 0:
            factors.append(x)
            n = n / x

    return factors

# Primitive Root Search Algo
def primRootSearch(n):
    rootFound = False
    count = 0

    while rootFound == False:
        count = count + 1
        root = secrets.randbelow(n)
        rootFound = True
        factors = list(set(primeFactors(n-1)))

        for x in factors:
            # print("Root:    %d  p-1/q:  %d  M:  %d" % (root,(n-1)/x,n))
            if fastExpo(root,(n-1)/x,n) == 1:
                rootFound = False

    # print("Count:   %d" % (count))
    return root

# Baby-Step Giant-Step
def babyStepGiantStep(b, a, p):
    m = math.ceil(math.sqrt(p - 1))
    jdict = {}

    # Compute b ^ all values from 0 to sqrt p and put in Dict
    for x in range(m):
        jdict[fastExpo(b, x, p)] = x

    # Get Inverse of b
    _, inv, _ = extendedEuclid(b, p)
    if inv < 0:
        inv = inv + p
    
    c = fastExpo(inv, m, p)

    for i in range(m):
        res = (fastExpo(c, i, p) * a) % p
        if res in jdict:
            return ((i * m) + jdict[res]) % (p - 1)

    
    

