import random

user_choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors: \n"))

choice_list = [0, 1, 2]

computer_choice = random.choice(choice_list)

# print(type(computer_choice))
# print(type(user_choice))


print(f"computer chose {computer_choice}")

if user_choice == computer_choice:
  print("Its a tie")
elif (user_choice - computer_choice) % 3 == 1:
  print("You Win!")
else:
  print("Computer Wins!")


  # Rock-Paper-Scissors is a CYCLE: 0->1->2->back to 0 (each one beats the one before it).
  # When something wraps around in a circle, use %  (modulo) to stay inside the range.
  # (user - computer) % 3 tells you the gap on that circle:
  #   0 = same choice      -> tie
  #   1 = you're 1 ahead   -> you win
  #   2 = you're 2 ahead (= 1 behind) -> computer wins
  # Rule of thumb: anything that loops (clock, weekdays, RPS) -> reach for % n