import math
import random
import chensta_crypto

class NaorRein:
    def __init__(self, n):
        self.n = n
        max_val = math.pow(2, n)
        p = random.randrange(2, max_val)
        q = random.randrange(2, max_val)
        while not chensta_crypto.millerRabin(p):
            p = random.randrange(2, max_val)
        while not chensta_crypto.millerRabin(q):
            q = random.randrange(2, max_val)
        
        self.N = p * q

        self.a = [] # list of tuples
        for _ in range(n):
            pair = (random.randrange(1,self.N), random.randrange(1,self.N))
            self.a.append(pair)
        
        square_base = random.randrange(1, self.N)
        while chensta_crypto.gcd(square_base, self.N) != 1:
            square_base = random.randrange(1, self.N)

        self.square = chensta_crypto.fastExpo(square_base, 2, self.N)

        r_dec = random.randrange(1, math.pow(2, 2 * n))
        self.r_bin = chensta_crypto.decToBin(r_dec)
        while len(self.r_bin) < 2 * n:
            self.r_bin.insert(0,0)

    def f(self, x):
        x_bin = chensta_crypto.decToBin(x)
        a_sum = 0
        for i in range(len(x_bin)):
            a_sum = a_sum + self.a[i][x_bin[i]]
            # print(a_sum)

        beta_dec = chensta_crypto.fastExpo(self.square, a_sum, self.N)
        # print(beta_dec)
        beta_bin = chensta_crypto.decToBin(beta_dec)
        while len(beta_bin) < 2 * self.n:
            beta_bin.insert(0,0)

        dot_sum = 0
        for pos in range(2 * self.n):
            dot_sum = dot_sum + (self.r_bin[pos] * beta_bin[pos])
        
        return dot_sum % 2