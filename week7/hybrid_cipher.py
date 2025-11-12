from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import PKCS1_OAEP, AES

# 대칭키의 빠름 + 비대칭키의 안전함 = 하이브리드 암호화
# 공개키는 비밀키를 암호화하는데 사용
# 비밀키는 실제 메시지를 암호화하는데 사용

# A
key = b"it's secret01234"
iv = b"0000000000000000"
plaintext = b"this must be protected!!!"

aes_ctx = AES.new(key, AES.MODE_CBC, iv=iv)

# B
# 자신의 공개키 생성 후 A에게 전달
rsa_key = RSA.generate(2048)
rsa_ctx = PKCS1_OAEP.new(rsa_key)
public_key = rsa_key.public_key().export_key()

# A
# B의 공개키로 비밀키 암호화
print("Publick Key:")
print(public_key)

public_key_b = RSA.import_key(public_key)
rsa_ctx_a = PKCS1_OAEP.new(public_key_b)

encrypted_secret = rsa_ctx_a.encrypt(key)
print(encrypted_secret)

# B 
# 자신의 개인키로 비밀키 복호화
decrypted_secret = rsa_ctx.decrypt(encrypted_secret)
print(decrypted_secret)

# A
# 공유한 비밀키로 메시지 암호화
plaintext_padded = pad(plaintext, 16)
encrypted_message = aes_ctx.encrypt(plaintext_padded)


# B
# 메시지 복호화
aes_ctx_b = AES.new(decrypted_secret, AES.MODE_CBC, iv=iv)
decrypted_message = aes_ctx_b.decrypt(encrypted_message)
decrypted_message = unpad(decrypted_message, 16)

print(decrypted_message)