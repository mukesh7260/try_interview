
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
            