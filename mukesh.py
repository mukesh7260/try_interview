n = int(input("how many no. of items for dictionary : ")) 
d = {}
for i in range(n):
    k = input("enter key: ")
    v = input("enter value : ") 
    d.update({k:v}) 
print(d) 