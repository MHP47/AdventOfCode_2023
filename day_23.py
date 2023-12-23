from utils import *
from operator import sub


def part_1(p_Input):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    move = lambda x,y: tuple(sum(z) for z in zip(x, y))
    grid = Grid(rows = p_Input.strip().splitlines())
    start = next((k, 0) for k in range(grid.width) if grid[(k,0)] == '.')
    goal = next((k, grid.height-1) for k in range(grid.width) if grid[(k, grid.height-1)] == '.')
    path = deque([[start]])
    result = 0

    while path:
        p = path.popleft()
        c = p[-1]
        if c == goal:
            result = max(result, len(p))
            continue
        for s in [x for x in grid.neighbors(c) if grid[x] != '#']:
            if s in p: continue
            if grid[s] == '.':
                path.append(p + [s])
            elif grid[s] == { UP: '^', DOWN: 'v', LEFT: '<', RIGHT: '>' }[tuple(sub(*z) for z in zip(s,c))]:
                path.append(p + [s])

    return result - 1


def part_2(p_Input):
    pass


example_input_1 = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""
challenge_input = Input(23)

assert(part_1(example_input_1) == 94)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
