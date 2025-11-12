from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 암호화키와 복호화키가 다른 비대칭키 암호화
# 공개키로 암호화, 개인키로 복호화

key = RSA.generate(2048)
pubkey_export = key.public_key().export_key()

# print(pubkey_export)

prikey_export = key.export_key()

# print(prikey_export)

plaintext = b"Let's have a lunch"
rsa_ctx = PKCS1_OAEP.new(key)
ciphertext = rsa_ctx.encrypt(plaintext)

print(ciphertext)