#Define a first_three_characters function that accepts a string argument
#The function should return the first characters of the string 

def first_three_characters(alphabet):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[:3]


#Define a last_five_characters function that accepts a string argument
#The function should return the last five characters of the string

def _three_characters(alphabet):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[-5:]

#Define a is_palindrome function that accepts a string argument.
#The function should return True if the string is spelt
#the same way backwards as it is forwards
#Returns False otherwise
def is_palindrome(word):
    # Reversing the string using slicing and comparing it to the original string
    return word == word[::-1]

print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("level"))  # Output: True




