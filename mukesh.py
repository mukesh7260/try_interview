l = [[54, 233, 67,43, 21, 19], [12, 45, 637,66 ,89], [90, 34, 233, 12]]

# Function to perform bubble sort on a list
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for arr in l:
    bubble_sort(arr)

print(l)