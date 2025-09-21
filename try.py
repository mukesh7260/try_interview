
# find largest number in the list without using bultin method and function 

l = [23,45,64,34,98,76]
lmax = l[3]
for i in range(len(l)):
    if l[i] > lmax:
        lmax = l[i]
print(lmax)



l = [23,65,45,98,75,35] 
for i in range(len(l)):
    for j in range(len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i] 
print(l)

        # Diamond shape 


n = int(input("enter number of rows : ")) 
for i in range(n+1):
    print('  '*(n-i) + ' *  '*i) 
for i in range(n-1, -1,-1):
    print('  '*(n-i) + ' *  '*i) 

import re 
s = input('Enter mobile number : ') 
f = re.match(r"(\+91|91|0)?[\s]?[7-9][0-9]{9}",s) 
if f: 
    print('valid') 
else: 
    print('invalid')


for i in range(1,1000):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break 
        else:
            print(i, end=' ')


#  program for reverse number 

n = int(input("enter any number : "))
sum = 0 
while n > 0:
        r = n % 10 
        sum = sum * 10 + r 
        n = n // 10 
print(sum)


n = int(input("enter any number !   ")) 
for i in range(n+1):
        if i % 2 == 0:
                print("buzz") 
        elif i % 2 == 1:
                print("fuzz")
        else:
                print('buzz fuzz')



n = int(input("Enter any number! "))
for i in range(n + 1):
    if i % 4 == 0:
        print("buzz fuzz")  # Special case for multiples of 4
    elif i % 2 == 0:
        print("buzz")
    else:
        print("fuzz")                


# DIAMOND SHAPE 


n = int(input("enter no. of rows !!  ")) 
for i in range(n+1):
    print('  '*(n-i) + ' *  '*i) 
for i in range(n-1, -1,-1):
    print('  '*(n-i) + ' *  '*i)



# triangle shape rotation 

n = int(input("enter no. of rows !!  ")) 
for i in range(n+1):
    print('  '*(n-i) + '* '*i) 
for i in range(n-1, -1,-1):
    print('  '*(n-i) + '* '*i)


n = int(input("enter no. of rows !!  ")) 
for i in range(n+1):
    print('* '*i) 
for i in range(n-1, -1,-1):
    print('* '*i)



# find maximum number in the list 


l = [23,65,45,98,75,35] 
d =l[-3]
for i in range(len(l)):
    if l[i] > d:
        d = l[i] 
print(d) 


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter a number: ")) 
print("The factorial of", n, "is", factorial(n)) 



n = int(input("enter any number !  ")) 
for i in range(1,11):
    a = n * i 
    print(n,"*",i,"=",a)



a = lambda a, b : a + b 
print(a(2,3))



import datetime 
from datetime import timedelta , date
t = date.today() + timedelta(days=10)
print(t) 


import random 
a = random.randint(000000,999999)
print(f'{a:06d}')


def kumar(mukesh):
    def abc():
        d = mukesh()
        e = d * 10000
        return e
    return abc
@kumar
        
def mukesh():
    a = 10 
    b = 20
    c = a + b 
#     print(c)
    return c 
m = mukesh()
print(m) 





s = 'rohit shrama'
v = ['a','e','i','o','u']
for i in s:
    if i in v:
        print('vowel',i)
    else:
        print('consonant',i)


s = 'rohit shrama'
v = ['a','e','i','o','u']
for i in s:
    if i in v:
        print('vowel',i) 
for i in s:
    if i not in v and i != ' ':
        print('consonant',i)
 



# method overloading example in python 

class Polymer:
    def abc(self , a= None, b = None,c = None):
       if a != None and b != None and c != None:
           return a + b + c
       elif a != None and b != None:
           return a + b
       else:
           return a 
       
p = Polymer()
print(p.abc(2,3,4))
print(p.abc(2,3))
print(p.abc(2))
print(p.abc())


n = int(input("entre how many number rows : ")) 
for i in range(n+1):
    print('  '*(n-i) + '* '*i) 
for i in range(n-1,-1,-1):
    print('  '*(n-i) + '* '*i) 




n = int(input("entre how many number rows : ")) 
for i in range(n+1):
    print('*'*(n-i)) 
for i in range(n-1,-1,-1): 
    print('*'*(n-i)) 



