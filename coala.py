def search_not_free_positions(pieces,board):
    '''Searches not free positions
    (list,Board)->(list,list)'''
    free = []
    not_free = []
    for piece in pieces:
        for p in piece:
            not_free.append(p.tup)
    for el in board.create_board():
        for e in el:
            if e not in not_free:
                free.append(e)
    return free, not_free


def write_the_board(pieces):
    '''Writes the board
    (pieces)->None
    '''
    lst_coor = []
    for lst in pieces:
        lst[0].__str__()
        for el in lst:
            lst_coor.append(el.tup)
        print(lst_coor)
        lst_coor = []


def moving_checks(white_pawns, white_rooks, white_queens, white_kings, white_bishops, white_knights, game):
    '''Checks the movements of board for two'''
    print(game.move(white_pawns[0], 2, 3))
    print(game.move(white_rooks[0], 2, 4))
    print(game.move(white_queens[0], 5, 1))
    print(game.move(white_kings[0], 3, 2))
    print(game.move(white_bishops[0], 5, 2))
    print(game.move(white_knights[0], 7, 3))


class ChessSet:
    '''Class represents chessset'''
    def __init__(self, board, pieces):
        '''Initialises chessset
        (ChessSet,Board,list)->None
        '''
        self.board = board
        self.pieces = pieces

    def check_is_free(self, x, y):
        '''Checks whether the figure is there.
        ChessSet,int,int)->bool
        '''
        return True
    def move(self, piece, x1, y1):
        if self.check_is_free(x1, y1):
            piece.move(x1, y1)


class Position:
    '''Class represents position'''
    def __init__(self, x, y):
        '''Initialises position
        (Position,int,int)->None
        '''
        self.x = x
        self.y = y

    def __str__(self):
        '''Represents description'''
        pass


class ChessboardBase:
    '''Parent class for all boards'''
    SIDES = None
    CELLS = None

    def __init__(self, name):
        '''Initialises board
        (ChessboardBase,str)->None
        '''
        self.name = name

    def check_out_of_board(self, x1, y1):
        '''Checks the limits of the board'''
        raise NotImplemented

    def create_board(self):
        '''Creates a board'''
        raise NotImplemented

    def __str__(self):
        '''Description for user'''
        print("This is a board {0}.".format(self.name))


class ChessboardTwo(ChessboardBase):
    '''Represents chessboard for two'''
    SIDES = 8
    CELLS = 64

    def check_out_of_board(self, x1, y1):
        '''Checks the measures'''
        if x1 <= 8 and (y1 <= 6) and (y1 >= 3):
            return True
        return False

    def create_board(self):
        '''Creates a board
        ( ChessboardTwo)->list of lists
        '''
        return [[(i, j) for j in range(1, 9)] for i in range(1, 9)]


class ChessboardSix(ChessboardBase):
    '''Represents chessboard for six'''
    def create_board(self):
        '''Creates a board
        ( ChessboardSix)->list of lists
        '''
        return [[(i, j) for j in range(1, 13)] for i in
                          ["a", "b", "c", "d", "e", "f", "g", "h"]]

class ChessboardGlynskyii(ChessboardBase):
    '''Represents chessboard Glynskyii'''
    def create_board(self):
        '''Creates a board
        (ChessboardGlynskyii)->list of lists
        '''
        return [[(i, j) for j in range(1, 12)] for i in
                          ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l"]]


class ChessboardFour(ChessboardBase):
    '''Represents chessboard for four'''
    def create_board(self):
        '''Creates a board
        (ChessboardFour)->list of lists
        '''
        return [[(i, j) for j in range(1, 15)] for i in
                          ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]]


class ChessboardDouble(ChessboardBase):
    '''Represents double chessboard'''
    def create_board(self):
        '''Creates a board
        (ChessboardDouble)->list of lists
        '''
        return [[(i, j) for j in range(1, 13)] for i in range(1, 17)]



