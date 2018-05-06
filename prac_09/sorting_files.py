import shutil
import os


def main():
    print("Current directory is", os.getcwd())
    os.chdir('FilesToSort')
    print(os.listdir('.'))

    for filename in os.listdir('.'):
        name_and_extention = filename.split('.')
        file_extention = name_and_extention[1]
        if not os.path.exists(file_extention):
            os.mkdir(file_extention)
        shutil.move(filename, file_extention)

main()