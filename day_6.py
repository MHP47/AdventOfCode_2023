from utils import *


def part_1(p_Input):
    matches = [parse_ints(x) for x in p_Input.splitlines()]
    return mul_reduce(
        [
            len(
                [
                    z
                    for z in [
                        (x-i) * i
                        for i in range(x+1)
                    ]
                    if z > y
                ]
            )
            for x,y in zip(*matches)
        ]
    )


def part_2(p_Input):
    pass


example_input_1 = """Time:      7  15   30
Distance:  9  40  200
"""
challenge_input = Input(6)

assert(part_1(example_input_1) == 288)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
