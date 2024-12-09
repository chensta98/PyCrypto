import unittest
import chensta_crypto
import ElGamal
import randomPrime
import RSA

class TestChenstaCrypto(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(chensta_crypto.gcd(24,36), 12)

    def test_extendedEuclid(self):
        self.assertEqual(chensta_crypto.extendedEuclid(121, 28), (1, -3, 13))

    def test_fastExpo(self):
        self.assertEqual(chensta_crypto.fastExpo(3, 128, 7), 2)

    def test_baby(self):
        self.assertEqual(chensta_crypto.babyStepGiantStep(16, 9, 13), 2)
    
    def test_millerRabin(self):
        self.assertFalse(chensta_crypto.millerRabin(221))
        self.assertEqual(chensta_crypto.millerRabin(2351), True)
    
    def test_PollardRho(self):
        self.assertIn(chensta_crypto.pollardRho(12674147), (11617, 1091))

class TestElGamal(unittest.TestCase):
    
    def test_encryption(self):
        G = randomPrime.randomPrimeBits(30)
        
        alice = ElGamal.Alice(G)
        b = alice.b
        bob = ElGamal.Bob(G, b)

        alice.setKey(bob.b_l)
        bob.setKey(alice.b_r)

        m = 50
        cypherText = alice.encrypt(m)

        self.assertEqual(bob.decrypt(cypherText), 50)

class TestRSA(unittest.TestCase):

    def test_encryption(self):
        p1 = randomPrime.randomPrimeBits(15)
        q1 = randomPrime.randomPrimeBits(15)
        n = p1 * q1
        e = 65537

        bob = RSA.RSA(p=p1,q=q1, e=e)
        bob.setFactors(p1,q1)

        alice = RSA.RSA(n=n, e=e)
        cypherText = alice.encrypt(3981)
        self.assertEqual(bob.decrypt(cypherText), 3981)


if __name__ == '__main__':
    unittest.main()
