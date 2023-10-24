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

# print("is +254 790 963 a kenyan number")
# print(is_kenyan_number("+254 790 963"))

