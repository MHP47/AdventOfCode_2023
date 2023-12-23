from utils import *
from queue import PriorityQueue


class Brick:
    def __init__(self, sx, sy, sz, ex, ey, ez):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.ex = ex
        self.ey = ey
        self.ez = ez
        self.floor = min(sz, ez)
        self.height = abs(sz - ez)
        self.support = []
        self.supporting = []
    def __lt__(self, other):
        return self.floor < other.floor
    def __repr__(self):
        return str(id(self))


def part_1(p_Input):
    b = [Brick(*parse_ints(x)) for x in p_Input.strip().splitlines()]
    lowest_level = min(i.floor for i in b)
    bricks = PriorityQueue()
    settled_bricks = []
    for i in b: bricks.put(i)

    while not bricks.empty():
        b = bricks.get(False)
        if b.floor == lowest_level:
            settled_bricks.append(b)
            continue
        support = []
        support_level = 0
        for sb in settled_bricks:
            if sb.sx <= b.ex and b.sx <= sb.ex and sb.sy <= b.ey and b.sy <= sb.ey:
                sb_top = sb.floor + sb.height
                if sb_top > support_level:
                    support = []
                    support_level = sb_top
                if sb_top == support_level:
                    support.append(sb)
        b.support = support[:]
        b.floor = support_level + 1
        settled_bricks.append(b)
        for s in support:
            s.supporting.append(b)

    return sum(not sb.supporting or all(len(s.support) > 1 for s in sb.supporting) for sb in settled_bricks)


def part_2(p_Input):
    b = [Brick(*parse_ints(x)) for x in p_Input.strip().splitlines()]
    lowest_level = min(i.floor for i in b)
    bricks = PriorityQueue()
    settled_bricks = []
    for i in b: bricks.put(i)

    while not bricks.empty():
        b = bricks.get(False)
        if b.floor == lowest_level:
            settled_bricks.append(b)
            continue
        support = []
        support_level = 0
        for sb in settled_bricks:
            if sb.sx <= b.ex and b.sx <= sb.ex and sb.sy <= b.ey and b.sy <= sb.ey:
                sb_top = sb.floor + sb.height
                if sb_top > support_level:
                    support = []
                    support_level = sb_top
                if sb_top == support_level:
                    support.append(sb)
        b.support = support[:]
        b.floor = support_level + 1
        settled_bricks.append(b)
        for s in support:
            s.supporting.append(b)

    total = 0
    for sb in settled_bricks:
        stack = deque([s for s in sb.supporting if len(s.support) == 1])
        fallen = set()
        while stack:
            b = stack.popleft()
            fallen.add(b)
            stack.extend(
                [
                    s for s in b.supporting
                    if set(s.support).issubset(fallen)
                ]
            )
        total += len(fallen)

    return total


example_input_1 = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""
challenge_input = Input(22)

assert(part_1(example_input_1) == 5)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 7)
print(f"Part 2: {part_2(challenge_input)}")
