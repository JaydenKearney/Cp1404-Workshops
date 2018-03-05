
def main():
    user_name = get_name()
    letter_frequency = input("Please input a frequency: \n")
    print_name(user_name, letter_frequency)


def print_name(name, frequency):
    for i in range(0, len(name), frequency):
        print(name[i])


def get_name():
    user_name = input("please input your name: \n")
    while len(user_name) == 0:
        print("Name cannot be left blank.")
        user_name = input("please input your name: \n")
    return user_name


main()