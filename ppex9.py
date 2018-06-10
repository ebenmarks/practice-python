import random

count = 0

while True:
    a = random.randint(1, 9)
    guess = int(input("Pick a number from 1-9: "))

    if guess < a:
        print("Too low!")
        print("My number was:",a)
    elif guess > a:
        print("Too high!")
        print("My number was:",a)
    elif guess == a:
        print("You got it!")

    count = count + 1

    stop_game = input("Type 'exit' to end the game or hit the Enter key to continue. ")

    if stop_game == "exit":
        print(f"You played {count} rounds.")
        break
    else:
        continue
