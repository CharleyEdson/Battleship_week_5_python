
from board import Board
from ship import Ships
from ship import Destroyer
from ship import Submarine
from ship import Battleship
from ship import Aircraft_Carrier


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.board = Board()
        self.opponent_view_board = Board()
        self.list_of_ships = ''
        self.has_won = False

    def create_opponent_view_board(self):
        row = 0
        column_headers = []
        for num in range(1,21):
            col_header_string = str(num)
            column_headers.append(col_header_string)
        self.opponent_view_board.board.append(column_headers)    
        for item in range(20):   #this is the number of column headers
            self.opponent_view_board.board.append(['-']*20)
            for j in self.opponent_view_board.board:
                if len(j) <= 20:
                    j.append(row)
                    row += 1

    def attack_other_player_update(self, player_attacking, player_defending):
        valid_coordinate_on_board = False
        not_repeated_selection = False
        is_attack_over = False
        while is_attack_over is False:
            list_of_cords = []
            #Make a checker for this
            view_opponent_board = input('Would you like to see the map of the opponents Board before attacking?: Y or N')
            if view_opponent_board == 'Y':
                player_attacking.opponent_view_board.display_board()  
            while valid_coordinate_on_board is False or not_repeated_selection is False:
                print(f"{player_attacking.name}, please select the coordinates you'd like to attack your opponents board with!")
                try:
                    x_axis, y_axis = int(input()), int(input())
                except ValueError as error:
                    print("Error: ", error)
                    print('Please pick a valid number.')
                    continue
                valid_coordinate_on_board = self.board.validate_choice(x_axis, y_axis)
                if valid_coordinate_on_board is False:
                    continue
                not_repeated_selection = self.board.validate_non_repeated_selection(x_axis, y_axis, player_attacking)
            valid_coordinate_on_board = False
            not_repeated_selection = False
            list_of_cords.append(x_axis-1)
            list_of_cords.append(y_axis)
            is_it_a_hit = player_attacking.board.check_if_attacking_player_hit_defending(x_axis, y_axis, player_attacking, player_defending)
            if is_it_a_hit == True:
                is_attack_over = False
                player_attacking.board.direct_attack(x_axis, y_axis, player_attacking, player_defending)  
                if player_attacking.points == 18:
                    player_attacking.has_won = True
                    is_attack_over = True
                    break          
                list_of_cords = []
                valid_coordinate_on_board = False
                not_repeated_selection = False
            player_attacking.board.update_attackers_board(y_axis, x_axis, player_attacking,is_it_a_hit)
            if is_it_a_hit == False:
                is_attack_over = True
            
            """if valid_coordinate_on_board is False:
                print('Please re-pick a coordinate on the board, between 1 and 20')
                continue
            not_repeated_selection = False
            while not_repeated_selection is False:
                not_repeated_selection = self.validate_ship_not_touching_another_ship(y_axis,x_axis)
                if not_repeated_selection is False:
                    print('You have already selected those coordinates. Please try again.')
                    x_axis, y_axis = int(input()), int(input())"""
            

          


    
