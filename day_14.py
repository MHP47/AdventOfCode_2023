from utils import *


def part_1(p_Input):
    g = Grid(rows = p_Input.splitlines())
    UP = (0,-1)
    rocks = [k for k,v in g.items() if v == 'O']
    for r in rocks:
        while True:
            move = tuple(sum(x) for x in zip(UP, r))
            if Y(r)==0 or g[move] in ('O','#'):
                break
            g[r] = '.'
            g[move] = 'O'
            r = move

    return sum([g.height-k[1] for k,v in g.items() if v == 'O'])


def part_2(p_Input):
    def tilt(records):
        height = len(records)
        width = len(records[0])
        for x in range(width):
            for _ in range(height):
                for y in range(height):
                    if records[y][x] == 'O' and y > 0 and records[y-1][x] == '.':
                        records[y][x] = '.'
                        records[y-1][x] = 'O'
        return records

    def rotate(records):
        height = len(records)
        width = len(records[0])
        new_grid = [['x' for _ in range(height)] for _ in range(width)]
        for y in range(height):
            for x in range(width):
                new_grid[x][height-1-y] = records[y][x]
        return new_grid

    g = [[r for r in row] for row in p_Input.strip().splitlines()]
    cache = {}
    counter = 0
    while counter < 1000000000:
        counter += 1
        for _ in range(4):
            g = tilt(g)
            g = rotate(g)
        hashed = tuple(tuple(row) for row in g)
        if hashed in cache:
            cycle_length = counter - cache[hashed]
            step_amount = (1000000000 - counter) // cycle_length
            counter += step_amount * cycle_length
        cache[hashed] = counter

    total = 0
    height = len(g)
    width = len(g[0])
    for y in range(height):
        for x in range(width):
            if g[y][x] == 'O':
                total += height - y

    return total


example_input_1 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
challenge_input = Input(14)

assert(part_1(example_input_1) == 136)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 64)
print(f"Part 2: {part_2(challenge_input)}")
