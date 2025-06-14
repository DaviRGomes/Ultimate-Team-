from bson import ObjectId
from typing import List, Optional
from entity.Team import Team
from entity.Player import Player

class TeamDAO:
    def __init__(self, collection, league_dao):
        self.collection = collection
        self.league_dao = league_dao
        self.player_dao = None 

    def create_team(self, team: Team) -> str:
        team_data = {
            "name": team.name,
            "league_id": ObjectId(team.league_id)
        }
        result = self.collection.insert_one(team_data)
        print(f"Time criado: {team.name} - ID: {result.inserted_id}")
        return str(result.inserted_id)

    def read_team(self, team_id: str) -> Optional[Team]:
        data = self.collection.find_one({"_id": ObjectId(team_id)})
        if data:
            league_id = str(data["league_id"])
            league = self.league_dao.read_league(league_id)
            return Team(
                name=data["name"],
                league=league,
                _id=data["_id"]
            )
        return None

    def update_team(self, team_id: str, update_data: dict) -> bool:
        if "league_id" in update_data:
            update_data["league_id"] = ObjectId(update_data["league_id"])
        result = self.collection.update_one(
            {"_id": ObjectId(team_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    def delete_team(self, team_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(team_id)})
        return result.deleted_count > 0

    def find_all_teams(self) -> List[Team]:
        teams = []
        for data in self.collection.find():
            league_id = str(data["league_id"])
            league = self.league_dao.read_league(league_id)
            teams.append(Team(
                name=data["name"],
                league=league,
                _id=data["_id"]
            ))
        return teams

    def set_player_dao(self, player_dao):
            self.player_dao = player_dao

    def get_team_players(self, team_id: str) -> List['Player']:
            if not self.player_dao:
                raise ValueError("PlayerDAO não foi injetado no TeamDAO.")
            return self.player_dao.find_by_team(team_id)