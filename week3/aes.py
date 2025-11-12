from Crypto.Cipher import AES

def aes_encrypt(plaintext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(plaintext)

def aes_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

key = b'aaaaaaaaaaaaaaaa'
plaintext = b'ABCDEFGHABCDEFGH'

encrypted = aes_encrypt(plaintext, key)
print("Encrypted (hex): ", encrypted.hex())

decrypted = aes_decrypt(encrypted, key)
print("Decrypted: ", decrypted)