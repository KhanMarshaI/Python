# RSA Algorithm
def RSA(message):
    p = 19
    q = 13
    n = p*q
    phi= (p-1) * (q-1)
    #print(n,phi)
    e = 7 # https://www.numere-prime.ro/coprime-numbers-prime-to-each-other-relatively-prime.php
    d = 31 # https://planetcalc.com/3298/

    # m = 11  #message

    # encrypt
    enc = (message**e)%n
    print(f'encrypted: {enc}')
    # decrypt
    dec = (enc ** d) % n
    print(f'decrypted: {dec}')

string = "taha khan"

def trans(text):
    res = ""
    i = 0
    while i < len(text):
        res += text[i + 1] + text[i]
        i += 2
    return res

print('Transposition Cipher:')
enc = trans(string.replace(" ", ""))
print(f'encrypted: {enc}')

dec = trans(enc)
print(f'decrypted: {dec}')
print('\nRSA Algorithm')
RSA(14)