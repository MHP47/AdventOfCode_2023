from utils import *
import functools


def part_1(p_Input, steps=64):
    g = Grid(rows = p_Input.strip().splitlines())
    start = next(k for k,v in g.items() if v == 'S')
    g[start] = '.'
    L = set(k for k,v in g.items() if v == '.')
    visited = dict()
    state = deque([(n, 1) for n in g.neighbors(start) if n in L])

    while state:
        (x,y), s = state.popleft()
        visited[(x,y)] = s
        for n in set([(x+1, y), (x-1, y), (x, y+1), (x, y-1)]) & L:
            state.append([n, s+1])
            L.remove(n)

    return sum(1 for v in visited.values() if v<=steps and not v%2)


def part_2(p_Input):
    pass


example_input_1 = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""
challenge_input = Input(21)

assert(part_1(example_input_1, 6) == 16)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
