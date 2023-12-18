from utils import *


def part_1(p_Input):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    D = { 'R': RIGHT, 'D': DOWN, 'L': LEFT, 'U': UP }
    move = lambda x,y: tuple(sum(z) for z in zip(x, y))
    position = (0,0)
    grid = {}
    grid[position] = '#'

    for d,l,c in [x.split() for x in p_Input.strip().splitlines()]:
        for _ in range(int(l)):
            position = move(position, D[d])
            grid[position] = '#'

    y_min, y_max = min(x[0] for x in grid), max(x[0] for x in grid)
    x_min, x_max = min(x[1] for x in grid), max(x[1] for x in grid)

    to_check = deque([(y_min-1, x_min-1)])
    xr = range(x_min-1, x_max+2)
    yr = range(y_min-1, y_max+2)
    seen = set()
    while to_check:
        y,x = to_check.popleft()
        if y not in yr or x not in xr: continue
        if (y,x) in seen: continue
        seen.add((y,x))
        for i in neighbors4((y,x)):
            if i not in grid:
                to_check.append(i)

    y_min, y_max = min(x[0] for x in seen), max(x[0] for x in seen)
    x_min, x_max = min(x[1] for x in seen), max(x[1] for x in seen)
    return len(range(y_min, y_max+1))*len(range(x_min, x_max+1)) - len(seen)


def part_2(p_Input):
    pass


example_input_1 = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""
challenge_input = Input(18)

assert(part_1(example_input_1) == 62)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
