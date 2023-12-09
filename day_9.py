from utils import *
from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def part_1(p_Input):
    results = defaultdict(int)

    for seq, nums in enumerate((parse_ints(x) for x in p_Input.splitlines())):
        while sum(nums) != 0:
            results[seq] += nums[-1]
            nums = [-sub_reduce(x) for x in pairwise(nums)]

    return sum(results.values())


def part_2(p_Input):
    pass


example_input_1 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
challenge_input = Input(9)

assert(part_1(example_input_1) == 114)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
