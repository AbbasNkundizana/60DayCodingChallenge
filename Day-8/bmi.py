weight = float(input('weight (in Kg): '))
height = float(input('height in (meters): '))
BMI = weight/height**2

print(f'Your BMI is {BMI}')

if BMI < 16.0:
    print('You are Underweight(Severe thinness)')
elif 16.0 <= BMI < 16.9:
    print('You are Underweight(Moderate thinness)')
elif 17.0 <= BMI < 18.4:
    print('You are Underweight(Mild thinness)')
elif 18.5 <= BMI < 24.9:
    print('You are in Normal range')
elif 25.0 <= BMI < 29.9:
    print('You are Overweight(Pre-obese)')
elif 30.0 <= BMI < 34.9:
    print('You are Obese(Class I)')
elif 35.0 <= BMI < 39.9:
    print('You are Obese(Class II)')
else:
    print('You are Obese(Class III)')




