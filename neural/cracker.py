import time

count = input("Input length: ")

possible = []

for x in range(94):
    x = x + 33
    l = chr(x)
    possible.append(l)

print(possible)
