from colorama import Fore, Style


class Console():
    def __init__(self, player_srv):
        self.__player_srv = player_srv

    @staticmethod
    def print_menu():
        print("1. Add player")
        print("2. Show players from country with number of points")
        print("3. Show players sorted by win percentage")
        print("4. Player evolution")
        print("10. Show all players")
        print("5. Exit")

    def __add_player_ui(self):
        name = input("Player name:")
        country = input("Country:")
        matches_played = int(input("Matches played:"))
        matches_won = int(input("Matches won:"))
        points = int(input("Points:"))
        self.__player_srv.add(name, country, matches_played, matches_won, points)
        print(Fore.GREEN + "Player successfully added." + Style.RESET_ALL)

    def run(self):
        while True:
            self.print_menu()
            try:
                option = int(input(">>>"))
                match option:
                    case 1:
                        self.__add_player_ui()
                    case 2:
                        self.__filter_players_ui()
                    case 3:
                        self.__sort_players_ui()
                    case 4:
                        self.__show_player_evolution_ui()
                    case 5:
                        break
                    case 10:
                        self.__print_list(self.__player_srv.get_all())
            except Exception as e:
                print(Fore.RED + str(e) + Style.RESET_ALL)

    def __filter_players_ui(self):
        country_to_filter = input("Country:")
        point_threshold = int(input("Point threshold:"))
        filtered_players = self.__player_srv.filter_players(country_to_filter, point_threshold)
        self.__print_list(filtered_players)

    def __print_list(self, players):
        for player in players:
            print(player)

    def __sort_players_ui(self):
        sorted_list = self.__player_srv.sort_by_win_percentage()
        self.__print_list(sorted_list)

    def __show_player_evolution_ui(self):
        name = input("Name:")
        country = input("Country:")
        tournament_points = int(input("Tournament points:"))
        tournament_result = input("Result [w, f, sf, qf, r16]: ")
        evaluation = self.__player_srv.evaluate_player(name, country, tournament_points, tournament_result)
        print(evaluation.player)
        print("New number of points would be:", Fore.CYAN + str(evaluation.get_number_of_points()) + Style.RESET_ALL)
