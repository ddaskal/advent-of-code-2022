# https://adventofcode.com/2022/day/1#part2

temp_cal = 0
winners = [0, 0, 0]


with open('/Users/ddaskal/git/advent-of-code-2022/day-1/input.txt') as input_file:
    for line in input_file:
        if line == '\n':
            temp_cal = 0
        else:
            temp_cal += int(line.rstrip())
            if temp_cal > min(winners):
                winners.append(temp_cal)
                winners.remove(min(winners))

print(sum(winners))
# answer 204639
