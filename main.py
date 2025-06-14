from database.database import Database
from DAO.DAO_country import CountryDAO
from DAO.DAO_league import LeagueDAO
from DAO.DAO_team import TeamDAO
from DAO.DAO_player import PlayerDAO
from DAO.DAO_user import UserDAO
from DAO.DAO_tatica import TaticaDAO
from database.menuCLI import UltimateTeamCLI

def main():
    db = Database("UltimateTeam_FIFA")

    country_dao = CountryDAO(db.get_collection("countries"))
    league_dao = LeagueDAO(db.get_collection("leagues"), country_dao)
    team_dao = TeamDAO(db.get_collection("teams"), league_dao)
    player_dao = PlayerDAO(db.get_collection("players"), team_dao, country_dao)
    tatica_dao = TaticaDAO(db.get_collection("tactics"), player_dao)
    user_dao = UserDAO(db.get_collection("users"), player_dao, tatica_dao)
    cli = UltimateTeamCLI(
        country_dao=country_dao,
        league_dao=league_dao,
        team_dao=team_dao,
        player_dao=player_dao,
        user_dao=user_dao,
        tatica_dao=tatica_dao
    )
    cli.run()

if __name__ == "__main__":
    main()
