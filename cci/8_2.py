class Coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.__class__ == other.__class__
                and self.x == other.x and self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return "({},{})".format(self.x, self.y)

    def move(self, m):
        return Coord(self.x + m.x, self.y + m.y)


class Grid():
    MOVES = {
        'r': Coord(1, 0),
        'd': Coord(0, 1),
    }
    def __init__(self, c, r, offlimits_tiles=[]):
        self.bottomright = Coord(c-1, r-1)
        # array of columns
        self.grid = [[False for _ in range(r)] for _ in range(c)]
        for c in offlimits_tiles:
            self.grid[c.x][c.y] = True

    def contains(self, c):
        return c.x < len(self.grid) and c.y < len(self.grid[0])

    def offlimit(self, c):
        return (not self.contains(c)) or self.grid[c.x][c.y]

    def path_to_end(self, curcoord=Coord(0,0), cache={}):
        if self.offlimit(curcoord):
            return None
        elif curcoord == self.bottomright:
            return []
        else:
            for name, m in self.MOVES.items():
                mc = curcoord.move(m)
                if mc not in cache:
                    cache[mc] = self.path_to_end(mc, cache)
                if cache[mc] is not None:
                    return [name] + cache[mc]
            return None


import unittest
class TestCase(unittest.TestCase):
    def test_path_to_end(self):
        # |...|
        # |.xx|
        # |...|
        # |xx.|
        g = Grid(3, 4, [Coord(1,1), Coord(2,1), Coord(0,3), Coord(1,3)])
        self.assertEqual(['d','d','r','r','d'], g.path_to_end())


if __name__ == '__main__':
    unittest.main()
