import cv2 as cv
import numpy as np
import CameraGroup
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
        file.release()

class Calib():
            def __init__(self,type,isfish=True,calibBoard=None):
                self.calibBoard=calibBoard
                #charuco
                self.cornersId = []
                self.cornersImg=[]
                self.cornersWorld = []
                self.cornersWorldWhole = []

                self.type=type
                self.isFish=isfish
                self._buildBoardCorrdination_3D()
                #rlt
                self.rvec=None
                self.tvec=None
                self.K=None
                self.D=None
            def detectCorners(self,img):
                if self.type==0:
                    if type(self.calibBoard) is not ChessBoard:return None
                    return self.detectChessBoard(img)
                else:
                    if type(self.calibBoard) is not CharucoBoard:return None
                    return self.detectCharuco(img)


            def calibCamera(self,imgSize):
               #retval, K, D, rvecs, tvecs
                retval=-1
                if self.isFish:
                    retval, self.K, self.D, self.rvec, self.tvec= cv.fisheye.calibrate(self.cornersWorld,self.cornersImg , imgSize, None,None)#None,None,0,(3,100,2.220446049250313e-16))
                else:
                    retval, self.K, self.D, self.rvec, self.tvec = cv.calibrateCamera(self.cornersWorld,self.cornersImg, imgSize, None,None)  # ,None,None,0,(3,10000,0.000001))

                return retval

            def detectCharuco(self,img):

                strictDetection=2 if self.type==2 else 1
                corners,ids,re =cv.aruco.detectMarkers(img,self.calibBoard.dictionary)
                if ids is not None:
                    number,chCorners,chIds=cv.aruco.interpolateCornersCharuco(corners, ids, img,self.calibBoard.board,None,None,None,None,strictDetection)
                    if number>=8:
                        self.cornersImg.append(np.array(chCorners))
                        correspondingCornersWorld=[]
                        for i in chIds[:,0]:
                            correspondingCornersWorld.append(self.cornersWorldWhole[i])
                        self.cornersId.append(chIds)
                        self.cornersWorld.append(np.array(correspondingCornersWorld))
                        image = cv.aruco.drawDetectedCornersCharuco(img, chCorners,chIds)
                        return image
            def detectChessBoard(self,img):
                print('Chess Board Detect')
                partternSize=self.calibBoard.partternSize
                partternSize=(partternSize[0]-1,partternSize[1]-1)
                retval, corners = cv.findChessboardCorners(img, partternSize)
                if retval:
                    self.cornersImg.append(np.array(corners))
                    self.cornersWorld.append(self.cornersWorldWhole)
                image=cv.drawChessboardCorners(img, partternSize, corners, retval)
                return image


            def calcProjectErro(self,index):
                sum=0
                if self.isFish:
                    imagePoints, __ = cv.fisheye.projectPoints(self.cornersWorld[index], self.rvec[index], self.tvec[index], self.K, self.D)
                else:
                    imagePoints,__  = cv.projectPoints(self.cornersWorld[index], self.rvec[index], self.tvec[index], self.K, self.D)


                for point,repoint in zip(self.cornersImg[index][:,0],imagePoints[:,0]):
                     sum=sum+np.linalg.norm(point-repoint)
                sum=sum/len(self.cornersImg[index])
                 #sum=np.sqrt(sum)/len(self.cornersImg[index])
                return sum

            def getCameraParameter(self):
                cParameter = CameraGroup.CameraParameter()
                cParameter.focal=self.K[0,0]
                cParameter.aspect=self.K[1,1]/self.K[0,0]
                cParameter.principal=[self.K[0,2],self.K[1,2]]
                cParameter.distortion=self.D
                return cParameter


            def _buildBoardCorrdination_3D(self):
                squareSize = self.calibBoard.squareSize / 100
                for y in range(self.calibBoard.partternSize[1]-1):
                    for x in range(self.calibBoard.partternSize[0]-1):
                        self.cornersWorldWhole.append([[x*squareSize,y*squareSize,0]])

                self.cornersWorldWhole=np.array(self.cornersWorldWhole,'float32')







if __name__ == "__main__":
    charuco=CharucoBoard()
    charuco.create(11,7,0,2.5,[29.7,21],96)
    caliber=Calib(charuco)
    caliber.calibCamera((100,100))
    img=cv.imread('C:/Users/w/Desktop/3.png')
    caliber.detectCharuco(img)
