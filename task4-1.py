import math

# task 1
for x in range (6):
            if x >= 1: print (x)

# task 2
print(3+4)

# task 3
mathSum = math.pi + math.sqrt(2)
print(mathSum)

# task 4
radian = math.sin(30) + math.cos(30)
radian = -1 * (radian/(2.0 * (math.pi)))
print(radian)

# task 5
x = "five"
y = "six"
z = "seven"

combined = x + ' ' + y + ' ' + z
print(combined.ljust(6))

# task 6
r = 5
c = 2 * math.pi * r
print(c)

# task 7
x = 5
y = 15
if (x > y):
    print(x)
else:
    print(y)

# task 8
A = True
B = False

print(bool(A))
print(bool(B))
print(not bool(A))
print(not bool(B))


# task 9
a = 10
i = 0
for number in range(a):
    if (a == 10):
        i = 0
    else:
        i = i + number
        print(i)
    a = a - 1

# task 10
count = 0
i = 0
while (count < 10):
    i = i + count
    print(i)
    count = count + 1
