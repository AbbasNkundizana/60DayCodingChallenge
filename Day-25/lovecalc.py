#Write a python program that calculates the compatibilty of two individuals in love basing on characters of both their names 

#Store both names in two separate variables
name1 = input("What is your name?: ")
name2 = input("What is his/her name?: ")

#Concatenate the names to have one string
combined_names = name1 + name2

#Convert the string of names to lower case
full_names = combined_names.lower()

#Count the characters within the full names that cancels out the characters 'TRUE LOVE'
t = full_names.count("t")
r = full_names.count("r")
u = full_names.count("u")
e = full_names.count("e")
true = t + r + u + e

l = full_names.count("l")
o = full_names.count("o")
v = full_names.count("v")
e = full_names.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))
if love_score < 10 and love_score > 90:
    print(f"Your love score is {love_score} and you go together like coke and mentos! DONT LET GO")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score} and you are alright together! HUNG IN THERE")
else:
    print(f"Your love score is {love_score}")
