import enum

BOUND_RAW = 10
BOUND_COL = 9

class Player(enum.Enum):
    Red = 0
    Blue = 1

class Chess(object):
    """棋子类"""
    def __init__(self,name='-',owner=Player.Red,raw=-1,col=-1,checkmoveFunc=None):
        #名字
        self.name = name
        #拥有者
        self.owner = owner
        #坐标 行raw 列col
        self.raw = raw
        self.col = col
        #移动判断函数
        self.checkMoveFunc = checkmoveFunc
    
    def checkMovable(self,chesses,tgtRaw,tgtCol):
        """chesses 期盘上的所有棋子，tgtRaw目标行，tgtCol目标列"""
        if  checkMoveFunc == None:
            return False
        return self.checkMoveFunc(chesses,self.raw,self.col,tgtRaw,tgtCol)

    def __str__(self):
        return self.name[0].upper()

#用来测试函数
def main():
    printChessBoard(None)

#打印棋盘
def printChessBoard(chesses):
    position = [ [ '_' for col in range(BOUND_COL)] for raw in range(BOUND_RAW)]

    if chesses:
        for chs in chesses:
            position[chs.raw][chs.col]=str(chs)
        
    for raw in position:
        print(raw) 

if __name__ == '__main__':
    main()