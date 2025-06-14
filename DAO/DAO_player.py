from bson import ObjectId
from typing import List, Optional
from entity.Player import Player


class PlayerDAO:
    def __init__(self, collection, team_dao, country_dao):
        self.collection = collection
        self.team_dao = team_dao  # Instância de TeamDAO
        self.country_dao = country_dao  # Instância de CountryDAO

    def create_player(self, player: Player) -> str:
        player_data = {
            "name": player.name,
            "team": ObjectId(player.team_id),
            "country": ObjectId(player.country_id),
            "position": player.position
        }
        result = self.collection.insert_one(player_data)
        print(f"Jogador criado: {player.name} - ID: {result.inserted_id}")
        return str(result.inserted_id)

    def read_player(self, player_id: str) -> Optional[Player]:
        data = self.collection.find_one({"_id": ObjectId(player_id)})
        if not data:
            return None

        # Resolver referências usando os DAOs injetados
        team = self.team_dao.read_team(str(data["team"]))
        country = self.country_dao.read_country(str(data["country"]))

        return Player(
            name=data["name"],
            team=team,
            country=country,
            position=data["position"],
            _id=data["_id"]
        )

    def update_player(self, player_id: str, update_data: dict) -> bool:
        if "team" in update_data:
            update_data["team"] = ObjectId(update_data["team"])
        if "country" in update_data:
            update_data["country"] = ObjectId(update_data["country"])
        result = self.collection.update_one(
            {"_id": ObjectId(player_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    def delete_player(self, player_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(player_id)})
        return result.deleted_count > 0

    def find_all_players(self) -> List[Player]:
        players = []
        for data in self.collection.find():
            team = self.team_dao.read_team(str(data["team"]))
            country = self.country_dao.read_country(str(data["country"]))

            players.append(Player(
                    name=data["name"],
                    team=team,
                    country=country,
                    position=data["position"],
                    _id=data["_id"]
                ))
        return players
    def find_by_team(self, team_id: str) -> List[Player]:
        players = []
        for data in self.collection.find({"team": ObjectId(team_id)}):
            team = self.team_dao.read_team(team_id) 
            country = self.country_dao.read_country(str(data["country"]))
            
            players.append(Player(
                name=data["name"],
                team=team,
                country=country,
                position=data["position"],
                _id=data["_id"]
            ))
        return players