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

hands = [rock, paper, scissors]

players_hand = int(input(
    'What would you like to choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))
computer_hand = random.randint(0, 2)

print(hands[players_hand])
print("Computer Chooses")
print(hands[computer_hand])

if(players_hand == computer_hand):
    print("It's a tie!")
elif(players_hand == 0 and computer_hand == 1):  # player rock, computer paper
    print("Paper covers Rock. You loose.")
elif(players_hand == 0 and computer_hand == 2):  # player rock, computer scissors
    print("Rock smashes Scissors. You win!")
elif(players_hand == 1 and computer_hand == 0):  # player paper, computer rock
    print("Paper covers Rock. You win!")
elif(players_hand == 1 and computer_hand == 2):  # player paper, computer scissors
    print("Scissors cuts Paper. You loose.")
elif(players_hand == 2 and computer_hand == 0):  # player scissors, computer rock
    print("Rock smashes Scissors. You loose.")
elif(players_hand == 2 and computer_hand == 1):  # player scissors, computer paper
    print("Scissors cuts Paper. You win!")
elif(players_hand < 0 or players_hand > 2):
    print("You have to choose between 0, 1, or 2.")
