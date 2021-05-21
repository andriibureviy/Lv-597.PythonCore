num1 = int(input('Enter u num:'))

factorial = 1

for item in range(1, num1):
    factorial = (factorial * item) + (factorial * 1)

print(f'Your factorial  {num1} is: {factorial}!')