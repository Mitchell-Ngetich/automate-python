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
import random, time 

number_questions = 10
correct_answers = 0
for question_Num in range(number_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f"#{question_Num + 1}: {num1} * {num2}  "
    
    try:
        pyip.inputStr(prompt, allowRegexes=["^%s$" % (num1 * num2)],
                      blockRegexes=[(".*", "Incorrect")],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries!")
    else:#runs if no exceptios were raised in the try block
        print("Correct!")
        correct_answers += 1
    
    time.sleep(1)
print(f"Score: {correct_answers}/ {number_questions}")