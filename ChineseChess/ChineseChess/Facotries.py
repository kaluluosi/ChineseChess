from ChessCfg import *
from Constant import *
from ChineseChess import *

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



