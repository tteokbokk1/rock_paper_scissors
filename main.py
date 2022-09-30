import random

print("Let's play rock, paper, scissors!")
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

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

#add possible outcomes to list
game_choices = [rock, paper, scissors]

print("You chose:")

if player_choice == "0" or player_choice == "1" or player_choice == "2":
    print(game_choices[int(player_choice)])
else:
    print("That's an invalid choice.")
    exit()

#randomly select from the list of outcomes
num_comp_choices = [0, 1, 2]
comp_selector = random.choice(num_comp_choices)

print("The computer chooses:")
print(game_choices[comp_selector])

#evalutating who won
#2 = draw, 1 = win, 0 = loss
# winner matrix
#       r   p   s
#   r   2   1   0
#   p   0   2   1
#   s   1   0   2

comp_was_rock = [2, 1, 0]
comp_was_paper = [0, 2, 1]
comp_was_scissors = [1, 0, 2]

outcome = [player_was_rock] + [player_was_paper] + [player_was_scissors]
winner = outcome[comp_selector][int(player_choice)]

if winner == 0:
    print("You lose")
elif winner == 1:
    print("You win")
else:
    print("Draw")