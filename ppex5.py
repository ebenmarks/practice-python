#put our lists in sets so that we can find intersections
a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 17])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17])

#because we used sets we can simply use "&" to find the numbers in both
print(a & b)
