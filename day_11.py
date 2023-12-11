from utils import *


def part_1(p_Input):
    inpt = re.sub(f'(\.{{{len(p_Input.splitlines()[0])}}}\n)', r'\1\1', p_Input).splitlines()
    grid = Grid(rows = inpt)
    for i in [x for x in range(grid.width) if all([grid[(x,y)] == '.' for y in range(grid.height)])][::-1]:
        for j in range(len(inpt)):
            inpt[j] = inpt[j][:i] + '.' + inpt[j][i:]
    grid = Grid(rows = inpt)
    return sum(cityblock_distance(*y) for y in itertools.combinations([k for k,v in grid.items() if v == '#'], 2))


def part_2(p_Input, expansion=1000000):
    grid = Grid(rows = p_Input.splitlines())

    blank_cols = [x for x in range(grid.width) if all([grid[(x,y)] == '.' for y in range(grid.height)])]
    blank_rows = [y for y in range(grid.height) if all([grid[(x,y)] == '.' for x in range(grid.width)])]

    galaxies = [
        (
            x+(expansion-1)*sum([x>z for z in blank_cols]),
            y+(expansion-1)*sum([y>z for z in blank_rows])
        )
        for x,y in [k for k,v in grid.items() if v == '#']
    ]

    return sum(cityblock_distance(*y) for y in itertools.combinations(galaxies, 2))


example_input_1 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
challenge_input = Input(11)

assert(part_1(example_input_1) == 374)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1, 10) == 1030)
assert(part_2(example_input_1, 100) == 8410)
print(f"Part 2: {part_2(challenge_input)}")
