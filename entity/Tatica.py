from entity.Player import Player
from typing import List,Optional

class Tatica:
    """
    Formação tática, com até 11 players escolhidos manualmente dentre os cards do Jogador.
    """
    def __init__(self, nome_formacao: str, players_escalados: List[Player], quimica: Optional[int] = None):
        if len(players_escalados) > 11:
            raise ValueError("Uma formação tática só pode ter até 11 players.")
        self.nome_formacao = nome_formacao
        self.players = players_escalados
        self.quimica = quimica if quimica is not None else self.calcular_quimica()

    def calcular_quimica(self) -> int:
        if not self.players:
            return 0
            
        n = len(self.players)
        if n <= 1:
            return 100

        total_pontos = 0
        max_pontos = 3 * (n * (n - 1) // 2)

        for i in range(n):
            for j in range(i + 1, n):
                p1 = self.players[i]
                p2 = self.players[j]
                
                # Verifica se os players têm time e país definidos
                if not hasattr(p1, 'team') or not hasattr(p2, 'team'):
                    continue
                if not hasattr(p1, 'country') or not hasattr(p2, 'country'):
                    continue
                
                if p1.team and p2.team and p1.team.name == p2.team.name:
                    total_pontos += 3
                elif p1.team.league and p2.team.league and p1.team.league.name == p2.team.league.name:
                    total_pontos += 2
                elif p1.country and p2.country and p1.country.name == p2.country.name:
                    total_pontos += 1

        quimica_normalizada = (total_pontos / max_pontos) * 100 if max_pontos > 0 else 0
        return round(quimica_normalizada)
    
    def __str__(self):
        nomes = ', '.join([j.name for j in self.players])
        return f"Tática: {self.nome_formacao} | players: {nomes} | Química: {self.quimica}%"