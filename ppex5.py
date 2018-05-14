#create two sample lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#make a variable of the the highest number in both lists
highest = max([max(a), max(b)])

#create list from 1 to the highest number to iterate through
lsrng = range(1, highest)

#create empty list for the results
results = []

#define a function to check if number is in both lists
def comp(n):
    if n in a and n in b:
        #add the number to the empty list
        results.append(n)

#iterate through the lists
for i in lsrng:
    comp(i)

#print the results
print(results)
