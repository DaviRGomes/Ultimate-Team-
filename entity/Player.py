from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entity.Team import Team
    from entity.Country import Country

class Player:
    def __init__(self, name: str, team: 'Team', country: 'Country', position: str, _id=None):
        self.name = name
        self.team = team
        self.country = country
        self.position = position
        self.team_id = team._id
        self.country_id = country._id
        self._id = _id

    def __str__(self):
        return f"Jogador: {self.name} | Time: {self.team.name} | País: {self.country.name} | Posição: {self.position} | ID: {self._id}"