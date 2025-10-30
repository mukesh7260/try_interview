s = "rohit sharma"

for letter in s:
    print(letter, "-", s.count(letter))

 # or secont method 

s = "rohit sharma".replace(" ", "")

for letter in set(s):
    print(letter, "-", s.count(letter))
