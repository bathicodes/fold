import pathlib
import os
import random
import shutil


def fold(path: str, train_size:float = 0.8, test_size: float = 0.2):

    counter = 0
    test_file_counter = 0
    train_file_counter = 0

    file_names = []
    

    # making test directory with in the target folder
    try:
        directory = "Test"
        parent_dir = path
        new_dir = os.path.join(parent_dir,directory)
        os.mkdir(new_dir)
        print("Test directory created!")
    except:
        print("Directory already exisited!")


    # split train and test files
    desktop = pathlib.Path(path)
    for files in desktop.iterdir():
        if files.is_file():
            if files.name == ".DS_Store":
                print("DS.Store found!!!")
                delete_file = pathlib.Path(files)
                print(files)
                delete_file.unlink()
            else:
                counter += 1
                file_names.append(files.as_posix())


    test_file_counter = counter * test_size
    
    # Randomly split test files and save them in a seperate list
    list_of_test_files = random.sample(file_names, int(test_file_counter))

    # move selected test files to the test folder
    dest_path = new_dir
    for i in list_of_test_files:
        print(rf"{i}")
        shutil.move(i, dest_path)

    # print("---------------------------------------")
    # print(f"Found {counter} files")
    # print("---------------------------------------")
    # print(f"Test file count: {int(test_file_counter)}")
    # print("---------------------------------------")
    # print(f"Train file count: {int(train_file_counter)}")
    # print("---------------------------------------")
    # print(file_names)
    # print("---------------------------------------")
    # print(list_of_test_files)

    

fold("/Users/bathiyaseneviratne/Desktop/ll",train_size=0.8, test_size=0.2)