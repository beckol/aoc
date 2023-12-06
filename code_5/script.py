file1 = open('input.txt', 'r')
Lines = file1.readlines()

res_task_1 = 0
res_task_2 = 0
seeds = [int(e) for e in Lines[0][7:].split(" ")]

rules_seed_to_soil = []
rules_soil_to_fertilizer = []
rules_fertilizer_to_water = []
rules_light_to_temperature = []
rules_water_to_light = []
rules_temperature_to_humidity = []
rules_humidity_to_location = []

def read_input(Lines):
    line_id = 1
    while Lines[line_id] != "\n":
        line = Lines[line_id]
        rules_seed_to_soil.append([int(e) for e in line.split(" ")])
        line_id += 1

    line_id += 2
    while Lines[line_id] != "\n":
        line = Lines[line_id]
        rules_soil_to_fertilizer.append([int(e) for e in line.split(" ")])
        line_id += 1

    line_id += 2
    while Lines[line_id] != "\n":
        line = Lines[line_id]
        rules_fertilizer_to_water.append([int(e) for e in line.split(" ")])
        line_id += 1

    line_id += 2
    while Lines[line_id] != "\n":
        line = Lines[line_id]
        rules_water_to_light.append([int(e) for e in line.split(" ")])
        line_id += 1

    line_id += 2
    while Lines[line_id] != "\n":
        line = Lines[line_id]
        rules_light_to_temperature.append([int(e) for e in line.split(" ")])
        line_id += 1

    line_id += 2
    while Lines[line_id] != "\n":
        line = Lines[line_id]
        rules_temperature_to_humidity.append([int(e) for e in line.split(" ")])
        line_id += 1

    line_id += 2
    while Lines[line_id] != "\n":
        line = Lines[line_id]
        rules_humidity_to_location.append([int(e) for e in line.split(" ")])
        line_id += 1

        if line_id >= len(Lines):
            break



def calc_dest_by_rule(number, rules, last_min, print_rules):
    last_min_for_this = -1
    for rule in rules:
        if rule[1] <= number <= rule[1] + rule[2]:
            if (rule[1] + rule[2] - number) < last_min or last_min == -1:
                last_min = rule[1] + rule[2] - number
            if print_rules:
                print((number - rule[1]) + rule[0])
            return (number - rule[1]) + rule[0], last_min
        if (last_min_for_this == -1 or 0 <= rule[1] - number < last_min_for_this) and 0 <= rule[1] - number:
            last_min_for_this = rule[1] - number

    if last_min_for_this != -1 and (last_min_for_this < last_min or last_min == -1):
        last_min = last_min_for_this
    return number, last_min


read_input(Lines[2:])

def calc_location(seed, print_rules):
    soil, last_min = calc_dest_by_rule(seed, rules_seed_to_soil, -1, print_rules)
    fertilizer, last_min = calc_dest_by_rule(soil, rules_soil_to_fertilizer, last_min, print_rules)
    water, last_min = calc_dest_by_rule(fertilizer, rules_fertilizer_to_water, last_min, print_rules)
    light, last_min = calc_dest_by_rule(water, rules_water_to_light, last_min, print_rules)
    temperature, last_min = calc_dest_by_rule(light, rules_light_to_temperature, last_min, print_rules)
    humidity, last_min = calc_dest_by_rule(temperature, rules_temperature_to_humidity, last_min, print_rules)
    location, last_min = calc_dest_by_rule(humidity, rules_humidity_to_location, last_min, print_rules)
    return location, last_min

locations = []
for seed in seeds:
    locations.append(calc_location(seed, False)[0])
print(f"res_task_1: {min(locations)}")
locations = []

location = -1
for i in range(0, len(seeds), 2):
    print(f"{int(i/2)+1}/{len(seeds)/2}")

    seed_id = seeds[i]
    while seed_id < seeds[i]+seeds[i+1]:
        location_new, last_min = calc_location(seed_id, False)

        if location == -1 or location_new < location:
            location = location_new
        seed_id += 1

        if last_min > 0:
            seed_id += last_min - 1
print(f"res_task_2: {location}")