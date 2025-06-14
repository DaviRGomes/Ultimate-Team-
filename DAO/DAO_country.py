from bson import ObjectId
from typing import List, Optional
from entity.Country import Country

class CountryDAO:
    def __init__(self, collection):
        self.collection = collection

    def create_country(self, country: Country) -> str:
        country_data = {"name": country.name}
        result = self.collection.insert_one(country_data)
        print(f"País criado: {country.name} - ID: {result.inserted_id}")
        return str(result.inserted_id)

    def read_country(self, country_id) -> Optional[Country]:
        data = self.collection.find_one({"_id": ObjectId(country_id)})
        if data:
            return Country(name=data["name"], _id=data["_id"])
        return None

    def update_country(self, country_id: str, update_data: dict) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(country_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    def delete_country(self, country_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(country_id)})
        return result.deleted_count > 0

    def find_all_countries(self) -> List[Country]:
        return [Country(name=data["name"], _id=data["_id"]) for data in self.collection.find()]