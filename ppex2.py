num = int(input("Give me a number to check: "))
check = int(input("Give me a number to divide it by: "))

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