a = 10 
def add():
    global a
    a = 40  # change the value of global variable inside the function add()
    print(a)
    a = 20  # local variable 
    print(a) 
add() 




class Abcde:
    def __init__(self,a ,b):
        self.a = a 
        self.b = b 
        print(a)
        print(b)

a = Abcde(10,20)



class Abcde:
    def __init__(self,a ,b):
        print(a)
        print(b)
a = Abcde(10,20) 


class Abcd:
    def __init__(self):
        self.a = 10   # a ,b is instance variable . 
        self.b = 20   # instance method : - those function contains self as a parameter
        print(self.a)
        print(self.b)

a = Abcd()




class Computer:
    def abcd(self):
        print('I m fathor of computer ') 

class Laptop(Computer):
    def abc(self):
        print('I m child of computer') 

l = Laptop()
l.abc()
l.abcd()

count = 0 
for i in range(1,1000):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break 
        else:
            count = count + 1 
            print(i , end= ' ')   
          
print('total number of prime number : ' ,count) 




s = 'india is great' 
a = s.split()
b = a[::-1]
c = ' '.join(b)
print(c)


s = 'india is great'.split()
for  i in s:
    a = i[::-1]
    b = a.title()
    c = b[::-1]
    d = ''.join(c)
    print(d,end=' ')


# o/p : - indiA iS greaT 



s = 'patna is beautifull place'
a = s[::-1] 
b = a.title()
c = b[::-1]
print(c,end=' ') 


# #  patnA iS beautifulL placE



s = 'patna is beatiful place'.title()
print(s,end=' ') 


s = 'patna is beatiful place' 
v = ['a','e','i','o','u']       
vowcont = [] 
vconst = []
for i in s:
    if i in ' ':
        continue 
    elif i in v:
        vowcont.append(i)
        a = len(vowcont)
    else:
        vconst.append(i)
        b = len(vconst)
print(vowcont)
print(vconst)
print('vowel count :' ,a) 
print('conostant count : ' ,b)
 
a = 'hello world'
a = a[:6] + '*' + a[7:]
print(a)


s = 'hello world' 
a = s[:6] + '*' + s[7:]
print(a)

n = int(input("enter number of rows : ")) 
for i in range(n+1):
    print('  '*(n-i) + ' *  '*i) 
for i in range(n-1, -1,-1):
    print('  '*(n-i) + ' *  '*i) 

d1 = {'namee':'mukesh','ages':23,'places':'patna'}
d2 = {'namge':'rohit','agsse':25,'placess':'delhi'}
d2.update({'namge':'rohit sharma'})
d3 = {'namhe':'sharma','agesss':30,'placssse':'bihar'} 
d3.update({'namhe':'Virat Kohli'})
d = [d1,d2,d3]
print(d)
d3 = {'namhe':'sharma','agesss':30,'placssse':'bihar'} 
d3.update({'namhe':'Rohit sharma'})
print(d3) 


s = 'rohit sharam'
d = {}
for i in s:
    if i in ' ':
        continue 
    elif i in s:
        d[i] = s.count(i)
for k , v in d.items():
    print(f'{k} : {v}')



def mukesh(add):
    def kumar():
        d = add() 
        e = d * 1000 
        return e 
    return kumar 

@mukesh
def add():
    a  = 10 
    b = 20 
    c = a + b 
    return c 
a = add()
print(a)


#  print middle element in the list 

l = [1,2,3,4,5] 
mie_term  = len(l) // 2 
print(l[mie_term]) 


