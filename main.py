import random 

choices =['rock', 'paper', 'scissors']
computer=random.choice(choices)
player_input=None

while player_input not in choices:
  player_input=input("rock, paper, or scissors?: ").lower()

if player_input==computer:
  print("Computer:", computer)
  print("Player: ", player_input)
  print("Its a tie")
