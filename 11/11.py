import re
from itertools import combinations
from bisect import bisect

def transpose(matrix):
    return [''.join([row[i] for row in matrix]) for i in range(len(matrix[0]))]

if __name__ == '__main__':
    with open('input') as reader:
        lines = reader.readlines()
        expanded_space = []

        ROWS = len(lines)
        COLS = len(lines[0].strip())

        empty_rows = []
        empty_cols = [ i for i in range(COLS) ]

        for row, line in enumerate(lines):
            digits = list(re.finditer('(#){1}', line))
            curr_line = list(line.strip())
            if len(digits) == 0:
                empty_rows.append(row)

            for d in digits:
                if d.span(0)[0] in empty_cols:
                    empty_cols.remove(d.span(0)[0])

        print(empty_rows)
        print(empty_cols)

        galaxies = {}
        curr_galaxy = 0
        expansion_factor = 1000000 - 1
        for row, line in enumerate(lines):
            digits = re.finditer('(#){1}', line)
            for d in digits:
                curr_galaxy += 1
                col = d.span(0)[0]
                new_row = row + (bisect(empty_rows, row) * expansion_factor)
                new_col = col + (bisect(empty_cols, col) * expansion_factor)
                galaxies[curr_galaxy] = (new_row, new_col)

        def shortest_path(g1, g2):
            return abs(galaxies[g1][0] - galaxies[g2][0]) + abs(galaxies[g1][1] - galaxies[g2][1])

        pairs = list(combinations(galaxies, 2))
        print(sum(shortest_path(pair[0], pair[1]) for pair in pairs))