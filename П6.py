player1 = input("Игрок 1: ")
player2 = input("Игрок 2: ")

if player1 not in ["rock", "scissors", "paper"] or player2 not in ["rock", "scissors", "paper"]:
    print("Ошибка")
elif player1 == player2:
    print("Ничья")
elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
    print("Победил игрок 1")
else:
    print("Победил игрок 2")
