
# Generator function 

def count_numbers():
    for i in range(1, 6):
        print(i)
        yield i

c = count_numbers()

print(next(c)) 


def count_numbers():
    for i in range(1, 6):
        yield i
c = count_numbers()
for num in c:
    print("Received:", num)


# When to Use Generator Functions

# | Scenario                         | Why a Generator Helps                                           |
# | -------------------------------- | --------------------------------------------------------------- |
# | ✅ **Large datasets**             | Avoids loading all data into memory at once                     |
# | ✅ **Infinite or long sequences** | You can generate items one by one without crashing your program |
# | ✅ **Streaming data**             | For real-time data (e.g., logs, sensor input, file streams)     |
# | ✅ **Performance optimization**   | Reduces memory usage and can make programs faster               |
# | ✅ **Custom iteration logic**     | Easier than writing a class with `__iter__` and `__next__`      |
