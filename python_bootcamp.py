#import random
# import my_module

# random_integer = random.randint(1,10)
# print(random_integer)

# print(my_module.my_fav_num)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

#differnce is 
#random() - Returns a random floating-point number (decimal) between and 0.0 and 1.0 The exact range is 0.0 <= x < 10 (1 is never included) It takes no arguments.

#randint(a,b)- returns a random integer (whole no) froma specific range
#Both a and b is inclusive

#uniform(a,b) - return random floating point no (decimal) from a custom range
#a and b both included in the range

#List - data sctrcture to store data in python
#friuts = [item1 , item2]
#how to access list ---> print(fruits[0]) ---> item1 is printed
#print(fruits[-1]) --> item2 is printed ---> from the end of the list
#change --> fruits[0] = item3  --> [item3 , item2]
#add one item  ---> fruits.append(item3) --> [item1, item2, item3]
#add more items --->fruits.extend([item3,item4]) --->[item1, item2, item3,item4]

#index error - acessing a index in a list out of boundary - fruits[2] 
#dirty_dozen[0][1] ---> there are 2 lists and 0 is sublist 1 and 1 is sublist 2---> we are going to access sublist 1's  [1] indexed element


#For loop
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)  -->
#  Apple  
# Peach 
#  Pear
#   print(fruits) ---> 
# Apple 
# ["Apple", "Peach", "Pear"]
#Peach 
# ["Apple", "Peach", "Pear"]
#Pear
#  ["Apple", "Peach", "Pear"]
#Execute same line of code many times

#for loops with range function
# for number in range(1,101): #last no is exculsive
#   print(number)

# for number in range(1,11,3):#3 is the step 
#   print(number)

# total =0
# for number in range(1,101): 
#   total += number
# print(total)

#FUNCTIONS
# num_char = len("Hello")
# print(num_char)

# def my_function():
#   print("HELLO")
#   print("BYE")

# my_function()


#while loop
#while something_is_true:
  #Do something repeatedly

# so when condition in while loop is false it will stop 

#when to use for loop and while loop
#iterate through something and do something with each item we iterate - for loop
#we dont care how many time runs , it stops when condition is met or false - while
#sometimes creates infinite loop - if condition is not met


#Functions with inputs
# def greet():
#   print("Hello")
#   print("How do you do?")

# greet()

# def my_function(something):
#   do this with something
#   then do this
#   finally do this
# my_function(123)
# something = 123 
#somthing - parameter | 123 -Argument 
#Name of the data we refer the value of it  | actual data pased to the function

# def greet_with_name(name):
#    print(f"Hello {name}")
#    print(f"How do you do {name}?")

# greet_with_name("Angela")

#Functions with more than 1 input
# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"What is in like in {location}")

# greet_with("Rosheni", "Moratuwa")

# greet_with("Nowhere", "Jack")
# output is 
# Hello Nowhere
# What is in like in Jack
#Postional arguments - when we call the function we havent called any sepcific position - default way


# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"What is in like in {location}")


# greet_with(location="Nowhere",name="Jack")

#Keyword arguments - telling the position of the argments

# .count() → counts how many times a value appears in a string.

# Syntax:
# string.count("value")

# Example:
# "banana".count("a") → 3
# it is case -sensitive and if value is capital it will give 0 
#can count words too

#lower() - make all words simple

#Dictionaries
#like two columns of table - key value pairs
#{key : Value}
# Programming_dictionry = {
#       "a" :"apple",
#        "b": "Ball",


# }

# print(Programming_dictionry["a"])

# Programming_dictionry["c"] = "Cat"
# print(Programming_dictionry)

# empty_dictionary = {}

# #wipe an existing dictionary
# Programming_dictionry = {}
# print(Programming_dictionry)

#Edit an item in a dictionary
# Programming_dictionry["a"] = "Alpha"
# print(Programming_dictionry)

# #Loop through dictionary
# for key in Programming_dictionry:
#   print(key)
#   print(Programming_dictionry[key]) # to get a value of a key

#{key: [List],
# key2 : {Dict},
# }

#Nest a list in dictionary
#Each key can have one value
# travel_log= {
#   "France":["Paris," "Dijon","Lille"],
#   "Germany":["Stuttgart" , "Berlin"],

# }

# #print Lille
# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1]) #Print D

# travel_log= {
#   "France":{
#     "cities_visited":["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#   },
#   "Germany":{
#   "cities_visited" : ["Stuttgart" , "Berlin"],
#   "total_visits":5
#   },
# }

# print(travel_log["France"]["cities_visited"][1]) #print Lille
# print(travel_log["Germany"]["total_visits"]) #print total visits for germany


