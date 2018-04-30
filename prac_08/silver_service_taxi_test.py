from prac_08.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Hummer", 200, 4)
taxi.drive(18)
print("${:.2f}".format(taxi.get_fare()))
print(taxi)