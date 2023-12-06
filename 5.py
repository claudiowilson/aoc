from input import get_split_input
import itertools
import math

TEST_CASE = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split('\n')

def has_mapping(mapping, num):
    for mappings in mapping:
        dest, source, range_len = mappings
        
        if source <= num < source + range_len:
            return mappings

    return None

def range_intersect(a, b):
    return range(max((a.start, b.start)), min((a.stop, b.stop)))

def has_mapping_two(mapping, num, num_end):
    num_len = num_end - num
    
    intersections = []
    dests = []
    for mappings in mapping:
        dest, source, range_len = mappings

        mapping_range = range(source, source + range_len)
        num_range = range(num, num + num_len)
         
        intersect = range_intersect(mapping_range, num_range)
        
        if len(intersect) == 0:
            continue
        
        intersections.append((intersect.start, intersect.stop))

        dest_start = dest + intersect.start - mapping_range.start
        dest_end = dest + intersect.stop - mapping_range.start

        # intersections.append((dest_start, dest_end))
        dests.append((dest_start, dest_end))
    
    num_range = range(num, num + num_len)

    if len(intersections) == 0:
        return [(num, num + num_len)]
    
    start = num_range.start
    end = num_range.stop
    print("BEFORE")
    print(intersections)
    for range_start, range_end in sorted(intersections, key=lambda x: x[0]):
        intersection = range(range_start, range_end)

        if intersection.start > num_range.start:
            dests.append((start, intersection.start))
            start = intersection.stop
        elif intersection.stop < num_range.stop:
            dests.append((intersection.stop, num_range.stop))
            end = intersection.stop
        else:
            print("AY")
    print("AFTER")
    print(dests)
    return dests

def get_mapping(mapping, num):
    mappings = has_mapping(mapping, num)

    if mappings:
        dest, source, range_len = mappings
        return (num - source) + dest

    return num

def solution():
    lines =  TEST_CASE #get_split_input(5)
    seeds_range = list(map(int, lines[0][lines[0].index(':') + 2:].split()))
    #seeds = list(range(seeds_range[0], seeds_range[1])) + list(range(seeds_range[1], seeds_range[2]))
    #print(seeds)
    #return
    #seeds = set(map(int, lines[0][lines[0].index(':') + 2:].split()))
    
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temp = []
    temp_to_humid = []
    humid_to_location = []
    
    curr = None
    for line in lines[1:]:
        if len(line) == 0:
            continue

        if line == "seed-to-soil map:":
            curr = seed_to_soil
            continue
        
        if line == 'soil-to-fertilizer map:':
            curr = soil_to_fertilizer
            continue

        if line == 'fertilizer-to-water map:':
            curr = fertilizer_to_water
            continue

        if line == 'water-to-light map:':
            curr = water_to_light
            continue

        if line == 'light-to-temperature map:':
            curr = light_to_temp
            continue

        if line == 'temperature-to-humidity map:':
            curr = temp_to_humid 
            continue

        if line == 'humidity-to-location map:':
            curr = humid_to_location 
            continue
            
        dest, source, range_len = map(int, line.split())

        curr.append([dest, source, range_len])
    
    lowest = math.inf
    for seed, seed_range in itertools.batched(seeds_range, 2):
        for soil, soil_end in has_mapping_two(seed_to_soil, seed, seed + seed_range):
            for fert, fert_end in has_mapping_two(soil_to_fertilizer, soil, soil_end):
                for water, water_end in has_mapping_two(fertilizer_to_water, fert, fert_end):
                    for light, light_end in has_mapping_two(water_to_light, water, water_end):
                        for temp, temp_end in has_mapping_two(light_to_temp, light, light_end):
                            for humid, humid_end in has_mapping_two(temp_to_humid, temp, temp_end):
                                for loc, loc_end in has_mapping_two(humid_to_location, humid, humid_end):
                                    lowest = min(lowest, loc)

    return lowest

    # soil_start, soil_end = has_mapping_two(seed_to_soil, 79, 93)
    # print(soil_start, soil_end)
    # fert_start, fert_end = has_mapping_two(soil_to_fertilizer, soil_start, soil_end)
    # print(fert_start, fert_end)
    # water_start, water_end = has_mapping_two(fertilizer_to_water, fert_start, fert_end)
    # print(water_start, water_end)
    # light_start, light_end = has_mapping_two(water_to_light, water_start, water_end)
    # print(light_start, light_end)
    # temp_start, temp_end = has_mapping_two(light_to_temp, light_start, light_end)
    # print(temp_start, temp_end)
    # humid_start, humid_end = has_mapping_two(temp_to_humid, temp_start, temp_end)
    # print(humid_start, humid_end)
    # location_start, location_end = has_mapping_two(humid_to_location, humid_start, humid_end)
    # print(location_start, location_end)

    # lowest = math.inf
    # for seed, seed_range in itertools.batched(seeds_range, 2):
        # print(f'SEEDS: {seed} {seed_range}')
        # soil_start, soil_end = has_mapping_two(seed_to_soil, seed, seed + seed_range)
        # print(soil_start, soil_end)
        # fert_start, fert_end = has_mapping_two(soil_to_fertilizer, soil_start, soil_end)
        # water_start, water_end = has_mapping_two(fertilizer_to_water, fert_start, fert_end)
        # light_start, light_end = has_mapping_two(water_to_light, water_start, water_end)
        # temp_start, temp_end  = has_mapping_two(light_to_temp, light_start, light_end)
        # humid_start, humid_end = has_mapping_two(temp_to_humid, temp_start, temp_end)
        # location_start, location_end = has_mapping_two(humid_to_location, humid_start, humid_end)
        # print(location_start, location_end)

         


print(solution())
