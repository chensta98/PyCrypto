import chensta_crypto
import randomNum

def randomPrimeBits(prime_size):
    test_bin = randomNum.blumBlumShub(prime_size)
    test_dec = chensta_crypto.binArrToDec(test_bin)

    while not chensta_crypto.millerRabin(test_dec) or test_dec < 2:
        test_bin = randomNum.blumBlumShub(prime_size)
        test_dec = chensta_crypto.binArrToDec(test_bin)

    return test_dec

def randomPrimeRange(prime_range):
    length_bin = len(chensta_crypto.decToBin(prime_range))
    return randomPrimeBits(length_bin)

    

if __name__ == "__main__":
    print(randomPrimeRange(32767))