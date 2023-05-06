# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

from pathlib import Path
input_folder = input("Enter the name of the folder you want to explore for JPG files: ")
given_folder = Path(f'/Users/13392/{input_folder}')

for each_item in given_folder.iterdir():
    if each_item.is_file():
        if ".jpg" in each_item.name:
            print(str(given_folder) + ": " + str(each_item.name))
    elif each_item.is_dir():
        for sub_item in each_item.iterdir():
            if sub_item.is_file():
                if ".jpg" in sub_item.name:
                    sub_item_path = given_folder.joinpath(each_item)
                    print(str(sub_item_path) + ": " + str(sub_item.name))