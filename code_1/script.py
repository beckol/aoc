import re

file1 = open('input.txt', 'r', encoding="utf-8")
Lines = file1.readlines()


def str_list_to_str(list):
    return_str = ""
    for s in list:
        return_str += str(s)
    return return_str


return_val = 0

meta = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


res_task_1 = 0
res_task_2 = 0

for line in Lines:
    matches = re.findall(r'(\d+)', line)
    text = str_list_to_str(matches)
    first_match_index = None
    second_match_index = None
    if len(text) > 0:
        first_match_index = line.find(text[0])
        first_char = text[0]
        second_match_index = line.rfind(text[-1])
        second_char = text[-1]
        res_task_1 += int(first_char + second_char)

    for key, val in meta.items():
        index = line.find(key)
        if index != -1 and (first_match_index == None or index < first_match_index):
            first_char = val
            first_match_index = index

        index = line.rfind(key)
        if index != -1 and (second_match_index == None or index > second_match_index):
            second_char = val
            second_match_index = index
    res_task_2 += int(first_char + second_char)


print(f"task1: {res_task_1}")
print(f"task2: {res_task_2}")
