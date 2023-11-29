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
response = pyip.inputNum(blockRegexes=[r"[034567]"])
