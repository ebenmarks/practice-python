num = int(input("Give me a number: "))
divi = []

list = range(1, num)

for i in list:
    if num % i == 0:
        divi.append(i)

print(f"Numbers that are divisors of {num}: {divi}")
