from hashlib import sha256
def xor(a,b):
    return bytes([i^j for i,j in zip(a,b)])
    
keys = '1010000110011101011100001001100110110010'
keys = sha256(key.encode()).digest()

encrypt_flag = b'3\xeb$b@\x8e\xa0E\xc8H\x08\xc0H3\x054\x0b\xbc\xb95\x81\xeb\xc1R\x97z\xe0qN\xe90N'

print(xor(key, encrypt_flag))