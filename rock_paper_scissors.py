"""This project helps to learn the usage of if, elif and else statements.

It also teaches the usage of the lists and call them using their index.
"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
user_choice = game[user_choice]
computer_choice = random.choice(game)

print("You chose: \n", user_choice)
print("Computer chose: \n", computer_choice)
if computer_choice == game[0] and user_choice == game[2]:
    print("You lose")
elif computer_choice == game[2] and user_choice == game[1]:
    print("You lose")
elif computer_choice == game[1] and user_choice == game[0]:
    print("You lose")
elif computer_choice == user_choice:
    print("It's a draw.")
else:
    print("You won")