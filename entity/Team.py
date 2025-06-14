from typing import List, Optional

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entity.League import League
    from entity.Player import Player

class Team:
    def __init__(self, name: str, league: 'League', players: Optional[List['Player']] = None, _id=None):
        self.name = name
        self.league = league
        self.league_id = league._id
        self.players = players if players is not None else []
        self._id = _id
    
    def __str__(self):
        return f"Time: {self.name} | Liga: {self.league.name} | ID: {self._id}"