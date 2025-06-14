from typing import List
from entity.Player import Player
from entity.Tatica import Tatica

class User:
    def __init__(self, username: str, nome_time: str, cards: List[Player] = None, taticas: List[Tatica] = None, _id=None):
        self.username = username
        self.nome_time = nome_time
        self.cards = cards if cards is not None else []
        self.taticas = taticas if taticas is not None else [] 
        self._id = _id
    
    def adicionar_carta(self, player: Player):
        self.cards.append(player)
    
    def criar_tatica(self, nome_formacao: str, jogadores_ids: List[str]):
        # Verifica se todos os jogadores estão na coleção do usuário
        jogadores_escalados = []
        for player_id in jogadores_ids:
            player = next((p for p in self.cards if str(p._id) == player_id), None)
            if not player:
                raise ValueError(f"Jogador com ID {player_id} não encontrado na sua coleção")
            jogadores_escalados.append(player)
        
        # Cria a nova tática
        nova_tatica = Tatica(nome_formacao, jogadores_escalados)
        self.taticas.append(nova_tatica)
        return nova_tatica
    
    def __str__(self):
        return f"Usuário: {self.username} | Time: {self.nome_time} | Cartas: {len(self.cards)} | Táticas: {len(self.taticas)} | ID: {self._id}"