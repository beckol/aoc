import re
import math

file1 = open('input.txt', 'r')
Lines = file1.readlines()

def calc_res(times, distances, task):
    res = []
    for time, distance in zip(times, distances):
        test = 0
        counter = 1
        for val in range(0, time-1, 2):
            bla = time-1 - val
            test += bla
            if test > distance:
                break
            counter += 1
        res.append(time - 2*counter + 1)

    print(f"{task}: {math.prod(res)}")

matches = re.findall(r'(\d+)', Lines[0])
times = [int(match) for match in matches]
matches = re.findall(r'(\d+)', Lines[1])
distances = [int(match) for match in matches]
calc_res(times, distances, "task_1")

matches = re.findall(r'(\d+)', Lines[0])
times = [int("".join(matches))]
matches = re.findall(r'(\d+)', Lines[1])
distances = [int("".join(matches))]
calc_res(times, distances, "task_2")