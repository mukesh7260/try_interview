
# Summary Table
# Feature	Shallow Copy	Deep Copy
# Copies outer object?	✅ Yes	✅ Yes
# Copies inner objects?	❌ No (same references)	✅ Yes (new objects)
# Module used	copy.copy()	copy.deepcopy()
# Use case	When nested objects are not being modified independently	When full independence is needed 

import copy 
original = [[1, 2], [3, 4]]
shallow = copy.copy(original) 
print(shallow)  
print(shallow)
print(original is shallow)  # False, different objects are created

# Modify the inner list
shallow[0][0] = 100

print("Original:", original)
print("Shallow Copy:", shallow)
# output : 

# Original: [[100, 2], [3, 4]]
# Shallow Copy: [[100, 2], [3, 4]]


# Deep copy example 

# original = [[1, 2], [3, 4]]
# deep = copy.deepcopy(original) 
# print(deep) 
# print(original)
# print(original is deep) 


# # Modify the inner list
# deep[0][0] = 100

# print("Original:", original)
# print("Deep Copy:", deep) # Now, modifying the inner list of the copy does not affect the original.

# output :
# Original: [[1, 2], [3, 4]]
# Deep Copy: [[100, 2], [3, 4]] 


# important point : - deep copy independent form original list but shallow copy is not independent from original list.
# shallow copy is used when nested objects are not being modified independently, while deep copy is used
# when full independence is needed.
# shallow copy is faster than deep copy because it does not create new objects for inner elements.
#