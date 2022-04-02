from bot import bot

def display(X,O):
    fmt = lambda num : "X" if num in X else "O" if num in O else " "
    print(f"""
    {fmt(1)}|{fmt(2)}|{fmt(3)}
    {fmt(4)}|{fmt(5)}|{fmt(6)}
    {fmt(7)}|{fmt(8)}|{fmt(9)}
    """)
    
class input_manager:
    def __init__(self):
        self.number_of_players = player_choice("number of players (1 or 2): ")
        self.human = ""
        if self.number_of_players == 1:
            self.human = input("select marker (X or O) : ").upper()

    def x_input(self, X_positions, O_positions):
        return self.__get_input("X", X_positions, O_positions)
    
    def o_input(self, X_positions, O_positions):
        return self.__get_input("O", X_positions, O_positions)

    def __get_input(self, input, X_positions, O_positions):
        if self.number_of_players == 2 or self.human == input:
            prompt = input + " move : "
            return player_choice(prompt)
        else :
            return bot(X_positions, O_positions)        
 
def player_choice(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except ValueError:
            print("not an integer")
    return value  