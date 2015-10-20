import ChessCfg

class Player(object):
    Red = 0
    Blue = 1


class ChessBoard(object):
    maxRaw = 10
    maxCol = 9
    def __init__(self, **kwargs):
        self.board = [ [ '_' for c in range(0,ChessBoard.maxCol)] for r in range(0,ChessBoard.maxRaw)]
        self.removedChesses = []

    def setChess(self,chess,raw,col):
        if ChessBoard.checkPosValid(raw,col) == False:
            raise ValueError('%s,%s is out of range' % (raw,col))

        if isinstance(self.board[raw][col],Chess):
            self.removedChesses.append(self.board[raw][col])
        self.board[raw][col] = chess

    def removeChess(self,raw,col):
        if ChessBoard.checkPosValid(raw,col) == False:
            raise ValueError('%s,%s is out of range' % (raw,col))

        self.board[raw][col] = '_'

    def getChess(self,raw,col):
        if ChessBoard.checkPosValid(raw,col) == False:
            raise ValueError('%s,%s is out of range' % (raw,col))
        chs = self.board[raw][col]
        return chs if isinstance(chs,Chess) else None

    def moveChessTo(self,raw,col,tgRaw,tgCol):
        if (ChessBoard.checkPosValid(raw,col) and ChessBoard.checkPosValid(tgRaw,tgCol))==False:
            raise ValueError('%s,%s or %s,%s is out of range' % (raw,col,tgRaw,tgCol))
        chs = self.getChess(raw,col)
        if chs and chs.checkMove(self,raw,col,tgRaw,tgCol):
            self.setChess(chs,tgRaw,tgCol)
            self.removeChess(raw,col)
            return True
        else:
            return False

    def countBetween(self,raw,col,tgRaw,tgCol):
        if raw - tgRaw != 0 and col - tgCol != 0:
            return False
        count = 0
        rangeRaw = [raw,tgRaw]
        rangeCol = [col,tgCol]
        rangeRaw.sort()
        rangeCol.sort()
        if raw - tgRaw == 0:
            '横向检查'
            r = self.board[raw]
            for chs in r[rangeCol[0]:rangeCol[1]+1]:
                if isinstance(chs,Chess):
                    count+=1
        else:
            '纵向检查'
            for r in self.board[rangeRaw[0]:rangeRaw[1]+1]:
                if isinstance(r[col],Chess):
                    count+=1
        return count

    def printBoard(self):
        for r in range(ChessBoard.maxRaw):
            for c in range(ChessBoard.maxCol):
                if isinstance(self.board[r][c],Chess):
                    self.board[r][c] = str(self.board[r][c])
        for r in self.board:
            print(r)

    def checkPosValid(raw,col):
        return 0 <= raw < ChessBoard.maxRaw and 0 <= col < ChessBoard.maxCol

class Chess(object):
    def __init__(self, name='Pawn',owner=Player.Red,moveFunc=lambda:True):
        self.name = name
        self.owner = owner
        self.moveFunc = moveFunc
    
    def checkMove(self,chessboard,raw,col,tgRaw,tgCol):
        if self.moveFunc != None:
            return self.moveFunc(self,chessboard,raw,col,tgRaw,tgCol)
        else:
            return False

    def __str__(self, **kwargs):
        return self.name[0].upper()

class ChessFactory(object):
    def create(name,owner):
        chs = Chess(name,owner)
        chs.moveFunc = funcs.get(name,'Default')
        return chs
        

class ChessBoardFacotry(object):
    def standard():
        cb = ChessBoard()
        posData = {
              Player.Red:{
                    'Pawn':([6,0],[6,2],[6,4],[6,6],[6,8]),
                    'Cannon':([7,1],[7,7]),
                    'Rook':([9,0],[9,8]),
                    'Knight':([9,1],[9,7]),
                    'Elephant':([9,2],[9,6]),
                    'Mandarin':([9,3],[9,5]),
                    'King':([9,4],)
                  },
              Player.Blue:{
                    'Pawn':([3,0],[3,2],[3,4],[3,6],[3,8]),
                    'Cannon':([2,1],[2,7]),
                    'Rook':([0,0],[0,8]),
                    'Knight':([0,1],[0,7]),
                    'Elephant':([0,2],[0,6]),
                    'Mandarin':([0,3],[0,5]),
                    'King':([0,4],)
                  }
               }
        for owner,data in posData.items():
            for name,poses in data.items():
                chs = ChessFactory.create(name,owner)
                for pos in poses:
                    cb.setChess(chs,pos[0],pos[1])
        return cb
    def load(data):
        pass


