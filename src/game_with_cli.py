from game import Game 
from mediator import Mediator  
from board import board

def game_with_cli():
    game = Game()
    mediator = Mediator()
    
    kill_game = False
    while not kill_game:
        
        board(game.X_positions, game.O_positions) 

        if game.state() == "X turn":
            X = mediator.x_input(game.X_positions, game.O_positions)
            game.x_input(X)
        elif game.state() =="O turn" : 
            O = mediator.o_input(game.X_positions, game.O_positions)
            game.o_input(O)
        else : 
            print(game.state())
            kill_game = True
