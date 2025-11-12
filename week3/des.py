from Crypto.Cipher import DES

def des_encrypt(plaintext: bytes, key: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(plaintext)

def des_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(ciphertext)

key = b'8bytekey'
plaintext = b'ABCDEFGH'

# Encrypt
encrypted = des_encrypt(plaintext, key)
print("Encryped (hex): ", encrypted.hex())

# Decrypt
decrypted = des_decrypt(encrypted, key)
print("Decrypted: ", decrypted)