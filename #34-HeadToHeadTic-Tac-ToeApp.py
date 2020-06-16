# all function definitions here
def show_board( positions ):
    print("\n   Tic-Tac-Toe")
    print("~~~~~~~~~~~~~~~~~")
    for i in range(0,7,3):
        for pos in range(3):
            print("||",positions[pos+i],'', end="")
        print("||\n")

def play_move(char):
    while True:
        pos = int(input(f"{char}: Where would you like to place your piece (1 - 9): "))
        if pos > 9 or pos < 1:
            print("\nThat is not a spot on the board. Try again.")
        elif '_' != sym_pos[pos-1]:
            print("\nThat spot has already been chosed. Try again.")
        else:
            sym_pos[pos-1] = char.upper()
            break

def check_for_win():
    # checking for 3-vertical combination
    if ( sym_pos[0]==sym_pos[3]==sym_pos[6]!='_' ) or ( sym_pos[1]==sym_pos[4]==sym_pos[7]!='_' ) or ( sym_pos[2]==sym_pos[5]==sym_pos[8]!='_' ):
        return True
    # checking for horizontal combination
    elif ( sym_pos[0]==sym_pos[1]==sym_pos[2]!='_' ) or ( sym_pos[3]==sym_pos[4]==sym_pos[5]!='_' ) or ( sym_pos[6]==sym_pos[7]==sym_pos[8]!='_' ):
        return True
    # checking for diagonal combination
    elif ( sym_pos[0]==sym_pos[4]==sym_pos[8]!='_' ) or ( sym_pos[2]==sym_pos[4]==sym_pos[6]!='_' ):
        return True
    else:
        return False


print("Welcome to the Head to Head Tic-Tac-Toe App!")   

# creating a list to store the positions on the board
num_pos = list(range(1, 10))
sym_pos = ['_']*9

# compiling all the functions to complete the whole game
playing = True

# winner var
winner_char = ''
current_player = 'O'

while playing:
    # checking for a tie
    if '_' not in sym_pos:
        print("\nUh-oh! It's a tie!")
        playing = False
        break
    show_board( num_pos )
    print("\n")
    show_board( sym_pos )
    print("\n")
    # changing players
    if current_player == 'O':
        current_player = 'X'
    else:
        current_player = 'O'
    # playing a move
    play_move(current_player)
    # checking for a win
    temp = check_for_win()
    if temp:
        show_board( num_pos )
        print("\n")
        show_board( sym_pos )
        print("\n")
        winner_char = 'X'
        playing = False
        print("Congratulations! Player",winner_char,"wins!\nWohoo!")
        break