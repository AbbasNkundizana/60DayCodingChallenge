#Calculate BMI using user input
#BMI = Weight(kg)/ Height^2(m)
#Return and integer value 

weight = int(input('Enter your weight in kg: '))
height = float(input('Enter your height in meters: '))

BMI = weight / height**2

#print(f'BMI = {BMI}')

print(f'BMI = {int(BMI)}')
