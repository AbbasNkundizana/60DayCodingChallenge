#Define a same_first_and_last letter function that accepts a string as an argument
#The function should return a True if the first and last letter character are the same and False otherwise
#Assume the string will always have 1 or more characters

def same_first_and_last_letter(word):
    return word[0] == word[-1]


# Define a three_number_sum function that accepts a 3-character string as an argument
# The function should add up the sum of the digits of the string
# HINT: You 'll have to figure out a way to convert the string-ified numbers to intengers 

def three_number_sum_function(number):
    return int (number[0]) + int(number[1]) + int(number[2])