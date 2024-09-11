class Country:
    name = ''
    total = 0
    cities = {}

    def __init__(self, country: str, cities: dict, show_cities: bool):
        self.name = country
        self.total = sum(cities.values())
        self.cities = cities

        if show_cities:
            self._sort_cities()

        self._show_cities = show_cities

    def __eq__(self, other):
        return self.total == other.total and self.name == other.name

    def __lt__(self, other):
        return (self.total < other.total) or (self.total == other.total and self.name < other.name)

    def __gt__(self, other):
        return (self.total > other.total) or (self.total == other.total and self.name > other.name)

    def __repr__(self):
        if self._show_cities:
            return f"{self.name}: {self.total} -> {str(self.cities)}"
        else:
            return f"{self.name}: {self.total}"

    def __str__(self):
        if self._show_cities:
            f"{self.name}: {self.total} -> {str(self.cities)}"
        else:
            return f"{self.name}: {self.total}"

    def _sort_cities(self):
        # Sort alphabetically
        self.cities = {k: v for k, v in sorted(self.cities.items(), key=lambda item: item[0], reverse=False)}

        # Sort by number of attempts (descending)
        self.cities = {k: v for k, v in sorted(self.cities.items(), key=lambda item: item[1], reverse=True)}
