from model import GameMaster 
from view import display_game_state, get_input  

def controller():
    game = GameMaster()

    while True:
        display_game_state(game.X_positions, game.O_positions) 

        if game.x_wins():
            print("X wins")
            break
        elif game.o_wins():
            print("O wins")    
            break
        elif game.draw():
            print("It is a Draw")
            break
        elif game.player_x_turn():
            X = get_input("X move : ")
            game.x_input(X)
        else : 
            O = get_input("O move : ")
            game.o_input(O)

