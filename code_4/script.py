file1 = open('input.txt', 'r')
Lines = file1.readlines()

res_task_1 = 0
res_task_2 = 0

correct_number_lines = [0 for _ in range(len(Lines))]
correct_number_lines_2 = [1 for _ in range(len(Lines))]

for line in Lines:
    line_split = line.split(":")
    game_id = int(line_split[0][4:].replace(" ", ""))
    line_split = line_split[1].split("|")
    numbers = [int(e) for e in line_split[0].split(" ") if e != ""]
    winning_numbers = [int(e) for e in line_split[1].split(" ") if e != ""]

    correct_numbers = [number for number in numbers if number in winning_numbers]

    if len(correct_numbers) != 0:
        res_task_1 += 2**(len(correct_numbers) - 1)
        for i in range(game_id-1, game_id+len(correct_numbers)-1):
            correct_number_lines[game_id-1]=len(correct_numbers)

for i in range(0, len(correct_number_lines)):
    correct_number = correct_number_lines[i]

    if correct_number > 0:
        for k in range(i+1, i+correct_number+1):
            correct_number_lines_2[k] += correct_number_lines_2[i]

print(f"task1: {res_task_1}")
print(f"task2: {sum(correct_number_lines_2)}")