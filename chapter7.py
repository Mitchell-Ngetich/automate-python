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
# phone_number = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# mo = phone_number.findall("Cell: 415-555-9999 Work: 212-555-0000")
# print(mo.group()) # will print 415-555-9999 and 212-555-0000


# Character classes
# \d+\s\w+ which match all the numeric digits(\d+) followed by one or more whitespace characters(\s)
# followed by one or more letter/digit/underscore characters(\w+)
# holidayRegex = re.compile(r"\d+\s\w+")
# mo = holidayRegex.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge")
# print(mo)

# CREATING YOUR OWN CHARACTER CLASSES
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# myRegex = vowelRegex.findall("Mitchell ngetich Jepsergon BABY FOOD Umbrella")
# print(myRegex)

# robocop = re.compile(r'robocop', re.
'''
(\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    '''
    
    # Phone number and email address extractor


# phone_regex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?          # area code
#     (\s|-|\.)?                  # separator
#     (\d{3})                      # first 3 digits
#     (\s|-|\.)?                   #separator
#     (\d{4})                     # last 4 digits
#     (\s*(ext|x|ext\.)\s*(\d{2,5}))?   # extension 
#     )''', re.VERBOSE)

# text = "My number is 123-456-7890 and my office number is (123) 456-7890 ext 1234"

# phone_number = phone_regex.findall(text)
# phone_numbers = ["".join(match) for match in phone_number]
# print(phone_numbers)
# import pyperclip, re
# import requests 
# from bs4 import BeautifulSoup

# response = requests.get("https://nostarch.com/contactus/")
# soup = BeautifulSoup(response.content, "html.parser")

# my_text = soup.get_text()
# # print(my_text)

# phone_regex = re.compile(r'''
#     (\d{3}|\(\d{3}\))?          # area code
#     (\s|-|\.)?                 # separator
#     (\d{3})                      # first 3 digits
#     (\s|-|\.)                 # separator
#     (\d{4})                      # last 4 digits
#     (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension 
#     ''', re.VERBOSE)

# # for email regex
# email_regex = re.compile(r'''(
#     [a-zA-Z0-9._%+-]+              #username(the + sign means that the email can have 1+ of the characters in [])
#     @                              #symbol
#     [a-zA-Z0-9.-]+                 #domain name
#     (\.[a-zA-Z]{2,4})              #dot-something
#     )''', re.VERBOSE)

# # find matches

# my_text = str(pyperclip.paste())
# matches = []
# for groups in phone_regex.findall(my_text):
#     phone_num = "-".join([groups[1], groups[3], groups[5]])
#     if groups[5] != "":
#         phone_num += " x" + groups[5]
#     matches.append(phone_num)
# for groups in email_regex.findall(my_text):
#     matches.append(groups[0])
    
# #join the matches
# if len(matches) > 0:
#     pyperclip.copy("\n".join(matches))
#     print("Copied to clipboard")
#     print("\n".join(matches))
# else: print("No phone numbers or email addresses found")
