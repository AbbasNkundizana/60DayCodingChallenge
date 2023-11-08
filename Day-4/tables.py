num = int(input('Enter Your number: '))
skip = int(input('Enter Your Skip number: '))
for x in range(1, 13):
    result = num * x
    if x == skip:
        break
    print(f'{num} x {x} = {result}')
   
   

