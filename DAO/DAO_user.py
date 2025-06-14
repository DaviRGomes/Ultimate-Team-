from bson import ObjectId
from typing import List, Optional
from entity.User import User

class UserDAO:
    def __init__(self, collection, player_dao, tatica_dao):
        self.collection = collection
        self.player_dao = player_dao
        self.tatica_dao = tatica_dao

    def create_user(self, user: User) -> str:
        user_data = {
            "username": user.username,
            "nome_time": user.nome_time,
            "cards": [ObjectId(p._id) for p in user.cards],
            "taticas": [ObjectId(t._id) for t in user.taticas]
        }
        result = self.collection.insert_one(user_data)
        user._id = str(result.inserted_id)
        return user._id

    def read_user(self, user_id: str) -> Optional[User]:
        data = self.collection.find_one({"_id": ObjectId(user_id)})
        if not data:
            return None

        cards = []
        for p_id in data["cards"]:
            player = self.player_dao.read_player(str(p_id))
            if player:
                cards.append(player)

        taticas = []
        for t_id in data["taticas"]:
            tatica = self.tatica_dao.read_tatica(str(t_id))
            if tatica:
                taticas.append(tatica)

        return User(
            username=data["username"],
            nome_time=data["nome_time"],
            cards=cards,
            taticas=taticas,
            _id=str(data["_id"])
        )

    def update_user(self, user_id: str, update_data: dict) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    def delete_user(self, user_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0

    def find_all_user(self) -> List[User]:
        return [self.read_user(str(j["_id"])) for j in self.collection.find()]

    def add_card(self, user_id: str, player_id: str) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$addToSet": {"cards": ObjectId(player_id)}}
        )
        return result.modified_count > 0

    def remove_card(self, user_id: str, player_id: str) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$pull": {"cards": ObjectId(player_id)}}
        )
        return result.modified_count > 0

    def add_tatica(self, user_id: str, tatica_id: str) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$addToSet": {"taticas": ObjectId(tatica_id)}}
        )
        return result.modified_count > 0
    
    def listar_cartas_usuario(self, user_id: str) -> None:
        user = self.read_user(user_id)

        if not user or not user.cards:
            print("O usuário não possui cartas ainda!")
            return
        
        print(f"\nCartas do usuário {user.username}:")
        print("-" * 50)
        for i, card in enumerate(user.cards, 1):
            team_name = card.team.name if card.team else "Sem time"
            country_name = card.country.name if card.country else "Sem país"
            
            print(f"{i}. {card.name}")
            print(f"   Posição: {card.position}")
            print(f"   Time: {team_name}")
            print(f"   País: {country_name}")
            print("-" * 50)