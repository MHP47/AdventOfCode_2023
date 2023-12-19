from utils import *


def part_1(p_Input):
    class Part():
        def __init__(self, x, m, a, s):
            self.x = x
            self.m = m
            self.a = a
            self.s = s
        def __str__(self):
            return f"x={self.x},m={self.m},a={self.a},s={self.s}"
        def __repr__(self):
            return f"Part(x={self.x},m={self.m},a={self.a},s={self.s})"
        def rating(self):
            return self.x + self.m + self.a + self.s

    def work(part, workflow):
        for work in workflow:
            try:
                e,d = work.split(':')
                if not eval('part.'+e):
                    continue
                else:
                    break
            except ValueError:
                d = work
        if d == 'A':
            accepted.append(part)
            return None
        if d == 'R':
            return None
        return d


    rules,parts = p_Input.strip().split('\n\n')
    parts = [Part(*parse_ints(x)) for x in parts.splitlines()]
    m = re.compile(r'^(\w+){(.*)}$')
    rules = { a: b.split(',') for a,b in [m.match(text).groups() for text in rules.splitlines()] }
    accepted = []
    for p in parts:
        cmd = 'in'
        while cmd := work(p, rules[cmd]):
            pass
    return sum(x.rating() for x in accepted)


def part_2(p_Input):
    pass


example_input_1 = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""
challenge_input = Input(19)

assert(part_1(example_input_1) == 19114)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
