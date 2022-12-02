# https://adventofcode.com/2022/day/1

max_calories = 0
temp_cal = 0


with open('/Users/ddaskal/git/advent-of-code-2022/day-1/input.txt') as input_file:
    for line in input_file:
        if line == '\n':
            temp_cal = 0
        else:
            temp_cal += int(line.rstrip())
            if temp_cal > max_calories:
                max_calories = temp_cal

print(max_calories)
# answer 71124
