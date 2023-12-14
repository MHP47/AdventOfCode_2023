from utils import *


def part_1(p_Input):
    g = Grid(rows = p_Input.splitlines())
    UP = (0,-1)
    rocks = [k for k,v in g.items() if v == 'O']
    for r in rocks:
        while True:
            move = tuple(sum(x) for x in zip(UP, r))
            if Y(r)==0 or g[move]in ('O','#'):
                break
            g[r] = '.'
            g[move] = 'O'
            r = move

    return sum([g.height-k[1] for k,v in g.items() if v == 'O'])


def part_2(p_Input):
    pass


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

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
