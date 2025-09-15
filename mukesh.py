n = int(input("Enter any number  : ")) 
if n < 0 : 
    print("Factorial does not exist for negative numbers" ) 
elif n == 1 or n == 0 : 
    print(f'factorial of {n} is : 1' )
else: 
    fact = 1 
    for i in range(2, n + 1): 
        fact = fact * i 
    print(f'Factorial of {n} is : {fact}') 



