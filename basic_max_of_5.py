# PLD
# find the highest number given 5 numbers using only if statementsre

def find_max(num_1,num_2,num_3,num_4,num_5):
    # assume the first number is the highest
    highest_num = num_1

    # then compare to the next numbers
    if num_2 > highest_num:
        highest_num = num_2

    if num_3 > highest_num:
        highest_num = num_3
    
    if num_4 > highest_num:
        highest_num = num_4

    if num_5 > highest_num:
        highest_num = num_5

    return highest_num

