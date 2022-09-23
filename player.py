class Player:
    def __init__(self, name):
        self.name = name
        self.ships = ''
        self.points = 0

    def place_ships(self):
        print('Please place your ships on the board, by indicating which coordinates. Lets start with a destroyer!')
        
