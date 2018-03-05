def main():
    name = input("Please input your name: \n")
    output_file = open("name.txt", "a")
    print("Your name is {}.".format(name), file=output_file)
    output_file.close()

    # input_file = open("numbers.txt", "r")
    # result = 0
    # amount_lines = input_file.read()
    # input_file.seek(0)
    # try:
    #     for i in range(len(amount_lines)):
    #         result = result + int(input_file.readline())
    # except ValueError:
    #     pass
    # print(result)
    # input_file.close()

    input_file = open("numbers.txt", "r")
    result = 0
    for line in input_file:
        result += int(line)
    print(result)
    input_file.close()
main()