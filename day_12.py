from utils import *


def part_1(p_Input):
    def checker(s, v):
        r = tuple(z for z in s.split('.') if z)
        if len(r) != len(v): return False
        return all(len(x) == y for x,y in zip(r,v))

    total = 0
    for x,y in [(y[0],parse_ints(y[1])) for y in [x.split() for x in p_Input.splitlines()]]:
        indexes = [i for i,j in enumerate(list(x)) if j == '?']
        for v in itertools.product(*[['.', '#']]*len(indexes)):
            t = list(x)
            for i,j in zip(indexes, v):
                t[i] = j
            if checker(cat(t), y):
                total += 1

    return total


def part_2(p_Input):
    pass


example_input_1 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
challenge_input = Input(12)

assert(part_1(example_input_1) == 21)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
