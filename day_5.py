from utils import *


def part_1(p_Input):
    almanac = p_Input.split('\n\n')
    seeds = parse_ints(almanac[0])
    searching = deque([(0,x) for x in seeds])

    def search_pos(data, searching):
        found = deque()
        for i in data:
            dest, start, rng = parse_ints(i)
            not_found = deque()
            while searching:
                *l,s = searching.popleft()
                if s in range(start, start+rng):
                    found.append(
                        tuple(l)+(s,dest+s-start)
                    )
                else:
                    not_found.append(tuple(l)+(s,))
            searching = not_found
        for *l,s in searching: found.append(tuple(l)+(s,s))
        return found

    for mapping in almanac[1:]:
        searching = search_pos(mapping.splitlines()[1:], searching)

    return min(searching, key=lambda x: x[-1])[-1]


def part_2(p_Input):
    pass


example_input_1 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
challenge_input = Input(5)

assert(part_1(example_input_1) == 35)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
