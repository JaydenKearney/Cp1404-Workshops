
class Guitar():
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """
        Get year from above
        subtract year from current and get age
        :return: age
        """
        self.guitar_age = 2018 - self.year
        return self.guitar_age

    def is_vintage(self):
        if self.guitar_age >= 50:
            return True
        else:
            return False

    def __str__(self):
        """
        :return: proper string formatting.
        """
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)