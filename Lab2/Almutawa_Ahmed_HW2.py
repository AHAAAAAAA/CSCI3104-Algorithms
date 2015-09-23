import sys
import random
from fractions import gcd
import time

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Found function online to avoid importing alternative libraries
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# Function found online to avoid importing libraries
# Inspired by: https://stackoverflow.com/questions/567222/simple-prime-generator-in-python/568618#568618
def genprimes(start, end):
    if start >= end:
        return []

    primes = [2]

    for n in range(3, end + 1, 2):
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)

    while primes and primes[0] < start:
        del primes[0]

    return primes

# Inspiration: Textbook and https://inventwithpython.com/hacking/chapter24.html
def generateKeys(keySize):
	# Make primes and compute n
	primes = genprimes(0, keySize)
	p      = random.choice(primes)
	q      = random.choice(primes)
	n      = p * q
	
	# Find relatively prime e
	while True:
	    # Keep trying random numbers for e until one is valid.
	    e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
	    if gcd(e, (p - 1) * (q - 1)) == 1:
	        break
	d = modinv(e, (p - 1) * (q - 1))
	
	publicKey = (n, e)
	privateKey = (n, d)
	
	return (publicKey, privateKey)


def encrypt(x, n, e):
    return pow(x, e, n)

def decrypt(x, n, d):
    return pow(x, d, n)

def test (n):
	print 'Testing for ', n,':'

	start_time = time.time()
	public, private = generateKeys(n)
	end_time = time.time()
	print 'Key Generation took ', end_time-start_time, 'seconds'

	start_time = time.time()
	x = encrypt(2015, public[0], public[1])
	end_time = time.time()
	print 'Encryption took ', end_time-start_time, 'seconds'

	start_time = time.time()
	y = decrypt(x, private[0], private[1])
	end_time = time.time()
	print 'Decryption took ', end_time-start_time, 'seconds'

	print '****'

# main function
def main(argv):
	test(1024)
	test(4096)
	test(8192)
	
# main entry point
if __name__ == "__main__":
	main(sys.argv)