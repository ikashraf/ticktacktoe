from core import win_condition_exist

class Game:
    def __init__(self):
        self.__avaiable_positions = {1,2,3,4,5,6,7,8,9}
        self.X_positions = set()
        self.O_positions = set()

    def x_wins(self):
        return win_condition_exist(self.X_positions)

    def o_wins(self):
        return win_condition_exist(self.O_positions)
    
    def draw(self):
        return self.__avaiable_positions == set()
    
    def player_x_turn(self):
        return len(self.__avaiable_positions) % 2 == 1

    def x_input(self,claimed_value):
        self.__update(claimed_value, self.X_positions, self.__avaiable_positions)

    def o_input(self,claimed_value):
        self.__update(claimed_value, self.O_positions, self.__avaiable_positions)

    def __update(self, claimed_value, positions, avaiable_position): 
        if claimed_value in avaiable_position:
            positions.add(claimed_value)
            avaiable_position.remove(claimed_value)
        else:
            print("position not available")

