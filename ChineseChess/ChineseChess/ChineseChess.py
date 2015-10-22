from Facotries import *
from Constant import *


class ChessBoard(object):
    maxRaw = 10
    maxCol = 9

    def __init__(self, **kwargs):
        self.board = [
            ['_' for c in range(0, ChessBoard.maxCol)] for r in range(0, ChessBoard.maxRaw)]
        self.removedChesses = []

    def setChess(self, chess, raw, col):
        if ChessBoard.checkPosValid(raw, col) == False:
            raise ValueError('%s,%s is out of range' % (raw, col))

        if isinstance(self.board[raw][col], Chess):
            self.removedChesses.append(self.board[raw][col])
        self.board[raw][col] = chess

    def removeChess(self, raw, col):
        if ChessBoard.checkPosValid(raw, col) == False:
            raise ValueError('%s,%s is out of range' % (raw, col))

        self.board[raw][col] = '_'

    def getChess(self, raw, col):
        if ChessBoard.checkPosValid(raw, col) == False:
            raise ValueError('%s,%s is out of range' % (raw, col))
        chs = self.board[raw][col]
        return chs if isinstance(chs, Chess) else None

    def moveChessTo(self, raw, col, tgRaw, tgCol):
        if (ChessBoard.checkPosValid(raw, col) and ChessBoard.checkPosValid(tgRaw, tgCol)) == False:
            raise ValueError('%s,%s or %s,%s is out of range' %
                             (raw, col, tgRaw, tgCol))
        chs = self.getChess(raw, col)
        if chs and chs.checkMove(self, raw, col, tgRaw, tgCol):
            self.setChess(chs, tgRaw, tgCol)
            self.removeChess(raw, col)
            return True
        else:
            return False

    def countBetween(self, raw, col, tgRaw, tgCol):
        if raw - tgRaw != 0 and col - tgCol != 0:
            return False
        count = 0
        rangeRaw = [raw, tgRaw]
        rangeCol = [col, tgCol]
        rangeRaw.sort()
        rangeCol.sort()
        if raw - tgRaw == 0:
            '横向检查'
            r = self.board[raw]
            for chs in r[rangeCol[0]:rangeCol[1]+1]:
                if isinstance(chs, Chess):
                    count += 1
        else:
            '纵向检查'
            for r in self.board[rangeRaw[0]:rangeRaw[1]+1]:
                if isinstance(r[col], Chess):
                    count += 1
        return count

    def printBoard(self):
        for r in range(ChessBoard.maxRaw):
            for c in range(ChessBoard.maxCol):
                if isinstance(self.board[r][c], Chess):
                    self.board[r][c] = str(self.board[r][c])
        for r in self.board:
            print(r)

    def checkPosValid(raw, col):
        return 0 <= raw < ChessBoard.maxRaw and 0 <= col < ChessBoard.maxCol


class Chess(object):

    def __init__(self, name='Pawn', owner=Player.Red, moveFunc=lambda: True):
        self.name = name
        self.owner = owner
        self.moveFunc = moveFunc

    def checkMove(self, chessboard, raw, col, tgRaw, tgCol):
        if self.moveFunc != None:
            return self.moveFunc(self, chessboard, raw, col, tgRaw, tgCol)
        else:
            return False

    def __str__(self, **kwargs):
        return self.name[0].upper()


def main():
    cb = ChessBoardFacotry.standard()

    print(cb.moveChessTo(9, 3, 8, 3))
    print(cb.moveChessTo(8, 3, 7, 4))
    print(cb.moveChessTo(8, 3, 8, 4))
    print(cb.moveChessTo(8, 4, 9, 5))
    print(cb.moveChessTo(8, 4, 7, 5))
    print(cb.moveChessTo(8, 5, 7, 6))
    print(cb.removedChesses)

    cb.printBoard()


if __name__ == '__main__':
    main()
