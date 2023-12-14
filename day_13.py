from utils import *
from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def part_1(p_Input):
    def checker(data):
        a = defaultdict(list)
        for k,v in enumerate(data, 1):
            a[v].append(k)
        hx,hy = 0,0
        lookup = flatten([tuple(itertools.combinations(x,2)) for x in a.values()])
        for hx,hy in [z for z in \
            flatten([list(pairwise(y)) for y in (x for x in a.values() if len(x) >= 2)]) if z[0]+1 == z[1]]:
            if all(z in lookup for z in zip(range(hx,0,-1), range(hy,k+1))):
                break
        else:
            return None
        return min(hx,hy)


    total = 0
    for t in p_Input.strip().split('\n\n'):
        data = t.splitlines()
        for mul in (100,1):
            if val := checker(data):
                break
            data = list(zip(*data))
        total += val*mul

    return total


def part_2(p_Input):
    def matches(data):
        b = defaultdict(list)
        for i in itertools.combinations(range(len(data)),2):
            b[sum(x!=y for x,y in zip(data[i[0]], data[i[1]]))].append(i)
        return b.get(0, []), b.get(1,[])

    total = 0
    for v,t in enumerate(p_Input.strip().split('\n\n')):
        data = t.splitlines()
        m,o = matches(data)
        mul = 0
        for (dx,dy),n in [(z,y) for y in [m+[x] for x in o] for z in y if z[0]+1==z[1]]:
            p = list(zip(range(dx,-1,-1), range(dy,len(data))))
            if all(z in n for z in p) and any(z in o for z in p):
                mul = 100
                break
        else:
            data = list(zip(*data))
            m,o = matches(data)
            for (dx,dy),n in [(z,y) for y in [m+[x] for x in o] for z in y if z[0]+1==z[1]]:
                p = list(zip(range(dx,-1,-1), range(dy,len(data))))
                if all(z in n for z in p) and any(z in o for z in p):
                    mul = 1
                    break
            else:
                raise NotImplementedError(v)
        total += (min(dx,dy)+1) * mul
    return total


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

assert(part_2(example_input_1) == 400)
print(f"Part 2: {part_2(challenge_input)}")