class Piece:
    '''Represents piece class'''
    def __init__(self, shape, tup, chessboard, color):
        '''Initialises piece
        (Piece,str,tuple,Board,str)->None
        '''
        self.tup = tup
        self.color = color
        self.shape = shape
        self.chessboard = chessboard

    def validate(self, x1, y1):
        '''Validation'''
        self.chessboard.check_out_of_board(x1, y1)

    def move(self, x1, y1):
        '''Movements
        (Piece,int,int)->None'''
        if self.validate(x1, y1):
            print(
                "\n{0} {1} successfully went to the position {2}, {3} from {4}, {5}".format(self.color, self.shape, x1,
                                                                                            y1,
                                                                                            self.tup[0],
                                                                                            self.tup[1]))
            self.x = x1
        else:
            print(
                "\n{0} {1} cannot go to the position {2}, {3} from {4}, {5}".format(self.color, self.shape, x1, y1,
                                                                                    self.tup[0],
                                                                                    self.tup[1]))

    def __str__(self):
        '''Description of piece'''
        print("\n{0} {1}s: ".format(self.color, self.shape))


class Pawn(Piece):
    '''Class represents pawn'''
    def validate(self, x1, y1):
        '''Validates pawn
        returns bool'''
        super().validate(x1, y1)
        if isinstance(x1, str):
            if (y1 == self.tup[1] + 1) and (ord(x1) == ord(self.tup[0]) or ord(x1) == ord((self.tup[0]) + 1)):
                return True
            else:
                return False
            return True
        else:
            return False


class Bishop(Piece):
    '''Represents bishop'''
    def validate(self, x1, y1):
        '''Validates bishop
        (Bishop,int,int)->bool'''
        super().validate(x1, y1)
        if isinstance(x1, str):
            if ord(x1) - ord(self.tup[0]) == y1 - self.tup[1]:
                return True
            return False
        else:
            if x1 - self.tup[0] == y1 - self.tup[1]:
                return True
            return False


class Queen(Piece):
    '''Represents Queen'''
    def validate(self, x1, y1):
        '''Validates queen
        (Queen,int,int)->bool
        '''
        super().validate(x1, y1)
        if (x1 == self.tup[0] or y1 == self.tup[1]) and not (x1 == self.tup[0] and y1 == self.tup[1]):
            return True
        return False


class King(Piece):
    '''Represents king'''
    def validate(self, x1, y1):
        '''Validates king
        (King,int,int)->bool
        '''
        super().validate(x1, y1)
        if isinstance(x1, str):
            if (ord(x1) == ord(self.tup[0]) and (y1 == self.tup[1] + 1 or y1 == self.tup[1] - 1)) and (
                    (ord(x1) == self.tup[0] + 1 or x1 == self.tup[0] - 1) or (
                    y1 == self.tup[1] + 1 or y1 == self.tup[1] - 1 or y1 == self.tup[1])):
                return True
            return False
        if (x1 == self.tup[0] and (y1 == self.tup[1] + 1 or y1 == self.tup[1] - 1)) and (
                (x1 == self.tup[0] + 1 or x1 == self.tup[0] - 1) or (
                y1 == self.tup[1] + 1 or y1 == self.tup[1] - 1 or y1 == self.tup[1])):
            return True
        return False


class Knight(Piece):
    '''Represents knight'''
    def validate(self, x1, y1):
        '''Validates knight
        (Knight,int,int)->bool
        '''
        super().validate(x1, y1)
        if ((x1 == self.tup[0] + 1 or x1 == self.tup[0] - 1) and (y1 == self.tup[1] + 2 or y1 == self.tup[1] - 2)) or (
                (x1 == self.tup[0] + 2 or x1 == self.tup[0] - 2) and (y1 == self.tup[1] + 1 or y1 == self.tup[1] - 1)):
            return True
        return False


class Rook(Piece):
    '''Class for rook representation'''
    def validate(self, x1, y1):
        '''Validates rook
        (Rook,int,int)->bool
        '''
        super().validate(x1, y1)
        if x1 == self.tup[0]:
            return True
        return False


