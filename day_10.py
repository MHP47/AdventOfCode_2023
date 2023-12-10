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

    # Set the start grid char value correctly
    first_step_dir = tuple([sub_reduce(x) for x in zip(path[1], path[0])])
    last_step_dir  = tuple([sub_reduce(x) for x in zip(path[-1], path[0])])
    if first_step_dir == UP:
        grid[start] = {DOWN: '|', RIGHT: 'F', LEFT: '7'}[last_step_dir]
    elif first_step_dir == LEFT:
        grid[start] = {UP: 'J', DOWN: '7', RIGHT: '-'}[last_step_dir]
    elif first_step_dir == RIGHT:
        grid[start] = {UP: 'L', DOWN: 'F', LEFT: '-'}[last_step_dir]

    path = set(path)
    inside_count = 0
    for i in set(grid) - path: grid[i] = '.'

    for y in range(grid.height):
        inside = False
        for x in range(grid.width):
            if grid[(x,y)] in {'|', 'J', 'L'}:
                inside = not inside
            elif inside and (x,y) not in path:
                inside_count += 1

    return inside_count


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
example_input_3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""
example_input_4 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""
example_input_5 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""
challenge_input = Input(10)

assert(part_1(example_input_1) == 4)
assert(part_1(example_input_2) == 8)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_3) == 4)
assert(part_2(example_input_4) == 8)
assert(part_2(example_input_5) == 10)
print(f"Part 2: {part_2(challenge_input)}")
