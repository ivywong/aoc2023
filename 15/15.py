from collections import defaultdict

def part_one(steps):
    value = 0
    for step in steps:
        value += hash(step)
    print(value)

def hash(step):
    curr = 0
    for c in step:
        curr += ord(c)
        curr = (curr * 17) % 256
    return curr

def part_two(steps):
    boxes = defaultdict(dict)
    for step in steps:
        if '-' == step[-1]:
            label = step[0:-1]
            box = hash(label)
            if box in boxes and label in boxes[box]:
                boxes[box].pop(label)
        else:
            label, focal = step.split('=')
            box = hash(label)
            boxes[box][label] = int(focal)

    focusing_power = 0
    for box in boxes:
        for i, (label, focal) in enumerate(boxes[box].items()):
            focusing_power += (1 + box) * (i + 1) * focal
    print(focusing_power)

if __name__ == '__main__':
    with open('input') as reader:
        lines = reader.readlines()
        steps = lines[0].strip().split(',')
    
        part_one(steps)
        part_two(steps)