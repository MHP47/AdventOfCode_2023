from utils import *


def part_1(p_Input):
    grid = Grid(rows = p_Input.splitlines())
    start = next(k for k,v in grid.items() if v == 'S')

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    STEPS = {
        # Point HowMovedOnToPoint NextMoveAway
        ('|', DOWN): DOWN,
        ('|', UP): UP,
        ('-', RIGHT): RIGHT,
        ('-', LEFT): LEFT,
        ('L', LEFT): UP,
        ('L', DOWN): RIGHT,
        ('J', RIGHT): UP,
        ('J', DOWN): LEFT,
        ('7', RIGHT): DOWN,
        ('7', UP): LEFT,
        ('F', LEFT): DOWN,
        ('F', UP): RIGHT,
    }

    def step(current, direction):
        return tuple(sum(x) for x in zip(current, direction))

    def get_first_step(point):
        l = (X(point)-1, Y(point))
        r = (X(point)+1, Y(point))
        u = (X(point), Y(point)-1)
        d = (X(point), Y(point)+1)

        if grid.get(u, '.') in ['|', '7', 'F']:
            return u, UP
        if grid.get(l, '.') in ['-', 'L', 'F'] \
            and (grid.get(r, '.') in ['-', 'J', '7'] or
                grid.get(d, '.') in ['|', 'L', 'J']):
            return l, LEFT
        if grid.get(r, '.') in ['-', 'J', '7'] \
            and grid.get(d, '.') in ['|', 'L', 'J']:
            return r, RIGHT

        raise ValueError()

    curr, direction = get_first_step(start)
    path = [start]
    while curr != start:
        path.append(curr)
        direction = STEPS[(grid[curr], direction)]
        curr = step(curr, direction)

    return len(path) // 2


def part_2(p_Input):
    pass


example_input_1 = """.....
.S-7.
.|.|.
.L-J.
.....
"""
example_input_2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""
challenge_input = Input(10)

assert(part_1(example_input_1) == 4)
assert(part_1(example_input_2) == 8)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
