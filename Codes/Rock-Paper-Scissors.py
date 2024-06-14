player1 = input("Player 1, enter your choice: ") #Take the player1 input
player2 = input("Player 2, enter your choice: ") #Take the player2 input

if player1 == player2: # Tie if both players choose same input
  print("It's a tie!")
elif player1 == "paper" and player2 =="rock":
  print("player1 wins with ", player1)
elif player1 == "paper" and player2 == "scissors":
  print("player2 wins with", player2)
elif player1 == "rock" and player2 == "paper":
  print("player2  wins with ", player2)
elif player1 == "rock" and player2 == "scissors":
  print("Player1 wins with ", player1)
elif player1 == "scissors" and player2 == "paper":
  print("player1 wins with", player1)
elif player1 == "scissors" and player2 == "rock":
  print("player2 wins with ", player2)
else:
  print("Please check the inputs again") # Error if the inputs are not right