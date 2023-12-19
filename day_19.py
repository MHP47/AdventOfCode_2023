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
    rules,_ = p_Input.strip().split('\n\n')
    matcher = re.compile(r'^(\w+){(.*)}$')
    rules = { a: b.split(',') for a,b in [matcher.match(text).groups() for text in rules.splitlines()] }
    matcher = re.compile(r'^([xmas])([<>])(\d+):(\w+)$')

    def work(cmd, parts = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}):
        if cmd == 'R':
            return 0
        if cmd == 'A':
            return math.prod(len(range(*b))+1 for b in parts.values())
        total = 0
        for rule in rules[cmd]:
            try:
                t,o,v,d = matcher.match(rule).groups()
                v = int(v)
                new_parts = dict(parts)
                if parts[t][0] < v < parts[t][1]:
                    if o == '<':
                        new_parts[t] = (parts[t][0], v - 1)
                        parts[t] = (v, parts[t][1])
                    else:
                        new_parts[t] = (v + 1, parts[t][1])
                        parts[t] = (parts[t][0], v)
                    total += work(d, new_parts)
            except AttributeError:
                total += work(rule, parts)
        return total

    return work('in')


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

assert(part_2(example_input_1) == 167409079868000)
print(f"Part 2: {part_2(challenge_input)}")
