
from entity.Country import Country
from entity.League import League
from entity.Team import Team
from entity.Player import Player
from entity.User import User
from entity.Tatica import Tatica

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")



class UltimateTeamCLI():
    def __init__(self, country_dao, league_dao, team_dao, player_dao, user_dao, tatica_dao):
        super().__init__()
        self.country_dao = country_dao
        self.league_dao = league_dao
        self.team_dao = team_dao
        self.player_dao = player_dao
        self.user_dao = user_dao
        self.tatica_dao = tatica_dao
    def run(self):
        print("Bem-vindo ao Ultimate Team FIFA CLI!")
        while True:
            print("\nEscolha a coleção:")
            print("1. País")
            print("2. Liga")
            print("3. Time")
            print("4. Jogador")
            print("5. Usuário")
            print("7. Sair")
            opcao = input("Opção: ")

            if opcao == '1':
                self.country_menu()
            elif opcao == '2':
                self.league_menu()
            elif opcao == '3':
                self.team_menu()
            elif opcao == '4':
                self.player_menu()
            elif opcao == '5':
                self.user_menu()
            elif opcao == '6':
                self.tactic_menu()
            elif opcao == '7' or opcao.lower() == 'quit':
                print("Goodbye!")
                break
            else:
                print("Opção inválida.")
    # ----------- PAÍS -----------
    def country_menu(self):
        while True:
            print("\n[País] Escolha a ação:")
            print("1. Criar")
            print("2. Ler")
            print("3. Atualizar")
            print("4. Deletar")
            print("5. Listar todos")
            print("6. Voltar")
            acao = input("Ação: ")
            if acao == '1':
                self.create_country()
            elif acao == '2':
                self.read_country()
            elif acao == '3':
                self.update_country()
            elif acao == '4':
                self.delete_country()
            elif acao == '5':
                self.list_countries()
            elif acao == '6':
                break
            else:
                print("Ação inválida.")

    def create_country(self):
        name = input("Nome do país: ")
        country = Country(name)
        self.country_dao.create_country(country)

    def read_country(self):
        country_id = input("ID do país: ")
        country = self.country_dao.read_country(country_id)
        print(country)

    def update_country(self):
        country_id = input("ID do país: ")
        new_name = input("Novo nome do país: ")
        self.country_dao.update_country(country_id, {"name": new_name})

    def delete_country(self):
        country_id = input("ID do país: ")
        self.country_dao.delete_country(country_id)

    def list_countries(self):
        countries = self.country_dao.find_all_countries()
        for country in countries:
            print(country)

    # ----------- LIGA -----------
    def league_menu(self):
        while True:
            print("\n[Liga] Escolha a ação:")
            print("1. Criar")
            print("2. Ler")
            print("3. Atualizar")
            print("4. Deletar")
            print("5. Listar todos")
            print("6. Voltar")
            acao = input("Ação: ")
            if acao == '1':
                self.create_league()
            elif acao == '2':
                self.read_league()
            elif acao == '3':
                self.update_league()
            elif acao == '4':
                self.delete_league()
            elif acao == '5':
                self.list_leagues()
            elif acao == '6':
                break
            else:
                print("Ação inválida.")

    def create_league(self):
        name = input("Nome da liga: ")
        country_id = input("ID do país: ")
        
        country = self.country_dao.read_country(country_id)
        
        if country:
            league = League(name, country)
            self.league_dao.create_league(league)
        else:
            print("País não encontrado!")

    def read_league(self):
        league_id = input("ID da liga: ")
        league = self.league_dao.read_league(league_id)
        print(league)

    def update_league(self):
        league_id = input("ID da liga: ")
        new_name = input("Novo nome da liga: ")
        self.league_dao.update_league(league_id, {"name": new_name})

    def delete_league(self):
        league_id = input("ID da liga: ")
        self.league_dao.delete_league(league_id)

    def list_leagues(self):
        leagues = self.league_dao.find_all_leagues()
        for league in leagues:
            print(league)

    # ----------- TIME -----------
    def team_menu(self):
        while True:
            print("\n[Time] Escolha a ação:")
            print("1. Criar")
            print("2. Ler")
            print("3. Atualizar")
            print("4. Deletar")
            print("5. Listar todos")
            print("6. Listar jogadores do time")
            print("7. Voltar")
            acao = input("Ação: ")
            if acao == '1':
                self.create_team()
            elif acao == '2':
                self.read_team()
            elif acao == '3':
                self.update_team()
            elif acao == '4':
                self.delete_team()
            elif acao == '5':
                self.list_teams()
            elif acao == '6':    
                self.list_players_in_team()
            elif acao == '7':
                break
            else:
                print("Ação inválida.")

    def create_team(self):
        name = input("Nome do time: ")
        league_id = input("ID da liga: ")

        league = self.league_dao.read_league(league_id)
        team = Team(name, league)
        self.team_dao.create_team(team)

    def read_team(self):
        team_id = input("ID do time: ")
        team = self.team_dao.read_team(team_id)
        print(team)

    def update_team(self):
        team_id = input("ID do time: ")
        new_name = input("Novo nome do time: ")
        self.team_dao.update_team(team_id, {"name": new_name})

    def delete_team(self):
        team_id = input("ID do time: ")
        self.team_dao.delete_team(team_id)

    def list_teams(self):
        teams = self.team_dao.find_all_teams()
        for team in teams:
            print(team)
    def list_players_in_team(self):
        team_id = input("ID do time: ")
        self.team_dao.set_player_dao(self.player_dao)
        team = self.team_dao.read_team(team_id)
        players = self.team_dao.get_team_players(team_id)
        if players:
            print(f"\nJogadores do time {team.name}:")
            for player in players:
                print(f"- {player.name} ({player.position})")
        else:
            print("Time não encontrado ou sem jogadores.")

    # ----------- JOGADOR -----------
    def player_menu(self):
        while True:
            print("\n[Jogador] Escolha a ação:")
            print("1. Criar")
            print("2. Ler")
            print("3. Atualizar")
            print("4. Deletar")
            print("5. Listar todos")
            print("6. Voltar")
            acao = input("Ação: ")
            if acao == '1':
                self.create_player()
            elif acao == '2':
                self.read_player()
            elif acao == '3':
                self.update_player()
            elif acao == '4':
                self.delete_player()
            elif acao == '5':
                self.list_players()
            elif acao == '6':
                break
            else:
                print("Ação inválida.")

    def create_player(self):
        name = input("Nome do jogador: ")
        position = input("Posição: ")
        team_id = input("ID do time: ")
        country_id = input("ID do país: ")

        team = self.team_dao.read_team(team_id)
        country = self.country_dao.read_country(country_id)

        player = Player(name,team,country,position)
        self.player_dao.create_player(player)

    def read_player(self):
        player_id = input("ID do jogador: ")
        player = self.player_dao.read_player(player_id)
        print(player)

    def update_player(self):
        player_id = input("ID do jogador: ")
        new_name = input("Novo nome do jogador: ")
        self.player_dao.update_player(player_id, {"name": new_name})

    def delete_player(self):
        player_id = input("ID do jogador: ")
        self.player_dao.delete_player(player_id)

    def list_players(self):
        players = self.player_dao.find_all_players()
        for player in players:
            print(player)

    # ----------- USUÁRIO/JOGADOR -----------
    def user_menu(self):
        while True:
            print("\n[Usuário] Escolha a ação:")
            print("1. Criar usuário")
            print("2. Ver detalhes do usuário")
            print("3. Atualizar usuário")
            print("4. Deletar usuário")
            print("5. Listar todos os usuários")
            print("6. Adicionar carta ao usuário")
            print("7. Remover carta do usuário")
            print("8. Gerenciar táticas do usuário")
            print("9. Listar cartas do usuário") 
            print("0. Voltar")
            acao = input("Ação: ")
            
            if acao == '1':
                self.create_user()
            elif acao == '2':
                self.read_user()
            elif acao == '3':
                self.update_user()
            elif acao == '4':
                self.delete_user()
            elif acao == '5':
                self.list_all_users()
            elif acao == '6':
                self.add_card_to_user()
            elif acao == '7':
                self.remove_card_from_user()
            elif acao == '8':
                self.manage_user_tactics()
            elif acao == '9':
                self.list_user_cards()
            elif acao == '0':
                break
            else:
                print("Ação inválida.")

    def create_user(self):
        username = input("Nome de usuário: ")
        nome_time = input("Nome do time: ")
        user = User(username, nome_time)
        user_id = self.user_dao.create_user(user)
        print(f"Usuário criado com ID: {user_id}")

    def read_user(self):
        user_id = input("ID do usuário: ")
        user = self.user_dao.read_user(user_id)
        if user:
            print("\nDetalhes do usuário:")
            print(user)
            print("\nCartas do usuário:")
            for card in user.cards:
                print(f"- {card.name} (ID: {card._id})")
            print("\nTáticas do usuário:")
            for tactic in user.taticas:
                print(tactic)
        else:
            print("Usuário não encontrado.")

    def update_user(self):
        user_id = input("ID do usuário: ")
        new_username = input("Novo nome de usuário: ")
        new_team = input("Novo nome do time: ")
        self.user_dao.update_user(user_id, {"username": new_username, "nome_time": new_team})

    def delete_user(self):
        user_id = input("ID do usuário: ")
        confirm = input(f"Tem certeza que deseja deletar o usuário {user_id}? (s/n): ")
        if confirm.lower() == 's':
            self.user_dao.delete_user(user_id)
            print("Usuário deletado com sucesso.")

    def list_all_users(self):
        users = self.user_dao.find_all_user()
        print("\nLista de usuários:")
        for user in users:
            print(f"ID: {user._id} | Usuário: {user.username} | Time: {user.nome_time}")

    def add_card_to_user(self):
        user_id = input("ID do usuário: ")
        card_id = input("ID da carta (Player) para adicionar: ")
        
        # Verifica se a carta existe
        card = self.player_dao.read_player(card_id)
        if not card:
            print("Carta não encontrada!")
            return
        
        # Adiciona a carta ao usuário
        self.user_dao.add_card(user_id, card_id)
        print("Carta adicionada com sucesso!")

    def remove_card_from_user(self):
        user_id = input("ID do usuário: ")
        card_id = input("ID da carta (Player) para remover: ")
        
        # Verifica se o usuário possui a carta
        user = self.user_dao.read_user(user_id)
        if not any(str(card._id) == card_id for card in user.cards):
            print("O usuário não possui esta carta!")
            return
        
        self.user_dao.remove_card(user_id, card_id)
        print("Carta removida com sucesso!")

    def list_user_cards(self):
        user_id = input("ID do usuário: ")
        self.user_dao.listar_cartas_usuario(user_id)

    def manage_user_tactics(self):
        user_id = input("ID do usuário: ")
        user = self.user_dao.read_user(user_id)
        if not user:
            print("Usuário não encontrado!")
            return
        self.tactic_menu(user)

    # ----------- TATICAS -----------    
    def tactic_menu(self, user):    
        while True:
            print(f"\nGerenciando táticas para {user.username}")
            print("1. Criar nova tática")
            print("2. Ver detalhe de tática")
            print("3. Listar todas as táticas")
            print("4. Remover tática")
            print("5. Voltar")
            option = input("Opção: ")
            
            if option == '1':
                self.create_tactic_for_user(user)
            elif option == '2':
                self.read_tactic()
            elif option == '3':
                self.find_all_tactics(user)
            elif option == '4':
                self.delete_user_tactic(user)
            elif option == '5':
                break
            else:
                print("Opção inválida.")

    def create_tactic_for_user(self, user):
        if not user.cards:
            print("O usuário não possui cartas para criar táticas!")
            return
        
        print("\nCartas disponíveis:")
        for i, card in enumerate(user.cards, 1):
            print(f"{i}. {card.name} ({card.position}) - {card.team.name if card.team else 'Sem time'}")
        
        tactic_name = input("\nNome da tática: ")
        selected = input("Selecione os números dos players (ex: 1,3,5): ").split(',')
        
        try:
            selected_indices = [int(num.strip()) - 1 for num in selected]
            selected_players = [user.cards[i] for i in selected_indices]
            
            if len(selected_players) > 11:
                print("Uma tática pode ter no máximo 11 players!")
                return
            
            tactic = Tatica(tactic_name, selected_players)
            # Cria a tática no banco de dados usando TaticaDAO
            tactic_id = self.tatica_dao.create_tatica(tactic, user._id)
            # Adiciona a tática ao player
            self.jogador_dao.add_tatica(user._id, tactic_id)
            print("Tática criada com sucesso!")
            print(f"Química: {tactic.quimica}%")
        except (ValueError, IndexError) as e:
            print(f"Erro: {str(e)}")

    def read_tactic(self):
        tactic_id = input("ID da tática: ")
        tactic = self.tatica_dao.read_tatica(tactic_id)
        if tactic:
                print("\nDetalhes da Tática:")
                print(f"Nome: {tactic.nome_formacao}")
                print(f"Química: {tactic.quimica:.1f}%")
                print("\nPlayers escalados:")
                for i, player in enumerate(tactic.players, 1):
                    print(f"{i}. {player.name} ({player.position}) - {player.team.name if player.team else 'Sem time'}")
        else:
                print("Tática não encontrada!")

    def find_all_tactics(self,user):
        tactics = self.tatica_dao.find_all_taticas(user._id)
        for tactic in tactics:
            print(tactic)

    def delete_user_tactic(self, user):
        """Remove uma tática do usuário"""
        if not user.taticas:
            print("\nVocê não possui táticas para remover!")
            return
        
        self.list_user_tactics(user)
        
        try:
            selected = int(input("\nDigite o número da tática para remover: "))-1
            if 0 <= selected < len(user.taticas):
                tactic_id = user.taticas[selected]
                
                # Confirmação
                confirm = input(f"Tem certeza que deseja remover esta tática? (s/n): ").lower()
                if confirm == 's':
                    # Remove do banco
                    if self.tatica_dao.delete_tatica(str(tactic_id)):
                        # Remove da lista do usuário
                        user.taticas.pop(selected)
                        self.player_dao.update_player(user)
                        print("Tática removida com sucesso!")
                    else:
                        print("Falha ao remover tática!")
                else:
                    print("Operação cancelada.")
            else:
                print("Número inválido!")
        except ValueError:
            print("Digite um número válido!")