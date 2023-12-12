from utils import *
import functools


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
    @functools.lru_cache(maxsize=None)
    def solver(springs, condition, damaged_count = 0):
        # Base case, reached end of string
        # If all conditions matched, return True (1) else False (0)
        if not springs:
            return 1 if not condition else 0
        if springs[0] == '#':
            if not condition: return 0
            # Increment damaged count and move along string
            return solver(springs[1:], condition, damaged_count + 1)
        elif springs[0] == '.':
            if condition and condition[0] == damaged_count:
                # If damaged count equals the next condition report, decrement and advance
                return solver(springs[1:], condition[1:], 0)
            elif damaged_count == 0:
                # Didn't match, and previous was not a #; move along string
                return solver(springs[1:], condition, 0)
            else:
                return 0
        elif springs[0] == '?':
            # Calculate each if ? is a . and a #
            return solver('.' + springs[1:], condition, damaged_count) + \
                solver('#' + springs[1:], condition, damaged_count)

    return sum(
        solver(
            '?'.join([x]*5)+'.',
            tuple(parse_ints(','.join([y]*5)))
        )
        for x,y in [z.split() for z in p_Input.strip().splitlines()]
    )



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

assert(part_2(example_input_1) == 525152)
print(f"Part 2: {part_2(challenge_input)}")
