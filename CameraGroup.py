import cv2 as cv;
import numpy as np


class CameraParameter():
    def __init__(self):
        self.focal=0
        self.aspect=1
        self.principal=[0,0]
        self.R=np.empty(0)
        self.distortion=np.empty(0)
    def writeToFile(self,fs):
        fs.write('focal',self.focal)
        fs.write('aspect',self.aspect)
        fs.write('principal_x',self.principal[0])
        fs.write('principal_y',self.principal[1])
        #fs.write('principal','[ '+str(self.principal[0])+', '+str(self.principal[1])+' ]')
        fs.write('R',np.empty(0))
        fs.write('distortion',self.distortion)
    def loadFromFile(self,fn):
        self.focal=fn.getNode('focal').real()
        self.aspect=fn.getNode('aspect').real()
        self.principal[0]=fn.getNode('principal_x').real()
        self.principal[1]=fn.getNode('principal_y').real()
        self.R=fn.getNode('R').mat()
        self.distortion=fn.getNode('distortion').mat()
    def print(self):
        print('focal:%f'%self.focal)
        print('aspect:%f'%self.aspect)
        print('principal:%f' % self.focal)
        print('R:',self.R,sep='\n')
        print('distortion:', self.distortion,sep='\n')


#=====================================
class CameraGroup():
    def __init__(self):
        self.cameras=[]
    def loadFromFile(self,fileName):
        A=cv.FileStorage_READ
        fs=cv.FileStorage(fileName,cv.FileStorage_FORMAT_YAML )
        if fs.isOpened()==False:
            print("Open Failed")
            return;
        n = int(fs.getNode('number').real())
        self.cameras=[]
        for i in range(n):
            node=fs.getNode('Camera_'+str(i))
            if node.empty()==True:
                print('Erro Camera_'+str(i)+'read failed!')
            camera=CameraParameter()
            camera.loadFromFile(node)
            self.cameras.append(camera)
    def saveToFile(self,fileName):
        fs=cv.FileStorage(fileName,cv.FileStorage_WRITE)
        n=0
        fs.write('number',len(self.cameras))
        for c in self.cameras:
            c.writeToFile(fs)
            n=n+1
        fs.release()

    def displayAll(self):
        for i in range(len(self.cameras)):
            print('-'*50)
            print('Camera_'+str(i))
            self.cameras[i].print()

    # def plot(self):
    #     rect = np.array([[1, -1, -1, 1, 1], [1, 1, -1, -1, 1], [1, 1, 1, 1, 1]])
    #     z = np.array([[0], [0], [1]])
    #     fig = plt.figure()
    #     ax = fig.gca(projection='3d')
    #     for i in range(len(self.cameras)):
    #         camera=np.matmul(self.cameras[i][1],rect)
    #         light=np.zeros((3,2))
    #         light[:,1,np.newaxis]=np.matmul(self.cameras[i][1],z)
    #         a=ax.plot(camera[0],camera[1],camera[2])
    #         b=a[0]._color
    #         ax.plot(light[0],light[1],light[2],color=b)
    #         #fig.show()
    #     plt.show()
    #    # input()
    #
    #
    #





if __name__ =='__main__':
    cg=CameraGroup()
    cg.saveToFile('E:/Code/pyside2/1_1gourp.yml')
    #cg.displayAll()
    #cg.plot()
