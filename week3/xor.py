def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

plain_text = b"hello"
key = b"12345"

print(xor_encrypt_decrypt(plain_text, key))