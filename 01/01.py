def part_one(lines):
    sum = 0
    for line in lines:
        nums = [ c for c in line if c.isdigit() ]
        calibration = nums[0] + nums[-1]
        sum += int(calibration)
        print(f"{line.strip()} = calibration: {calibration}")
    
    print(f"final sum part 1: {sum}")

def part_two(lines):
    sum = 0
    for line in lines:
        l = line.strip()
        first = get_first_digit(l)
        last = get_last_digit(l)

        calibration = first + last
        sum += int(calibration)
        print(f"{line.strip()} = calibration: {calibration}")
    
    print(f"final sum part 2: {sum}")

def get_first_digit(l):
    for idx in range(len(l)):
        s = get_num_at_idx(l, idx)
        if s != '':
            return s
    return ''

def get_last_digit(l): 
    for idx in range(len(l) - 1, -1, -1):
        s = get_num_at_idx(l, idx, reverse=True)
        if s != '':
            return s
    return ''

def get_num_at_idx(line: str, idx: int, reverse=False) -> str:
    if line[idx].isdigit():
        return line[idx]
    
    DIGITS = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    if not reverse:
        for d in DIGITS:
            end_idx = idx + len(d)
            if end_idx <= len(line) and line[idx:end_idx] == d:
                return DIGITS[d]
    else:
        for d in DIGITS:
            start_idx = idx - len(d) + 1
            if start_idx >= 0 and line[start_idx:idx+1] == d:
                return DIGITS[d]
    return ''

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    
        part_one(lines)
        part_two(lines)