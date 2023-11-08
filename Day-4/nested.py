# n = int(input('Enter a number for the multiples: '))
# for i in range(1, 13):
#     print(f'Multiplication Table for {i}')
#     for j in range(1, 13):
#         result = i * j
#         print(f'{i} x {j} = {result}')
#     print()
    

n = int(input('Enter a number for the multiples: '))
for i in range(1, n+1):
    for j in range(1, 13):
        result = i * j
        print(f'{i} x {j} = {result}')