board = ChessboardTwo("chessboard for two players")
board1 = ChessboardGlynskyii("один з варіантів шестикутних шахів Глинського")
board2 = ChessboardSix("шестикутна шахівниця для гри утрьох зі стартовою позицією")
board3 = ChessboardFour("шахівниця для гри учотирьох зі стартовою позицією")
board4 = ChessboardDouble("шахівниця для подвоєних шахів зі стартовою позицією")
board_for_two = ChessboardTwo("chessboard for two players").create_board()
board_Glynskii = ChessboardGlynskyii("один з варіантів шестикутних шахів Глинського").create_board()
board_for_six = ChessboardSix("шестикутна шахівниця для гри утрьох зі стартовою позицією").create_board()
board_for_four = board3.create_board()
board_double = board4.create_board()
if isinstance(board, ChessboardTwo):
    board.__str__()
    white_knights = [Knight("knight", board_for_two[1][0], board, "White"),
                     Knight("knight", board_for_two[6][0], board, "White")]
    black_knights = [Knight("knight", board_for_two[1][7], board, "Black"),
                     Knight("knight", board_for_two[6][7], board, "Black")]
    white_bishops = [Bishop("bishop", board_for_two[2][0], board, "White"),
                     Bishop("bishop", board_for_two[5][0], board, "White")]
    black_bishops = [Bishop("bishop", board_for_two[2][7], board, "Black"),
                     Bishop("bishop", board_for_two[5][7], board, "Black")]
    white_rooks = [Rook("rook", board_for_two[0][0], board, "White"),
                   Rook("rook", board_for_two[7][0], board, "White")]
    black_rooks = [Rook("rook", board_for_two[0][7], board, "Black"),
                   Rook("rook", board_for_two[7][7], board, "Black")]
    black_pawns = [Pawn("pawn", board_for_two[j][6], board, "Black") for j in range(0, 8)]
    white_pawns = [Pawn("pawn", board_for_two[j][1], board, "White") for j in range(0, 8)]
    white_queen = [Queen("queen", board_for_two[3][0], board, "White")]
    black_queen = [Queen("queen", board_for_two[3][7], board, "Black")]
    white_king = [King("king", board_for_two[4][0], board, "White")]
    black_king = [King("king", board_for_two[4][7], board, "Black")]
    pieces = [white_pawns, black_pawns, white_bishops, black_bishops, white_knights, black_knights, white_rooks,
              black_rooks, white_king, white_queen, black_king, black_queen]
    game1 = ChessSet(board, pieces)
    print(write_the_board(pieces))
    print("\nFree: \n", search_not_free_positions(pieces,board))
    print(moving_checks(white_pawns, white_rooks, white_queen, white_king, white_bishops, white_knights, game1))
if isinstance(board1, ChessboardGlynskyii):
    board1.create_board()
    board1.__str__()
    white_knights = [Knight("knight", board_Glynskii[3][0], board1, "White"),
                     Knight("knight", board_Glynskii[7][0], board1, "White")]
    black_knights = [Knight("knight", board_Glynskii[3][8], board1, "Black"),
                     Knight("knight", board_Glynskii[7][8], board1, "Black")]
    white_queen = [Queen("queen", board_Glynskii[4][0], board1, "White")]
    black_queen = [Queen("queen", board_Glynskii[4][9], board1, "Black")]
    white_king = [King("king", board_Glynskii[6][0], board1, "White")]
    black_king = [King("king", board_Glynskii[6][9], board1, "Black")]
    white_bishops = [Bishop("bishop", board_Glynskii[5][i], board1, "White") for i in range(3)]
    black_bishops = [Bishop("bishop", board_Glynskii[5][8:12], board1, "Black")]
    white_rooks = [Rook("rook", board_Glynskii[2][0], board1, "White"),
                   Rook("rook", board_Glynskii[8][0], board1, "White")]
    black_rooks = [Rook("rook", board_Glynskii[2][7], board1, "Black"),
                   Rook("rook", board_Glynskii[8][7], board1, "Black")]
    black_pawns = [Pawn("pawn", board_Glynskii[k][6], board1, "Black") for k in range(1, 10)]
    white_pawns = [Pawn("pawn", board_Glynskii[1][0], board1, "White"),
                   Pawn("pawn", board_Glynskii[2][1], board1, "White"),
                   Pawn("pawn", board_Glynskii[3][2], board1, "White"),
                   Pawn("pawn", board_Glynskii[4][3], board1, "White"),
                   Pawn("pawn", board_Glynskii[5][4], board1, "White"),
                   Pawn("pawn", board_Glynskii[6][4], board1, "White"),
                   Pawn("pawn", board_Glynskii[7][3], board1, "White"),
                   Pawn("pawn", board_Glynskii[8][2], board1, "White"),
                   Pawn("pawn", board_Glynskii[9][1], board1, "White")]
    pieces = [white_pawns, black_pawns, white_bishops, black_bishops, white_knights, black_knights,
              white_rooks, black_rooks, white_king, white_queen, black_king, black_queen]
    game2 = ChessSet(board1, pieces)
    print(write_the_board(pieces))
    print("\nFree: \n", search_not_free_positions(pieces,board1))
