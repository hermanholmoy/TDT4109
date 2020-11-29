def print_board(board):
    def pad(n):
        return " "*n
    def sep(n):
        return pad(2) + "-"*n
    
    s = 13
    p = 1
    sp = 4
    print(pad(sp) + "1" + pad(sp-1) + "2" + pad(sp-1) + "3")
    print(sep(s))
    for row_num, row in enumerate(board):
        print_row = str(row_num+1) + pad(p)
        
        for item in row:
            print_row += "|" + pad(p) + item + pad(p)
        print_row +=  "|"
        print(print_row)
        print(sep(s))


def all_same(r):
    return True if len(set(r)) == 1 and " " not in r else False

def check_win(board):
    # returner bool, vinner
    for row in board: 
        # sjekker rader
        if all_same(row):
            return True, row[0]
        
    cols = [[board[0][i], board[1][i], board[2][i]] for i in range(len(board[0]))]
    # sjekker kolonner
    for col in cols:
        if all_same(col):
            return True, col[0]
        
    # sjekker diagonalt
    positions = [[[0, 0], [1, 1], [2,2]], [[0, 2], [1, 1], [2, 0]]]
    for position in positions:
        diag = [board[y][x] for x, y in position]
        if all_same(diag):
            return True, diag[0]
    
    # ingen vinnner
    return False, ""


def get_names():
    n1 = input("Skriv inn navn til spiller 1: ")
    n2 = input("Skriv inn navn til spiller 2: ")
    return n1, n2


def is_legal(board, move):
    x, y = int(move[0]), int(move[1])
    
    if board[y][x] == " ":
        return True
    else:
        return False
    

def validate_input(inp):
    try: 
        move = int(inp)
        if move in range(1, 4):
            return True
        else: 
            return False
    except:
        return False
    

def get_move(p):
    print(f"{p} sin tur.")
    print("Skriv inn x og y-koordinatene til trekket ditt.")
    x = input("x: ")
    y = input("y: ")
    if validate_input(x) and validate_input(y):
        x = int(x) - 1
        y = int(y) - 1
        if is_legal(board, [x, y]):
            return x, y
        else:
            print(f"({x+1}, {y+1}) er ikke et gyldig trekk. Prøv igjen.")
            return get_move(p)
    else:
        print("En av verdiene var ikke riktige. Prøv igjen. ")
        return get_move(p)
        
        
def make_move(board, move, p):
    if is_legal(board, move):
        x, y = move
        board[y][x] = p
    return board
    


def game():
    i = 0
    p1, p2 = get_names()
    while True:
        current_player = [p1, "x"] if i % 2 == 0 else [p2, "o"]
        print("Foreløpig brett: ")
        print_board(board)
        x, y = get_move(current_player[0])
        make_move(board, [x, y], current_player[1])
        
        win, player = check_win(board)
        if win:
            if player == "x": 
                player = p1
            else:
                player = p2
            print_board(board)
            print(f"{player} vant!")
            break
        i += 1
            
    


board = [
    [" ", " ", " "], 
    [" ", " ", " "], 
    [" ", " ", " "]
]

game()

