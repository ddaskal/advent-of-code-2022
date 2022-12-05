# https://adventofcode.com/2022/day/3#part2
with open('/Users/ddaskal/git/advent-of-code-2022/day-3/input.txt') as input_file:
    line_count = -1
    total = 0
    group = []
    compare = {}

    for line in input_file:
        line_count += 1

        if line_count % 3 == 0:
            # new group
            compare.clear()
            group.clear()
            group.append(line)
        elif line_count % 3 == 1:
            group.append(line)

        elif line_count % 3 == 2:
            # group is populated
            group.append(line)

            for letter in group[0]:
                if letter in group[1]:
                    compare[letter] = True

            for letter in group[2]:
                if letter in compare:
                    if letter == letter.upper():
                        total += ord(letter) - 64 + 26
                        break
                    elif letter == letter.lower():
                        total += ord(letter) - 96
                        break

    print(total)
    # answer 2604
