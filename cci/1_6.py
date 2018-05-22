from io import StringIO
def compress_string(string):
    if not string:
        return string

    output = StringIO()
    count = 1
    prevchr = string[0]
    for i in range(1, len(string)):
        if string[i] == prevchr:
            count += 1
        else:
            output.write(prevchr)
            output.write(str(count))
            count = 1
        prevchr = string[i]

    output.write(prevchr)
    output.write(str(count))

    output = output.getvalue()
    if len(output) < len(string):
        return output
    else:
        return string


import unittest
class TestCase(unittest.TestCase):
    def test_compress_string(self):
        # compressed string is smaller: return the compressed string
        self.assertEqual('a2b1c5a3', compress_string('aabcccccaaa'))
        self.assertEqual('c5a1', compress_string('ccccca'))
        self.assertEqual('a1b4', compress_string('abbbb'))

        # compressed string is bigger: return the original string
        self.assertEqual('a', compress_string('a'))
        self.assertEqual('ab', compress_string('ab'))

        # same size: returns the original string
        self.assertEqual('abbb', compress_string('abbb'))


if __name__ == '__main__':
    unittest.main()
