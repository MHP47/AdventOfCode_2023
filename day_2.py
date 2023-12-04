from utils import *


def part_1(p_Input):
    games = defaultdict(lambda: defaultdict(int))
    for game in p_Input.strip().splitlines():
        game_no, game_data = game.split(': ')
        game_rounds = game_data.split('; ')
        game_no = parse_ints(game_no)[0]
        games[game_no]['red'] = 0
        games[game_no]['green'] = 0
        games[game_no]['blue'] = 0
        for rnd in game_rounds:
            for cubes in rnd.split(', '):
                count,colour = cubes.split()
                games[game_no][colour] = max(int(count), games[game_no][colour])

    return sum([k for k,v in games.items() if v['red'] <= 12 and v['green'] <= 13 and v['blue'] <= 14])


def part_2(p_Input):
    pass


example_input_1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
challenge_input = Input(2)

assert(part_1(example_input_1) == 8)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
