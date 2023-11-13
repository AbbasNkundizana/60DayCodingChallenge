#write a code such that if the user enters 1 it prints "one", 2 "two" 3 "three" 4 "four" otherwise "wrong number" and "Exit program"

number = int(input('Please Enter a number: '))
if number == 1:
    print('One')
elif number == 2:
    print('Two')
elif number == 3:
    print('Three')
elif number == 4:
    print('Four')
else:
    print('Wrong Number')
    print('Exit')



