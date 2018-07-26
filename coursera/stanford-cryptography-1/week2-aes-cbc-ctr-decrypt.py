import sys
from io import BytesIO
from Crypto.Cipher import AES

if len(sys.argv) < 3:
    print('usage: <CBC|CTR> <key> <ciphertext>', file=sys.stderr)
    sys.exit(1)

mode = sys.argv[1].lower()
key = bytes.fromhex(sys.argv[2])
ciphertext = BytesIO()
ciphertext.write(bytes.fromhex(sys.argv[3]))
ciphertext.seek(0)

iv = None
m = b""
cipher = AES.new(key, AES.MODE_ECB)

for c in iter(lambda: ciphertext.read(16), b""):
    if iv is None:
        if mode == 'cbc':
            iv = c
        elif mode == 'ctr':
            iv = int.from_bytes(c, byteorder='big')
        continue

    if mode == 'cbc':
        m += bytes(iv[i] ^ b for i, b in enumerate(cipher.decrypt(c)))
        iv = c
    elif mode == 'ctr':
        kiv = cipher.encrypt(iv.to_bytes(16, byteorder='big'))
        m += bytes(kiv[i] ^ b for i, b in enumerate(c))
        iv += 1

if mode == 'cbc':
    m = m[0:-m[-1]]  # PKCS#5 padding

print(m)
