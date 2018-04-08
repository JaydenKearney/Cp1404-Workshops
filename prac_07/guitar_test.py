from prac_07.guitar_storage import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
print(gibson)
print(gibson.get_age())
print(gibson.is_vintage())
print("Gibson L-5 CES get_age() - Expected 96. Got {}".format(gibson.get_age()))

another_guitar = Guitar("Guitar", 2017, 2)
print(another_guitar)
print(another_guitar.get_age())
print(another_guitar.is_vintage())
print("Guitar get_age() - Expected 1. Got {}".format(another_guitar.get_age()))