if isinstance(board2, ChessboardSix):
    board2.create_board()
    board2.__str__()
    white_knights = [Knight("knight", board_for_six[1][0], board2, "White"),
                     Knight("knight", board_for_six[6][0], board2, "White")]
    black_knights = [Knight("knight", board_for_six[1][7], board2, "Black"),
                     Knight("knight", board_for_six[6][7], board2, "Black")]
    red_knights = [Knight("knight", board_for_six[1][10], board2, "Red"),
                   Knight("knight", board_for_six[6][10], board2, "Red")]
    white_queen = [Queen("queen", board_for_six[3][0], board2, "White")]
    black_queen = [Queen("queen", board_for_six[3][7], board2, "Black")]
    red_queen = [Queen("queen", board_for_six[3][10], board2, "Red")]
    white_king = [King("king", board_for_six[4][0], board2, "White")]
    black_king = [King("king", board_for_six[4][7], board2, "Black")]
    red_king = [King("king",board_for_six[4][10], board2, "Red")]
    white_bishops = [Bishop("bishop", board_for_six[2][0], board2, "White"),
                     Bishop("bishop", board_for_six[5][0], board2, "White")]
    black_bishops = [Bishop("bishop", board_for_six[2][7], board2, "Black"),
                     Bishop("bishop", board_for_six[5][7], board2, "White")]
    red_bishops = [Bishop("bishop", board_for_six[2][10], board2, "Red"),
                   Bishop("bishop", board_for_six[5][10], board2, "Red")]
    red_pawns = [Pawn("pawn", board_for_six[k][6], board2, "Red") for k in range(7)]
    white_pawns = [Pawn("pawn", board_for_six[k][1], board2, "White") for k in range(7)]
    black_pawns = [Pawn("pawn", board_for_six[k][10], board2, "Black") for k in range(7)]
    red_rooks = [Rook("rook", board_for_six[0][7], board2, "Red"),
                 Rook("rook", board_for_six[7][7], board2, "Red")]
    white_rooks = [Rook("rook", board_for_six[0][0], board2, "White"),
                   Rook("rook", board_for_six[7][0], board2, "White")]
    black_rooks = [Rook("rook", board_for_six[0][10], board2, "Black"),
                   Rook("rook", board_for_six[7][10], board2, "Black")]
    pieces = [red_pawns, white_pawns, black_pawns, white_rooks, red_rooks, black_rooks, white_bishops, black_bishops,
              red_bishops, red_knights, black_knights, white_knights, white_queen, black_queen, red_queen, white_king,
              black_king, red_king]
    print(write_the_board(pieces))
    print("\nFree: \n", search_not_free_positions(pieces,board2))
if isinstance(board3, ChessboardFour):
    board3.__str__()
    white_knights = [Knight("knight", board_for_four[4][0], board3, "White"),
                     Knight("knight", board_for_four[9][0], board3, "White")]
    black_knights = [Knight("knight", board_for_four[4][7], board3, "Black"),
                     Knight("knight", board_for_four[9][7], board3, "Black")]
    red_knights = [Knight("knight", board_for_four[0][4], board3, "Red"),
                   Knight("knight", board_for_four[0][9], board3, "Red")]
    blue_knights = [Knight("knight", board_for_four[13][4], board3, "Blue"),
                    Knight("knight", board_for_four[13][9], board3, "Blue")]
    white_bishops = [Bishop("bishop", board_for_four[5][0], board3, "White"),
                     Bishop("bishop", board_for_four[8][0], board3, "White")]
    black_bishops = [Bishop("bishop", board_for_four[5][13], board3, "Black"),
                     Bishop("bishop", board_for_four[8][13], board3, "Black")]
    red_bishops = [Bishop("bishop", board_for_four[0][5], board3, "Red"),
                   Bishop("bishop", board_for_four[0][8], board3, "Red")]
    blue_bishops = [Bishop("bishop", board_for_four[12][5], board3, "Blue"),
                    Bishop("bishop", board_for_four[12][8], board3, "Blue")]
    black_rooks = [Rook("rook", board_for_four[3][0], board3, "Black"),
                   Rook("rook", board_for_four[9][0], board3, "Black")]
    white_rooks = [Rook("rook", board_for_four[3][0], board3, "White"),
                   Rook("rook", board_for_four[9][0], board3, "White")]
    red_rooks = [Rook("rook", board_for_four[0][3], board3, "Red"),
                 Rook("rook", board_for_four[0][10], board3, "Red")]
    blue_rooks = [Rook("rook", board_for_four[12][3], board3, "Blue"),
                  Rook("rook", board_for_four[12][10], board3, "Blue")]
    black_pawns = [Pawn("pawn", board_for_four[j][1], board3, "Black") for j in range(3, 10)]
    white_pawns = [Pawn("pawn", board_for_four[j][13], board3, "White") for j in range(3, 10)]
    red_pawns = [Pawn("pawn", board_for_four[1][j], board3, " Red") for j in range(3, 11)]
    blue_pawns = [Pawn("pawn", board_for_four[11][j], board3, "Blue") for j in range(3, 11)]
    white_queen = [Queen("queen", board_for_four[7][0], board3, "White")]
    black_queen = [Queen("queen", board_for_four[6][13], board3, "Black")]
    red_queen = [Queen("queen", board_for_four[0][7], board3, "Red")]
    blue_queen = [Queen("queen", board_for_four[13][6], board3, "Blue")]
    white_king = [King("king", board_for_four[6][0], board3, "White")]
    black_king = [King("king", board_for_four[7][13], board3, "Black")]
    red_king = [King("king", board_for_four[0][6], board3, "Red")]
    blue_king = [King("king", board_for_four[13][7], board3, "Blue")]
    pieces = [white_pawns, black_pawns, red_pawns, blue_pawns, white_rooks, black_rooks, blue_rooks, red_rooks,
              white_bishops, black_bishops, blue_bishops, red_bishops, white_knights, black_knights, blue_knights,
              red_knights, white_queen, black_queen, red_queen, blue_queen, white_king, black_king, red_king, blue_king]
    game1 = ChessSet(board3, pieces)
    print(write_the_board(pieces))
    print("\nFree: \n", search_not_free_positions(pieces,board3))
