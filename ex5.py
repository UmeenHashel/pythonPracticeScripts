import random

a = []
b = []

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in range(10):
    a.append(random.randint(1, 10))

for i in range(15):
    b.append(random.randint(1, 15))

print(a)
print(b)

n = []

for element in a:
    if element in b:
        n.append(element)

print(n)