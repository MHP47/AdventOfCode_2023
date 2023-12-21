from utils import *


def part_1(p_Input):
    HIGH = True
    LOW = False

    class Module():
        def __init__(self, data='', name='', type='', destinations='', state=''):
            n,d = data.split(' -> ')
            self.name = name or re.sub(r'\W+', '', n)
            self.type = type or re.sub(r'\w+', '', n)
            self.destinations = destinations or d.split(', ')
            self.state = state or False if self.type == '%' else {} if self.type == '&' else None
        @staticmethod
        def get_name(data):
            return re.sub(r'\W+', '',data.split(' -> ')[0])
        def __repr__(self):
            return f"Module(name={self.name},type={self.type},destinations={self.destinations},state={self.state})"
        def process_pulse(self, p, s):
            if self.type == '%':
                self.state = not self.state
                return self.state
            elif self.type == '&':
                self.state[s] = p
                if all(self.state.values()): return LOW
                return HIGH

    modules = {}
    for i in p_Input.strip().splitlines():
        modules[Module.get_name(i)] = Module(i)

    for m in modules.values():
        for d in m.destinations:
            if d not in modules: continue
            m2 = modules[d]
            if m2.type != '&': continue
            m2.state[m.name] = LOW

    seen = { LOW: 0, HIGH: 0}

    for _ in range(1000):
        # Destination, Pulse, Sender
        states = deque([(d, LOW, 'broadcaster') for d in modules['broadcaster'].destinations])
        seen[LOW] += 1
        while states:
            current, pulse, sender = states.popleft()
            seen[pulse] += 1
            if current not in modules: continue
            current = modules[current]
            if current.type == '%' and pulse == HIGH: continue
            next_pulse = current.process_pulse(pulse, sender)
            states.extend([(d2, next_pulse, current.name) for d2 in current.destinations])

    return math.prod(seen.values())


def part_2(p_Input):
    pass


example_input_1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""
example_input_2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""
challenge_input = Input(20)

assert(part_1(example_input_1) == 32000000)
assert(part_1(example_input_2) == 11687500)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
