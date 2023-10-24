#! - Building A multi-cliboard automatic messages program.
import sys, pyperclip

# pyperclip.copy("Hello, world!")
# print(pyperclip.paste())

# TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
#         'busy': """Sorry, can we do this later this week or next week?""",
#         'upsell': """Would you consider making this a monthly donation?"""}


# if len(sys.argv) < 2:
#     print("Usage: python mclip.py [keyphrase] - copy phrase text")
#     sys.exit()
    
# keyphrase = sys.argv[1]

# if keyphrase in TEXT:
#         pyperclip.copy(TEXT[keyphrase])
#         print("Text for " + keyphrase +  " copied to clipboard.")
#         print(pyperclip.paste())
# else: print("There is no text for " + keyphrase)

# Adding Bullets to Wiki Markup - Adds wikipedia bullet points to the start of each line of text on the clipboard


# Copy text from the clipboard
# text = pyperclip.paste()
# print(text)

# # Separate lines and add stars
# lines = text.split("\n")

# # Loop through all indexes in lines and add a star to each string in lines list
# for i in range(len(lines)):
#     lines[i] = "* " + lines[i]
#     print(lines[i])

# # Since .copy() expects a single line, not a list, we have to join the lines
# text = "\n".join(lines)
# print(text)

# # Copy the modified text back to the clipboard
# pyperclip.copy(text)

# A Short Program: Pig Latin(Translates english to pig latin)

# message = input("Enter the english message to translate into Pig Latin: ")

# vowels = ("a", "e", "i", "o", "u")
# pig_latin = []
# input_message = message.split(" ")

# for word in input_message:
#         # separate the non letters at the start of this word
#         prefix_non_letters = ''
#         while len(word) > 0 and not word[0].isalpha():
#                 prefix_non_letters += word[0]
#                 word = word[1:]
#         if len(word) == 0:
#                 pig_latin.append(prefix_non_letters)
#                 continue
        
#         #separate the non-letters at the end of this word
#         suffix_non_letters = ''
#         while not word[-1].isalpha():
#                 suffix_non_letters += word[-1]
#                 word = word[:-1]
                
#         was_upper = word.isupper()
#         was_title = word.istitle()   
#         word = word.lower()
        
        
#         #separate the consonants at the start of the word
#         prefix_consonants = ''
#         while len(word) > 0 and not word[0] in vowels:
#                 prefix_consonants += word[0]
#                 word = word[1:]
                
#         #Add the Pig latin ending to the word
#         if prefix_consonants != "":
#                 word += prefix_consonants + "ay"
#         else: word += "yay"

        
#         # set the word back to uppercase or title case
#         if was_upper:
#                 word = word.upper()
#         if was_title:
#                 word = word.title()
#         pig_latin.append(prefix_non_letters + word + suffix_non_letters)
        
# #join all the words back together into a single string
# print(" ".join(pig_latin))


# output should look like this:
#  apples Alice  dogs
#   oranges   Bob  cats
#  cherries Carol moose
#    banana David goose

# def printTable(tableData):
#     if not tableData:
#         return  # If the table is empty, return without printing anything.

#     # Determine the number of rows and columns in the table
#     num_rows = len(tableData)
#     num_columns = len(tableData[0])

#     # Create a list to store the width of the longest element in each column
#     colWidths = [0] * num_columns

#     # Calculate the maximum width for each column
#     for col in range(num_columns):
#         for row in range(num_rows):
#             element = tableData[col][row]
#             colWidths[col] = max(colWidths[col], len(element))

#     # Print the table with right-justified columns
#     for col in range(num_columns):
#         for row in range(num_rows):
#             element = tableData[col][row]
#             # Print the element, right-aligned and padded with spaces to match the column width
#             print(element.rjust(colWidths[row]), end=" ")
#         # Move to the next row
#         print()

# # Example usage
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]
# printTable(tableData)

# def printTable(tableData):
#     if not tableData:
#         return  # If the table is empty, return without printing anything.

#     # Determine the number of rows and columns in the table
#     num_rows = len(tableData)
#     num_columns = len(tableData[0])

#     # Create a list to store the width of the longest element in each column
#     colWidths = [0] * num_columns

#     # Calculate the maximum width for each column
#     for col in range(num_columns):
#         for row in range(num_rows):
#             element = tableData[row][col]
#             colWidths[col] = max(colWidths[col], len(element))

#     # Print the transposed table with elements right-aligned and padded with spaces
#     for col in range(num_columns):
#         for row in range(num_rows):
#             element = tableData[row][col]
#             # Right-align the element and pad with spaces
#             print(element.rjust(colWidths[col]), end=" ")
#         # Move to the next column
#         print()

# # Example usage
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]

# printTable(tableData)