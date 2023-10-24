# Pattern matching with regular expressions

# def check_phone_number(text):
#     if len(text) != 12:
#         return False
    
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
        
#     if text[3] != "-":
#         return False
    
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
        
#     if text[7] != "-":
#         return False
    
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
        
#     return True
        
# print("is 415-555-4242 a phone number")
# print(check_phone_number("415-555-4242"))
# print("is Mitch-Mitch a phone number")
# print(check_phone_number("Mitch-Mitch"))
    
# def is_kenyan_number(number):
#     if len(number) != 12:
#         return False
    
#     if number[:4] != "+254":
#             return False
    
#     if number[4] != " ":
#         return False
    
#     for i in range(5, 8):
#         if not number[i].isdecimal():
#             return False
        
#     if number[8] != " ":
#         return False
    
#     for i in range(9, 12):
#         if not number[i].isdecimal():
#             return False
    
#     return True

# message = "Call me at +254 724 867 356 tomorrow. +254 726 789 674 is my office."
# for i in range(len(message)):
#     chunk = message[i:i+12] # it extracts a substring from the message that is potential kenyan phone number.
#     if is_kenyan_number(chunk): # checks if its valid kenyan number, then prints the number.
#         print(f"Phone number found: {chunk}")
# print("Done!")

#Creating Regex object
import re

# # Creating Regex object
# phone_number_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# mo = phone_number_regex.search("My number is: 415-555-4242.")
# #its not necessary to use mo
# print(f"Phone number found: {mo.group()}") #.group() is used to obtain the matched number

# kenyan_phone_number = re.compile(r"\+254 \d\d\d \d\d\d \d\d\d")
# #we escape even + coz its a special character
# match = kenyan_phone_number.search("My number is: +254 790 963 288")
# print(f"Phone number found: {match.group()}")


# sing parenthesis
# phone_number = re.compile(r"(d\d\d)-(\d\d\d-\d\d\d)")
# # used for grouping numbers
# mo = phone_number.search("My number is: 415-555-4242")
# mo.group(1) # will print 415
# mo.group(2) # will print 555-4242
# mo.group(0) # or group() without an argument # will print 415-555-4242

# # if you want to separate code and the number we have to escape the () with \
# phone_number2 = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d)")

#Matching with pipe
# hero_regex = re.compile(r"Batman|Tina Fey")
# mo2 = hero_regex.search("Tina Fey and Batman")
# print(mo2.group())

# OPtional matching with the question mark
# batRgex = re.compile(r"(Bat(wo)?man)")
# mo1 = batRgex.search("The Adventure of Batwoman")
# print(mo1.group()) # match only optionally

# matching zero or more with a star*

# bat_regex = re.compile(r"Bat(wo)*man")
# mo = bat_regex.search("The Adventures of Batwowowowowman")
# mo.group() # will print Batwowowowman coz it can match 0 or more tha one
# # it can also print Batman without "wo"

# Matching one or more with the plus +(match one or more)
# batRegex = re.compile(r"Bat(wo)+ man")
# mo = batRegex.search("The Adventures of Batwoman")
# print(mo.group()) # will print Bat Batwoman depending on the number of wo you have

# Matching specific repetitions with braces
# ha_regex = re.compile(r"(Ha){3}")
# mo = ha_regex.search("He said HaHaHa")
# print(mo.group()) # will print HaHaHa

# The findall() method
phone_number = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phone_number.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo.group()) # will print 415-555-9999 and 212-555-0000
