from bson import ObjectId
from typing import Optional, List
from entity.League import League

class LeagueDAO:
    def __init__(self, collection, country_dao):
        self.collection = collection
        self.country_dao = country_dao 

    def create_league(self, league: League) -> str:
        league_data = {
            "name": league.name,
            "country": ObjectId(league.country._id)  # Armazena o ObjectId do país
        }
        result = self.collection.insert_one(league_data)
        print(f"Liga criada: {league.name} - ID: {result.inserted_id}")
        return str(result.inserted_id)

    def read_league(self, league_id: str) -> Optional[League]:
        data = self.collection.find_one({"_id": ObjectId(league_id)})
        if not data:
            return None

        country_id = data["country"]
        country_obj = self.country_dao.read_country(str(country_id))
        if not country_obj:
            return None

        return League(
            name=data["name"],
            country=country_obj,
            _id=data["_id"]
        )

    def update_league(self, league_id: str, update_data: dict) -> bool:
        # Se atualizar o país, garanta que é um ObjectId
        if "country" in update_data:
            update_data["country"] = ObjectId(update_data["country"])
        result = self.collection.update_one(
            {"_id": ObjectId(league_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    def delete_league(self, league_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(league_id)})
        return result.deleted_count > 0
    
    def find_all_leagues(self) -> List[League]:
        leagues = []
        for data in self.collection.find():
            country = self.country_dao.read_country(str(data["country"]))

            leagues.append(League(
                    name=data["name"],
                    country=country,
                    _id=data["_id"]
                ))
        return leagues
    