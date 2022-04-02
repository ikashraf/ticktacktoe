from game import Game 
from input_manager import input_manager  
from display import display

def game_with_cli():
    game = Game()
    manager = input_manager()

    while True:
        display(game.X_positions, game.O_positions) 

        if game.x_win():
            print("X wins")
            break
        elif game.o_win():
            print("O wins")    
            break
        elif game.draw():
            print("It is a Draw")
            break
        elif game.x_turn():
            X = manager.x_input(game.X_positions, game.O_positions)
            game.x_input(X)
        else : 
            O = manager.o_input(game.X_positions, game.O_positions)
            game.o_input(O)

