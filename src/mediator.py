from replies import bot_reply, player_reply
    
class Mediator:
    def __init__(self):
        self.number_of_players = player_reply("number of players (1 or 2): ")
        if self.number_of_players == 1:
            self.human = input("select marker (X or O) : ").upper()
        else:  
            self.human = ""

    def x_input(self, X_positions, O_positions):
        return self.__get_input("X", X_positions, O_positions)
    
    def o_input(self, X_positions, O_positions):
        return self.__get_input("O", X_positions, O_positions)

    def __get_input(self, input, X_positions, O_positions):
        if self.number_of_players == 2 or self.human == input:
            return player_reply(input + " move : ")
        else :
            return bot_reply(X_positions, O_positions)        