# write a script that searches an user specified
# folder for .jpg files and compiles a list that
# includes the directory of all said files. 

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