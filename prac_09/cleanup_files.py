"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')
    walk_file = ".."
    count = 0
    # loop through each file in the (original) directory
    os.chdir(walk_file)  # .. means "up" one directory
    for dir_name, subdir_list, file_list in os.walk('.'):
        # print("In", dir_name)
        # print("\tcontains subdirectories:", subdir_list)
        # print("\tand files:", file_list)
        if dir_name == '.':
            print("Top dir")
        # elif dir_name == ".\Christmas\temp":
        #     print("Temp file")
        else:
            print(file_list)
            for filename in file_list:
                # ignore directories, just process files
                if not os.path.isdir(filename):
                    new_name = get_fixed_filename(filename)
                    print(new_name)

            # NOTE: These options won't just work...
            # they show you ways of renaming and moving files,
            # but you need to have valid filenames. You can't make a file with
            # a blank name, and on Windows you can't have files with the same
            # characters but different case (e.g. a.TXT and A.txt)
            # So, you need to get valid filenames before you can use these.

            # Option 1: rename file to new name - in place
                    os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)

            # Processing subdirectories using os.walk()

        walk_file = '.'




def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    for i, letter in enumerate(filename):
        previous_letter = i - 1
        if filename[previous_letter] == "_":
            letter = letter.upper()
        letter_check_lower = letter.islower()
        letter_check_upper = letter.isupper()
        last_letter = len(filename) - 1
        next_letter = i + 1
        if i is not last_letter:
            name_check = filename[next_letter].isupper()
        else:
            name_check = False
        new_name = new_name + letter
        if letter_check_lower and name_check:
            new_name = new_name + "_"
        elif letter_check_upper and name_check:
            new_name = new_name + "_"
    return new_name


main()