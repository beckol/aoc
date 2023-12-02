import re
import math

file1 = open('input.txt', 'r')
Lines = file1.readlines()

meta = {
    "green": 13,
    "red": 12,
    "blue": 14,
}

res_task_1 = 0
res_task_2 = 0

for line in Lines:
    valid = True
    matches = re.findall(r'Game (\d+):', line)

    game_id = int(matches[0])
    line = line.split(f"Game {game_id}: ")[1]
    round_split = line.split(";")

    max_keys = {key: 0 for key in meta.keys()}
    for round in round_split:
        for key, value in meta.items():
            matches = re.findall(fr'(\d+) {key}', round)
            matches = [int(match) for match in matches]

            if len(matches) > 0 and max_keys[key] < max(matches):
                max_keys[key] = max(matches)

            if sum(matches) > value:
                valid = False

    res_task_2 += math.prod(max_keys.values())
    if valid:
        res_task_1 += game_id

print(f"task1: {res_task_1}")
print(f"task2: {res_task_2}")
