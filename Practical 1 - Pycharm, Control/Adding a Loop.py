def main():
    """
    Adding a loop to the sales exercise from above,
    so that the program repeatedly asks for the user's sales and
    prints the bonus until they enter a negative number.
    """
    while sales >= 0:
        sales = float(input("Enter sales: $"))
        if sales < 1000:
            bonus = sales * 0.1
            print(str("Result: ${:.2f} F".format(bonus)))
        else:
            bonus = sales * 0.15
            print(str("Result: ${:.2f} F".format(bonus)))

main()
