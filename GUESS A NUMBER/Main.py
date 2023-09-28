from art import logo
print(logo)
from random import randint
hard_level=5
easy_level=10
#Number Guessing Game Objectives:
def ch_num(num,gnum,turns):
  if gnum>num:
    print("It's too high.")
    return turns-1
  elif gnum<num:
    print("It's too low.")
    return turns-1
  else:
    print(f"You got it. The answer is {num}")
def main():
  print("Welcome to the number Guessing game")
  print("I'm thinking of number between 1 to 100")
  num=randint(1,100)
  def levels():
    choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose == "hard":
      return hard_level
    else:
      return easy_level
  turns = levels()
  guess=0
  while guess!= num:
    print(f"You have {turns} attempts remaining to guess the number.")
    gnum = int(input("Make a guess:"))
    turns = ch_num(num, gnum,turns)
    if turns== 0:
      print("You run out of guesses. You lose!")
      return
    elif guess!=num:
      print("Guess again")
    

main()
    

# Include an ASCII art logo.
  
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

