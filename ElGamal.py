import chensta_crypto
import secrets

class Alice:
    def __init__(self, G):
        self.G = G
        self.b = chensta_crypto.primRootSearch(G)
        self.r = secrets.randbelow(G)
        self.b_r = chensta_crypto.fastExpo(self.b, self.r, G)

    def pubKey(self):
        return self.b, self.b_r

    def setKey(self, b_l):
        self.b_rl = chensta_crypto.fastExpo(b_l, self.r,self.G)

    def encrypt(self, x):
        return (x * self.b_rl) % self.G

class Bob:
    def __init__(self, G, b):
        self.G = G
        self.b = b
        self.l = secrets.randbelow(G)
        self.b_l = chensta_crypto.fastExpo(self.b, self.l, G)

    def pubKey(self):
        return self.b, self.b_l

    def setKey(self, b_r):
        self.b_lr = chensta_crypto.fastExpo(b_r, self.l, self.G)

    def decrypt(self, x):
        _, inv, _ = chensta_crypto.extendedEuclid(self.b_lr, self.G)
        if inv < 0:
            inv = inv + self.G

        return (x * inv) % self.G


if __name__ == "__main__":
    print("El Gamal")

    G = 101
    x = 50
    
    alice = Alice(G)
    b = alice.b
    bob = Bob(G, b)

    print("Alice:   B:  %2d, R:  %2d, B_R:    %2d" % (alice.b, alice.r, alice.b_r))
    print("Bob:     B:  %2d, L:  %2d, B_L:    %2d" % (bob.b, bob.l, bob.b_l))

    alice.setKey(bob.b_l)
    bob.setKey(alice.b_r)
    print("B_RL and B_LR:   %d, %d" % (alice.b_rl, bob.b_lr))
    
    
    m = 50
    x = alice.encrypt(x)
    print("Message: %d" % (m))
    print("Encrypted Message:   %d" % (x))
    print("Decrypted Message:   %d" % (bob.decrypt(x)))



