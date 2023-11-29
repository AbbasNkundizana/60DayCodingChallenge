#Write an autimatic pizza order program
# Small Pizza = 100
# Medium Pizza = 200
# Large Pizza = 300
# Pepperoni for small Pizza = 30
# Pepperoni for medium or large pizza = 50
# Extra cheese for any size Pizza = 20

pizza = input("Enter size of Pizza (small, medium, large): ").lower()
small = 100
medium = 200
large = 300

peppsmall = 30
peppmedium = 50
pepplarge = 50

cheese = 20

if pizza == "small":
    total_bill = small
elif pizza == "medium":
    total_bill = medium
else:
    total_bill = large

pepp = input("Enter pepperoni size (small, medium, large): ").lower()

if pepp == small:
    total_bill += peppsmall
else:
    total_bill += peppmedium #medium and large have similar price
    
cheese_input = input("Do you need extra cheese? (yes/no): ").lower()

if cheese_input == "yes":
    total_bill += cheese

print(f"Your total pizza bill is {total_bill}")



