from player import Player



class Board:
    def __init__(self):
    
        #self.ship = Ship_list()
        self.player_one = ''
        self.player_two = ''
        self.rows = 20
        self.cols = 20
        self.board = []
        
    def create_board(self):
        row = 1
        column_headers = ['A', 'B', 'C', 'D', 'E']  #need to get to 20 here 
        self.board.append(column_headers)    
        for item in range(5):   #this is the number of column headers
            self.board.append(['0']*5)
            for j in self.board:
                if len(j) <= 5:
                    j.append(row)

    def display_board(self):
        for letter in self.board:
            print(letter)
                
    def start_game(self):
        self.create_board()
        self.player_one = Player('Player 1')
        self.player_two = Player('Player 2')
        print(self.player_one.name)


