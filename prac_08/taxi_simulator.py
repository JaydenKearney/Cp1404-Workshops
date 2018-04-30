from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    bill = 0.0
    print("Lets Drive!")
    menu_choice = input("q)uit, c)hoose taxi, d)rive").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            taxi_choice = int(input("Choose taxi: "))
            print("Bill to date: ${:.2f}".format(bill))

        elif menu_choice == "D":
            distance = int(input("Drive how far? (in km)"))
            try:
                taxis[taxi_choice].drive(distance)
                fare = taxis[taxi_choice].get_fare()
                print("Your {} trip cost you ${:.2f}".format(taxis[taxi_choice].name, fare))

            except UnboundLocalError:
                taxis[0].drive(distance)
                fare = taxis[0].get_fare()
                print("Your {} trip cost you ${:.2f}".format(taxis[taxi_choice].name, fare))

            bill += fare
            print("Bill to date: ${:.2f}".format(bill))

        print("Lets Drive!")
        menu_choice = input("q)uit, c)hoose taxi, d)rive").upper()

    print("Your total trip cost you ${:.2f}".format(bill))


main()
