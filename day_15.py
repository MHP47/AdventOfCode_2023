from utils import *


def part_1(p_Input):
    return sum([reduce((lambda x,y: ((x+y)*17)%256), [0]+[ord(x) for x in i]) for i in p_Input.strip().split(',')])


def part_2(p_Input):
    boxes = defaultdict(list)
    for i in p_Input.strip().split(','):
        k,v = re.split('=|-', i)
        box_num = reduce((lambda x,y: ((x+y)*17)%256), [0]+[ord(x) for x in k])
        if v:
            if k in [z[0] for z in boxes[box_num]]:
                z = next(z for z,d in enumerate(boxes[box_num]) if d[0] == k)
                boxes[box_num][z] = (k,v)
            else:
                boxes[box_num].append((k,v))
        elif k in [z[0] for z in boxes[box_num]]:
            _ = boxes[box_num].pop(next(z for z,d in enumerate(boxes[box_num]) if d[0] == k))


    return sum(sum([(k+1)*math.prod(x) for x in enumerate(map(int, [y for x,y in v]), 1)]) for k,v in boxes.items())



example_input_1 = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
challenge_input = Input(15)

assert(part_1(example_input_1) == 1320)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 145)
print(f"Part 2: {part_2(challenge_input)}")
