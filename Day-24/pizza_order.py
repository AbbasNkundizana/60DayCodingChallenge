#Write an autimatic pizza order program
# Small Pizza = 100
# Medium Pizza = 200
# Large Pizza = 300
#Pepperoni_small = 30
#Pepperoni_medium = 50
#Pepperoni_large = 50
# Extra cheese for any size Pizza = 20

pizza_size = input("What pizza size would you like to order? S/M/L?: ")

if pizza_size == 'S' or pizza_size == 's':
    bill = 100
    print(f"Your bill is {bill}Rs")
elif pizza_size == 'M' or pizza_size == 'm':
    bill = 200
    print(f"Your bill is {bill} Rs")
else:
    bill = 300
    print(f"Your bill is {bill}Rs")
    

pepperoni = input("Would you like pepperoni with your pizza?: Y/N: ")

if pepperoni == 'Y' or pepperoni == 'y':
    if pizza_size == 'S' or pizza_size == 's':
        bill += 30 
        print(f"Your bill is {bill}")
    elif pizza_size == 'M' or pizza_size == 'm':
        bill += 50 
        print(f"Your bill is {bill}")
    else:
        bill += 50 
        print(f"Your bill is {bill}")
else:
    print(f"Your bill is {bill}")

extra_cheese = input("Do you need extra cheese on your pizza?: Y/N: ")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 20
    print(f"Your bill is {bill}")
else:
    print(f"Your bill is {bill}")


    
