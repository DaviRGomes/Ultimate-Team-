from entity.Country import Country
class League:
    def __init__(self, name: str, country: Country, _id = None):
        self.name = name
        self.country = country
        self.country_id = country._id 
        self._id = _id
    
    def __str__(self):
        return f"Liga: {self.name} | País: {self.country.name} | ID: {self._id}"