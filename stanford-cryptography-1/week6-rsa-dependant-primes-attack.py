import gmpy2


# find out the prime factors p and q of N
def factor(N, A_min_sqrt_N_lt):
    sqrt_N, r = gmpy2.isqrt_rem(N)
    if r:  # if the remainder is != 0, the sqrt is not a round number: round it
        sqrt_N += 1

    p = q = None
    # try possible values for A from √N to the bigger value of (A - √N)
    for A in range(sqrt_N, sqrt_N + A_min_sqrt_N_lt):
        x = gmpy2.isqrt(pow(A, 2) - N)
        p = A - x
        q = A + x
        if gmpy2.mul(p, q) == N:  # we found a valid value for A
            return p, q

    raise ValueError('Cannot factor p and q from modulus')


# decrypts a PKCS#1 v1.5 ciphertext by factoring the prime factors of N
def decrypt(ciphertext, N, A_min_sqrt_N_lt, e=65537):
    # factor p and q
    p, q = factor(N, A_min_sqrt_N_lt)

    # find out RSA private exponent from p and q knowing that e.d = 1 mod(ϕ(N))
    phiN = N - p - q + 1
    d = gmpy2.invert(e, phiN)

    # decipher the ciphertext
    text = gmpy2.powmod(ciphertext, d, N)

    # convert the number to it's hexadecimal notation
    hextext = hex(text)

    # find the indice of the '0x00' separator
    endpadi = hextext.find('00', 2)

    # remove the pad from the message and return the text
    return bytes.fromhex(hextext[endpadi + 2:])


if __name__ == '__main__':
    import sys

    # default values
    N = int(
        ('17976931348623159077293051907890247336179769789423065727343008115'
         '77326758055056206869853794492129829595855013875371640157101398586'
         '47833778606925583497541085196591615128057575940752635007475935288'
         '71082364994994077189561705436114947486504671101510156394068052754'
         '0071584560878577663743040086340742855278549092581'), 10)
    A_min_sqrt_N_lt = 1
    ciphertext = int(
        ('22096451867410381776306561134883418017410069787892831071731839143'
         '67613560012053800428232965047350942434394621975151225646583996794'
         '28894607645420405815647489880137348641204523252293201764879166664'
         '02997509188729971690526083222067771600019329260870009579993724077'
         '458967773697817571267229951148662959627934791540'), 10)
    e = 65537

    if len(sys.argv) <= 1:
        print('usage: {} <factor|decrypt> <N> <(A-√N) max> [<ciphertext>]'
              .format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    mode = sys.argv[1].strip().lower()

    if mode == 'factor':
        if len(sys.argv) > 3:
            N = int(sys.argv[2].strip(), 10)
            A_min_sqrt_N_lt = int(sys.argv[3].strip(), 10)

        p, q = factor(N, A_min_sqrt_N_lt)
        if p and q:
            print('p={}\nq={}'.format(p, q), file=sys.stderr)
            print(min(p, q))

    elif mode == 'decrypt':
        if len(sys.argv) > 4:
            N = int(sys.argv[2].strip(), 10)
            A_min_sqrt_N_lt = int(sys.argv[3].strip(), 10)
            ciphertext = int(sys.argv[4].strip(), 10)

        sys.stdout.buffer.write(decrypt(ciphertext, N, A_min_sqrt_N_lt, e))

    else:
        sys.exit(1)
