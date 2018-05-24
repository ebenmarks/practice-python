phrase = input("Type your phrase here: ")

compare = ("")

for i, c in enumerate(phrase):
    if phrase[i] == phrase[len(phrase)-1-i]:
        compare += c

if phrase == compare:
    print("It's a palindrome!")
else:
    print("It's not a palindrome")
