import os
import requests
import re
import itertools
import operator
import math
from collections import defaultdict, deque, Counter
from pprint import pprint
from copy import deepcopy, copy
from heapq import heappop, heappush
from functools import reduce
# try:
#         from aocd import data,lines
# except:
#         pass

BIG = 10 ** 999
alphabet = 'abcdefghijklmnopqrstuvwxyz'
cat = ''.join
# 2-D points implemented using (x, y) tuples
def X(p_Point): return p_Point[0]
def Y(p_Point): return p_Point[1]
COOKIE = None
COOKIE_FILE = "cookie.txt"

flatten = lambda l: [item for sublist in l for item in sublist]

# Enum def
def enum(**enums):
        return type('Enum', (), enums)


def input_download(p_Day, p_Filename):
        "Download the input for a day"
        global COOKIE
        if not COOKIE:
            with open(COOKIE_FILE, 'r') as f:
                COOKIE = f.read().strip()
        with open(p_Filename, "w") as f:
                l_Request = requests.get('https://adventofcode.com/2023/day/%s/input' % p_Day, 
                        headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                                'Accept-Language': 'en-US,en;q=0.5',
                                'Cache-Control': 'max-age=0',
                                'Connection': 'keep-alive',
                                'Cookie': 'session=' + COOKIE,
                                'Upgrade-Insecure-Requests': '1',
                                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'})
                l_Request.raise_for_status()
                f.write(l_Request.text)


def Input(p_Day):
        "Open this day's input file."
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input_files/input{}.txt'.format(p_Day))
        try:
                return open(filename).read()
        except:
                input_download(p_Day, filename)
                return open(filename).read()


def iterative_levenshtein(s, t, costs=(1, 1, 1)):
        """
                iterative_levenshtein(s, t) -> ldist
                ldist is the Levenshtein distance between the strings
                s and t.
                For all i and j, dist[i,j] will contain the Levenshtein
                distance between the first i characters of s and the
                first j characters of t

                costs: a tuple or a list with three integers (d, i, s)
                           where d defines the costs for a deletion
                                         i defines the costs for an insertion and
                                         s defines the costs for a substitution
                Code taken from here: https://www.python-course.eu/levenshtein_distance.php
        """
        rows = len(s)+1
        cols = len(t)+1
        deletes, inserts, substitutes = costs

        dist = [[0 for x in range(cols)] for x in range(rows)]
        # source prefixes can be transformed into empty strings
        # by deletions:
        for row in range(1, rows):
                dist[row][0] = row * deletes
        # target prefixes can be created from an empty source string
        # by inserting the characters
        for col in range(1, cols):
                dist[0][col] = col * inserts

        for col in range(1, cols):
                for row in range(1, rows):
                        if s[row-1] == t[col-1]:
                                cost = 0
                        else:
                                cost = substitutes
                        dist[row][col] = min(dist[row-1][col] + deletes,
                                                                 dist[row][col-1] + inserts,
                                                                 dist[row-1][col-1] + cost) # substitution

        return dist[row][col]


def neighbors4(p_Point):
        "The four neighbors (without diagonals)."
        x, y = p_Point
        return ((x+1, y), (x-1, y), (x, y+1), (x, y-1))


def neighbors8(p_Point):
        "The eight neighbors (with diagonals)."
        x, y = p_Point
        return ((x+1, y), (x-1, y), (x, y+1), (x, y-1),
                        (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1))

def cityblock_distance(p, q=(0, 0)):
        "City block distance between two points."
        return abs(X(p) - X(q)) + abs(Y(p) - Y(q))

def parse_ints(p_Inpt):
        "All the integers anywhere in text."
        return list(map(int, re.findall(r'-?\d+', p_Inpt)))

def astar_search(start, h_func, moves_func):
        "Find a shortest sequence of states from start to a goal state (a state s with h_func(s) == 0)."
        frontier  = [(h_func(start), start)] # A priority queue, ordered by path length, f = g + h
        previous  = {start: None}  # start state has no previous state; other states will
        path_cost = {start: 0}     # The cost of the best path to a state.
        while frontier:
                (f, s) = heappop(frontier)
                if h_func(s) == 0:
                        return Path(previous, s)
                for s2 in moves_func(s):
                        new_cost = path_cost[s] + 1
                        if s2 not in path_cost or new_cost < path_cost[s2]:
                                heappush(frontier, (new_cost + h_func(s2), s2))
                                path_cost[s2] = new_cost
                                previous[s2] = s
        return dict(fail=True, front=len(frontier), prev=len(previous))

def Path(previous, s):
        "Return a list of states that lead to state s, according to the previous dict."
        return ([] if (s is None) else Path(previous, previous[s]) + [s])

def mul_reduce(p_List):
        return reduce((lambda x, y: x * y), p_List)

def add_reduce(p_List):
        return reduce((lambda x, y: x + y), p_List)

def sub_reduce(p_List):
        return reduce((lambda x, y: x - y), p_List)

def lcm(*p_List):
  return reduce(lambda n, lcm: lcm * n // math.gcd(lcm, n), p_List)

def doesContainB(a, b, c):
    """
    In an infinite sequence, A is the first number, C is the common difference
    check if the number B will appear in the sequence or not
    """
    if (a == b):
        return True
    if ((b - a) * c > 0 and (b - a) % c == 0):
        return True
    return False

class Grid(dict):
    """A 2D grid, implemented as a mapping of {(x, y): cell_contents}."""
    def __init__(self, mapping=(), rows=()):
        """Initialize with, e.g., either `mapping={(0, 0): 1, (1, 0): 2, ...}`,
        or `rows=[(1, 2, 3), (4, 5, 6)]."""
        self.update(mapping if mapping else
                    {(x, y): val
                     for y, row in enumerate(rows)
                     for x, val in enumerate(row)})
        self.width  = max(x for x, y in self) + 1
        self.height = max(y for x, y in self) + 1

    def copy(self): return Grid(self)

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self[(x,y)], end='')
            print()
        print()

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
