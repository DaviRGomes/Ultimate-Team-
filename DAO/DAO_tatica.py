from bson import ObjectId
from typing import List, Optional
from entity.Tatica import Tatica

class TaticaDAO:
    def __init__(self, collection, player_dao):
        self.collection = collection
        self.player_dao = player_dao
         # PlayerDAO instance to fetch players

    def create_tatica(self, tatica: Tatica, user_id: str) -> str:  # Alterado para user_id
        if len(tatica.players) > 11:
            raise ValueError("A tactical formation can only have up to 11 players.")
        
        player_ids = [ObjectId(player._id) for player in tatica.players]
        
        tatica_data = {
            "nome_formacao": tatica.nome_formacao,
            "players": player_ids,
            "user_id": ObjectId(user_id),
            "quimica": tatica.quimica
        }
        result = self.collection.insert_one(tatica_data)
        print(f"Tática created: {tatica.nome_formacao} - ID: {result.inserted_id}")
        return str(result.inserted_id)


    def read_tatica(self, tatica_id: str) -> Optional[Tatica]:
        data = self.collection.find_one({"_id": ObjectId(tatica_id)})
        if not data:
            return None

        # Resolve player references using player_dao
        players = []
        for player_id in data["players"]:
            player = self.player_dao.read_player(str(player_id))
            if player:
                players.append(player)
        
        return Tatica(
            nome_formacao=data["nome_formacao"],
            players_escalados=players
        )

    def update_tatica(self, tatica_id: str, update_data: dict) -> bool:
        if "players" in update_data:
            if len(update_data["players"]) > 11:
                raise ValueError("The tactic cannot have more than 11 players.")
            # Convert list of Player objects to IDs
            update_data["players"] = [ObjectId(p._id) for p in update_data["players"]]
        
        result = self.collection.update_one(
            {"_id": ObjectId(tatica_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    def delete_tatica(self, tatica_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(tatica_id)})
        return result.deleted_count > 0

    def find_all_taticas(self, user_id: str) -> List[Tatica]:
        taticas = []
        try:
            for data in self.collection.find({"user_id": ObjectId(user_id)}): 
                players = []
                for player_id in data["players"]:
                    player = self.player_dao.read_player(str(player_id))
                    if player:
                        players.append(player)
                
                tatica = Tatica(
                    nome_formacao=data["nome_formacao"],
                    players_escalados=players,
                    quimica=data.get("quimica", 0)
                )
                taticas.append(tatica)
        except Exception as e:
            print(f"Error fetching tactics: {str(e)}")
        
        return taticas
