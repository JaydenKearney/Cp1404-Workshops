def main():
    """"
    The program allows the user to enter the number of items and the price of each different item.
    Then the program computes and displays the total price of those items.
    If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen
    """
    number_of_items = int(input("Number of items: "))
    while number_of_items >= 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    overall_price = 0
    for i in range(number_of_items):
        price_of_item = int(input("Price of item: "))
        overall_price = overall_price + price_of_item
    if overall_price > 100:
        discount = overall_price * 0.1
        overall_price -= discount
    print(overall_price)

main()