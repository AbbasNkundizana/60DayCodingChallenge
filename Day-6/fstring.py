#Write a program to calculate how many day, weeks and months we have left if we live until 90 years old
#Input = age
#Output = You have 'a' days, 'b' weeks and 'c' months left 
#Given that
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months 

#SOLUTION
age = int(input('Enter your current age: '))
years = 90 - age
months = years * 12
weeks = years * 52
days = years * 365

print(f'You have {days} days, {weeks} weeks and {months} months left')



