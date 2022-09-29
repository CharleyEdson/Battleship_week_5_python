from tabnanny import check
from ship import Ships
from ship import Destroyer
from ship import Submarine
from ship import Battleship
from ship import Aircraft_Carrier
import math



class Board:

    def __init__(self):
        self.rows = 20
        self.cols = 20
        self.board = []
        self.list_of_ships = []  #I want to eventually add in this list
        self.destroyer = Destroyer()
        self.submarine = Submarine()
        self.battleship_one = Battleship()
        self.battleship_two = Battleship()
        self.aircraft_carrier = Aircraft_Carrier()

 
        
    def create_list_of_ships(self):
        self.list_of_ships.append(Destroyer())
        self.list_of_ships.append(Submarine())
        self.list_of_ships.append(Battleship())
        self.list_of_ships.append(Battleship())
        self.list_of_ships.append(Aircraft_Carrier())

    
    def create_board(self):
        """This function creates the board. NEED TO UPDATE SO THE BOARD STARTS AT 1, AND ENDS AT 20 BOTH WAYS."""
        
        self.create_list_of_ships()
        row = 0
        column_headers = []
        for num in range(1,21):
            col_header_string = str(num)
            column_headers.append(col_header_string)
        self.board.append(column_headers)    
        for item in range(20):   #this is the number of column headers
            self.board.append(['-']*20)
            for j in self.board:
                if len(j) <= 20:
                    j.append(row)
                    row += 1
    

    def place_ship_on_board_update(self):
        """Function that takes in each X&Y coordinate for each ship. It will not validate"""
        for ship in self.list_of_ships:
            number_of_spaces = ship.space
            if ship.name == 'Destroyer':
                ship_type = 'D'
            if ship.name == 'Submarine':
                ship_type = 'S'
            if ship.name == 'Battleship':
                ship_type = 'B'
            if ship.name == 'AirCraft Carrier':
                ship_type = 'A'
            counter = 1
            for space in range(number_of_spaces):
                valid_coordinate_on_board = False
                coordinate_not_touching_another_ship = False
                coordinates_touching = False
                #while valid_coordinate_on_board is False or coordinate_not_touching_another_ship is False or coordinates_touching is False:
                #Will remove the if's and while, just check if all of them are ok, and if one isn't repeat.
                while valid_coordinate_on_board is False:
                    list_of_cords = []
                    print(f'Please pick the {counter}: x & y axis coordinate for {ship.name}')
                    x_axis, y_axis = int(input()), int(input())
                    valid_coordinate_on_board = self.validate_choice(x_axis, y_axis)
                    if valid_coordinate_on_board is False:
                        print('Please re-pick a coordinate on the board, between 1 and 20')
                        continue
                    coordinate_not_touching_another_ship = False
                    while coordinate_not_touching_another_ship is False:
                        coordinate_not_touching_another_ship = self.validate_ship_not_touching_another_ship(y_axis,x_axis)
                        if coordinate_not_touching_another_ship is False:
                            print('Please make sure the coordinates are not touching another ships. Pick again')
                            x_axis, y_axis = int(input()), int(input())
                    #Need to add in logic if he places a non_valid_coordinate on board, check for that    
                    coordinates_touching = False 
                    while coordinates_touching is False:
                        coordinates_touching = self.validate_ship_coordinates_touching(y_axis, x_axis, ship, space)
                        if coordinates_touching is False:
                            print('Please make sure the ships coordinates are touching each other. Pick again')
                            x_axis, y_axis = int(input()), int(input())
                    #Need to add in logic if he places a non_valid_coordinate on board
                    list_of_cords.append(x_axis-1)
                    list_of_cords.append(y_axis)
                    ship.list_of_coordinates.append(list_of_cords)
                    self.board_set_up(list_of_cords, ship_type)
                    counter += 1

    def check_if_attacking_player_hit_defending(self,x_axis,y_axis, player_attacking, player_defending):
        if player_defending.board.board[y_axis][x_axis-1] == 'D' or player_defending.board.board[y_axis][x_axis-1] == 'S' or player_defending.board.board[y_axis][x_axis-1] == 'B' or player_defending.board.board[y_axis][x_axis-1] == 'A':
            is_hit = True
            print('You have hit the enemy ships...')
            return is_hit          
        if player_defending.board.board[y_axis][x_axis-1] == '-':
            is_hit = False
            print('You have missed the enemy ships!')
            return is_hit
        

    def direct_attack(self, x_axis, y_axis, player_attacking, player_defending):
        player_attacking.points += 1
        ship_type = player_defending.board.board[y_axis][x_axis-1] 
        if ship_type == 'D':
            player_defending.board.list_of_ships[0].health_points -= 1
            if player_defending.board.list_of_ships[0].health_points == 0:
                print(f"You have sank {player_defending.name}'s {player_defending.board.list_of_ships[0].name}!")
        if ship_type == 'S':
            player_defending.board.list_of_ships[1].health_points -= 1
            if player_defending.board.list_of_ships[1].health_points == 0:
                print(f"You have sank {player_defending.name}'s {player_defending.board.list_of_ships[1].name}!")
        if ship_type == 'B':
            player_defending.board.list_of_ships[2].health_points -= 1
            if player_defending.board.list_of_ships[2].health_points == 0:
                print(f"You have sank {player_defending.name}'s {player_defending.board.list_of_ships[2].name}!")
        if ship_type == 'A':
            player_defending.board.list_of_ships[3].health_points -= 1
            if player_defending.board.list_of_ships[3].health_points == 0:
                print(f"You have sank {player_defending.name}'s {player_defending.board.list_of_ships[3].name}!")


    def update_attackers_board(self, y_axis, x_axis, player_attacking, is_it_a_hit):
        if is_it_a_hit == True:
            player_attacking.opponent_view_board.board[y_axis][x_axis-1] = 'X'
        else:
            player_attacking.opponent_view_board.board[y_axis][x_axis-1] = 'O'
        player_attacking.opponent_view_board.display_board()
        


    def board_set_up(self,coordinates,ship_type):
        """This function places the users pick on the board"""
        self.board[coordinates[1]][coordinates[0]] = ship_type

    def validate_ship_not_touching_another_ship(self, y_axis, x_axis):
        """This function checks to see if the users picks are touching another ship"""
        if self.board[y_axis][x_axis-1] == 'D' or self.board[y_axis][x_axis-1] == 'S' or self.board[y_axis][x_axis-1] == 'B' or self.board[y_axis][x_axis-1] == 'A':
            check = False
            return check 
        else:
            check = True
            return check

    def validate_non_repeated_selection(self, y_axis, x_axis):
        if self.board[y_axis][x_axis-1] == 'X':
            check = False
            return check
        else:
            check = True
            return check
        
    def validate_ship_coordinates_touching(self, y_axis, x_axis, ship, space):
        """This function checks to see if they are placing the ship's coordinates next to each other."""
        #Can certainly improve logic
        if space == 0:
            check = True
            return check
        if space == 1:
            p1 = ship.list_of_coordinates[0]
            p1[0] = p1[0] + 1
            p2 = []
            p2.append(x_axis)
            p2.append(y_axis)
            distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
            p1[0] = p1[0] - 1
            if distance > 1:
                check = False
                return check
            elif distance <=1:
                check = True
                return check
        if space == 2:
            p1 = ship.list_of_coordinates[1]
            p1[0] = p1[0] + 1
            p2 = []
            p2.append(x_axis)
            p2.append(y_axis)
            distance_1 = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
            p1[0] = p1[0] - 1
            p3 = ship.list_of_coordinates[0]
            p3[0] = p3[0] + 1
            distance_2 = math.sqrt( ((p3[0]-p2[0])**2)+((p3[1]-p2[1])**2) )
            if distance_1 > 1 and distance_2 > 1:
                check = False
                return check
            elif distance_1 <=1 and distance_2 <= 1:
                check = True
                return check
        if space == 3:
            p3 = ship.list_of_coordinates[0]
            p3[0] = p3[0] + 1
            p2 = []
            p2.append(x_axis)
            p2.append(y_axis)
            distance_1 = math.sqrt( ((p3[0]-p2[0])**2)+((p3[1]-p2[1])**2) )
            p3[0] = p3[0] - 1
            p1 = ship.list_of_coordinates[2]
            p1[0] = p1[0] + 1
            distance_2 = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
            p1[0] = p1[0] - 1
            if distance_1 > 1 and distance_2 > 1:
                check = False
                return check
            elif distance_1 <=1 and distance_2 <= 1:
                check = True
                return check
        if space == 4:
            p3 = ship.list_of_coordinates[0]
            p3[0] = p3[0] + 1
            p2 = []
            p2.append(x_axis)
            p2.append(y_axis)
            distance_1 = math.sqrt( ((p3[0]-p2[0])**2)+((p3[1]-p2[1])**2) )
            p3[0] = p3[0] - 1
            p1 = ship.list_of_coordinates[3]
            p1[0] = p1[0] + 1
            distance_2 = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
            p1[0] = p1[0] - 1
            if distance_1 > 1 and distance_2 > 1:
                check = False
                return check
            elif distance_1 <=1 and distance_2 <= 1:
                check = True
                return check


    
                    


    def validate_choice(self, x_axis, y_axis):
        if x_axis > 20 or x_axis <= 0 or y_axis > 20 or y_axis <1:
            coordinate_one = False
            return coordinate_one
        else:
            coordinate_one = True
            return coordinate_one
    
    def update_board(self):
        self.board[1][1] = 'd'
        self.board[1][2] = 'd'

    def display_board(self):
        for letter in self.board:
            print(letter)
    
    
    
    


