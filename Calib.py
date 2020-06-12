import cv2 as cv
import numpy as np
import CameraGroup
import CharucoBoard as ucoBoard
import ChessBoard   as cheBoard



class Calib():
            def __init__(self,calibType,isfish=True,calibBoard=None):
                self.calibBoard=calibBoard
                self.calibType = 0
                #charuco
                self.cornersId = []
                self.cornersImg=[]
                self.cornersWorld = []
                self.cornersWorldWhole = []

                self.calibType=calibType
                self.isFish=isfish
                self._buildBoardCorrdination_3D()
                #rlt
                self.rvec=None
                self.tvec=None
                self.K=None
                self.D=None
            def detectCorners(self,img):
                if self.calibType==0:
                    if type(self.calibBoard) is not cheBoard.ChessBoard:return None
                    return self.detectChessBoard(img)
                else:
                    if type(self.calibBoard) is not ucoBoard.CharucoBoard:return None
                    return self.detectCharuco(img)


            def calibCamera(self,imgSize): #calib-->
               #retval, K, D, rvecs, tvecs
                retval=-1
                if self.isFish:
                    retval, self.K, self.D, self.rvec, self.tvec= cv.fisheye.calibrate(self.cornersWorld,self.cornersImg , imgSize, None,None)#None,None,0,(3,100,2.220446049250313e-16))
                else:
                    retval, self.K, self.D, self.rvec, self.tvec = cv.calibrateCamera(self.cornersWorld,self.cornersImg, imgSize, None,None)  # ,None,None,0,(3,10000,0.000001))
                return retval

            def detectCharuco(self,img):
                strictDetection=2 if self.calibType == 2 else 1
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


            def calcProjectErro(self,index):               #计算每张图的
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
    charuco=ucoBoard.CharucoBoard()
    charuco.create(11,7,0,2.5,[29.7,21],96)
    caliber=Calib(charuco)
    caliber.calibCamera((100,100))
    img=cv.imread('C:/Users/w/Desktop/3.png')
    caliber.detectCharuco(img)
