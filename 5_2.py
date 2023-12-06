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

def get_intersect(a, b):
    return range(max(a.start, b.start), min(a.stop, b.stop))

def get_intersections(source_range, num_range):
    intersect = get_intersect(source_range, num_range)

    if len(intersect) == 0:
        return [None, [num_range]]

    if intersect == num_range:
        return [intersect, []]

    ranges = []
    
    if intersect.start == num_range.start:
        return [intersect, [range(intersect.stop, num_range.stop)]]

    if intersect.stop == num_range.stop:
        return [intersect, [range(num_range.start, intersect.start)]]

    return [intersect, [range(num_range.start, intersect.start), range(intersect.stop, num_range.stop)]]



def get_transformed_range(dest, source_range, intersect):
    dest_start = dest + intersect.start - source_range.start
    dest_end = dest + intersect.stop - source_range.start
    return range(dest_start, dest_end)

def transform_mapping_to_ranges(mappings, current_range):
    transformed_ranges = []
    remaining = current_range
    
    mapped_ranges = list(map(lambda x: range(x[1], x[1] + x[2]), mappings))
    start, end = min(map(lambda x: x.start, mapped_ranges)), max(map(lambda x: x.stop, mapped_ranges))
    
    intersect, non_intersect = get_intersections(range(start, end), current_range)
    
    if not intersect:
        return non_intersect

    dests = []
    for dest, mapping_start, mapping_len in sorted(mappings, key=lambda x: x[1]):
        minor_intersect, herp = get_intersections(intersect, range(mapping_start, mapping_start + mapping_len))
        if minor_intersect:
            dests.append(get_transformed_range(dest, range(mapping_start, mapping_start + mapping_len), minor_intersect))

    return dests + non_intersect

def get_mapped_values(mappings, current_range):
    intersects = set()
    non_intersect = current_range

    for dest, source, source_len in mappings:
        source_range = range(source, source + source_len)
        intersect, non_intersects = get_intersections(source_range, current_range)

        if intersect:
            intersects.add(intersect)

    return intersects

def solution():
    lines = get_split_input(5)
    seeds_range = list(itertools.batched(map(int, lines[0][lines[0].index(':') + 2:].split()), 2))

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
    for seed_start, seed_range in seeds_range:
        for soil_range in transform_mapping_to_ranges(seed_to_soil, range(seed_start, seed_start + seed_range)):
            for fert_range in transform_mapping_to_ranges(soil_to_fertilizer, soil_range):
                for water_range in transform_mapping_to_ranges(fertilizer_to_water, fert_range):
                    for light_range in transform_mapping_to_ranges(water_to_light, water_range):
                        for temp_range in transform_mapping_to_ranges(light_to_temp, light_range):
                            for humid_range in transform_mapping_to_ranges(temp_to_humid, temp_range):
                                for loc_range in transform_mapping_to_ranges(humid_to_location, humid_range):
                                    lowest = min(loc_range.start, lowest)

    print(lowest)

solution()
