def part_one(lines):
    pass

def get_dest_for_sources(lines, sources):
    res = [-1]*len(sources)
    for line in lines:
        dest_start, source_start, range_len = map(int, line.strip().split(' '))
        for i, source in enumerate(sources):
            if source in range(source_start, source_start + range_len):
                res[i] = dest_start + (source - source_start)

    for i, r in enumerate(res):
        if r == -1:
            res[i] = sources[i]
    print(res)
    return res

if __name__ == '__main__':
    with open('input') as reader:
        lines = reader.readlines()

        seeds = list(map(int, lines[0].strip().split(': ')[1].split(' ')))
        print(seeds)

        # hardcoding this for now
        seed_soil = lines[3:35]
        soil_fertilizer = lines[37:55]
        fertilizer_water = lines[57:105]
        water_light = lines[107:140]
        light_temp = lines[142:178]
        temp_humidity = lines[180:209]
        humidity_loc = lines[211:]

        chain = [seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temp, temp_humidity, humidity_loc]
        
        curr = seeds
        for map_lines in chain:
            curr = get_dest_for_sources(map_lines, curr)

        print(min(curr))