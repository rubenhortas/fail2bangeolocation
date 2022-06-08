class CountryStats:
    name: str
    cities: dict

    def __init__(self, name, city):
        self.name = name
        self.cities = {}
        self.add_city(city)

    def add_city(self, city):
        if city in self.cities:
            self.cities[city] = self.cities[city] + 1
        else:
            self.cities[city] = 1

    def get_count(self):
        count = 0

        for city in self.cities:
            count = count + self.cities[city]

        return count
