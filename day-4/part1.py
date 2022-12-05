# https://adventofcode.com/2022/day/4
with open('/Users/ddaskal/git/advent-of-code-2022/day-4/input.txt') as input_file:
    total = 0

    for line in input_file:
        first = line.strip().split(',')[0]
        second = line.strip().split(',')[1]
        first_min = int(first.split('-')[0])
        first_max = int(first.split('-')[1])
        second_min = int(second.split('-')[0])
        second_max = int(second.split('-')[1])

        if first_min <= second_min and first_max >= second_max:
            total += 1
        elif first_min >= second_min and first_max <= second_max:
            total += 1

    print(total)
    # answer 424
