# https://adventofcode.com/2022/day/3
with open('/Users/ddaskal/git/advent-of-code-2022/day-3/input.txt') as input_file:
    total = 0

    for line in input_file:
        first, second = line[:len(line)//2], line[len(line)//2:]

        for letter in second:
            if letter in first:
                if letter == letter.upper():
                    total += ord(letter) - 64 + 26
                    break
                elif letter == letter.lower():
                    total += ord(letter) - 96
                    break
                else:
                    continue
            else:
                continue

    print(total)
    # answer 7746
