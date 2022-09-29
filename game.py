from player import Player

class Game:

    def __init__(self):
        self.player_one = Player('Player 1')
        self.player_two = Player('Player 2')
        

    def start_game(self):
        self.player_one.board.create_board()
        self.player_two.board.create_board()
        self.player_one.board.display_board()
        self.player_one.board.place_ship_on_board_update()
        self.player_one.board.display_board()
        self.game_play()
        

    def game_play(self):
        while self.player_one.points <18 or self.player_two.point < 18:
            self.player_one.attack_other_player(self.player_one,self.player_two)

    

    def display_welcome(self):
        pass

    def run_game(self):
        pass