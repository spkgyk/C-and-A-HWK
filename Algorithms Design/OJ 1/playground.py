c = 0
lower = -200
upper = 200
L = [23, 45, 67, 68, 89, 286]
R = [1, 34, 45, 67, 90]

i = 0
j = 0
for x in L:
    while i < len(R) and R[i] < lower + x:
        i += 1
    while j < len(R) and R[j] <= upper + x:
        j += 1
    c += j - i

print(c)
