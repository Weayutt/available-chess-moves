# author: Wyatt Avilla
# date: 5-31-22
# file: chess.py shows available moves given chess piece and position on chess board
# input: user's chess piece and piece location
# output: move availability for given piece

class Board:
    def __init__(self):
        self.board = {}
        self.empty()
        self.row_idx = "12345678"
        self.col_idx = "abcdefgh"
    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col+row] = ' '
    def set(self, pos, piece):   # pos is a square label (a1, a2, ..., h8)
        if pos in self.board.keys():
            self.board[pos] = piece
    def draw(self):
        print("   a   b   c   d   e   f   g   h")
        for row in self.row_idx[::-1]:
            print(" +---+---+---+---+---+---+---+---+")
            print(row, end="")
            for col in self.col_idx:
                #row, col
                v = self.board[col + row]
                print(f"| {v} ", end="")
            print(f"|{row}")
        print(" +---+---+---+---+---+---+---+---+")
        print("   a   b   c   d   e   f   g   h")

class Chess_Piece:
    def __init__(self, board, pos, color='white'):
        self.pos = pos
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())
    def get_index(self, pos):
        return ('abcdefgh'.index(pos[0]), '12345678'.index(pos[1]))
    def get_name(self):
        pass
    def moves(self, board):
        pass

class Rook(Chess_Piece):
    def __init__(self, board, pos, color='white'):
        Chess_Piece.__init__(self, board, pos, color='white')
        Chess_Piece.get_index(self, pos)
    def get_name(self):
        return "R"
    def moves(self, board):
        row = 'abcdefgh'.index(self.pos[0])
        col = '12345678'.index(self.pos[1])
        for var in range(9):
            board.set(str(self.pos[0]) + str(var), "X")
        for letter in ("abcdefgh"):
            board.set(str(letter) + str(self.pos[1]), "X")
        board.set(self.pos, "R")

class King(Chess_Piece):
    def __init__(self, board, pos, color='white'):
        Chess_Piece.__init__(self, board, pos, color='white')
        Chess_Piece.get_index(self, pos)
    def get_name(self):
        return "K"
    def moves(self, board):
        row = int('abcdefgh'.index(self.pos[0]))
        col = int('12345678'.index(self.pos[1]))
        try:
            board.set(str('abcdefgh'[row])+str('12345678'[col+1]), "X")
        except:
            IndexError
        try:
            board.set(str('abcdefgh'[row+1])+str('12345678'[col]), "X")
        except:
            IndexError
        try:
            board.set(str('abcdefgh'[row+1])+str('12345678'[col+1]), "X")
        except:
            IndexError
        board.set(str('abcdefgh'[abs(row-1)])+str('12345678'[col]), "X")
        board.set(str('abcdefgh'[row])+str('12345678'[abs(col-1)]), "X")
        try:
            board.set(str('abcdefgh'[abs(row-1)])+str('12345678'[col+1]), "X")
        except:
            IndexError
        try:  
            board.set(str('abcdefgh'[row+1])+str('12345678'[abs(col-1)]), "X")
        except:
            IndexError
        board.set(str('abcdefgh'[abs(row-1)])+str('12345678'[abs(col-1)]), "X")
        board.set(self.pos, "K")

class Bishop(Chess_Piece):
    def __init__(self, board, pos, color='white'):
        Chess_Piece.__init__(self, board, pos, color='white')
        Chess_Piece.get_index(self, pos)
    def get_name(self):
        return "B"
    def moves(self, board):
        row = int('abcdefgh'.index(self.pos[0]))
        col = int('12345678'.index(self.pos[1]))
        try:
            for x in range(8):
                board.set(str('abcdefgh'[row+x])+str('12345678'[col+x]), "X")
        except:
            IndexError
        try:
            for x in range(8):
                if col-x >= 0:
                    board.set(str('abcdefgh'[row+x])+str('12345678'[col-x]), "X")
                else:
                    break
        except:
            IndexError
        try:
            for x in range(8):
                if row-x >= 0:
                    board.set(str('abcdefgh'[row-x])+str('12345678'[col+x]), "X")
                else:
                    break
        except:
            IndexError
        try:
            for x in range(8):
                if col-x >= 0 and row-x >= 0:
                    board.set(str('abcdefgh'[row-x])+str('12345678'[col-x]), "X")
                else:
                    break
        except:
            IndexError
        board.set(self.pos, "B")

