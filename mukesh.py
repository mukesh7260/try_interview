class Summation():
    def sum(self,a=None ,b = None , c = None):
        if a != None and b !=None and c != None:
            return a + b + c 
        elif a !=None and b != None:
            return a +b 
        else:
            return a 

s = Summation()
print(s.sum(1,2,3))
print(s.sum(1,2))
print(s.sum(1))




class Summation:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def sum(self, a=None, b=None, c=None):
        # Use method arguments if provided, otherwise use instance attributes
        a = a if a is not None else self.a
        b = b if b is not None else self.b
        c = c if c is not None else self.c

        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        elif a is not None:
            return a
        else:
            return 0  # Optional: handle case where no value is provided

# Examples
s1 = Summation(1, 2, 3)
print(s1.sum())        # Output: 6 (uses values from __init__)
print(s1.sum(4, 5))    # Output: 9 (overrides init values with method args)
print(s1.sum(7))       # Output: 7

s2 = Summation()
print(s2.sum(1, 2, 3)) # Output: 6 (no init values, uses method args)
