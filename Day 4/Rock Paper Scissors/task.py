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

player_choice= int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
computer_choice = random.randint(0, 2)

hands = [rock, paper, scissors]

if 0 <= player_choice <= 2:
    print(f"You chose: {hands[player_choice]}\n Computer chose: {hands[computer_choice]}")
    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
else:
    print("Enter a valid input!")
