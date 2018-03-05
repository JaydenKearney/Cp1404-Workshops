def main():
    """
    CP1404/CP5632 - Practical
    Pseudocode for temperature conversion
    """

    MENU = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit
    """
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_celcius_to_farenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = convert_farenheit_to_celcius()
            print("Result: {:.2f} F".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_farenheit_to_celcius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celcius_to_farenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()