if isinstance(board4, ChessboardDouble):
    board.__str__()
    white_knights = [Knight("knight", board_double[1][0], board4, "White"),
                     Knight("knight", board_double[6][0], board4, "White"),
                     Knight("knight", board_double[9][0], board4, "White"),
                     Knight("knight", board_double[14][0], board4, "White")]
    black_knights = [Knight("knight", board_double[1][11], board4, "Black"),
                     Knight("knight", board_double[6][11], board4, "Black"),
                     Knight("knight", board_double[9][11], board4, "Black"),
                     Knight("knight", board_double[14][11], board4, "Black")]
    white_bishops = [Bishop("bishop", board_double[2][0], board4, "White"),
                     Bishop("bishop", board_double[5][0], board4, "White"),
                     Bishop("bishop", board_double[10][0], board4, "White"),
                     Bishop("bishop", board_double[13][0], board4, "White")]
    black_bishops = [Bishop("bishop", board_double[2][11], board4, "Black"),
                     Bishop("bishop", board_double[5][11], board4, "Black"),
                     Bishop("bishop", board_double[10][11], board4, "Black"),
                     Bishop("bishop", board_double[13][11], board4, "Black")]
    white_rooks = [Rook("rook", board_double[0][0], board4, "White"),
                   Rook("rook", board_double[7][0], board4, "White"),
                   Rook("rook", board_double[8][0], board4, "White"),
                   Rook("rook", board_double[15][0], board4, "White")]
    black_rooks = [Rook("rook", board_double[0][11], board4, "Black"),
                   Rook("rook", board_double[7][11], board4, "Black"),
                   Rook("rook", board_double[8][11], board4, "Black"),
                   Rook("rook", board_double[15][11], board4, "Black")]

    black_pawns = [Pawn("pawn", board_double[j][10], board4, "Black") for j in range(0, 16)]
    white_pawns = [Pawn("pawn", board_double[j][1], board4, "White") for j in range(0, 16)]
    white_queen = [Queen("queen", board_double[3][0], board4, "White"),
                   Queen("queen", board_double[11][0], board4, "White")]
    black_queen = [Queen("queen", board_double[3][11], board4, "Black"),
                   Queen("queen", board_double[11][11], board4, "Black")]
    white_king = [King("king", board_double[4][0], board4, "White"),
                  King("king", board_double[12][0], board4, "White")]
    black_king = [King("king", board_double[4][11], board4, "Black"),
                  King("king", board_double[12][11], board4, "Black")]
    pieces = [white_pawns, black_pawns, white_knights, black_knights, white_bishops, black_bishops, white_rooks,
              black_rooks, white_queen, black_queen, white_king, black_king]
    game4 = ChessSet(board4, pieces)
    print(write_the_board(pieces))
    print("\nFree: \n", search_not_free_positions(pieces, board4))
