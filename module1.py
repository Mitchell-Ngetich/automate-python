# calc = (5-1) * ((7 + 1) / (3 - 1))
# print(calc)
# print("Alice " * 6)

# This program says hello and asks for your name.
# print("Hello, world!")
# print("What is your name?")
# my_name = input()
# print(f"It is good to meet you, {my_name}")
# print("The length of your name is:")
# print(len(my_name))
# print("What is your age?")
# myAge = input()
# print(type(myAge))
# print(f"You will be {int(myAge) + 1} in a year.")

# def a():
#        print('a() starts')
#        b()
#        d()
#        print('a() returns')

# def b():
#        print('b() starts')
#        c()
#        print('b() returns')

# def c():
#        print('c() starts')
#        print('c() returns')

# def d():
#        print('d() starts')
#        print('d() returns')

# a()

# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()

# def spam():
#     print(eggs)
# eggs = 42
# spam()

# import time, sys
#  # Whether the indentation is increasing or not.

# def game():
#     indent = 0 # How many spaces to indent.
#     indentIncreasing = True
#     while True:
#         print(" " * indent, end="")
#         print("++++++++++")
#         time.sleep(0.1)
        
#         if indentIncreasing:
#             indent += 1
#             if indent == 30:
#                 indentIncreasing = False
#         else:
#             indent -= 1
#             if indent == 0:
#                 indentIncreasing = True
# game()

# def collatz(number):
#     if number % 2 == 0:
#         result = number // 2
#     else:
#         result = 3 * number + 1
#     print(result)
#     return result

# number = int(input("Enter a number: "))
# while number != 1:
# # we use number as a variable and also as a parameter in order
# # to keep updating the current value returned after a while loop
#     number = collatz(number)

# total = 0
# #adds until number == 0`
# number = int(input("Enter a number: "))
# while number != 0:
#     total += number
    
#     number = int(input("Enter a number: "))
# print(total) #if you indent print(total) it will print the total after each number is entered

#Slice method
# animals = ['cat', 'bat', 'rat', 'elephant', "Rhino", "lion"]
# for index, element in enumerate(animals):
#     print(f"Index {index} in animals list is: {element}")

# my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# print(type(my_cat))

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}


# while True:
#     name = input("Enter your name: ")
#     if name == "":
#         break
#     if name in birthdays:
#         print(f"{birthdays[name]} is the birthday of {name}")
#     else: 
#         print(f"I don't have a birthday information for {name}")
#         break
    
# spam = {'color': 'red', 'age': 42}
# for k, v in spam.items():
#     print(f"Key: {k}, Value: {v}")

# spam = {'name': 'Pooka', 'age': 5}
# spam.setdefault("color", "black")
# # print(spam)
# spam.setdefault("color", "white")
# # even if you set the color to white, it will not change the color to white
# # because the key(color) already exists
# print(spam)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

# counts the occurence of each character in a string in the dictionary
# if the key i.e i, is not there, then it sets the value to 0 and increments it
# and if the key i.e i, is there, then setdefault() does nothing.
for i in message:
    count.setdefault(i, 0)
    count[i] += 1
    
print(count)