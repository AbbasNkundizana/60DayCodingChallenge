#allow user type in preferred password
# confirm that password
# if not a match, reprompt
#if reprompting is up to 3 times with still incorrect confirmations, kick user out

#get user's password
password = input("Enter Password: ")

#reprompt if there's mismatch
trials = 3
while True:
     #confirm password
    confirm_password = input("Confirm Password: ")
    
    #for max number of trials and if still not correct
    if trials == 0:
            if password != confirm_password:
                print(":( You've been kicked out :(")
                break
    
     #confirm password
    if password != confirm_password:
        print(f"< Password Incorrect >\nYou have {trials} more trial(s)")
        trials -= 1
        print()
    
    #log in was successful    
    else:
        print("<<< Login Successful >>>")
        break