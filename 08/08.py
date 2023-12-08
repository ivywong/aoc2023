import re
from math import lcm

def part_one(lines: list[str]):
    steps = lines[0].strip()

    nodes = {}
    for i in range(2, len(lines)):
        node, l, r = re.findall('\w+', lines[i])
        nodes[node] = {'L': l, 'R': r}
    
    # print(nodes)

    curr = 'AAA'
    step_count = 0
    while curr != 'ZZZ':
        for step in steps:
            if curr == 'ZZZ':
                break
            curr = nodes[curr][step]
            step_count += 1
    print(step_count)

def part_two(lines: list[str]):
    steps = lines[0].strip()

    nodes = {}
    start_nodes = set()
    end_nodes = set()
    for i in range(2, len(lines)):
        node, l, r = re.findall('\w+', lines[i])
        nodes[node] = {'L': l, 'R': r}
        if node[2] == 'A':
            start_nodes.add(node)
        elif node[2] == 'Z':
            end_nodes.add(node)
    
    # print(nodes)
    print(start_nodes, end_nodes)

    req_steps = []
    for n in start_nodes:
        curr = n
        total_steps = 0
        while curr not in end_nodes:
            curr = nodes[curr][steps[total_steps % len(steps)]]
            total_steps += 1
        print(n, total_steps)
        req_steps.append(total_steps)

    print(lcm(*req_steps))

if __name__ == '__main__':
    with open('input') as reader:
        lines = reader.readlines()

        part_one(lines)
        part_two(lines)
        