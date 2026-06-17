
 
def add(n1,n2):
  return n1 + n2

def substract(n1,n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

operations = {
  "+":add,
  "-": substract,
  "*" : multiply,
  "/": divide
}

def calculator():
  should_quit = True
  should_calculate = True
  num1 = float(input("What is the first number? "))

  while should_quit:
    while should_calculate:
      for symbol in operations:
        print(symbol)
      operation_symbol = input("Pick an operation: ")
      num2 = float(input("What is the second number? "))
      answer = operations[operation_symbol](num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")

      choice = input(f"Type 'y' continue calculating with the {answer} or 'n' to start a new calculation or do you want to quit , type 'quit':  ")
      if choice == 'y':
        num1 = answer
      elif choice == 'quit':
        should_quit = False
        should_calculate = False
        print("Goodbye!")

      else:
        should_calculate = False
        print("\n" * 20)
        calculator()

calculator()
       
       

      


  