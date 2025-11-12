from Crypto.Hash import HMAC, SHA256

msg1 = b"HELLO CSE!"
msg2 = b"HELLO CSE?"

hash_ctx1 = SHA256.new(msg1)
hash1 = hash_ctx1.hexdigest()

hash_ctx2 = SHA256.new(msg2)
hash2 = hash_ctx2.hexdigest()

print("HASH 1:", hash1)
print("HASH 2:", hash2)

# HMAC

msg1 = b"HELLO CSE!"
hmac_key = b"this is password for hmac"

hmac_ctx = HMAC.new(hmac_key, msg1, digestmod=SHA256)
orig_hmac = hmac_ctx.hexdigest()

print("HMAC:", orig_hmac)