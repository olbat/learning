class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "[({}) L:{} R:{}]".format(self.value, self.left, self.right)

    @classmethod
    def create_bst(cls, sorted_array, istart=0, iend=None):
        if iend is None:
            iend = len(sorted_array) - 1
        if istart > iend:
            return None

        imiddle = (istart + iend) // 2
        node = Node(sorted_array[imiddle])
        node.left = cls.create_bst(sorted_array, istart, imiddle - 1)
        node.right = cls.create_bst(sorted_array, imiddle + 1, iend)

        return node

    def in_order(self, ret=[]):
        if self.left:
            self.left.in_order(ret)
        ret.append(self.value)
        if self.right:
            self.right.in_order(ret)
        return ret

print(Node.create_bst([1,2,3,4,5,6,7,8,9,10]).in_order())
