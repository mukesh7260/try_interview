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
