from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("| ", board[0][0],"   |", board[0][1],"    |  " ,board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("| ", board[1][0],"   |", board[1][1],"    |  " ,board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("| ", board[2][0],"   |", board[2][1],"    |  " ,board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    #Diagonal izsup to derinf
    if board[0][0]==sign and board[1][1]==sign and board[2][2]==sign:
        display_board(board)
        return print("HA GANADO EL JUGADOR QUE UTILIZA",sign,"'s")
    #diagonal dersup to izinf
    elif board[0][2]==sign and board[1][1]==sign and board[2][0]==sign:
        display_board(board)
        return print("HA GANADO EL JUGADOR QUE UTILIZA",sign,"'s")
        
    elif board[0][0]==sign and board[1][0]==sign and board[2][0]==sign:
        display_board(board)
        return print("HA GANADO EL JUGADOR QUE UTILIZA",sign,"'s")
    elif board[0][1]==sign and board[1][1]==sign and board[2][1]==sign:
        display_board(board)
        return print("HA GANADO EL JUGADOR QUE UTILIZA",sign,"'s")    
    elif board[0][2]==sign and board[1][2]==sign and board[2][2]==sign:
        display_board(board)
        return print("HA GANADO EL JUGADOR QUE UTILIZA",sign,"'s")
    elif board[0][0]==sign and board[0][1]==sign and board[0][2]==sign:
        display_board(board)
        return print("HA GANADO EL JUGADOR QUE UTILIZA",sign,"'s")
    elif board[1][0]==sign and board[1][1]==sign and board[1][2]==sign:
        display_board(board)
        return print("HA GANADO EL JUGADOR QUE UTILIZA",sign,"'s")
    elif board[2][0]==sign and board[2][1]==sign and board[2][2]==sign:
        display_board(board)
        return print("HA GANADO EL JUGADOR QUE UTILIZA",sign,"'s")
    else:
        if make_list_of_free_fields(board) == []:
            return "tie"
        else:
            return "c"


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    freeSquares=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not(board[i][j]=="X" or board[i][j]=="O"):
                freeSquares.append((i,j))
    return freeSquares
    

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    turno = True
    while turno:
        try:
            move = int(input("Por favor ingresa el número en donde quieres poner tu O\n"))
            freeSpaces = make_list_of_free_fields(board)
            if isinstance(move, int):
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j]== move:
                            tup = (i,j)
                            if tup in freeSpaces:
                                board[i][j] = "O"
                                turno = False
                            else:
                                print("Ese espacio está tomado")
                        else:
                            continue                    
            else:
                print("No te entendí bien o pusiste un número fuera de rango, vuelve a ingresar el número")
        except:
            print("No te entendí bien o pusiste un número fuera de rango, vuelve a ingresar el número")
    return victory_for(board,"O")


def draw_move(board):
    # The function draws the computer's move and updates the board.
    #move = randrange(1,10)
    #freeSpaces = make_list_of_free_fields(board)
    #for i in range(len(board)):
    #    for j in range(len(board[i])):
    #        if board[i][j]== move:
    #            tup = (i,j)
    #            if tup in freeSpaces:
    #                board[i][j] = "X"
    #            else:
    #                print("ESTOY FEO")
    #                return draw_move(board)
    #        else:
    #            continue
    #return victory_for(board,"X")
    freeSpaces = make_list_of_free_fields(board)
    if freeSpaces:
        i,j = freeSpaces[randrange(len(freeSpaces))]
        board[i][j]="X"
        return victory_for(board,"X")

print("Hola humano, vamos a jugar gato")
print("Como eres un humano, yo iré primero, jugaré con las X´s")
board = [[j for j in range(1,4)],[j for j in range(4,7)],[j for j in range(7,10)]]
board[1][1]= "X"
while True:
    display_board(board)
    r = enter_move(board)
    if r !="c" and r !="tie":
        break
    elif r=="tie":
        print("Es un empate!")
        break
    m = draw_move(board)
    if m !="c" and m !="tie":
        break
    elif m=="tie":
        print("Es un empate!")
        break
    
