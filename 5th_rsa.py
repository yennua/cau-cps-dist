import random

p = 11
q = 13

n = p*q
phi_n = (p-1)*(q-1)

# e = 7
while True:
    temp = random.randint(2, n-1)
    if temp % p != 0 and temp % q != 0:
        e = temp
        break

d = 0
mod = 0

while True:
    d += 1
    mod = (e*d) % phi_n
    if mod == 1:
        break

# Encryption
# C = P^e mod n

plain = "CAU CPS DIST"
plain_list = [ord(x) for x in plain]

cipher = []
for i in plain_list:
    x = (i**e) % n
    cipher.append(int(x))

# Decryption
# P = C^d mod n

decryted = []
for i in cipher:
    x = (i**d) % n
    decryted.append(int(x))

print('plain text', plain_list)
print('cipher text', cipher)
print('decryted text', decryted)

print([chr(x) for x in decryted])
decryted_text = ''.join([chr(x) for x in decryted])
print(decryted_text)
