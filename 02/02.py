import re
from math import prod

def part_one(games):
    valid_games = [ id for id in games if is_possible(games[id])]
    print(sum(valid_games))

def part_two(games):
    powers = [ prod(get_min_cubes(games[id]).values()) for id in games ]
    print(sum(powers))

def is_possible(game):
    max_colors = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    for turn in game:
        for color in turn:
            if max_colors[color] < turn[color]:
                return False
    return True

def get_min_cubes(game):
    min_colors = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for turn in game:
        for color in turn:
            if min_colors[color] < turn[color]:
                min_colors[color] = turn[color]
    return min_colors

def set_to_dict(s):
    return { color: int(n) for n, color in s }

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

        games = {}
        for line in lines:
            id = int(re.search('Game (\d+):', line).group(1))
            set_pattern = re.compile(r'(\d+) (\w+),?\s?')
            games[id] = [ set_to_dict(set_pattern.findall(s)) for s in line.split('; ')]
        
        for gid in games:
            print(f"{gid}: {games[gid]}")
        
        part_one(games)
        part_two(games)