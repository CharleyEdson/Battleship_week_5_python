
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

    def create_opponent_view_board(self):
        row = 0
        column_headers = []
        for num in range(1,21):
            col_header_string = str(num)
            column_headers.append(col_header_string)
        self.opponent_view_board.board.append(column_headers)    
        for item in range(20):   #this is the number of column headers
            self.opponent_view_board.board.append(['-']*20)
            for j in self.board:
                if len(j) <= 20:
                    j.append(row)
                    row += 1

    def attack_other_player(self, player_name, opponent_board):
        valid_coordinate_on_board = False
        not_repeated_selection = False
        while valid_coordinate_on_board is False:
            print(f"{player_name.name}, please select the coordinates you'd like to attack your opponents board with!")
            x_axis, y_axis = int(input()), int(input())
            valid_coordinate_on_board = self.board.validate_choice(x_axis, y_axis)
            not_repeated_selection = self.board.validate_ship_not_touching_another_ship(x_axis,y_axis):
            
            """if valid_coordinate_on_board is False:
                print('Please re-pick a coordinate on the board, between 1 and 20')
                continue
            not_repeated_selection = False
            while not_repeated_selection is False:
                not_repeated_selection = self.validate_ship_not_touching_another_ship(y_axis,x_axis)
                if not_repeated_selection is False:
                    print('You have already selected those coordinates. Please try again.')
                    x_axis, y_axis = int(input()), int(input())"""
            

          


    
