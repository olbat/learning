class EmptyShelterError(Exception):
    pass

class NoAnimalError(Exception):
    pass

class Node():
    def __init__(self, name=None):
        self.name = name
        self.next = None
        self.prev = None

class CatNode(Node):
    pass

class DogNode(Node):
    pass

class AnimalShelter():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        ptr = self.head
        while ptr and ptr.next:
            yield ptr
            ptr = ptr.next
        if ptr:
            yield ptr

    def enqueue(self, node):
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.tail = self.head = node

    def dequeue(self):
        if not self.head:
            raise EmptyShelterError()

        ret = self.head
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = self.tail = None
        return ret

    def dequeue_animal(self, klass=CatNode):
        if not self.head:
            raise EmptyShelterError()

        ptr = iter(self)
        try:
            ret = next(ptr)
            while ret.__class__ != klass:
                ret = next(ptr)
            if ret.prev:
                ret.prev.next = ret.next
            if ret.next:
                ret.next.prev = ret.prev
            return ret
        except StopIteration:
            raise NoAnimalError()

    def dequeue_cat(self):
        return self.dequeue_animal(CatNode)

    def dequeue_dog(self):
        return self.dequeue_animal(DogNode)


import unittest
class TestCase(unittest.TestCase):
    def test_dequeue(self):
        a = AnimalShelter()
        a.enqueue(DogNode())
        a.enqueue(DogNode())
        a.enqueue(CatNode())
        self.assertIsInstance(a.dequeue(), DogNode)

    def test_dequeue_cat(self):
        a = AnimalShelter()
        a.enqueue(DogNode())
        a.enqueue(DogNode())
        a.enqueue(CatNode())
        self.assertIsInstance(a.dequeue_cat(), CatNode)

    def test_dequeue_dog(self):
        a = AnimalShelter()
        a.enqueue(CatNode())
        a.enqueue(DogNode())
        a.enqueue(DogNode())
        self.assertIsInstance(a.dequeue_dog(), DogNode)


if __name__ == '__main__':
    unittest.main()