a = 15
print(a//2)     # print integer value 7.2 . so it take only 7. 
print(a/2)      # print float value 







# #   # find 3rd element in the list 

l = [34, 23, 45, 67, 89, 12, 98, 45, 34, 28, 76]

# Indexing starts from 0, so 4th element is at index 3
count = 0
for item in l:
    if count == 3:
        print("4th element is:", item)
        break
    count = count + 1 

n = int(input('how many no. of rows : ')) 
for i in range(n+1):
    print('  '*(n-i) + ' *  '*i) 
for i in range(n-1,-1,-1):
    print('  '*(n-i) + ' *  '*i)





l = [45,34,35,98,87,47,32,94] 
count = 0 
for i in l:
    if count == 5:
        print(f'5th element is : {i}') 
        break 
    count = count + 1




l = [34,65,47,98,76,23,45,67,89,12,34] 
count = 0 
for i in l:
    if count == 7:
        print(f'7th element is : {i}') 
        break 
    count = count + 1 




class Employee:
    def __init__(self,name ,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age) 

e = Employee('rikesh',34) 
e1 = Employee('rikesh',34) 
print(e == e1) 


d = {}
d[1] = 1 
d[True] = 2 
d[1.0] = 3 
# print(len(d)) 
print(d)

#       sort the element 

l = [23,43,21,35,46,25] 
for i in range(len(l)):
    for j in range(i):
        if l[i] < l[j]:
            l[i],l[j] = l[j],l[i]
print(l)  




def add():
    global a  # declare 'a' as global inside the function
    a = 24
    print(a)    # this will now act as a global variable

add()  
# a = 45      # call the function to set the global variable
print(a) 





n = int(input("Enter any number: ")) 

for i in range(n+1):
    if i % 2 == 0 and i % 3 == 0:
        print("buzz fuzz")       # divisible by 2 and 3
    elif i % 2 == 0:
        print("buzz")            # only divisible by 2
    elif i % 3 == 0:
        print("fuzz")            # only divisible by 3
    else:
        print(i)





n = 3456432 
sum = 0 
while n > 0 :
    r = n % 10 
    sum = sum * 10 + r 
    n = n // 10 
print(sum)



a = [i for i in range(10) if i % 2 == 0] 
print(a)  



a = list(filter(lambda i: i % 2 == 0, range(10))) # very important concept 
print(a)


# lambda function use for only short task and one line expression and not call lambda function anywhere as like def 

# Use lambda when you need a quick function for a small task — and don’t want to define a whole def block.
# A lambda function is an anonymous (unnamed) function that you define in one line. It can take any number of arguments but only has one expression.
# When not to use lambda:

# If the function is complex or has multiple lines → use def

# If you need to reuse the function in multiple places






with open("/home/mukesh/try/try.txt", "w") as f:
    content = f.write("mukesh kumar full stack developer  ")
    
with open("/home/mukesh/try/try.txt", "r") as f:
    content = f.read()
    print(content)






user_input = input("Enter text to save in file: ")
with open("/home/mukesh/try/try.txt", "w") as f:
    f.write(user_input)
print("Data written to try.txt successfully.")


print("Enter multiple lines (type 'exit' to stop):")
with open("/home/mukesh/try/try.txt", "w") as f:
    while True:
        line = input()
        if line.lower() == 'exit':
            break
        f.write(line + '\n')

print("All lines saved to file.")





# Best factorial example in python 

n = int(input('Enter any number ! ')) 
if n < 0:
    print('Factorial is not defined for negative numbers')
elif n == 0 or n == 1:
    print(1) 
else:
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    print(f'Factorial of {n} is : {fact}')




user_input = input("Enter text to save in file: ")
with open("E:/try/try.txt", "w") as f:
    f.write(user_input)
print("Data written to try.txt successfully.") 





l = [[54,233,21,197] , [152,45,637,89] , [90,934,233,12]]
for sublist in l:
    sublist.sort()

print(l)



l = [[54, 233, 67,43, 21, 19], [12, 45, 637,66 ,89], [90, 34, 233, 12]]

# Function to perform bubble sort on a list
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Sort each sublist
for arr in l:
    bubble_sort(arr)

print(l)



l = [23,43,65,45,87,52,16 ,[76,43,27]]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i] < l[j]:
            l[i] , l[j] = l[j],l[i] 
print(l)




l = [[54, 233, 21, 19], [12, 45, 637, 89], [90, 34, 233, 12]]

# Sort each sublist using inline bubble sort (no function)
for arr in l:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(l)




# Methood overloading examle in python 

class Cricket:
    def sum(self,a = None, b = None, c = None):
        if a != None and b != None and c != None:
            return a + b + c 
        elif a != None and b != None:
            return a + b 
        elif a != None:
            return a 
        else:
            return 0 
c = Cricket() 
print(c.sum(2,3,4)) 
print(c.sum(2,3)) 
print(c.sum(2)) 
print(c.sum())



# comprehension list using of lambda 

# l = lambda : [i for i in range(10) if i % 2 == 0] 
# print(l()) 



a = lambda b ,c : b + c 
print(a(2,3)) 