class Attempt:
    def __init__(self, country):
        self.__country = country
        self.__cities = {}
        self.__total = 0

    def get_country(self):
        return self.__country

    def get_cities(self):
        return self.__cities

    def get_total(self):
        return self.__total

    def add_city(self, city):
        if city in self.__cities:
            self.__cities[city] = self.__cities[city] + 1
        else:
            self.__cities[city] = 1

        self.__total = self.__total + 1

    def __eq__(self, obj):
        return self.__country == obj.get_country() and self.__cities == obj.get_cities() and self.__total == obj.get_total()
