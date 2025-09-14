n = int(input('Enter any number ! ')) 
if n < 0:
    print('Factorial is not defined for negative numbers')
elif n == 0 or n == 1:
    print(1) 
else:
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    print(f'Factorial of {n} is : {fact}')  #