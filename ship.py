class Ships:
    def __init__(self) -> None:
        self.list_of_ships = ''
        self.space = None
        self.coordinates = []
        self.list_of_coordinates = []
        self.health_points = ''

        

    
    def location(self):
        pass
#Can each ship have coordinates class?
#each coordinate would have an x and y axis.
#each ship would have 2 up to 5 coordinates
class Coordinates:
    def __init__(self):
        self.x_axis = 0
        self.y_axis = 0
        self.coordinates = [self.x_axis, self.y_axis]

class Destroyer(Ships):
    def __init__(self) -> None:
        super().__init__()
        self.space = 2
        self.name = "Destroyer"
        self.health_points = 2
       

class Submarine(Ships):
    def __init__(self) -> None:
        super().__init__()
        self.space = 3
        self.name = "Submarine"
        self.health_points = 3


class Battleship(Ships):
    def __init__(self) -> None:
        super().__init__()
        self.space = 4
        self.name = "Battleship"
        self.health_points = 4

class Aircraft_Carrier(Ships):
    def __init__(self) -> None:
        super().__init__()
        self.space = 5
        self.name = "AirCraft Carrier"
        self.health_points = 5