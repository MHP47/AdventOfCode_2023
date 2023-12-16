from utils import *


def part_1(p_Input):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    g = Grid(rows = p_Input.strip().splitlines())
    start = ((-1,0), RIGHT)
    cache = set()
    heads = deque()
    heads.append(start)
    while heads:
        loc,bearing = heads.popleft()
        if (loc, bearing) in cache:
            continue
        cache.add((loc,bearing))
        n = tuple(sum(x) for x in zip(loc, bearing))
        if n not in g:
            continue
        if g[n] == '.':
            heads.append((n, bearing))
        elif g[n] == '|':
            if bearing in (LEFT, RIGHT):
                heads.append((n, UP))
                heads.append((n, DOWN))
            else:
                heads.append((n, bearing))
        elif g[n] == '-':
            if bearing in (UP, DOWN):
                heads.append((n, LEFT))
                heads.append((n, RIGHT))
            else:
                heads.append((n, bearing))
        elif g[n] == '/':
            new_bearing = { LEFT: DOWN, RIGHT: UP, DOWN: LEFT, UP: RIGHT }[bearing]
            heads.append((n, new_bearing))
        elif g[n] == '\\':
            new_bearing = { LEFT: UP, RIGHT: DOWN, DOWN: RIGHT, UP: LEFT }[bearing]
            heads.append((n, new_bearing))

    return len(set(x for x,_ in cache if x in g))


def part_2(p_Input):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    g = Grid(rows = p_Input.strip().splitlines())
    MAX = 0
    for start in [((-1,y),RIGHT) for y in range(g.height)] + \
                 [((g.width,y),LEFT) for y in range(g.height)] + \
                 [((x,-1),DOWN) for x in range(g.width)] + \
                 [((x,g.height),UP) for x in range(g.width)]:
        cache = set()
        heads = deque()
        heads.append(start)
        while heads:
            loc,bearing = heads.popleft()
            if (loc, bearing) in cache:
                continue
            cache.add((loc,bearing))
            n = tuple(sum(x) for x in zip(loc, bearing))
            if n not in g:
                continue
            if g[n] == '.':
                heads.append((n, bearing))
            elif g[n] == '|':
                if bearing in (LEFT, RIGHT):
                    heads.append((n, UP))
                    heads.append((n, DOWN))
                else:
                    heads.append((n, bearing))
            elif g[n] == '-':
                if bearing in (UP, DOWN):
                    heads.append((n, LEFT))
                    heads.append((n, RIGHT))
                else:
                    heads.append((n, bearing))
            elif g[n] == '/':
                new_bearing = { LEFT: DOWN, RIGHT: UP, DOWN: LEFT, UP: RIGHT }[bearing]
                heads.append((n, new_bearing))
            elif g[n] == '\\':
                new_bearing = { LEFT: UP, RIGHT: DOWN, DOWN: RIGHT, UP: LEFT }[bearing]
                heads.append((n, new_bearing))
        MAX = max(MAX, len(set(x for x,_ in cache if x in g)))
    return MAX


example_input_1 = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""
challenge_input = Input(16)

assert(part_1(example_input_1) == 46)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 51)
print(f"Part 2: {part_2(challenge_input)}")
