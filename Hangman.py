import random

word_list = ["Hello", "Camel", "Bamboo", "Headphones"]

stages = [r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
      |
      |
      |
      |
=========
"""]

lives = 6

chosen_word = random.choice(word_list).lower()

print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
  placeholder += "_"
print(placeholder)

correct_letters = []
game_over = False

while not game_over :

  print(f"************{lives}/6 LIVES LEFT*********")
  guess = input("Guess a letter:")
  if guess in correct_letters:
    print(f"You already guessed {guess}")
  
  display = ""


  for letter in chosen_word:
    if guess == letter:
      display += letter
      correct_letters.append(letter)

    elif letter in correct_letters:
      display += letter
    else:
      display += "_"
      
  print(display)



  if guess not in chosen_word:
    lives -= 1
    print(f"You guess { guess}, that's not in the word.You lose a life")
    if lives == 0:
      game_over = True
      print(f"You loose, the correct word is {chosen_word}")


  if "_" not in display:
    game_over= True
    print("You win!")


  print(stages[lives])
  