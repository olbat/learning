class Node():
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def linkto(self, node):
        self.children.append(node)

    def path_exists(self, node, nodes=None, visited={}):
        if not nodes:
            nodes = self.children

        for n in nodes:
            if n == node:
                return True
            elif n not in visited:
                visited[n] = True
                if self.path_exists(node, n.children, visited):
                    return True
        return False


import unittest
class TestCase(unittest.TestCase):
    def test_pathexists(self):
        n = Node()
        m = Node()
        o = Node()
        n.linkto(m)
        m.linkto(o)
        self.assertTrue(n.path_exists(o))
        self.assertFalse(o.path_exists(n))
        o.linkto(n)
        self.assertTrue(o.path_exists(n))


if __name__ == '__main__':
    unittest.main()
