from Constant import *

def defaultFunc(self, chessboard, raw, col, tgRaw, tgCol):
    return True


def pawnFunc(self, chessboard, raw, col, tgRaw, tgCol):
    if abs(raw-tgRaw)+abs(col-tgCol) != 1:
        return False
    chs = chessboard.getChess(tgRaw, tgCol)
    if (chs and chs.owner != self.owner) or chs == None:
        return True
    else:
        return


def cannonFunc(self, chessboard, raw, col, tgRaw, tgCol):
    if raw - tgRaw != 0 and col-tgCol != 0:
        return False
    count = chessboard.countBetween(raw, col, tgRaw, tgCol)
    if count == 1:
        return True
    elif count == 3:
        chs = chessboard.getChess(tgRaw, tgCol)
        if chs and chs.owner != self.owner:
            return True
    return False


def rookFunc(self, chessboard, raw, col, tgRaw, tgCol):
    if raw - tgRaw != 0 and col-tgCol != 0:
        return False
    count = chessboard.countBetween(raw, col, tgRaw, tgCol)
    if count == 1:
        return True
    elif count == 2:
        chs = chessboard.getChess(tgRaw, tgCol)
        if chs and chs.owner != chs.owner:
            return True
    return False


def knightFunc(self, chessboard, raw, col, tgRaw, tgCol):
    if abs(raw-tgRaw) != 2 and abs(col-tgCol) != 1:
        return False
    blockPos = [[raw-1, col], [raw+1, col], [raw, col-1], [raw, col+1]]
    for pos in blockPos:
        if ChessBoard.checkPosValid(pos[0], pos[1]) == False:
            blockPos.remove(pos)
    blocks = []
    for pos in blockPos:
        chs = chessboard.getChess(pos[0], pos[1])
        if chs:
            blocks.append([pos[0], pos[1]])
    for pos in blocks:
        if abs(pos[0]-tgRaw) == 1 and abs(pos[1]-tgCol) == 1:
            return False

    chs = chessboard.getChess(tgRaw, tgCol)
    if (chs and chs.owner != self.owner) or chs == None:
        return True
    else:
        return False


def elephantFunc(self, chessboard, raw, col, tgRaw, tgCol):
    if abs(raw-tgRaw) != 2 and abs(col-tgCol) != 2:
        return False
    blockPos = [[raw+1, col+1], [raw-1, col+1], [raw-1, col-1], [raw-1, col+1]]
    for pos in blockPos:
        if ChessBoard.checkPosValid(pos[0], pos[1]) == False:
            blockPos.remove(pos)
    blocks = []
    for pos in blockPos:
        chs = chessboard.getChess(pos[0], pos[1])
        if chs:
            blocks.append([pos[0], pos[1]])
    for pos in blocks:
        if abs(pos[0]-tgRaw) == 1 and abs(pos[1]-tgCol) == 1:
            return False

    chs = chessboard.getChess(tgRaw, tgCol)
    if (chs and chs.owner != self.owner) or chs == None:
        return True
    else:
        return False


def mandarinFunc(self, chessboard, raw, col, tgRaw, tgCol):
    if self.owner == Player.Red and (7 <= tgRaw <= 9 and 3 <= tgCol <= 5) == False:
        return False
    if self.owner == Player.Blue and (0 <= tgRaw <= 2 and 3 <= tgCol <= 5) == False:
        return False

    posDict = {
        (8, 3): [[8, 4], [7, 3], [9, 3]],
        (8, 5): [[8, 4], [7, 5], [9, 5]],
        (7, 4): [[7, 3], [7, 5], [8, 4]],
        (9, 4): [[9, 3], [9, 5], [8.4]]
    }
    pos = posDict.get((raw, col))
    if pos and [tgRaw, tgCol] not in pos:
        return False

    chs = chessboard.getChess(tgRaw, tgCol)
    if (chs and chs.owner != self.owner) or chs == None:
        return True
    else:
        return False


funcs = {
    'Default': defaultFunc,
    'Pawn': pawnFunc,
    'Cannon': cannonFunc,
    'Rook': rookFunc,
    'Knight': knightFunc,
    'Elephant': elephantFunc,
    'Mandarin': mandarinFunc
}
