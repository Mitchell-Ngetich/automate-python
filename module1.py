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
