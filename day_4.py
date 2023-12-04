from utils import *


def part_1(p_Input):
    total = 0
    for game in p_Input.strip().splitlines():
        game_no, game_data = game.split(': ')
        winning_numbers, card_numbers = [set(parse_ints(x)) for x in game_data.split(' | ')]
        if winners := card_numbers.intersection(winning_numbers):
            total += 2**(len(winners)-1)

    return total


def part_2(p_Input):
    wins = dict()
    for game in p_Input.strip().splitlines():
        game_no, game_data = game.split(': ')
        game_no = parse_ints(game_no)[0]
        winning_numbers, card_numbers = [set(parse_ints(x)) for x in game_data.split(' | ')]
        wins[game_no] = len(card_numbers.intersection(winning_numbers))

    cards = { x: 1 for x in wins }

    for card in cards:
        have_amount = cards[card]
        win_amount = wins[card]
        for i in range(card + 1, card + win_amount + 1):
            if i in cards: cards[i] += have_amount

    return sum(cards.values())


example_input_1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
challenge_input = Input(4)

assert(part_1(example_input_1) == 13)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 30)
print(f"Part 2: {part_2(challenge_input)}")
