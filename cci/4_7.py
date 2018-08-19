class Node():
    def __init__(self, value):
        self.value = value
        self.children = []

    def adj(self, node):
        self.children.append(node)

class Graph():
    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)

    def build_order(self):  # FIXME: destructive method
        order = []
        seen = {}
        queue = [n for n in self.nodes if len(n.children) == 0]

        for n in queue:
            seen[n] = True

        # there is no nodes with no outbound nodes: the graph has cycles
        if not queue:
            return None

        while queue:
            node = queue.pop(0)
            order.append(node.value)
            for n in self.nodes:
                if node in n.children:
                    n.children.remove(node)
                if (n not in seen) and (len(n.children) == 0):
                    seen[n] = True
                    queue.append(n)
        return order


import unittest
class TestCase(unittest.TestCase):
    def test_build_order(self):
        g = Graph()
        a = Node('a')
        g.add(a)
        b = Node('b')
        g.add(b)
        c = Node('c')
        g.add(c)
        d = Node('d')
        g.add(d)
        e = Node('e')
        g.add(e)
        f = Node('f')
        g.add(f)

        d.adj(a)
        b.adj(f)
        d.adj(b)
        a.adj(f)
        c.adj(d)

        self.assertEqual(['e', 'f', 'a', 'b', 'd', 'c'], g.build_order())


if __name__ == '__main__':
    unittest.main()
