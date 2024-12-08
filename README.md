# Chensta Crypto Package
Programming excercises for BU Cryptography

## Files
<pre>
example.py:         Example functions implemented  
chensta_crypto.py:  Implementation of functions used in Cryptographic exchanges
ElGamal.py:         Implementation of ElGamal Library
RSA.py:             Implementation of RSA Library
randomNum.py:       Implementation of Naor Rein and Blum-Blum-Shub PSNG
unit_test.py:       Unit testing functions
randomPrime.py:     returns a random prime of a given size
Resources:          Picutres of running code
</pre>

## Running El Gamal
This file was intended for use as a library, however, it can be run using the Python IDLE

### As Alice:

![Alice CLI](/Resources/AliceElGamalCLI.png)

1. Start by running `python3 .\randomPrime.py` this will generate a random prime
2. import the library. If you are using a file `import ElGamal` otherwise if using IDLE `from ElGamal import *`
3. Init alice as an object with the prime `alice = Alice(prime)`
4. alice calculates the base in `alice.b`
5. alice then shares her b and her shared key `alice.b_r`
6. alice then gets bobs.b_l and uses `alice.setKey(key)` to calculate her secret key
7. alice can then encrypt anything in the group with `alice.encrypt(plainText)`

Here is an Example of an exchange:

![Alice Test](/Resources/AliceElGamal.png)

### As Bob:

![Bob CLI](/Resources/BobElGamalCLI.png)
![Bob Test](/Resources/BobElGamal.png)

### Cracking El Gamal
We need to use Baby-Step Giant-Step to crack the secret keys

#### Example:

![EveCLI](/Resources/EveElGamalCLI.png)
![EveTest](/Resources/EveElGamal.png)

1. Import the `chensta_crypto` library using `from chensta_crypto import *`
2. Using `babyStepGiantStep` to crack Alices secret value or Bobs
3. Calculate the shared secret using `extendedEuclid(sharedSecret, prime)`
4. Calculate the inverse of the shared secret to get decryption key (if negative make positive in group)
5. Decrypt by multiplying decryption key by cypherText mod prime

## Running RSA
This was also intended to be used a library

### As Alice

![Alice Test](/Resources/AliceRSA.png)

1. Ask for Bobs public key
2. Initialize a bob object `bob = RSA(n=publicKey, e=encryptionKey)`
3. Encrypt a private message `bob.encrypt(plainText)`

![Alice CLI](/Resources/AliceRSACLI.png)

### As Bob

![Bob Test](/Resources/BobRSA.png)

1. generate 2 primes by running `python3 .\randomPrime.py`
2. calc m by multiplying n = p * q
3. initialize Bob with `bob = RSA(n=publicKey, e=encryptionKey)`
4. Set the factors with `bob.setFactors(p, q)`
5. Decrypt messages that are sent `bob.decrypt(cypherText)`

![Bob CLI](/Resources/BobRSACLI.png)

### Cracking RSA
We need to factor the public key and use that to calculate the decryption key

![Eve Test](/Resources/EveRSA.png)

1. Use PollardRho to crack the encryption key `pollardRho(n)`
2. Calculate the totient(n) with p-1 * q-1
3. Get the decryption key by calculating the inverse with extended euclid
4. Use fastExpo to decrypt the message with the decryption key.

![Eve CLI](/Resources/EveRSACLI.png)

## Testing
To run unit test run the following command `python3 .\unit_test.py`