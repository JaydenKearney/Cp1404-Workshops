# numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = 10
# numbers[-1] = 1
# print(numbers[1:7])
# print(9 in numbers)



"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    creating_report(incomes, months)


def creating_report(incomes, months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()