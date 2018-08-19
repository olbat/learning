import itertools

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bst_array_recurse(root, lvl, ret):
    if len(ret) < lvl + 1:
        ret.append([])

    ret[lvl].append(root.value)
    if root.left:
        bst_array_recurse(root.left, lvl + 1, ret)
    if root.right:
        bst_array_recurse(root.right, lvl + 1, ret)

def bst_array(tree):
    comb = []
    bst_array_recurse(tree, 0, comb)
    return [v for v in itertools.combinations(comb, len(comb))]


root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)

print(bst_array(root))
