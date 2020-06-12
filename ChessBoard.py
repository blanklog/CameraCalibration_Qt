import cv2 as cv
import numpy as np

class CalibBoard():
    def __init__(self):
        self.partternSize=None
        self.squareSize=None

class  ChessBoard():
    def __init__(self):
        self.partternSize=(11,8)
        self.squareSize=2.5
        self.printSize=(29.7,21)
        self.dpi=96
    def create(self,parternSize,squareSize,dpi,imageSize):
        self.partternSize = parternSize
        self.squareSize = squareSize
        self.printSize = imageSize
        self.dpi = dpi
        return self.print()
    def print(self):
        dpi=self.dpi/2.54
        suqrelen=int(dpi*self.squareSize)
        imageSize=(int(self.printSize[0]*dpi),int(self.printSize[1]*dpi))
        board=(imageSize[0]-suqrelen*self.partternSize[0],imageSize[1]-suqrelen*self.partternSize[1])
        board=(board[0]//2,board[1]//2)
        chessBoard=np.array(np.zeros((imageSize[1],imageSize[0]),'uint8'))
        chessBoard[:]=255
        flag=1
        for i in range(0,self.partternSize[0]):
            flag=0 if flag else 1
            for j in range(flag,self.partternSize[1],2):
                x=(i*suqrelen+board[0],(i+1)*suqrelen+board[0])
                y=(j*suqrelen+board[1],(j+1)*suqrelen+board[1])
                chessBoard[y[0]:y[1],x[0]:x[1]]=0
        return chessBoard



if __name__ == '__main__':
    a=ChessBoard()
    b=a.create()
    cv.imshow('a',b)
    cv.imwrite('C:\\Users\\w\\Desktop\\chssboard.png',b)
    cv.waitKey()
