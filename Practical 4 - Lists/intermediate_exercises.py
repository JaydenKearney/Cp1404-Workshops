
def main():
    numbers = []
    for i in range(5):
        user_input = int(input("Number: "))
        numbers.append(user_input)
    number_average = sum(numbers) / len(numbers)
    print("The first number is {}.".format(numbers[0]))
    print("The last number is {}.".format(numbers[-1]))
    print("The smallest number is {}.".format(min(numbers)))
    print("The largest number is {}.".format(max(numbers)))
    print("The average of the numbers is {}.".format(int(number_average)))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    name = input("Please input your name: ")
    if name in usernames:
        print("Access Granted")
    else:
        print("Access Denied")



    

main()
