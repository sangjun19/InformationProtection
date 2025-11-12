from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

# ECB : 블럭 단위로 암호화, 동일한 평문 블럭은 동일한 암호문 블럭으로 암호화
# CBC : 이전 블럭의 암호문을 현재 블럭의 암호화에 사용, 동일한 평문 블럭도 다른 암호문 블럭으로 암호화

plaintext = b"AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCC"
key = b"0123456701234567"

# ECB (사용 권장하지 않음) -> 무결성 보장 안됨(블럭을 재배치 가능)
aes_ctx_ecb = AES.new(key, AES.MODE_ECB)
plaintext = pad(plaintext, 16)
ciphertext = aes_ctx_ecb.encrypt(plaintext)
ciphertext = ciphertext[0:16] + ciphertext[32:48] + ciphertext[16:32]

plaintext_2 = aes_ctx_ecb.decrypt(ciphertext)
print(plaintext_2)

# CBC -> 무결성 보장
iv = b"0000000000000000" # 초기화 벡터(Initial Vector), 이전 블럭이 없는 첫 블럭에 사용, 랜덤하게 생성하여 사용
aes_ctx_cbc = AES.new(key, AES.MODE_CBC, iv=iv)
ciphertext = aes_ctx_cbc.encrypt(plaintext)
ciphertext = ciphertext[0:16] + ciphertext[32:48] + ciphertext[16:32]

plaintext_2 = AES.new(key, AES.MODE_CBC, iv=iv).decrypt(ciphertext)
print(plaintext_2)