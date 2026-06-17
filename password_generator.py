import random  # built-in module: gives us random.choice() and random.shuffle()


# LISTS: ordered collections in [ ]. Each item here is a string in quotes.
# Three separate pools so we can control how many of each type go in the password.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
  'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
  'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
  'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
  'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# input() always returns a string, so wrap it in int() to get a number we can count with.
# \n just prints a newline so the user types their answer on the next line.
print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password = []  # start with an empty LIST and build it up with .append()

# for _ in range(N): runs the body exactly N times.
# _ means "I don't use the counter" — it's just controlling repetition.
# random.choice(list) picks ONE random item from the list.
for _ in range(nr_letters):
  random_letter = random.choice(letters)
  password.append(random_letter)  # .append() adds one item to the end of the list

for _ in range(nr_symbols):
  random_symbol = random.choice(symbols)
  password.append(random_symbol)

for _ in range(nr_numbers):
  random_number = random.choice(numbers)
  password.append(random_number)


# Right now the list is in a predictable order (letters, then symbols, then numbers).
# random.shuffle() scrambles the list IN PLACE (changes it, returns nothing).
random.shuffle(password)

# "".join(list) glues every item into one string. The "" is the separator (nothing between).
# Note the shape: "glue".join(list)  — join belongs to the string, not the list.
password = "".join(password)

# f-string: the {password} inside the quotes gets replaced with its actual value.
print(f"Your password is {password}")