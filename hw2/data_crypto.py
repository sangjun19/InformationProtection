import os
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Util.Padding import pad, unpad

hmac_key = b'12345678123456781234567812345678'
aes_key = b'12345678123456781234567812345678'

def encrypt():
    
    iv = b'1234567812345678'
    
    h = HMAC.new(key=hmac_key, digestmod=SHA256)

    try:
        with open("Origin_Data.txt", "rb") as f:
            file_data = f.read()
            
        h.update(file_data)
        hmac_digest = h.digest()
        
        # print("HMAC Digest:", hmac_digest.hex())
        
        total_data = file_data + hmac_digest
        padded_data = pad(total_data, AES.block_size)
        
        aes = AES.new(aes_key, AES.MODE_CBC, iv=iv)
        ciphertext = aes.encrypt(padded_data)
        
        final_encrypt_data = iv + ciphertext
        # print("Final Encrypted Data:", final_encrypt_data)
        
        with open("Origin_Data.enc", "wb") as f:
            f.write(final_encrypt_data)

    except FileNotFoundError:
        print("파일이 존재하지 않음.")
        return
        
def decrypt():
    try:
        with open("Origin_Data.enc", "rb") as f:
            encrypted_data = f.read()            
            
            iv = encrypted_data[:16]
            ciphertext = encrypted_data[16:]
            
            aes = AES.new(aes_key, AES.MODE_CBC, iv=iv)
            padded_data = aes.decrypt(ciphertext)
            total_data = unpad(padded_data, AES.block_size)
            
            original_data = total_data[:-32]
            hmac = total_data[-32:]
            
            h = HMAC.new(key=hmac_key, digestmod=SHA256)
            h.update(original_data)
            
            if hmac == h.digest():
                print("원본 데이터:", original_data.decode())        
                print("데이터 무결성 검증 성공.") 
            else:
                print("데이터 무결성 검증 실패.")                
    
    except FileNotFoundError:
        print("암호화된 파일이 존재하지 않음.")
        return
    
if __name__ == "__main__":
    encrypt()
    decrypt()