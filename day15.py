

# initialise parameters
numbers_spoken_original = [19, 0, 5, 1, 10, 13]
number_turns = 30000000

# fill dictionary with numbers spoken and what turn they were spoken
# remember turns start at 1, not 0
numbers_spoken_and_last_turn_spoken = {}
for i, number in enumerate(numbers_spoken_original):
    turn = i + 1
    numbers_spoken_and_last_turn_spoken[number] = turn

# initialise last number spoken and number turns so far
last_number_spoken = numbers_spoken_original[-1]
turn_to_follow = numbers_spoken_and_last_turn_spoken[last_number_spoken] + 1

# remove last number spoken from dictionary
numbers_spoken_and_last_turn_spoken.pop(last_number_spoken)




# loop over subsequent turns
for turn in range(turn_to_follow, number_turns+1):

    # if last number spoken not in dictionary, next number to speak will be 0
    if last_number_spoken not in numbers_spoken_and_last_turn_spoken.keys():
        number_to_speak = 0

    # else number to speak is difference between the turn number when it was last spoken 
    # (the previous turn) and the turn number of the time it was most recently spoken before then        
    else:
        number_to_speak = (turn - 1) - numbers_spoken_and_last_turn_spoken[last_number_spoken]

    # update dictionary with the last number spoken and its turn (previous turn)
    numbers_spoken_and_last_turn_spoken[last_number_spoken] = turn - 1

    # as at end of loop, set last number spoken to the number that was spoken
    last_number_spoken = number_to_speak

    if turn == 2020:
        print('PART 1 LAST NUMBER SPOKEN =', last_number_spoken)

print('PART 2 LAST NUMBER SPOKEN =', last_number_spoken)
