a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 17]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17]

results = []

def look_in_b(n):
    #We want to know if a number from list a is in list b
    if n in b:
        #then we want to save the results so we can print them later
        results.append(n)

#now we need to run each number in a through the look_in_b function
for i in a:
    look_in_b(i)

print(results)
