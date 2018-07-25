import sys
import itertools

ciphers = [l.strip() for l in sys.stdin]
mincipherlen = min(len(cipher) for cipher in ciphers)
bciphers = [bytes.fromhex(c[0:mincipherlen]) for c in ciphers]
cipherslen = len(bciphers[0])

xored_pairs = {
    c: bytes([b ^ bciphers[c[1]][i] for i, b in enumerate(bciphers[c[0]])])
    for c in itertools.permutations(range(0, len(bciphers)), 2)
}

key = [None for _ in range(cipherslen)]

for pos in range(0, cipherslen):
    counts = [len([j for j in range(0, len(bciphers))
                   if i != j
                   and (
                       (
                            xored_pairs[i, j][pos] >= ord('A')
                            and xored_pairs[i, j][pos] <= ord('Z')
                       ) or (
                           xored_pairs[i, j][pos] >= ord('a')
                           and xored_pairs[i, j][pos] <= ord('z')
                       )
                   )])
              for i, bcipher in enumerate(bciphers)]
    mx = max(counts)
    for i, count in enumerate(counts):
        if count == mx:
            if key[pos] is None:
                key[pos] = set()
            key[pos].add(bciphers[i][pos] ^ ord(' '))

print('key:', key, file=sys.stderr)
for bcipher in bciphers:
    for i, b in enumerate(bcipher):
        if key[i] is None:
            c = '�{}'
        elif len(key[i]) == 1:
            c = chr(b ^ list(key[i])[0])
        else:
            c = '�{{{}}}'.format(','.join([chr(b ^ v) for v in key[i]]))
        sys.stdout.write(c)
    print()
