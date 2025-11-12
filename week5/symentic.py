from Crypto.Cipher import AES
from base64 import b64encode, b64decode

# AES
# Block size : 128 bits, 16 bytes(고정)
# Key size : 128 bits(AES-128), 256 bits(AES-256) 
# key 길이는 암호의 강도를 결정

plaintext = b"abcdefgh01234567"
key = b"1234567812345678"

aes_ctx = AES.new(key, AES.MODE_ECB)
ciphertext = aes_ctx.encrypt(plaintext)

print(ciphertext)

# Base64 인코딩, 깨짐 방지
ciphertext_b64 = b64encode(ciphertext)
print(ciphertext_b64)

ciphertext = b64decode(ciphertext_b64)

plaintext = aes_ctx.decrypt(ciphertext)
print(plaintext)