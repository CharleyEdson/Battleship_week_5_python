from player import Player

class Game:

    def __init__(self):
        self.player_one = Player('Player 1')
        self.player_two = Player('Player 2')
        

    def start_game(self):
        self.player_one.board.create_board()
        self.player_two.board.create_board()
        #enable functions below for real
        self.player_one.board.place_ship_on_board_update()
        self.player_two.board.place_ship_on_board_update()
        #Enable below function for sample automatic sample board setups
        #self.sample_boards()
        self.player_one.board.display_board()
        self.player_one.create_opponent_view_board()
        self.player_two.create_opponent_view_board()
        self.game_play()
        self.end_game()
        

    def game_play(self):
        while self.player_one.has_won is False and self.player_two.has_won is False:
            self.player_one.attack_other_player_update(self.player_one,self.player_two)
            if self.player_one.points ==18:
                continue
            self.player_two.attack_other_player_update(self.player_two,self.player_one)
            if self.player_two.points == 18:
                continue
        if self.player_one.points == 18:
            print(f'Congratulations {self.player_one.name}, you have won!')
            print(f'{self.player_two.name}, has lost!')
        if self.player_two.points == 18:
            print(f'Congratulations {self.player_two.name}, you have won!')
            print(f'{self.player_one.name}, has lost!')

    def end_game(self):
        print('What a great game. Congratulations to the winner!')

    def display_welcome(self):
        pass

    def run_game(self):
        pass


    def sample_boards(self):
        self.player_one.board.board[2][4] = 'D'
        self.player_one.board.board[2][5] = 'D'
        self.player_one.board.board[3][4] = 'S'
        self.player_one.board.board[3][5] = 'S'
        self.player_one.board.board[4][4] = 'B'
        self.player_one.board.board[4][5] = 'B'
        self.player_one.board.board[5][5] = 'A'
        self.player_one.board.board[5][6] = 'A'
        self.player_two.board.board[2][4] = 'D'
        self.player_two.board.board[2][5] = 'D'
        self.player_two.board.board[3][4] = 'S'
        self.player_two.board.board[3][5] = 'S'
        self.player_two.board.board[4][4] = 'B'
        self.player_two.board.board[4][5] = 'B'
        self.player_two.board.board[5][5] = 'A'
        self.player_two.board.board[5][6] = 'A'