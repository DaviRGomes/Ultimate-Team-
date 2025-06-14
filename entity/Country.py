class Country:
    def __init__(self, name: str, _id = None):
        self.name = name
        self._id = _id
    
    def __str__(self):
        return f"País: {self.name} | ID: {self._id}"