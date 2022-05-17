from win_condition import has_win_condition

class Game:
    def __init__(self):
        self.__avaiable_positions = {1,2,3,4,5,6,7,8,9}
        self.X_positions = set()
        self.O_positions = set()

    def state(self):
        if has_win_condition(self.X_positions) :
            return "X wins"
        elif has_win_condition(self.O_positions) :
            return "O wins"
        elif self.__avaiable_positions == set() :
            return "It is a Draw"
        elif len(self.__avaiable_positions) % 2 == 1 :
            return "X turn"
        else :
            return "O turn"

    def x_input(self,player_choice):
        self.__update(player_choice, self.X_positions)
    def o_input(self,player_choice,):
        self.__update(player_choice, self.O_positions)

    def __update(self, player_choice, positions): 
        if player_choice in self.__avaiable_positions:
            positions.add(player_choice)
            self.__avaiable_positions.remove(player_choice)
        else:
            print("position not available")

