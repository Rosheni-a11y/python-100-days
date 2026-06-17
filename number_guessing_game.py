# import random

# def easy():
#   print("You have 10 attempts remaining to guess the number")
 
  
#   guess_continue = True
#   attempts = 10
#   correct_number = random.randint(1,100)
#   while guess_continue :

    

#     if attempts == 0:
#       guess_continue = False
#       print( f"Your attempts are over, You have lost\n The correct number was {correct_number}")
#       break
      
    
#     guess = int(input("Make a guess: "))

#     if guess > correct_number:
#       attempts -= 1
#       print(f"Too high \n Guess again \n You have {attempts} attempts remaining to guess the number ")
#     elif guess < correct_number:
#       attempts -= 1
#       print(f"Too Low \n Guess again \n You have {attempts} attempts remaining to guess the number ")
#     else:
#       print( f"You got it!, You win ")
#       guess_continue = False



# def hard():
#   print("You have 5 attempts remaining to guess the number")
 
  
#   guess_continue = True
#   attempts = 5
#   correct_number = random.randint(1,100)
#   while guess_continue :
    

#     if attempts == 0:
#        guess_continue = False
#        print (f"Your attempts are over, You have lost\n The correct number was {correct_number}")
#        break
      
    
#     guess = int(input("Make a guess: "))

#     if guess > correct_number:
#       attempts -= 1
#       print(f"Too high \n Guess again \n You have {attempts} attempts remaining to guess the number ")
#     elif guess < correct_number:
#       attempts -= 1
#       print(f"Too Low \n Guess again \n You have {attempts} attempts remaining to guess the number ")
#     else:
#       print( f"You got it!, You win ")
#       guess_continue = False

# print("Welcme to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100")
# difficulty = input("Choose a difficulty. Type 'easy' or ''hard': ")
# if difficulty == 'easy':
#    easy()
# elif difficulty == 'hard':
#   hard()
# else:
#   print("Invalid choice")


import random
EASY_LEVEL = 10   #Global variables
HARD_LEVEL = 5



def check_answer(user_guess, actual_answer, turns):
  """checks answer against guess"""
  if user_guess > actual_answer:
    print("Too High")
    return turns -1
  elif user_guess < actual_answer:
    print("Too Low")
    return turns -1
  else:
    print(f"You got it! The answer was {actual_answer}")


def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL
    



def game():

  print("Welcme to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")

  answer = random.randint(1,100)
  turns = set_difficulty()
 

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts left")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you loose")
      return
    elif guess != answer:
      print("Guess again")

game()
     
    


      
      