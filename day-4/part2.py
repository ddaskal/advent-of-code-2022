# https://adventofcode.com/2022/day/4#part2
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
        else:

            if first_min <= second_min:
                if first_max < second_min:
                    continue
                else:
                    total += 1
            elif second_min <= first_min:
                if second_max < first_min:
                    continue
                else:
                    total += 1

    print(total)
    # answer 804
