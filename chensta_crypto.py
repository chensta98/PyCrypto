# Greatest Common Divisor using Euclid Algo
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Extended Euclid
def extendedGcd(a, b):
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
        return fastExpoRecur(x2, e2, m, y)
    else:
        y2 = (x * y) % m
        e2 = e - 1
        return fastExpoRecur(x, e2, m, y2)

# Primitive Root Search Algo

# Baby-Step Giant-Step


