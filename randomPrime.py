import chensta_crypto
import randomNum

prime_size = 15

test_bin = randomNum.blumBlumShub(prime_size)
test_dec = chensta_crypto.binArrToDec(test_bin)

while not chensta_crypto.millerRabin(test_dec):
    test_bin = randomNum.blumBlumShub(prime_size)
    test_dec = chensta_crypto.binArrToDec(test_bin)

print(test_dec)