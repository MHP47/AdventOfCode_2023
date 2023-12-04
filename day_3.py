from utils import *


def part_1(p_Input):
    parts = re.findall(r'\d+', p_Input)
    grid = Grid(rows=p_Input.strip().splitlines())
    part_locs = dict()
    real_parts = []
    p_counter = 0

    for h in range(grid.height):
        w = 0
        while w < grid.width:
            v = grid[(w,h)]
            if not v.isdigit():
                w += 1
                continue
            part = parts[p_counter]
            p_counter += 1
            to_check = [(w+i,h) for i in range(len(part))]
            w += len(part)
            checked = [y for x in to_check for y in neighbors8(x) if y in grid and y not in to_check]
            assert all([grid[x].isdigit() for x in to_check]), to_check
            for i in to_check:
                part_locs[i] = part
            if any([not grid[x].isdigit() and grid[x] != '.' for x in checked]):
                real_parts.append(part)

    return sum(list(map(int, real_parts)))


def part_2(p_Input):
    parts = re.findall(r'\d+', p_Input)
    grid = Grid(rows=p_Input.strip().splitlines())
    part_locs = dict()
    real_parts = []
    p_counter = 0

    for h in range(grid.height):
        w = 0
        while w < grid.width:
            v = grid[(w,h)]
            if not v.isdigit():
                w += 1
                continue
            part = parts[p_counter]
            p_counter += 1
            to_check = [(w+i,h) for i in range(len(part))]
            w += len(part)
            checked = [y for x in to_check for y in neighbors8(x) if y in grid and y not in to_check]
            assert all([grid[x].isdigit() for x in to_check]), to_check
            for i in to_check:
                part_locs[i] = part
            if any([not grid[x].isdigit() and grid[x] != '.' for x in checked]):
                real_parts.append(part)

    gears = [k for k,v in grid.items() if v == '*']
    gear_ratio = 0
    for gear in gears:
        gear_set = set([part_locs[x] for x in neighbors8(gear) if x in grid and grid[x].isdigit()])
        if len(gear_set) == 2:
            gear_ratio += mul_reduce(map(int, gear_set))

    return gear_ratio


example_input_1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
challenge_input = Input(3)

assert(part_1(example_input_1) == 4361)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 467835)
print(f"Part 2: {part_2(challenge_input)}")
