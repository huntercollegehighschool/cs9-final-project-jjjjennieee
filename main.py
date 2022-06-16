"""
Name(s): Jennifer Mah
Name of Project: Dice Guess
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

import random

#functions to continue or end game
def play_game():
  guess = input("\nWhat do you think the sum of the dice faces will be? ")
  while guess not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
    guess = input("What do you think the sum of the dice faces will be? ")
  print("\nRolling dice...")
  die1 = random.randint(1,6)
  if die1 == 1:
    print(" ________\n|       |\n|       |\n|   .   |\n|       |\n|_______|")
  elif die1 == 2:
    print(" ________\n|       |\n|       |\n|  . .  |\n|       |\n|_______|")
  elif die1 == 3:
    print(" ________\n|       |\n|  . .  |\n|       |\n|   .   |\n|_______|")
  elif die1 == 4:
    print(" ________\n|       |\n|  . .  |\n|       |\n|  . .  |\n|_______|")
  elif die1 == 5:
    print(" ________\n|       |\n|  . .  |\n|  . .  |\n|   .   |\n|_______|")
  elif die1 ==6:
    print(" ________\n|       |\n|  . .  |\n|  . .  |\n|  . .  |\n|_______|")
  die2 = random.randint(1,6)
  if die2 == 1:
    print(" ________\n|       |\n|       |\n|   .   |\n|       |\n|_______|")
  elif die2 == 2:
    print(" ________\n|       |\n|       |\n|  . .  |\n|       |\n|_______|")
  elif die2 == 3:
    print(" ________\n|       |\n|  . .  |\n|       |\n|   .   |\n|_______|")
  elif die2 == 4:
    print(" ________\n|       |\n|  . .  |\n|       |\n|  . .  |\n|_______|")
  elif die2 == 5:
    print(" ________\n|       |\n|  . .  |\n|  . .  |\n|   .   |\n|_______|")
  elif die2 ==6:
    print(" ________\n|       |\n|  . .  |\n|  . .  |\n|  . .  |\n|_______|")
  dice_sum = die1 + die2
  print("\nThe sum of the dice faces is:",dice_sum)
  guess = int(guess)
  if guess == dice_sum:
    print("Wow, you were right.")
  elif guess != dice_sum:
    print("You got it wrong, loser.")


def quit_game():
  print("That's unfortunate.")


#displays for actually playing the game
print("Welcome to Dice Guess!")
print("Wanna play?")
yes_no = input("(Y/N)\n")
yes_no = str.lower(yes_no)
if yes_no == "y":
  play_game()
  play_again = input("\nDo you wanna play again? (Y/N)\n")
  play_again = str.lower(play_again)
  while play_again == "y":
    play_game()
    play_again = input("\nDo you wanna play again? (Y/N)\n")
  if play_again == "n":
    print("\nOf course you're quiting, you suck at this.")
  while play_again not in ["y", "n"]:
    play_again = input("\nDo you wanna play again? (Y/N)\n")  
elif yes_no == "n":
  quit_game()
while yes_no not in ["y", "n"]:
  yes_no = input("(Y/N)\n")