# PLD
# find the highest number but with the use of try and except block, for loop, and lists

def find_max(array):
    #assume the first number is the highest
    highest = array[0]

    for i in array[1::]:
        if i > highest:
            highest = i
    
    return highest

list_of_numbers = []
print("Enter 5 numbers and the program will find the highest number")
while len(list_of_numbers) != 5:
    try:
        user_input = int(input("Enter a number"))
        list_of_numbers.append(user_input)
    except ValueError:
        print("Error! Only enter numbers.")

print("The highest number is",find_max(list_of_numbers))