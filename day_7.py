from utils import *
from functools import cmp_to_key


def part_1(p_Input):
    def get_hand(h):
        c = Counter(h).most_common()
        e = tuple([x[1] for x in c])
        if e == (5,): return 1 # 5 of a kind
        if e == (4, 1): return 2 # 4 of a kind
        if e == (3, 2): return 3 # Full house
        if e == (3, 1, 1): return 4 # 3 of a kind
        if e == (2, 2, 1): return 5 # 2 pair
        if e == (2, 1, 1, 1): return 6 # 1 pair
        if e == (1, 1, 1, 1, 1): return 7 # High card

    def compare(x, y):
        S = [ 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ]
        if S.index(x[0]) < S.index(y[0]):
            return -1
        elif S.index(x[0]) > S.index(y[0]):
            return 1
        else:
            return compare(x[1:], y[1:])

    lookup = dict()
    hands = defaultdict(list)

    for hand in p_Input.splitlines():
        cards, bid = hand.split()
        lookup[cards] = int(bid)
        hands[get_hand(cards)].append(cards)

    results = []

    for k,v in sorted(hands.items()):
        results.extend(sorted(v, key=cmp_to_key(lambda x, y: compare(x, y))))

    return sum([mul_reduce((i, lookup[x])) for i,x in enumerate(results[::-1], 1)])


def part_2(p_Input):
    def get_hand(h):
        h = h.replace('J', '')
        if not h: return 1
        c = Counter(h).most_common()
        v = c[0][1] + 5 - len(h)
        e = tuple([v] + [x[1] for x in c[1:]])
        if e == (5,): return 1 # 5 of a kind
        if e == (4, 1): return 2 # 4 of a kind
        if e == (3, 2): return 3 # Full house
        if e == (3, 1, 1): return 4 # 3 of a kind
        if e == (2, 2, 1): return 5 # 2 pair
        if e == (2, 1, 1, 1): return 6 # 1 pair
        if e == (1, 1, 1, 1, 1): return 7 # High card

    def compare(x, y):
        S = [ 'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J' ]
        if S.index(x[0]) < S.index(y[0]):
            return -1
        elif S.index(x[0]) > S.index(y[0]):
            return 1
        else:
            return compare(x[1:], y[1:])

    lookup = dict()
    hands = defaultdict(list)

    for hand in p_Input.splitlines():
        cards, bid = hand.split()
        lookup[cards] = int(bid)
        hands[get_hand(cards)].append(cards)

    results = []

    for k,v in sorted(hands.items()):
        results.extend(sorted(v, key=cmp_to_key(lambda x, y: compare(x, y))))

    return sum([mul_reduce((i, lookup[x])) for i,x in enumerate(results[::-1], 1)])


example_input_1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
challenge_input = Input(7)

assert(part_1(example_input_1) == 6440)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 5905)
print(f"Part 2: {part_2(challenge_input)}")
