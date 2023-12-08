from utils import *


def part_1(p_Input):
    instructions, nav = p_Input.split('\n\n')
    instructions = [0 if x == 'L' else 1 for x in instructions]
    network = dict()
    for i in [ {a: (b,c)} for a,b,c in [re.findall(r'\w+', x) for x in nav.splitlines()]]:
        network.update(i)
    curr = 'AAA'
    for counter in itertools.count(0):
        direction = instructions[counter%len(instructions)]
        next_dest = network[curr][direction]
        if next_dest == 'ZZZ': return counter + 1
        curr = next_dest


def part_2(p_Input):
    pass


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
challenge_input = Input(8)

assert(part_1(example_input_1) == 2)
assert(part_1(example_input_2) == 6)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
