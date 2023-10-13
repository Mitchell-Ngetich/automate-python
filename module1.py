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

# import pprint

# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# # counts the occurence of each character in a string in the dictionary
# # if the key i.e i, is not there, then it sets the value to 0 and increments it
# # and if the key i.e i, is there, then setdefault() does nothing.
# for i in message:
#     count.setdefault(i, 0)
#     count[i] += 1
    
# print(pprint.pformat(count))

# Tick-tac-toe
# the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
# turn = "X"
# for i in range(9):
#     printBoard(the_board)
#     print(f"Turn for {turn}. Move on which space?")
#     move = input()
#     the_board[move] = turn
#     # check the current player if its X, next switch to O
#     if turn == "X":
#         turn = "O"
#     else: turn = "X"
# printBoard(the_board)

all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, items):
    num_brought = 0
    for k, v in guests.items(): #v reprents the {'apples': 5, 'pretzels': 12},and so on...
        num_brought = num_brought + v.get(items, 0) # so items is equal to apples/cups etc...and if the item isn't present it will return 0
    return num_brought

print("Number of things being brought:")
print(f"- Apples {total_brought(all_guests, 'apples')}")
print(f"- Pretzels {total_brought(all_guests, 'pretzels')}")
print(f"- Ham Sandwisches {total_brought(all_guests, 'ham sandwiches')}")
print(f"- Cups {total_brought(all_guests, 'cups')}")
print(f"- Apple Pies {total_brought(all_guests, 'apple pies')}")
print(f"- cookies {total_brought(all_guests, 'cookies')}")