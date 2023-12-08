import re
from math import prod

def get_num_ways(race_len, record_dist):
    curr_ways = 0
    curr_speed = 0
    for i in range(race_len):
        if (race_len - i) * curr_speed > record_dist:
            curr_ways += 1
        curr_speed += 1
    return curr_ways

if __name__ == '__main__':
    with open('example') as reader:
        lines = reader.readlines()
        times = list(map(int, re.findall('\d+', lines[0])))
        dists = list(map(int, re.findall('\d+', lines[1])))
        print(times)
        print(dists)

        ways = []
        for race_len, record_dist in zip(times, dists):
            ways.append(get_num_ways(race_len, record_dist))
        print(ways)
        print(prod(ways))

        print(get_num_ways(int("".join(re.findall('\d+', lines[0]))), int("".join(re.findall('\d+', lines[1])))))