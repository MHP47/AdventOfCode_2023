from utils import *


class Hailstone:
    def __init__(self, px, py, pz, vx, vy, vz):
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self._px = px + vx
        self._py = py + vy
        self._pz = pz + vz
        self.m = (self.py - self._py) / (self.px - self._px)
        self.dx = 1 if self._px > self.px else -1
        self.dy = 1 if self._py > self.py else -1
    def __repr__(self):
        return str(self.__dict__)
    def __str__(self):
        return f"{self.px}, {self.py}, {self.pz} @ {self.vx}, {self.vy}, {self.vz}"


def part_1(p_Input):
    window_min = 200_000_000_000_000
    window_max = 400_000_000_000_000
    hailstones = [Hailstone(*parse_ints(x)) for x in p_Input.strip().splitlines()]
    total = 0
    for a,b in itertools.combinations(hailstones, 2):
        if a.m == b.m: continue
        try:
            # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line_segment
            xi = ((a.px*a._py - a.py*a._px)*(b.px-b._px) - (a.px-a._px)*(b.px*b._py-b.py*b._px)) / ((a.px-a._px)*(b.py-b._py)-(a.py-a._py)*(b.px-b._px))
            yi = ((a.px*a._py - a.py*a._px)*(b.py-b._py) - (a.py-a._py)*(b.px*b._py - b.py*b._px)) / ((a.px-a._px)*(b.py-b._py) - (a.py-a._py)*(b.px-b._px))
        except ZeroDivisionError:
            continue
        if not window_min <= xi <= window_max or not window_min <= yi <= window_max: continue
        if not doesContainB(a.px, int(xi), a.dx) or not doesContainB(a.py, int(yi), a.dy): continue
        if not doesContainB(b.px, int(xi), b.dx) or not doesContainB(b.py, int(yi), b.dy): continue
        total += 1
    return total


def part_2(p_Input):
    pass


example_input_1 = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""
challenge_input = Input(24)

# assert(part_1(example_input_1) == None)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
