import unittest
import chensta_crypto

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



if __name__ == '__main__':
    unittest.main()
