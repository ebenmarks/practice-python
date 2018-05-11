all = [1, 1, 2, 11, 5, 5, 5, 6, 7, 9, 9, 10, 11, 12, 14, 18, 23]
less = []

check = int(input("Give me a number: "))

for n in all:
    if n < check:
        less.append(n)

print("Numbers smaller than the one you gave me:", less)
