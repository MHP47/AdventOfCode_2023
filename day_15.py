from utils import *


def part_1(p_Input):
    return sum([reduce((lambda x,y: ((x+y)*17)%256), [0]+[ord(x) for x in i]) for i in p_Input.strip().split(',')])


def part_2(p_Input):
    pass


example_input_1 = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
challenge_input = Input(15)

assert(part_1(example_input_1) == 1320)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
