
n = int(input("How many numbers in the list: "))
a = []
for i in range(n):
    b = int(input(f"Enter element {i+1}: "))  # Convert input to int
    a.append(b)
    
    if len(a) >= 2:
        c = 3
        d = a[0]
        e = a[1]
        f = d + e
        if f == c:
            print(d, e)
        else:
            print(1)
