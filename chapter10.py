# CHAPTER 10
import shutil, os
from pathlib import Path


# p = Path.home()

# # check the file and if it exists
# if not (p /"spam.text").exists():
#     print("The file spam.txt does not exist. Creating it...")
#     (p / "spam.txt").touch()
    
# # check the folder and if it exists  
# if not (p / "some_folder").exists():
#     print("The folder spam.txt does not exist. Creating it...")
#     (p / "some_folder").mkdir()
    
# # Now copy the file
# shutil.copy(p / "spam.txt", p / "some_folder")

# shutil.move("/bacon.text", "/eggs")

# from pathlib import Path
# for filename in Path.home().glob("*.txt"): #will delete all files with .txt extension.
#     # os.unlink(filename)
#     print(filename)

# import send2trash
# baconfile = open("bacon.txt", "a") # creaes the file
# print(baconfile.write("Bacon is not a vegetable."))
# baconfile.close()
# send2trash.send2trash("bacon.txt")

# Walking a directory Tree
import zipfile, os

# p = Path.home()
# # exampleZip = zipfile.ZipFile(p/"Python")
# # exampleZip.namelist()
# # print(os.listdir(p))
# print(list((p / "Python").glob("*")))