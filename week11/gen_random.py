import random
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

# Generate pseudo-random bytes with a fixed seed

random.seed(1234)

sequence = random.randbytes(16)
print(sequence)

random.seed(5678)
sequence = random.randbytes(16)
print(sequence)

# Generate cryptographically secure random bytes

bytes = get_random_bytes(16).hex()
print(bytes)

# Derive a key from a password using PBKDF2

password = "cnu is good"
salt = get_random_bytes(16)
KDF = PBKDF2(password, salt, count=610000, hmac_hash_module=SHA256)
print(KDF.hex())