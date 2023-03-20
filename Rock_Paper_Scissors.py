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

player = int(input("What do you want? Type 0 for Rock,1 for paper, or 2 for scissors"))

computer = random.randint(0,2)
if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif player == 2:
    print(scissors)

if computer == 0:
    print(f"Computer chose:{rock}")
elif computer == 1:
    print(f"Computer chose:{paper}")
elif computer == 2:
    print(f"Computer chose:{scissors}")



if computer == player:
    print("Draw")
elif player == 0:
    if computer == 1:
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player == 1:
    if computer == 0:
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player == 2:
    if computer == 1:
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

