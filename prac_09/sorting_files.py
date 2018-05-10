import shutil
import os


def main():
    print("Current directory is", os.getcwd())
    os.chdir('FilesToSort')
    print(os.listdir('.'))
    extentions = []
    # new_files = []
    filenames_and_extentions = {}
    for filename in os.listdir('.'):
        name_and_extention = filename.split('.')
        file_extention = name_and_extention[1]
        if not file_extention in extentions:
            print("Where would you like to sort {} files into?".format(file_extention))
            new_filename = input()
            filenames_and_extentions[file_extention] = new_filename
            if new_filename in os.listdir('.'):
                shutil.move(filename, new_filename)
                # new_files.append(new_filename)
            else:
                if not os.path.exists(new_filename):
                    os.mkdir(new_filename)
                    shutil.move(filename, new_filename)
            extentions.append(file_extention)
        else:
            # print(filenames_and_extentions[file_extention])
            shutil.move(filename, filenames_and_extentions[file_extention])






main()