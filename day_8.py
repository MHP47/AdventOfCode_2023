from utils import *


def part_1(p_Input):
    instructions, nav = p_Input.split('\n\n')
    instructions = itertools.cycle([0 if x == 'L' else 1 for x in instructions])
    network = dict()
    for i in [ {a: (b,c)} for a,b,c in [re.findall(r'\w+', x) for x in nav.splitlines()]]:
        network.update(i)
    curr = 'AAA'
    for counter in itertools.count(0):
        next_dest = network[curr][next(instructions)]
        if next_dest == 'ZZZ': return counter + 1
        curr = next_dest


def part_2(p_Input):
    instructions, nav = p_Input.split('\n\n')
    instructions = itertools.cycle([0 if x == 'L' else 1 for x in instructions])
    network = dict()
    for i in [ {a: (b,c)} for a,b,c in [re.findall(r'\w+', x) for x in nav.splitlines()]]:
        network.update(i)
    path_lengths = []
    for curr in [x for x in network.keys() if x[-1] == 'A']:
        for counter in itertools.count(0):
            next_dest = network[curr][next(instructions)]
            if next_dest[-1] == 'Z':
                path_lengths.append(counter + 1)
                break
            curr = next_dest
    return lcm(*path_lengths)


example_input_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""
example_input_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
example_input_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
challenge_input = Input(8)

assert(part_1(example_input_1) == 2)
assert(part_1(example_input_2) == 6)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_3) == 6)
print(f"Part 2: {part_2(challenge_input)}")
