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
    DIGIT_WORDS = {
      'one': 1,
      'two': 2,
      'three': 3,
      'four': 4,
      'five': 5,
      'six': 6,
      'seven': 7,
      'eight': 8,
      'nine': 9
    }
    return sum(
        x * 10 + y
        for x,y in [
            operator.itemgetter(0,-1)(
                [
                    int(DIGIT_WORDS.get(z, z))
                    for z in re.findall(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', i)
                ]
            )
            for i in p_Input.strip().splitlines()
        ]
    )


example_input_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
example_input_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
challenge_input = Input(1)

assert(part_1(example_input_1) == 142)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_2) == 281)
print(f"Part 2: {part_2(challenge_input)}")
