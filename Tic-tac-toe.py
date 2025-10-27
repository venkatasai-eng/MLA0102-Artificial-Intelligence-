board=[" "]*9

def show():
    print(board[0],"|",board[1],"|",board[2])
    print("--+---+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+---+--")
    print(board[6],"|",board[7],"|",board[8])

def win(p):
    return any(board[x]==board[y]==board[z]==p for x,y,z in
               [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)])

def ai():
    for i in range(9):
        if board[i]==" ":
            board[i]="O"; return

def game():
    show()
    while True:
        p=int(input("1-9:"))-1
        if board[p]!=" ": continue
        board[p]="X"
        if win("X"): show(); print("You Win"); break
        ai(); show()
        if win("O"): print("AI Win"); break
        if " " not in board: print("Draw"); break

game()
