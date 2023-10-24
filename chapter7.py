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
    
def is_kenyan_number(number):
    if len(number) != 12:
        return False
    
    if number[:4] != "+254":
            return False
    
    if number[4] != " ":
        return False
    
    for i in range(5, 8):
        if not number[i].isdecimal():
            return False
        
    if number[8] != " ":
        return False
    
    for i in range(9, 12):
        if not number[i].isdecimal():
            return False
    
    return True

message = "Call me at +254 724 867 356 tomorrow. +254 726 789 674 is my office."
for i in range(len(message)):
    chunk = message[i:i+12] # it extracts a substring from the message that is potential kenyan phone number.
    if is_kenyan_number(chunk): # checks if its valid kenyan number, then prints the number.
        print(f"Phone number found: {chunk}")
print("Done!")

