# https://adventofcode.com/2022/day/5#part2
with open('/Users/ddaskal/git/advent-of-code-2022/day-5/input.txt') as input_file:
    init = True
    init_stacks = []
    build_stacks = []
    stacks = [[], [], [], [], [], [], [], [], []]
    tops = ""

    for line in input_file:
        if init:
            if line != '\n':
                # init stacks
                line = line.strip('\n')
                line += ' ' * (35 - len(line))
                init_stacks.append(line)
            elif line == '\n':
                # set up stacks proper
                init_stacks.pop()  # removes line with naming stacks
                build_stacks = init_stacks[:: -1]

                for entry in build_stacks:
                    if entry[1] != " ":
                        stacks[0].append(entry[1])
                    if entry[5] != " ":
                        stacks[1].append(entry[5])
                    if entry[9] != " ":
                        stacks[2].append(entry[9])
                    if entry[13] != " ":
                        stacks[3].append(entry[13])
                    if entry[17] != " ":
                        stacks[4].append(entry[17])
                    if entry[21] != " ":
                        stacks[5].append(entry[21])
                    if entry[25] != " ":
                        stacks[6].append(entry[25])
                    if entry[29] != " ":
                        stacks[7].append(entry[29])
                    if entry[33] != " ":
                        stacks[8].append(entry[33])

                init = False
                continue

        # perform moving logic
        if not init:
            temp_stack = []
            command = line.strip('\n').split(" ")
            count = int(command[1])
            source = int(command[3])-1
            target = int(command[5])-1

            for crate in range(count):
                temp_stack.append(stacks[source].pop())

            for box in range(len(temp_stack)):
                stacks[target].append(temp_stack.pop())

    for stack in stacks:
        tops += stack.pop()

    print(tops)
    # answer BLSGJSDTS
