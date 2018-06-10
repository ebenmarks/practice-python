while True:
    usr_cmd = input("Do you want to play 'Rock, Paper, Scissors' (Y/N) ")
    if usr_cmd == "Y":

        player1 = input("Player 1, choose your weapon: ")
        player2 = input("Player 2, choose your weapon: ")

        if player1 == "rock" and player2 == "paper":
            print("Player 2 wins!")
        elif player1 == "scissors" and player2 == "paper":
            print("Player 1 wins!")
        elif player1 == "paper" and player2 == "rock":
            print("Player 1 wins!")
        elif player1 == "scissors" and player2 == "rock":
            print("Player 2 wins!")
        elif player1 == "paper" and player2 == "scissors":
            print("Player 2 wins!")
        elif player1 == "rock" and player2 == "scissors":
            print("Player 1 wins!")
        else:
            print("Draw!")

    else:
        break
