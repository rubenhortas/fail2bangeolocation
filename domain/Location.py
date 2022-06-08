class Location:
    country: str
    city: str

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city
