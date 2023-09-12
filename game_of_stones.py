def play_nims():
    """
    Play the game of Nims/Stones
    Two players take turns removing between 1 and 5 stones from a pile of 100 stones
    The player who removes the last stone(s) wins.
    """
    
    pile = 20
    current_player = 1 # Initialise the current player (1 or 2 )
    
    while pile > 0:
        print(f"Current pile size: {pile} stones   ")
        
        # Ask the current player for their move
        valid_move = False
        
        while not valid_move:
            try:
                move = int(input(f"Player {current_player}, enter a number between 1 or 5: "))
                
                if 1 <= move <= 5 and move <= pile:
                    valid_move = True
                    
                else:
                    print(f"Invalid move. Please enter a number between 1 or 5: ")
            
            except ValueError:
                print(f"Invalid move. Please enter a valid number between 1 or 5: ")
                
            # update the pile
            pile -= move
            
            current_player = 3 - current_player
        
    
    print(f"Player {3-current_player} wins!")
        
if __name__ == "__main__":
    play_nims()