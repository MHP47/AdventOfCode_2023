from utils import *


def part_1(p_Input):
    return sum(
        x * 10 + y
        for x,y in [
            operator.itemgetter(0,-1)(
                tuple(map(int, re.findall(r'\d', i)))
            )
            for i in p_Input.strip().splitlines()
        ]
    )


def part_2(p_Input):
    pass


example_input_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
challenge_input = Input(1)

assert(part_1(example_input_1) == 142)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
