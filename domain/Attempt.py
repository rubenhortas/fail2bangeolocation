class Attempt:
    def __init__(self, country):
        self.country = country
        self.cities = {}
        self.total = 0

    def add_city(self, city):
        if city in self.cities:
            self.cities[city] = self.cities[city] + 1
        else:
            self.cities[city] = 1

        self.total = self.total + 1