class Queen(Chess_Piece):
    def __init__(self, board, pos, color='white'):
        Chess_Piece.__init__(self, board, pos, color='white')
        Chess_Piece.get_index(self, pos)
    def get_name(self):
        return "Q"
    def moves(self, board):
        row = int('abcdefgh'.index(self.pos[0]))
        col = int('12345678'.index(self.pos[1]))
        for var in range(9):
            board.set(str(self.pos[0]) + str(var), "X")
        for letter in ("abcdefgh"):
            board.set(str(letter) + str(self.pos[1]), "X")

        try:
            for x in range(8):
                board.set(str('abcdefgh'[row+x])+str('12345678'[col+x]), "X")
        except:
            IndexError
        try:
            for x in range(8):
                if col-x >= 0:
                    board.set(str('abcdefgh'[row+x])+str('12345678'[col-x]), "X")
                else:
                    break
        except:
            IndexError
        try:
            for x in range(8):
                if row-x >= 0:
                    board.set(str('abcdefgh'[row-x])+str('12345678'[col+x]), "X")
                else:
                    break
        except:
            IndexError
        try:
            for x in range(8):
                if col-x >= 0 and row-x >= 0:
                    board.set(str('abcdefgh'[row-x])+str('12345678'[col-x]), "X")
                else:
                    break
        except:
            IndexError
        board.set(self.pos, "Q")

class Knight(Chess_Piece):
    def __init__(self, board, pos, color='white'):
        Chess_Piece.__init__(self, board, pos, color='white')
        Chess_Piece.get_index(self, pos)
    def get_name(self):
        return "N"
    def moves(self, board):
        row = int('abcdefgh'.index(self.pos[0]))
        col = int('12345678'.index(self.pos[1]))
        try:
            board.set(str('abcdefgh'[row+1])+str('12345678'[col+2]), "X")
        except:
            IndexError
        try:
            board.set(str('abcdefgh'[row+2])+str('12345678'[col+1]), "X")
        except:
            IndexError
        if col - 2 >= 0:
            try:
                board.set(str('abcdefgh'[row+1])+str('12345678'[col-2]), "X")
            except:
                IndexError
        if col - 1 >= 0:
            try:
                board.set(str('abcdefgh'[row+2])+str('12345678'[col-1]), "X")
            except:
                IndexError
        if row - 1 >= 0:
            try:
                board.set(str('abcdefgh'[row-1])+str('12345678'[col+2]), "X")
            except:
                IndexError
        if row - 2 >= 0:
            try:
                board.set(str('abcdefgh'[row-2])+str('12345678'[col+1]), "X")
            except:
                IndexError
        if row -2 >= 0 and col -1 >= 0:
            try:
                board.set(str('abcdefgh'[row-2])+str('12345678'[col-1]), "X")
            except:
                IndexError
        if row-1 >= 0 and col -2 >=0:
            try:
                board.set(str('abcdefgh'[row-1])+str('12345678'[col-2]), "X")
            except:
                IndexError
        board.set(self.pos, "N")



displayboard = Board() #main loop
print("Welcome to the Chess Game!")
displayboard.draw()
while True:

    userinput = input("Enter the chess piece initial (r k q n b) followed by its move index or type X to exit: \n").lower()
    if userinput == "x":
        print("Goobye!")
        exit()
    if len(userinput) != 3:
        continue
    elif userinput[0] not in "rkbqn":
        continue
    elif userinput[1] not in "abcdefgh":
        continue
    elif userinput[2] not in "12345678":
        continue

    elif userinput[0] == "r":  #rook
        userspace = str(userinput[1]) + str(userinput[2])
        userrook = Rook(displayboard, userspace)
        userrook.moves(displayboard)
        displayboard.draw()
        displayboard.empty()

    elif userinput[0] == "k":  #king
        userspace = str(userinput[1]) + str(userinput[2])
        userking = King(displayboard, userspace)
        userking.moves(displayboard)
        displayboard.draw()
        displayboard.empty()

    elif userinput[0] == "q":  #queen
        userspace = str(userinput[1]) + str(userinput[2])
        userqueen = Queen(displayboard, userspace)
        userqueen.moves(displayboard)
        displayboard.draw()
        displayboard.empty()

    elif userinput[0] == "n":
        userspace = str(userinput[1]) + str(userinput[2])
        userknight = Knight(displayboard, userspace)
        userknight.moves(displayboard)
        displayboard.draw()
        displayboard.empty()
    
    elif userinput[0] == "b":
        userspace = str(userinput[1]) + str(userinput[2])
        userbishop = Bishop(displayboard, userspace)
        userbishop.moves(displayboard)
        displayboard.draw()
        displayboard.empty()
    
    else:
        continue