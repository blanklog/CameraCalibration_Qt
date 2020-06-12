import cv2 as cv
import numpy as np
import CameraGroup


dicts=['DICT_4X4_50','DICT_4X4_100','DICT_4X4_250','DICT_4X4_1000','DICT_5X5_50','DICT_5X5_100','DICT_5X5_250','DICT_5X5_1000','DICT_6X6_50','DICT_6X6_100','DICT_6X6_250'
,'DICT_6X6_1000','DICT_7X7_50','DICT_7X7_100','DICT_7X7_250','DICT_7X7_1000','DICT_ARUCO_ORIGINAL','DICT_APRILTAG_16h5','DICT_APRILTAG_25h9','DICT_APRILTAG_36h10','DICT_APRILTAG_36h11']

class  ChessBoard():
    def __init__(self):
        self.partternSize=(11,8)
        self.squareSize=2.5
        self.printSize=(29.7,21)
        self.dpi=96
    def create(self):
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

class CharucoBoard():
    def __init__(self):
        self.dict=None
    def create(self,numX,numY,dict:int,squareSize,imageSize:list,dpi:int):
         self.dpi=dpi #*100/2.54   #pixel per inch
         self.dictID=dict
         self.partternSize=(numX,numY)
         self.imgSize=imageSize
         self.squareSize=squareSize
         self.markerSize=squareSize*0.6
         self.dictionary = cv.aruco.getPredefinedDictionary(dict)
         self.board=cv.aruco.CharucoBoard_create(numX,numY,self.squareSize,self.markerSize,self.dictionary)
         minSize=min(imageSize[0]-squareSize*numX,imageSize[1]-squareSize*numY)/2
         if minSize<0:
             print('too much square!')
             return None
         print((int(imageSize[0]*dpi),int(imageSize[1]*dpi)),int(minSize*dpi))
         img = self.board.draw((int(imageSize[0]*self.dpi/2.54),int(imageSize[1]*self.dpi/2.54)),None,int(minSize*self.dpi/2.54),1)
         return img
    def saveConfig(self,path):
        file=cv.FileStorage(path+'/charucoBoard_Parameter.yml',cv.FileStorage_WRITE)
        file.write('DPI', self.dpi)
        file.write('dictID', self.dictID)
        file.write('squareNumber_X', self.partternSize[0])
        file.write('squareNumber_Y', self.partternSize[1])
        file.write('imageSize_X', self.imgSize[0])
        file.write('imageSize_Y', self.imgSize[1])
        file.write('squareSize', self.squareSize)
        file.write('markSize',self.markerSize)
        file.release()
    def loadFromFile(self,path):
        file=cv.FileStorage(path+'/charucoBoard_Parameter.yml',cv.FileStorage_READ)
        pass #unimplemented
        file.release()








