#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)
print("This is a number guessing game.\nI am thinking of a number between 1 and 100 and you have to guess it.")

level = input("Choose a difficulty level by typing 'easy' or 'hard': ")
if level == "easy":
  rounds = 10
else:
  rounds = 5

number = random.randint(1,100)
print(f"psssst, the secret number is {number}")
solved = False

# def decrease_rounds():
#   return rounds - 1

while not rounds == 0 and solved == False :
  guess = int(input("Make a guess: "))
  if guess == number:
    print(f"You guessed it! I thought of {number}")
    solved = True
  elif guess > number:
    print("Too high.")
    rounds -= 1
    print(f"You have {rounds} guesses left")
  else:
    print("Too low.")
    rounds -= 1
    print(f"You have {rounds} guesses left")

if rounds == 0:
  print(f"Sorry, you took too long. The secret number was {number}")
