
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog
from PySide2.QtCore import Slot,QSize
from PySide2.QtGui import QImage,QPixmap,QStandardItemModel,QStandardItem,QIcon

from mainwindow import Ui_MainWindow
import sys
import os.path

import cv2 as cv
import CharucoBoard
import CameraGroup


dicts=['DICT_4X4_50','DICT_4X4_100','DICT_4X4_250','DICT_4X4_1000','DICT_5X5_50','DICT_5X5_100','DICT_5X5_250','DICT_5X5_1000','DICT_6X6_50','DICT_6X6_100','DICT_6X6_250'
,'DICT_6X6_1000','DICT_7X7_50','DICT_7X7_100','DICT_7X7_250','DICT_7X7_1000','DICT_ARUCO_ORIGINAL','DICT_APRILTAG_16h5','DICT_APRILTAG_25h9','DICT_APRILTAG_36h10','DICT_APRILTAG_36h11']

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_dict.addItems(dicts)
        #signal
        self.ui.pushButton_create.clicked.connect(self.createBoard)
        self.ui.pushButton_save.clicked.connect(self.saveBoard)
        self.ui.pushButton_open.clicked.connect(self.OpenImages)
        self.ui.tableView.clicked.connect(self.showImg)             #列表图片显示
        self.ui.pushButton_calib.clicked.connect(self.calib)
        self.ui.pushButton_saveParameter.clicked.connect(self.saveParameter)
        self.ui.pushButton_output.clicked.connect(self.saveCameraGroup)
        self.ui.pushButton_clear.clicked.connect(self.clearGroup)
        #property
        self.model = QStandardItemModel()
        self.caliber=None
        self.cameraGroup = CameraGroup.CameraGroup()

        #other
        self.calibBoard=CharucoBoard.ChessBoard()






    @Slot()     #CreateBoard
    def createBoard(self):
        self.calibBoard = CharucoBoard.CharucoBoard()
        numX=int(self.ui.lineEdit_numX.text())
        numY=int(self.ui.lineEdit_numY.text())
        dict=self.ui.comboBox_dict.currentIndex()
        squareSize=float(self.ui.lineEdit_squareSize.text())
        imgSize=(float(self.ui.lineEdit_printX.text()),float(self.ui.lineEdit_printY.text()))
        dpi=int(self.ui.lineEdit_DPI.text())
        self.board = self.calibBoard.create(numX,numY,dict,squareSize,imgSize,dpi)   #Create Board
        if self.board is None:                                                    ## splite Qt segment
            self.ui.label.setText("Create Failed,Please confire parameter!")
        image = QImage(self.board[:], self.board.shape[1], self.board.shape[0], self.board.shape[1], QImage.Format_Grayscale8)
        showBoard=QPixmap(image)
        if showBoard.width()>showBoard.height():
            showBoard=showBoard.scaledToWidth(self.ui.label.width())
        else:
            showBoard=showBoard.scaledToHeight(self.ui.label.height())
        self.ui.label.setPixmap(showBoard)
        #cv.imshow("2",self.board)


    @Slot()  #SaveBoard
    def saveBoard(self):
        name=QFileDialog.getSaveFileName(self,'Save Board','../',"Image(*.jpg *.png)")
        cv.imwrite(name[0],self.board)
        self.calibBoard.saveConfig(os.path.dirname(name[0]))

    @Slot()              #cereat Images data model
    def OpenImages(self):
        self.cacheDir=''
        fileList=QFileDialog.getOpenFileNames(self,"Load Files",'../')
        self.model=QStandardItemModel()
        for name in fileList[0]:
            item = QStandardItem(os.path.basename(name)) #QIcon(name),
            item.setData(name)
            item2=QStandardItem('NULL')
            self.model.appendRow([item,item2])
        self.ui.tableView.setModel(self.model)

    @Slot()
    def showImg(self,index):
        if self.cacheDir=='':
            return
        currentImg=QPixmap(self.cacheDir+'/marked_'+self.model.item(index.row(),0).text())
        if currentImg.width()>currentImg.height():
            currentImg=currentImg.scaledToWidth(self.ui.label_show.width())
        else:
            currentImg=currentImg.scaledToHeight(self.ui.label_show.height())
        self.ui.label_show.setPixmap(currentImg)

    @Slot()
    def calib(self):                                         #Calib
        n=self.model.rowCount()
        if n==0:return
        # strictDetection=2 if self.ui.checkBox_strick.isChecked() else 1
        self.caliber=CharucoBoard.Calib(self.ui.comboBox_detectType.currentIndex(),self.ui.checkBox_isFish.isChecked(),self.calibBoard)
        path = self.model.item(0, 0).data()                   #directionary related
        self.cacheDir=os.path.dirname(path)+'/DetectCache'
        if not os.path.exists(self.cacheDir):
            os.mkdir(self.cacheDir)
        validIndex=[]

        for i in range(n):                                  #detect
            print(path)
            path=self.model.item(i,0).data()
            img=cv.imread(path)
            markedImg=self.caliber.detectCorners(img)
            if markedImg is None: markedImg=img
            else: validIndex.append(i)
            cv.imwrite(self.cacheDir+'/marked_'+self.model.item(i,0).text(),markedImg)

        rerro=self.caliber.calibCamera(img.shape[1::-1])   #calib
        self.ui.statusbar.showMessage("重投影误差(平方根):"+str(rerro))

        for i in range(len(validIndex)):                   #each image reproject erro
            erro=self.caliber.calcProjectErro(i)
            self.model.item(validIndex[i],1).setText(str(erro))
    @Slot()
    def saveParameter(self):
        self.cameraGroup.cameras.append(self.caliber.getCameraParameter())
        self.ui.pushButton_saveParameter.setText('save('+str(len(self.cameraGroup.cameras))+')')

    @Slot()
    def saveCameraGroup(self):
        name=QFileDialog.getSaveFileName(self,'Save Board','../',"Image (*.yml)")
        self.cameraGroup.saveToFile(name[0])
    @Slot()
    def clearGroup(self):
        self.cameraGroup.cameras=[]
        self.ui.pushButton_saveParameter.setText('save(0)')








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())