# Make a set A which is all the even numbers from 1 to 100. Also
# make a set B which is the multiples of 3 (1 to 100)
# A = {2, 4, 6, 8,......,100}
# B = {3, 6, 9, 12, 15,......,99}
# Calculate A intersection  B
# Hint: Use a loop

A = set()
B = set()
for x in range(1,101):
    if x%2 == 0:
        A.add(x)
    print(A)

for z in range(1,101):
    if z%3 == 0:
        B.add(z)
    print(B)
