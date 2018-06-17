def permutations(string):
    if not string:
        return ['']
    else:
        perms = permutations(string[:-1])
        curchr = string[-1]
        newperms = []
        for p in perms:
            newperms.append(curchr + p)
            for i in range(1, len(p)):
                newperms.append(p[i-1] + curchr + p[i])
            if p:
                newperms.append(p + curchr)
        #perms.extend(newperms)
        #return perms
        return newperms

def permutations_with_dups(string):
    return permutations(''.join(set(string)))


import unittest
class TestCase(unittest.TestCase):
    def test_permutations(self):
        self.assertEqual(sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']),
            sorted(permutations_with_dups('abc')))


if __name__ == '__main__':
    unittest.main()