def defaultFunc(self,chessboard,raw,col,tgRaw,tgCol):
    return True

def pawnFunc(self,chessboard,raw,col,tgRaw,tgCol):
    if abs(raw-tgRaw)+abs(col-tgCol) !=1:
        return False
    chs = chessboard.getChess(tgRaw,tgCol)
    if (chs and chs.owner != self.owner) or chs==None:
        return True
    else:
        return 

def cannonFunc(self,chessboard,raw,col,tgRaw,tgCol):
    if raw -tgRaw!=0 and col-tgCol!=0:
        return False
    count = chessboard.countBetween(raw,col,tgRaw,tgCol)
    if count ==1:
        return True
    elif count ==3:
        chs = chessboard.getChess(tgRaw,tgCol)
        if chs and chs.owner!=self.owner:
            return True
    return False

def rookFunc(self,chessboard,raw,col,tgRaw,tgCol):
    if raw -tgRaw!=0 and col-tgCol!=0:
        return False
    count = chessboard.countBetween(raw,col,tgRaw,tgCol)
    if count == 1:
        return True
    elif count == 2:
        chs = chessboard.getChess(tgRaw,tgCol)
        if chs and chs.owner!=chs.owner:
            return True
    return False

def knightFunc(self,chessboard,raw,col,tgRaw,tgCol):
    if abs(raw-tgRaw)!=2 and abs(col-tgCol)!=1:
        return False
    blockPos =[[raw-1,col],[raw+1,col],[raw,col-1],[raw,col+1]]
    for pos in blockPos:
        if ChessBoard.checkPosValid(pos[0],pos[1])==False:
            blockPos.remove(pos)
    blocks = []
    for pos in blockPos:
        chs = chessboard.getChess(pos[0],pos[1])
        if chs:
            blocks.append([pos[0],pos[1]])
    for pos in blocks:
        if abs(pos[0]-tgRaw)==1 and abs(pos[1]-tgCol)==1:
            return False
    
    chs = chessboard.getChess(tgRaw,tgCol)
    if (chs and chs.owner != self.owner) or chs==None:
        return True
    else:
        return False

def elephantFunc(self,chessboard,raw,col,tgRaw,tgCol):
    if abs(raw-tgRaw)!=2 and abs(col-tgCol)!=2:
        return False
    blockPos = [[raw+1,col+1],[raw-1,col+1],[raw-1,col-1],[raw-1,col+1]]
    for pos in blockPos:
        if ChessBoard.checkPosValid(pos[0],pos[1])==False:
            blockPos.remove(pos)
    blocks = []
    for pos in blockPos:
        chs = chessboard.getChess(pos[0],pos[1])
        if chs:
            blocks.append([pos[0],pos[1]])
    for pos in blocks:
        if abs(pos[0]-tgRaw)==1 and abs(pos[1]-tgCol)==1:
            return False

    chs = chessboard.getChess(tgRaw,tgCol)
    if (chs and chs.owner != self.owner) or chs==None:
        return True
    else:
        return False

def mandarinFunc(self,chessboard,raw,col,tgRaw,tgCol):
    if self.owner==Player.Red and (7<=tgRaw<=9 and 3<=tgCol<=5)==False:
        return False
    if self.owner==Player.Blue and (0<=tgRaw<=2 and 3<=tgCol<=5)==False:
        return False

    posDict = {
        (8,3):[[8,4],[7,3],[9,3]],
        (8,5):[[8,4],[7,5],[9,5]],
        (7,4):[[7,3],[7,5],[8,4]],
        (9,4):[[9,3],[9,5],[8.4]]
        }
    pos = posDict.get((raw,col))
    if pos and [tgRaw,tgCol] not in pos:
        return False

    chs = chessboard.getChess(tgRaw,tgCol)
    if (chs and chs.owner != self.owner) or chs==None:
        return True
    else:
        return False
            



funcs ={
        'Default':defaultFunc,
        'Pawn':pawnFunc,
        'Cannon':cannonFunc,
        'Rook':rookFunc,
        'Knight':knightFunc,
        'Elephant':elephantFunc,
        'Mandarin':mandarinFunc
    }



def main():
    cb = ChessBoardFacotry.standard()

    print(cb.moveChessTo(9,3,8,3))
    print(cb.moveChessTo(8,3,7,4))
    print(cb.moveChessTo(8,3,8,4))
    print(cb.moveChessTo(8,4,9,5))
    print(cb.moveChessTo(8,4,7,5))
    print(cb.moveChessTo(8,5,7,6))
    print(cb.removedChesses)

    cb.printBoard()


if __name__ == '__main__':
	main()