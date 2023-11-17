# Define a first_longer_than_second function that accepts two arguments.
# The function should return a True if the first string is longer than the second and
# and a False otherwise(including if they are equal in length).

def first_longer_than_second(word1, word2):
    return len(word1) > len(word2)

print(first_longer_than_second('Khart', 'Glasgow'))