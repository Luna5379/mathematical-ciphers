def egcd(a, b):
    x,y,u,v = 0,1,1,0
    while a!= 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a,x,y,u,v = a,r,u,v,m,n
    gcd = b
    return gcd, x, y
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m
def encrypt(text, key):
    return ''.join([ chr((( key[0]*(ord(i)-ord('A')) + key[1]) %26) + ord('A')) for i in text.upper().replace(' ', '') ])

def decrypt(cipher, key):
    return ''.join( [ chr((( modinv(key[0], 26)*(ord(j)-ord('A') - key[1])) %26) + ord('A')) for j in cipher ])

plaintext = "FIRST EVER AFFINE CIPHER"
key = [5, 25]

ciphertext = encrypt(plaintext, key)
print(ciphertext)

print(decrypt(ciphertext, key))
