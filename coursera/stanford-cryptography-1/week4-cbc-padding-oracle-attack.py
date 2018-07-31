import sys
import math
import time
import string
import urllib.request
import urllib.error

AES_BLOCK_SIZE = 16
BASEURL = 'http://crypto-class.appspot.com/po?er='
# the characters that can be used in a message
PRINTABLE_CHARACTERS = [ord(c) for c in string.printable]

if len(sys.argv) > 1:
    cipher = sys.argv[1].strip()
else:
    cipher = ('f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd'
              '4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4')

cipher = bytes.fromhex(cipher)
nblocks = math.ceil(len(cipher) / AES_BLOCK_SIZE) + 1
message = ''

# start from the second block since the first block is the IV
for iblk in range(1, nblocks-1):
    # here we will modify the prevblock to use padding info from the current one
    startblocks = cipher[:(iblk-1) * AES_BLOCK_SIZE]
    prevblock = cipher[(iblk-1) * AES_BLOCK_SIZE:iblk * AES_BLOCK_SIZE]
    curblock = cipher[iblk * AES_BLOCK_SIZE:(iblk+1) * AES_BLOCK_SIZE]

    if len(curblock) != AES_BLOCK_SIZE:
        raise ValueError('invalid block size')

    lastblock = (iblk == (nblocks-2))
    mblk = []
    pad = None

    # iterate on every possible pads for the block
    for padsize in range(1, AES_BLOCK_SIZE + 1):
        poschars = PRINTABLE_CHARACTERS  # the list of "guessable" characters
        if lastblock:
            if padsize == 1:  # first byte of the last block: guess the pad
                # add valid padding bytes to the list of "guessable" characters
                poschars = list(range(1, 17)) + poschars
            elif padsize <= pad:  # following bytes: skip padding bytes
                mblk.insert(0, pad)
                continue

        # iterate over possible values for the character at this position
        for c in poschars:
            cval = chr(c) if c in PRINTABLE_CHARACTERS else hex(c)
            sys.stderr.write("\rb#{}:p#{} trying '{}'"
                             .format(iblk, padsize, cval))

            pblk = [b for b in prevblock]  # dup. and convert list of bytes

            for i in range(-padsize, 0):
                # XOR the prev block and the pad value
                pblk[i] ^= padsize
                if i == -padsize:  # try the c character
                    pblk[i] ^= c
                else:  # use the value we guessed for previous characters
                    pblk[i] ^= mblk[padsize + i - 1]

                curcipher = startblocks + bytes(pblk) + curblock

            try:
                time.sleep(0.1)  # avoid DoSing the service
                url = ''.join([BASEURL, curcipher.hex()])
                urllib.request.urlopen(url)
                # continue iterating on success
            except urllib.error.HTTPError as err:
                # invalid pad => bad value for c
                if err.code == 403:
                    pass
                # invalid message => pad is OK => c value is OK
                elif err.code == 404:
                    print("\rb#{}:p#{} found: '{}'"
                          .format(iblk, padsize, cval), file=sys.stderr)
                    mblk.insert(0, c)
                    break

        # last byte of last block: save the padding value
        if lastblock and (padsize == 1):
            pad = c

        # the previous character was not found
        if len(mblk) != padsize:
            raise ValueError('cannot guess the character #{} of block #{}'
                             .format(AES_BLOCK_SIZE - padsize, iblk))

    # remove the padding bytes from the message
    if lastblock:
        mblk = mblk[0:-mblk[-1]]
    message += ''.join(chr(c) for c in mblk)
    print('curmsg: "{}"'.format(message), file=sys.stderr)

print(message)
