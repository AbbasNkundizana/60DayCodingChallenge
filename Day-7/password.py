# Print out a python program that allows a user to create password and confirm the password.
# if the input in the create password does not match the confirm password, the program should print out "passwords do not match.
# please try again" and prompt the user to enter the password again.
# The program should only allow the user to enter the password 3 times. if the user enters the wrong password 3 times,
# the program should print out "maximum attempts reached. please re-start again" and exit the program.
# if the user enters the correct password, the program should print out "password created successfully!" and return the password. 

password1 = input('Create Password: ')
password2 = input('Confirm Password: ')
attempts = 3

if password1 == password2:
    print('Password created successfully')
else:
    while attempts > 0:
        print('Passwords do not match')
        password2 = input('Please try again: ')
        attempts -= 1 

        if attempts == 1:
            print('maximum attempts reached. please re-start again" and exit the program')
            break
        
        if password1 == password2:
            print('Password created successfully')
            break
            
        






    



            