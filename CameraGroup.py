import cv2 as cv;
import numpy as np
import matplotlib.pyplot as plt



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
        fs.write('ppx',self.principal[0])
        fs.write('ppy',self.principal[1])
        fs.write('R',np.empty(0))
        fs.write('distortion',self.distortion)
    def loadFromFile(self,fn):
        self.focal=fn.getNode('focal').real()
        self.aspect=fn.getNode('aspect').real()
        self.principal[0]=fn.getNode('ppx').real()
        self.principal[1]=fn.getNode('ppy').real()
        self.R=fn.getNode('R').mat()
        self.distortion=fn.getNode('distortion').mat()
    def print(self):
        print('focal:%f'%self.focal)
        print('aspect:%f'%self.aspect)
        print('principal:%f' % self.principal)
        print('R:',self.R,sep='\n')
        print('distortion:', self.distortion,sep='\n')
    def __str__(self):
        return "focal:"+str(self.focal)+"\naspect:"+str(self.aspect)+"\nppx:"+str(self.principal[0])+"\nppy"+str(self.principal[1])+"\nR:"+str(self.R)+"\ndistortion:"+str(self.distortion)
    def plot(self,rad=1.5):
        theta=np.arange(0,rad,0.1)
        r=theta*(1+self.distortion[0]*theta**2+self.distortion[1]*theta**4+self.distortion[2]*theta**6+self.distortion[3]*theta**8)
        theta=theta*(180.0/3.1415926)
        plt.plot(theta,r)
        plt.xlabel("Theta(rad)")
        plt.ylabel("r")
        plt.ylim(ymin=0)
        plt.margins(x=0)
        plt.show()




#=====================================
class CameraGroup():
    def __init__(self):
        self.cameras=[]
    def loadFromFile(self,fileName):
        #A=cv.FileStorage_READ
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

    def __getitem__(self, item):
        return self.cameras[item]

    def __setitem__(self, key, value):
        self.cameras[key]=value

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
