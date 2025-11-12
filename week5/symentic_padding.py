from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

# allingn을 맞추기 위해 padding
# plaintext = b"012345"
# \n = 0xA
# plaintext_padded = b"012345\n\n\n\n\n\n\n\n\n\n" (pkcs#7, default)
# pkcs#7: 빈 공간의 크기만큼 바이트 값을 채움

plaintext = b"0123456789" # 10 bytes
key = b"0123456701234567" # 16 bytes(128 bits)

aes_ctx = AES.new(key, AES.MODE_ECB)
plaintext_padded = pad(plaintext, 16) # block size 16 bytes
print(plaintext_padded)

ciphertext = aes_ctx.encrypt(plaintext_padded)
ciphertext_b64 = b64encode(ciphertext) # base64 인코딩, 깨짐 방지

plaintext = b64decode(ciphertext_b64)
plaintext = aes_ctx.decrypt(plaintext)
plaintext = unpad(plaintext, 16)

print(plaintext)