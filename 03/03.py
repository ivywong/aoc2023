import re
from collections import defaultdict
from math import prod

DIRECTIONS = [
    (0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)
]

def part_one(symbols_dict, digits_dict):
    part_sum = sum(digits_dict[num_pos] for num_pos in digits_dict if has_neighboring_symbol(num_pos, symbols_dict))
    print(f"part 1: {part_sum}")

def has_neighboring_symbol(num_pos, symbols_dict):
    num_row, num_start, num_end = num_pos

    visited = set()
    for num_col in range(num_start, num_end):
        visited.add((num_row, num_col))
        for dr, dc in DIRECTIONS:
            neighbor = num_row + dr, num_col + dc
            if neighbor not in visited and neighbor in symbols_dict:
                return True
            visited.add(neighbor)
    return False

def part_two(symbols_dict, digits_dict):
    gears_to_nums = defaultdict(set)
    for num_pos in digits_dict:
        add_to_neighboring_gears(num_pos, digits_dict[num_pos], symbols_dict, gears_to_nums)

    ratio_sum = sum(prod(gears_to_nums[gear]) for gear in gears_to_nums if len(gears_to_nums[gear]) == 2)
    print(f"part 2: {ratio_sum}")

def add_to_neighboring_gears(num_pos, num, symbols_dict, gears_to_nums):
    num_row, num_start, num_end = num_pos

    visited = set()
    for num_col in range(num_start, num_end):
        visited.add((num_row, num_col))
        for dr, dc in DIRECTIONS:
            neighbor = num_row + dr, num_col + dc
            if neighbor not in visited and neighbor in symbols_dict and symbols_dict[neighbor] == '*':
                gears_to_nums[neighbor].add(num)
            visited.add(neighbor)

if __name__ == '__main__':
    with open('input') as reader:
        lines = reader.readlines()

        symbols = re.compile(r"[*/=+%@#&\-$]")
        symbols_dict = {}
        for row, line in enumerate(lines):
            for match in re.finditer(symbols, line):
                char_idx = match.span()[0]
                symbols_dict[row, char_idx] = match.group()
        
        digits_dict = {}
        digits = re.compile(r"\d+")
        for row, line in enumerate(lines):
            for match in re.finditer(digits, line):
                num_start = match.span()[0]
                num_end = match.span()[1]
                digits_dict[row, num_start, num_end] = int(match.group())
        
        part_one(symbols_dict, digits_dict)
        part_two(symbols_dict, digits_dict)