#Functions with outputs
# def format_name(f_name , l_name):
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()

#   return f"{formated_f_name} {formated_l_name}"

# print(format_name("angela", "YU"))

#Multiple return values
# def format_name(f_name , l_name):
#   if f_name == "" or l_name == "":
#     return "You did not provide valid inputs"
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"{formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name?"), input("What is your last name?")))

#Docstrings
# def format_name(f_name , l_name):
#   """Take a first and last name and format it to return the title 
#   cae version of the name.
  
#   """
#   if f_name == "" or l_name == "":
#     return "You did not provide valid inputs"
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"{formated_f_name} {formated_l_name}"

#Name spaces - Local and Global
# enemies = 1
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}") #2

# increase_enemies()
# print(f"enemies outside function: {enemies}") #1

#Local Scope
# def drink_portion():
#   portion_strength = 2
#   print(portion_strength)

# drink_portion()
# print(portion_strength) #gives a name error

#Global Scope
# player_health  =10

# def drink_portion():
#   portion_strength = 2
#   print(player_health)

# drink_portion()
# print(player_health)

#global and local scope differnce is where i create the varibles
#in the function
#global variables are available within functions no matter how deep it get nested
#also it is availble outside the function

#does python have block scope - no
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# def create_enemy():
#   if game_level <  5:
#     new_enemy = enemies[0]

# print(new_enemy) #Name error

#if a variable is declared inside a function , it is only avaible inside that function
#if a variable is declared within if block ,while loop or for loop or anything that has identation and colon 
#It is not in a seperate local scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# def create_enemy():
#   if game_level <  5:
#      new_enemy = enemies[0]

#      print(new_enemy)

# create_enemy()
# print(new_enemy)

#How to modify global variable
# enemies =  1
# def increase_enemies():
#   global enemies
#   enemies += 1
#   print(f"enemies inside function: {enemies}") 

# increase_enemies()
# print(f"enemies outside function: {enemies}") 

#avoid modifying global scope
# enemies = 1
# def increase_enemies(enemy):
#   print(f"enemies inside function: {enemies}") 
#   return enemy + 1

# enemies = increase_enemies(enemies)
# print(f"enemies outside function: {enemies}") 

#python constants and global scope
#Global constants - you define but never change them 
# PI = 3.14 #uppercase
# def my_fun():
#   print(PI)

#debugging
# 1) describe the problem
#2) Reproduce Bug
#3)play computer and evaluvate each line
#4) Fix the errors watching red lines
# try:
#   age = int(input("How old are you? "))
# except ValueError:
#   print("Invalid pls try again")
#   age = int(input("How old are you? "))

# if age > 10:
#   print(f"You can drive at age {age}")

#5) Use print() statement
#6) use a debugger

#Day 16 - OOP -object oriented programming
#procedural programming - functions or procedures that do particular things
#so procedural programming - larger restarurant everything i should handle
#i should be waitress, receptionist accordingly
#but oop - larger resatrurant there are specific roles like chef , waiter, receptionsit who knows how to do their thing
#as myself as the manager I don't have to tell these people , how things work - I don't have to guide chef to cook this dish , chef knows
#I have to only manage these roles only 

#How to use oop
#its trying model real world object
#we are going to model a waiter 
#2 things : has (attributes), does(methods)
#attributes: is_holding_plate = True | tables_responsible = [4,5,6]
#methods: def take_order(table,order): | def take_payment(amount)
#attribute - varaible asscoiated with a particular object
#method - a function a particular model can do
#object is combining data(attributes) with functionality
#we can genearte multiple versions of one object, blueprints of the objects - CLASS
#Eg: waiter ---> Henry , Betty
#Class - blueprint that individual objects are generated
#Car blueprint (class)- creates many car objects

# car = CarBlueprint() #Pascal case
#object     #class

#turtle graphics
# import turtle #blueprint

# timmy = turtle.Turtle() 
# #timmy is an object , Turtle is the class

# # another way
# from turtle import Turtle , Screen
# timmy = Turtle()
# print(timmy)

# #accessing attributes 
# # Eg: car.speed (object | attribute)

# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.shape("turtle") #method
# timmy.color("blue") #method
# timmy.forward(100) #method

# #accessing methods
# #Eg: def move()
# #       speed = 60

# #car.move()

# my_screen.exitonclick()

#python packages - using code other developers have written
#module is single file with code others have written
#package is a folder that contains multiple modules
#turtle library - module
#python standard library - package
#In the terminal pip install prettytable
# install package into the project
# import prettytable

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["a", "b", "c"])
# table.add_column("Type", ["water", "Electric", "Fire"])
# table.align = "l"
# print(table)

