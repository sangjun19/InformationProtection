from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import PKCS1_OAEP, AES

# 공개키의 주인이 누구인지 모름 -> 중간자 공격(Man-In-The-Middle, MITM)

# A
key = b"it's secret01234" # 세션키
iv = b"0000000000000000"
plaintext = b"this must be protected!!!"

aes_ctx = AES.new(key, AES.MODE_CBC, iv=iv)

# B
# 자신의 공개키 생성 후 A에게 전달
rsa_key = RSA.generate(2048)
rsa_ctx = PKCS1_OAEP.new(rsa_key)
public_key = rsa_key.public_key().export_key()

# A
print("Publick Key:")
print(public_key)

public_key_b = RSA.import_key(public_key)
rsa_ctx_a = PKCS1_OAEP.new(public_key_b)

encrypted_secret = rsa_ctx_a.encrypt(key)
print(encrypted_secret)

# B 
decrypted_secret = rsa_ctx.decrypt(encrypted_secret)
print(decrypted_secret)

# A
plaintext_padded = pad(plaintext, 16)
encrypted_message = aes_ctx.encrypt(plaintext_padded)


# B
aes_ctx_b = AES.new(decrypted_secret, AES.MODE_CBC, iv=iv)
decrypted_message = aes_ctx_b.decrypt(encrypted_message)
decrypted_message = unpad(decrypted_message, 16)

print(decrypted_message)