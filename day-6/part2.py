# https://adventofcode.com/2022/day/6#part2

def isUnique(x, max):
    temp_stack = set([])
    for elem in x:
        temp_stack.add(elem)
    return (len(temp_stack) == max)


with open('/Users/ddaskal/git/advent-of-code-2022/day-6/input.txt') as input_file:
    q = []
    unique = False
    count = 0
    distinct = 14

    for line in input_file:
        while not unique:
            for char in line:
                count += 1

                # init queue
                if count <= distinct:
                    q.append(char)
                else:
                    # check if all four are unique
                    if isUnique(q, distinct):
                        unique = True
                        break
                    else:
                        q.pop(0)
                        q.append(char)

    print(count-1)
    # answer 3534
