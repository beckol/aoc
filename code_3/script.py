import re
import math

file1 = open('input.txt', 'r')
Lines = file1.readlines()

lst_numbers = [[None for _ in range(len(Lines[0]) - 1)] for _ in range(len(Lines))]
lst_signs = [["" for _ in range(len(Lines[0]) - 1)] for _ in range(len(Lines))]
lst_signs_mult = [[[] for _ in range(len(Lines[0]) - 1)] for _ in range(len(Lines))]

res_task_1 = 0
res_task_2 = 0

for line_id in range(0, len(Lines)):
    line = Lines[line_id]
    line = line.replace("\n", "")
    # find numbers
    indices = [(m.start(), m.group()) for m in re.finditer(r'(\d+)', line)]
    for (start, number_str) in indices:
        lst_numbers[line_id][start] = number_str

    # find points
    indices = [(m.start(), m.group()) for m in re.finditer(r'[^0-9.]', line)]
    for (i, sign) in indices:
        lst_signs[line_id][i] = sign

for list_n_number_id in range(0, len(lst_numbers)):
    for list_i_number_id in range(0, len(lst_numbers[list_n_number_id])):
        number_str = lst_numbers[list_n_number_id][list_i_number_id]
        valid = False
        if number_str:
            from_i = list_i_number_id - 1
            to_i = list_i_number_id + len(number_str)
            from_n = list_n_number_id - 1
            to_n = list_n_number_id + 1
            for n in range(from_n, to_n + 1):
                for i in range(from_i, to_i + 1):
                    if i >= 0 and n >= 0 and n < len(lst_signs) and i < len(lst_signs[0]):
                        if lst_signs[n][i] != "":
                            valid = True

                            if lst_signs[n][i] == "*":
                                lst_signs_mult[n][i].append(int(number_str))
            if valid:
                res_task_1 += int(number_str)

for row_signs_mult in lst_signs_mult:
    for sign_mult in row_signs_mult:
        if len(sign_mult) == 2:
            res_task_2 += math.prod(sign_mult)

print(f"task_1: {res_task_1}")
print(f"task_2: {res_task_2}")