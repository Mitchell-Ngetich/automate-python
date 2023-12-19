# while True:
#    print("enter your age: ")
#    age = input()

#    try:
#        age = int(age)
#    except:
#        print("Please enter a numeric digit.")
#        continue
#    if age < 1:
#         print("Please enter a positive number.")
#         continue
#    break

# print(f"your age is {age}")

import pyinputplus as pyip

# response = pyip.inputNum()
# response = pyip.inputInt(prompt= "Enter a number: ", min = 1)
# response = pyip.inputNum(">", min = 4, lessThan = 8)
# response = pyip.inputInt("Enter a number: ")
# response = pyip.inputNum(limit = 3)
# response = pyip.inputNum(timeout = 5)
# response = pyip.inputNum(allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"])
# response = pyip.inputNum(blockRegexes=[r"[034567]"])

# def add_to_ten(numbers):
#     numbers_list = list(numbers) #converts numbers into an array
#     for i, digit in enumerate(numbers_list):
#         numbers_list[i] = int(digit)
#     if sum(numbers_list) != 10:
#         raise Exception(f"The digits must add to 10, and not {sum(numbers_list)}")
#     return int(numbers)

# response = pyip.inputCustom(add_to_ten)

# while True:
#     prompt = "Want to know how to keep an idiot busy for hours? \n"
#     response = pyip.inputYesNo(prompt)
#     if response == "no": break
# print("Thank you. Have a nice day!")

# Multiplication Quiz
# import random, time

# number_questions = 10
# correct_answers = 0
# for question_Num in range(number_questions):
#     num1 = random.randint(0, 9)
#     num2 = random.randint(0, 9)
#     prompt = f"#{question_Num + 1}: {num1} * {num2}  "

#     try:
#         pyip.inputStr(prompt, allowRegexes=["^%s$" % (num1 * num2)],
#                       blockRegexes=[(".*", "Incorrect")],
#                       timeout=8, limit=3)
#     except pyip.TimeoutException:
#         print("Out of time!")
#     except pyip.RetryLimitException:
#         print("Out of tries!")
#     else:#runs if no exceptios were raised in the try block
#         print("Correct!")
#         correct_answers += 1

#     time.sleep(1)
# print(f"Score: {correct_answers}/ {number_questions}")\


# CHAPTER 9 - READING AND WRITTING FILES
from pathlib import Path

# path = Path("spam", "bacon", "eggs")
# print(path)
# path_string = str(Path(path))
# print(path_string)

# myFiles = ["accounts.txt", "details.csv", "invite.docx"]
# for filename in myFiles:
#     print(Path(r"C:/Users/Al", filename)) # r indicates its a raw string which treats backslashes as literal xters rather than escape characters

# homeFolder = Path("C:/Users/Al")
# subFolder = Path("spam")
# combine = homeFolder / subFolder
# print(combine)
import os

# path = Path.cwd()
# print(path)

# os.chdir("C:/home/mitchell/Python")
# print(Path.cwd())
# print(Path.home())

# print(Path.cwd())
# print(Path.cwd().is_absolute())
# print(Path("spam/bacon/eggs").is_absolute())

# p = Path("/home/mitchell/Python")
# print(p.anchor)
# print(p.parent)
# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.drive)

p = Path("/home/mitchell")
# print(p.glob("*.txt"))
# print(list(p.glob("*")))
# print(list(p.glob("project?.docx")))
# print(list(p.glob("*.?x?")))
# for filepath in p.glob("*.txt"):
# print(filepath)
# below is the basic interactions with files. The common way involves using open(), read(), write(), and close().
# p = Path("spam.txt")
# print(p.write_text("Hello, world!"))
# print(p.read_text())

# Opening files with the open() function
# p = Path("/home/mitchell/hello.txt")
# p.write_text("Hello, world!")

# helloFile = open("/home/mitchell/hello.txt")
# content = helloFile.read()
# print(content)

# baconFile = open("bacon.txt", "w")
# print(baconFile.write("Hello world!\n"))
# baconFile.close()

# baconFile = open("bacon.txt", "a")
# print(baconFile.write("Bacon is not a vegetable."))
# baconFile.close()

# baconFile = open("bacon.txt")
# content = baconFile.read()
# baconFile.close()
# print(content)

# SAVING VARIABLES WITH THE SHELVE MODULE

