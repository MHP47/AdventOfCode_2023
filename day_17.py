from utils import *


def part_1(p_Input):
    grid = Grid(rows = p_Input.strip().splitlines())
    for k,v in grid.items(): grid[k] = int(v)
    start = (0, 0)
    goal = (grid.width-1, grid.height-1)
    seen = {}
    frontier = [(0, start, 0, 1)] # heat_loss, position, direction, dir_steps
    adjacent = lambda x, y: ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)) # R D L U

    while frontier:
        loss, current, direction, steps = heappop(frontier)
        k = (current, direction, steps)
        if seen.get(k, BIG) <= loss: continue
        if current == goal: return loss
        seen[k] = loss
        neighbours = adjacent(*current)
        for d in [(direction - 1) % 4, direction, (direction + 1) % 4]:
            if d == direction and steps == 3: continue
            next_steps = steps + 1 if d == direction else 1
            if (neighbour := neighbours[d]) in grid and seen.get((neighbour, d, next_steps), loss + 1) > loss:
                heappush(frontier, (loss + grid[neighbour], neighbour, d, next_steps))


def part_2(p_Input):
    pass


example_input_1 = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""
challenge_input = Input(17)

assert(part_1(example_input_1) == 102)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
