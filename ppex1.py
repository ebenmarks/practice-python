# lets us look up the current year
import datetime
now = datetime.datetime.now()

# prompts user for input and saves that to the relevant variables
name = input("What is your name? ")
age = int(input("How old are you? "))
repeats = int(input("How many times do you want the answer?"))

# calculate in which calendar year the user turns 100
year100 = now.year + (100 - age)

# prints the results as many times as the user requested
print(f"{name}, you will be 100 years old in {year100}.\n" * repeats)
