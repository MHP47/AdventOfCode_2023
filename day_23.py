from utils import *
from operator import sub
import networkx as nx


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
    grid = Grid(rows = p_Input.strip().splitlines())
    adj = dict()
    start = next((k, 0) for k in range(grid.width) if grid[(k,0)] == '.')
    goal = next((k, grid.height-1) for k in range(grid.width) if grid[(k, grid.height-1)] == '.')
    intersections = set([start, goal])

    for i in [k for k,v in grid.items() if v in {'>','<','v','^'}]:
        grid[i] = '.'

    for k,v in grid.items():
        if v == '.':
            adj[k] = [x for x in grid.neighbors(k) if grid[x] == '.']
            if sum([grid[x]=='.' for x in grid.neighbors(k)]) > 2:
                intersections.add(k)

    paths = defaultdict(dict)
    state = deque([start])

    while state:
        c = state.popleft()
        for n in [x for x in adj[c]]:
            p = set([c])
            while n not in intersections:
                p.add(n)
                n = next(x for x in adj[n] if x not in p)
            paths[c][n] = len(p) - 1
            if n not in paths:
                state.append(n)

    network = nx.Graph()
    for k,v in paths.items():
        for i,j in v.items():
            network.add_edge(k, i, weight=j)

    # This is a bit slow, >1-2min
    return max(
        nx.classes.function.path_weight(network, p, weight="weight") + len(p) - 1
        for p in nx.all_simple_paths(network, start, goal)
    )


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

assert(part_2(example_input_1) == 154)
print(f"Part 2: {part_2(challenge_input)}")
