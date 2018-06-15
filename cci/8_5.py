def simple_mul(a, b):
    ret = 0
    if a < b:
        times = a
        num = b
    else:
        times = b
        num = a
    for _ in range(times):
        ret += num

    return ret

def digit_at(n, lvl):
    pass

def recursive_mul(a, b, lvl=0):
    digit = digit_at(b, lvl)
    ret = simple(a, digit)
    ret += recursive_mul(a, b, lvl + 1)
print(simple_mul(15, 13))
