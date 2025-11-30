s = input("Enter any string : ")
a = s.replace(" ", "") 
for letter in set(a):
    print(letter ,"- " ,  a.count(letter))


              