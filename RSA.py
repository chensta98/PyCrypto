import chensta_crypto
import secrets

class RSA:
    def __init__(self, n = None, p = None, q = None, e = None):
        if n == None and None not in (p,q):
            self.n = p * q
            self.p = p
            self.q = q
            self.e = e
        elif None not in (p,q) and n != None:
            self.n = n
            self.e = e
        else:
            self.n = n
            self.p = p
            self.q = q
            self.e = e


    def setFactors(self, p, q):
        if n == p * q:
            self.p = p
            self.q = q
            self.tot_n = (p-1) * (q-1)
            self.d = self.getDecryptionKey()
        else:
            print("factors do not equal n")

    def setEncryptionKey(self, e):
        # Gotta check if e is in tot_n
        self.e = e

    def publishKeys(self):
        if e == None:
            return 0, 0
        else:
            return self.n, self.e

    def getDecryptionKey(self):
        _, inv, _ = chensta_crypto.extendedEuclid(self.e, self.tot_n)
        if inv < 0:
            inv = inv + self.tot_n
        
        return inv
    
    def encrypt(self, x):
        return chensta_crypto.fastExpo(x, self.e, self.n)

    def decrypt(self, c):
        return chensta_crypto.fastExpo(c, self.d, self.n)

if __name__ == "__main__":
    
    n = 12091
    e = 3

    bob = RSA(p=107,q=113, e=e)
    bob.setFactors(107,113)

    alice = RSA(n=n, e=e)
    cypherText = alice.encrypt(3981)
    print("Cypher Text: %d" % (cypherText))

    print("Decrypted: %d" % (bob.decrypt(cypherText)))



