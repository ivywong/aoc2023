def part_one(lines):
    MAX_ROWS = len(lines)
    MAX_COLS = len(lines[0].strip())
    rocks = {}
    for c in range(MAX_COLS):
        next_space = 0
        for r in range(MAX_ROWS):
            if lines[r][c] == '#':
                next_space = r + 1
            if lines[r][c] == 'O':
                rocks[c, next_space] = rocks.get(next_space, 0) + 1
                next_space += 1
    
    total_load = 0
    for c, r in rocks:
        total_load += MAX_ROWS - r
    print(rocks)
    print(total_load)

if __name__ == '__main__':
    with open('input') as reader:
        lines = reader.readlines()

        part_one(lines)
