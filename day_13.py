from utils import *
from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def part_1(p_Input):
    total = 0
    for i,data in enumerate(p_Input.strip().split('\n\n')):
        d = data.splitlines()
        a = defaultdict(list)
        for k,v in enumerate(d, 1):
            a[v].append(k)
        hx,hy,vx,vy = 0,0,0,0
        lookup = flatten([tuple(itertools.combinations(x,2)) for x in a.values()])
        for hx,hy in [z for z in \
            flatten([list(pairwise(y)) for y in (x for x in a.values() if len(x) >= 2)]) if z[0]+1 == z[1]]:
            if all(z in lookup for z in zip(range(hx,0,-1), range(hy,k+1))):
                break
        else:
            hx,hy,vx,vy = 0,0,0,0
            a = defaultdict(list)
            for k,v in enumerate(zip(*d),1):
                a[v].append(k)
            lookup = flatten([tuple(itertools.combinations(x,2)) for x in a.values()])
            for vx,vy in [z for z in \
                flatten([list(pairwise(y)) for y in (x for x in a.values() if len(x) >= 2)]) if z[0]+1 == z[1]]:
                if all(z in lookup for z in zip(range(vx,0,-1), range(vy,k+1))):
                    break
            else:
                vx,vy = 0,0
        total += min(vx,vy) + min(hx,hy)*100
    return total


def part_2(p_Input):
    pass


example_input_1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
challenge_input = Input(13)

assert(part_1(example_input_1) == 405)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
