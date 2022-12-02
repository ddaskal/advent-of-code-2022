# https://adventofcode.com/2022/day/2

# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors),
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).


with open('/Users/ddaskal/git/advent-of-code-2022/day-2/input.txt') as input_file:
    guide = {"A": "Rock", "B": "Paper", "C": "Scissors",
             "X": "Rock", "Y": "Paper", "Z": "Scissors"}
    total = 0

    for line in input_file:
        opponent, me = line.split()[0], line.split()[1]

        if guide[opponent] == guide[me]:
            total += 3  # draw
            if guide[me] == "Rock":
                total += 1  # rock
            elif guide[me] == "Paper":
                total += 2  # paper
            elif guide[me] == "Scissors":
                total += 3  # scissors
            else:
                # magic
                pass
        elif guide[opponent] == "Rock" and guide[me] == "Paper":
            total += 2  # paper
            total += 6  # win
        elif guide[opponent] == "Rock" and guide[me] == "Scissors":
            total += 3  # scissors
            # lose
        elif guide[opponent] == "Paper" and guide[me] == "Rock":
            total += 1  # rock
            # lose
        elif guide[opponent] == "Paper" and guide[me] == "Scissors":
            total += 3  # scissors
            total += 6  # win
        elif guide[opponent] == "Scissors" and guide[me] == "Rock":
            total += 1  # rock
            total += 6  # win
        elif guide[opponent] == "Scissors" and guide[me] == "Paper":
            total += 2  # paper
            # lose
        else:
            # magic
            pass

print(total)
# answer 14297
