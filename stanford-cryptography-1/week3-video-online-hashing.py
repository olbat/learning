import os
import sys
from Crypto.Hash import SHA256

BLOCK_SIZE = 1024

if len(sys.argv) < 2:
    print("usage: {} [hash <file>|verify <hash> < file]".format(sys.argv[0]),
          file=sys.stderr)
    sys.exit(1)

mode = sys.argv[1].lower()

if mode == 'hash':
    with open(sys.argv[2], 'rb') as f:
        # read the file from the end to the begining
        f.seek(0, os.SEEK_END)
        size = f.tell()

        # size of the last block
        pos = f.tell() % BLOCK_SIZE
        h = None

        while pos <= size:
            f.seek(-pos, os.SEEK_END)
            block = f.read(BLOCK_SIZE)
            h = SHA256.new(data=b"".join([block, (h.digest() if h else b"")]))
            pos += BLOCK_SIZE

        print(h.hexdigest())

elif mode == 'verify':
    verh = bytes.fromhex(sys.argv[2])
    # read a block and it's hash
    while True:
        block = sys.stdin.buffer.read(BLOCK_SIZE + 32)
        if len(block) < (BLOCK_SIZE + 32):  # last block
            break

        calch = SHA256.new(data=block).digest()

        if calch != verh:  # FIXME: timing attacks
            print('Error: hash does not match !', file=sys.stderr)
            sys.exit(1)

        verh = block[-32:]

    print('OK!')
