import sys
import gmpy2

XMAX = 2**40
B = gmpy2.isqrt(XMAX)

if len(sys.argv) > 3:
    p = int(sys.argv[1].strip(), 10)
    g = int(sys.argv[2].strip(), 10)
    h = int(sys.argv[3].strip(), 10)
else:
    p = int(('134078079299425970995740249982058461274793658205923933'
             '77723561443721764030073546976801874298166903427690031'
             '858186486050853753882811946569946433649006084171'), 10)
    g = int(('11717829880366207009516117596335367088558084999998952205'
             '59997945906392949973658374667057217647146031292859482967'
             '5428279466566527115212748467589894601965568'), 10)
    h = int(('323947510405045044356526437872806578864909752095244'
             '952783479245297198197614329255807385693795855318053'
             '2878928001494706097394108577585732452307673444020333'), 10)

# compute all possible values for h/g^x1 with x1∈[0..2^20]
msg = 'compute the table containing h/g^x1 values …'
h_div_g_pow_x1_values = {}
for x1 in range(B + 1):
    inv_g_pow_x1 = gmpy2.invert(gmpy2.powmod(g, x1, p), p)
    h_div_g_pow_x1 = gmpy2.f_mod(gmpy2.mul(h, inv_g_pow_x1), p)
    h_div_g_pow_x1_values[h_div_g_pow_x1] = x1

    if (x1 % 1000) == 0:  # debug display
        sys.stderr.write("\r{} {}".format(msg, x1))
sys.stderr.write('\n')

g_pow_B = gmpy2.powmod(g, B, p)

# look for values of (g^B)^x0 in the precomputed table
msg = 'looking for values of (g^B)^x0 in the table …'
for x0 in range(B + 1):
    g_pow_B_pow_x0 = gmpy2.powmod(g_pow_B, x0, p)
    if g_pow_B_pow_x0 in h_div_g_pow_x1_values:
        # match found: solve the equation
        x1 = h_div_g_pow_x1_values[g_pow_B_pow_x0]
        x = x0 * B + x1
        print("\n{}".format(x))
        break

    if (x0 % 1000) == 0:  # debug display
        sys.stderr.write("\r{} {}".format(msg, x0))
