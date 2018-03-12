
import random


def main():

    amount_of_lines = int(input("How many quick picks? "))
    for i in range(amount_of_lines):
        numbers = []
        random_number = random.randint(1, 45)
        numbers.append(random_number)
        for j in range(5):
            while random_number in numbers:
                random_number = random.randint(1, 45)
            numbers.append(random_number)
        list_of_numbers = [number for number in numbers]
        sorted_numbers = sorted(list_of_numbers)
        outputting_numbers(sorted_numbers)


def outputting_numbers(sorted_numbers):
    for number in sorted_numbers:
        if number == max(sorted_numbers):
            print("{:2}".format(number), end='\n')
        else:
            print("{:2}".format(number), end=' ')


main()