#Day 17
#How to create your own class in python

# class User:
#   pass  #have to intend inside a class

# user_1 = User()
# user_1.id = "001"  #attrbute is a variable associated with an object

# print(user_1.id)
 
#constructor - part of blueprint that specify what should happen when our object is constructed
#when object is initialized - can set variables, counters  to  their starting values
#create constructor using special function - __init__ function
#class Car:
    # def __init__(self):
    #initialise attributes

# class User:
  
#   def __init__(self, user_id, username):
#     #everytime a new user is created , what is under this function is triggered
#     self.id = user_id
#     self.username = username
#     self.followers = 0
#     self.following = 0

#     #Adding methods to class
# #function attch to a object - method

#   def  follow(self,user):
#     user.followers += 1
#     self.following += 1



# user_1 = User("001", "angela")
# user_2 = User("002", "jack")
# print(user_1.id)
# print(user_1.followers)

# user_1.follow(user_2)
# print()
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

#Day 18 - Turtle Graphics
# from turtle import Turtle,Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
# for _ in range(4): #Draw a sqaure
#   timmy.forward(100)
#   timmy.right(90)




# screen = Screen()
# screen.exitonclick()

#GUI - python to create a graphical user interface - Tkinter
#tkinter - what turtle graphics use for the underlying graphics

#how to import 
# #Basic import 
# import turtle
# tim = turtle.Turtle()

# #from import
# from turtle import Turtle
# tim = Turtle()

# #Import everything
# from turtle import *
# #very rare to use , we dont where the method ,attributes come from

# #import using alias name
# import turtle as t
# tim = t.Turtle()   #t is the alais name

#if module is not in the python standard libaray we need to install it for the project

#virtual environment - define a small sandbox to our project
#so I have installed python 2 for the project and code is complie with that
# but i want to install a package but it works in python 3 only
#so instaed of downloading python 3 all overagain i create a venv , like a seperate environment
#where packages compatible with python 3 works , i created it but have to activate it everytime im close and open my code editor(vs code)

#draw a dashed line (turtle)
# import turtle
# from turtle import Turtle,Screen
# import random
# tim = Turtle()
# screen = Screen()
# # for _ in range(15):
# #   tim.forward(10)
# #   tim.pendown()
# #   tim.forward(10)
# #   tim.penup()

# #draw a differnt shapes

# # colors = ["blue", "red", "yellow", "pink", "grey", "black","green","orange","purple"]


# # def draw_shape(num_sides):
# #   angle = 360/ num_sides
# #   for _ in range(num_sides):
# #    tim.forward(100)
# #    tim.right(angle)

# # for shape_side_n in range(3, 11):
# #    tim.color(random.choice(colors))
# #    draw_shape(shape_side_n)
 
# turtle.colormode(255)

# def random_color():
#   r = random.randint(0,255)
#   g = random.randint(0,255)
#   b = random.randint(0,255)

#   color = (r,g,b)
#   return color

# #Draw random walk
# directions = [0,90,180,270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#   tim.color(random_color())
#   tim.forward(30)
#   tim.setheading(random.choice(directions))


# screen.exitonclick()

#python tuple - (1,3,8) - they are ordered
# my_tuple = (1,3,8)
# print(my_tuple[2])
#Can't change the values by writing code, or move - immutable - so we use to define someting constant , that wont change
# this cant be changed - my_tuple[2] = 12 - this is wrong
#to change something in tuple we convert it to a list 
#list(my_tuple)

#Draw a spirograpgh
# from turtle import Turtle, Screen
# import random, turtle



# t = Turtle()
# turtle.colormode(255)


# def random_color():
#   r = random.randint(0,255)
#   g = random.randint(0,255)
#   b = random.randint(0,255)

#   color = (r,g,b)
#   return color

# t.speed("fastest")

# def draw_spirograpgh(size_of_gap):
  
#   for _ in range(int(360/ size_of_gap)):
#     t.color(random_color())
#     t.circle(100)
#     t.setheading(t.heading() + size_of_gap)

# draw_spirograpgh(5)

# screen = Screen()
# screen.exitonclick()

#Event listener in turtle
#Event listeners let your program react to user actions like keyboard presses or mouse clicks.
#Instead of code running top-to-bottom, the program waits for events.
#from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forward():
#     tim.forward(10)

# screen.listen()
# screen.onkey(move_forward, "space")

# screen.exitonclick()

#higher order functions - function that can work with other functions
#another function is passed as a input/argument to another function
# def move_forward():
#     tim.forward(10)

# screen.listen()
# screen.onkey(move_forward, "space")

#multiple objects from one class - instance










