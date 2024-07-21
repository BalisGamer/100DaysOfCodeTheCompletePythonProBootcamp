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

#Write your code below this line 👇
import random

list = [0, 1, 2]
player = int(input("Chose: Rock - 0, Paper - 1, Scissors - 2\n"))
computer = random.choice(list)
print("Player:")
if player == 0:
  print(rock)
elif player == 1:
  print(paper)
elif player == 2:
  print(scissors)
else:
  print("please chose correct number")

print("\nComputer:\n")

if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
  print("Player Win!")
elif player == computer:
  print("Draw!")
else:
  print("Computer Win!")
