num = int(input("Give me a number: "))
results_list = []

start_list = range(1, num)

for i in start_list:
    if num % i == 0:
        results_list.append(i)

print(f"Numbers that are divisors of {num}: {results_list}")
