import chensta_crypto
import randomNum

test_bin = randomNum.blumBlumShub(15)
test_dec = chensta_crypto.binArrToDec(test_bin)

while not chensta_crypto.millerRabin(test_dec):
    test_bin = randomNum.blumBlumShub(15)
    test_dec = chensta_crypto.binArrToDec(test_bin)

print(test_dec)