import shelve

# shelfFile = shelve.open("mydata")
# cats = ["Zophie", "pooka", "simon"]
# shelfFile["cats"] = cats
# print(cats)
# shelfFile.close()


# (PROJECT) GENERATING RANDOM QUIZ FILES
# import random

# capitals = {
#     "Alabama": "Montgomery",
#     "Alaska": "Juneau",
#     "Arizona": "Phoenix",
#     "Arkansas": "Little Rock",
#     "California": "Sacramento",
#     "Colorado": "Denver",
#     "Connecticut": "Hartford",
#     "Delaware": "Dover",
#     "Florida": "Tallahassee",
#     "Georgia": "Atlanta",
#     "Hawaii": "Honolulu",
#     "Idaho": "Boise",
#     "Illinois": "Springfield",
#     "Indiana": "Indianapolis",
#     "Iowa": "Des Moines",
#     "Kansas": "Topeka",
#     "Kentucky": "Frankfort",
#     "Louisiana": "Baton Rouge",
#     "Maine": "Augusta",
#     "Maryland": "Annapolis",
#     "Massachusetts": "Boston",
#     "Michigan": "Lansing",
#     "Minnesota": "Saint Paul",
#     "Mississippi": "Jackson",
#     "Missouri": "Jefferson City",
#     "Montana": "Helena",
#     "Nebraska": "Lincoln",
#     "Nevada": "Carson City",
#     "New Hampshire": "Concord",
#     "New Jersey": "Trenton",
#     "NewMexico": "Santa Fe",
#     "New York": "Albany",
#     "North Carolina": "Raleigh",
#     "North Dakota": "Bismarck",
#     "Ohio": "Columbus",
#     "Oklahoma": "Oklahoma City",
#     "Oregon": "Salem",
#     "Pennsylvania": "Harrisburg",
#     "Rhode Island": "Providence",
#     "South Carolina": "Columbia",
#     "South Dakota": "Pierre",
#     "Tennessee": "Nashville",
#     "Texas": "Austin",
#     "Utah": "Salt Lake City",
#     "Vermont": "Montpelier",
#     "Virginia": "Richmond",
#     "Washington": "Olympia",
#     "WestVirginia": "Charleston",
#     "Wisconsin": "Madison",
#     "Wyoming": "Cheyenne",
# }

# for quizNum in range(35):
#     #Crate the quiz and answer key files
#     quizfile = open(f"capitalsquiz{quizNum + 1}.txt", "w")
#     answerfile = open(f"capitalsquiz_answers{quizNum + 1}.txt", "w")
    
#     #Write out the header for the quiz
#     quizfile.write("Name:\n'nDate:\n\nPeriod:\n\n")
#     quizfile.write((" " * 20) + f"State Capitals quiz (Form{quizNum + 1})")
#     quizfile.write("\n\n")
    
#     #Shuffle the order of the states
#     states = list(capitals.keys())
#     random.shuffle(states)
    
#     #loop through all 50 states, making a question for each
#     for questionNum in range(50):
#         #get right and wrong answers
#         correctAnswer = capitals[states[questionNum]]
#         wrongAnswer = list(capitals.values())
#         del wrongAnswer[wrongAnswer.index(correctAnswer)]
#         wrongAnswer = random.sample(wrongAnswer, 3)
#         answerOptions = wrongAnswer + [correctAnswer]
#         random.shuffle(answerOptions)
        
#         # Write the question and answer options to the quiz file
#         quizfile.write(f"{questionNum + 1}. What is the capital of {states[questionNum]}?\n")
#         for i in range(4):
#             quizfile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n")
#         quizfile.write("\n")
        
#         # Write the answer key to a file
#         answerfile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
#     quizfile.close()
#     answerfile.close()

# UPDATABLE MULTI-CLIPBOARD
# import shelve, pyperclip, sys

# mcbShelf = shelve.open("mcb")

# if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
#     mcbShelf[sys.argv[2]] = pyperclip.paste()
# elif len(sys.argv) == 2:
    
#     # List keywords and load content
#     if sys.argv[1].lower == "list":
#         pyperclip.copy(str(list(mcbShelf.keys())))
#     elif sys.argv[1] in mcbShelf:
#         pyperclip.copy(mcbShelf[sys.argv[1]])
# mcbShelf.close()