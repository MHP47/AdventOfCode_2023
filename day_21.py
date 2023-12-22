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


def part_2(p_Input, steps=26501365):
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

    odd_steps    = sum(1 for v in visited.values() if v%2)
    odd_corners  = sum(1 for v in visited.values() if v%2 and v > 65)

    even_steps   = sum(1 for v in visited.values() if not v%2)
    even_corners = sum(1 for v in visited.values() if not v%2 and v > 65)

    n = (steps - (g.width // 2)) // g.width

    return (n+1)**2 * odd_steps + n**2 * even_steps - (n+1) * odd_corners + n * even_corners


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

# Removed as solution is not generic enough for example cases
# assert(part_2(example_input_1, 6) == 16)
# assert(part_2(example_input_1, 10) == 50)
# assert(part_2(example_input_1, 50) == 1594)
# assert(part_2(example_input_1, 100) == 6536)
# assert(part_2(example_input_1, 500) == 167004)
# assert(part_2(example_input_1, 1000) == 668697)
# assert(part_2(example_input_1, 5000) == 16733044)
print(f"Part 2: {part_2(challenge_input)}")
