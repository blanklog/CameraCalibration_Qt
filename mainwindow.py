# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget{background-color: rgb(228, 228, 225);}")
        self.tab_calib = QWidget()
        self.tab_calib.setObjectName(u"tab_calib")
        self.verticalLayout = QVBoxLayout(self.tab_calib)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_open = QPushButton(self.tab_calib)
        self.pushButton_open.setObjectName(u"pushButton_open")

        self.horizontalLayout_4.addWidget(self.pushButton_open)

        self.pushButton_calib = QPushButton(self.tab_calib)
        self.pushButton_calib.setObjectName(u"pushButton_calib")

        self.horizontalLayout_4.addWidget(self.pushButton_calib)

        self.comboBox_detectType = QComboBox(self.tab_calib)
        self.comboBox_detectType.addItem("")
        self.comboBox_detectType.addItem("")
        self.comboBox_detectType.addItem("")
        self.comboBox_detectType.setObjectName(u"comboBox_detectType")

        self.horizontalLayout_4.addWidget(self.comboBox_detectType)

        self.checkBox_isFish = QCheckBox(self.tab_calib)
        self.checkBox_isFish.setObjectName(u"checkBox_isFish")
        self.checkBox_isFish.setChecked(True)

        self.horizontalLayout_4.addWidget(self.checkBox_isFish)

        self.pushButton_saveParameter = QPushButton(self.tab_calib)
        self.pushButton_saveParameter.setObjectName(u"pushButton_saveParameter")

        self.horizontalLayout_4.addWidget(self.pushButton_saveParameter)

        self.pushButton_clear = QPushButton(self.tab_calib)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout_4.addWidget(self.pushButton_clear)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.tableView = QTableView(self.tab_calib)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setIconSize(QSize(60, 60))
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.horizontalHeader().setMinimumSectionSize(100)
        self.tableView.horizontalHeader().setDefaultSectionSize(140)
        self.tableView.verticalHeader().setDefaultSectionSize(40)

        self.horizontalLayout_3.addWidget(self.tableView)

        self.label_show = QLabel(self.tab_calib)
        self.label_show.setObjectName(u"label_show")
        self.label_show.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_show)

        self.horizontalLayout_3.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.pushButton_output = QPushButton(self.tab_calib)
        self.pushButton_output.setObjectName(u"pushButton_output")

        self.horizontalLayout_5.addWidget(self.pushButton_output)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_calib, "")
        self.tab_Create = QWidget()
        self.tab_Create.setObjectName(u"tab_Create")
        self.verticalLayout_2 = QVBoxLayout(self.tab_Create)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.tab_Create)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_7 = QLabel(self.tab_Create)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)

        self.label_3 = QLabel(self.tab_Create)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.lineEdit_numX = QLineEdit(self.tab_Create)
        self.lineEdit_numX.setObjectName(u"lineEdit_numX")

        self.gridLayout.addWidget(self.lineEdit_numX, 0, 1, 1, 1)

        self.comboBox_dict = QComboBox(self.tab_Create)
        self.comboBox_dict.setObjectName(u"comboBox_dict")

        self.gridLayout.addWidget(self.comboBox_dict, 0, 9, 1, 1)

        self.label_6 = QLabel(self.tab_Create)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineEdit_numY = QLineEdit(self.tab_Create)
        self.lineEdit_numY.setObjectName(u"lineEdit_numY")

        self.gridLayout.addWidget(self.lineEdit_numY, 1, 1, 1, 1)

        self.label_5 = QLabel(self.tab_Create)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 8, 1, 1)

        self.lineEdit_printY = QLineEdit(self.tab_Create)
        self.lineEdit_printY.setObjectName(u"lineEdit_printY")

        self.gridLayout.addWidget(self.lineEdit_printY, 1, 5, 1, 1)

        self.label_4 = QLabel(self.tab_Create)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.lineEdit_printX = QLineEdit(self.tab_Create)
        self.lineEdit_printX.setObjectName(u"lineEdit_printX")

        self.gridLayout.addWidget(self.lineEdit_printX, 0, 5, 1, 1)

        self.lineEdit_squareSize = QLineEdit(self.tab_Create)
        self.lineEdit_squareSize.setObjectName(u"lineEdit_squareSize")

        self.gridLayout.addWidget(self.lineEdit_squareSize, 0, 3, 1, 1)

        self.label_8 = QLabel(self.tab_Create)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)

        self.lineEdit_DPI = QLineEdit(self.tab_Create)
        self.lineEdit_DPI.setObjectName(u"lineEdit_DPI")

        self.gridLayout.addWidget(self.lineEdit_DPI, 1, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_create = QPushButton(self.tab_Create)
        self.pushButton_create.setObjectName(u"pushButton_create")

        self.horizontalLayout.addWidget(self.pushButton_create)

        self.pushButton_save = QPushButton(self.tab_Create)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout.addWidget(self.pushButton_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label = QLabel(self.tab_Create)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QTabWidget::tab{background-color: rgb(238, 238, 0);}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout_2.setStretch(2, 12)
        self.tabWidget.addTab(self.tab_Create, "")
        self.tab_camera = QWidget()
        self.tab_camera.setObjectName(u"tab_camera")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_camera)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.listView_Camera = QListView(self.tab_camera)
        self.listView_Camera.setObjectName(u"listView_Camera")

        self.horizontalLayout_6.addWidget(self.listView_Camera)

        self.label_showCamera = QLabel(self.tab_camera)
        self.label_showCamera.setObjectName(u"label_showCamera")

        self.horizontalLayout_6.addWidget(self.label_showCamera)

        self.horizontalLayout_6.setStretch(1, 2)
        self.tabWidget.addTab(self.tab_camera, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushButton_calib.setText(QCoreApplication.translate("MainWindow", u"Calib", None))
        self.comboBox_detectType.setItemText(0, QCoreApplication.translate("MainWindow", u"chessBoard", None))
        self.comboBox_detectType.setItemText(1, QCoreApplication.translate("MainWindow", u"chArUco", None))
        self.comboBox_detectType.setItemText(2, QCoreApplication.translate("MainWindow", u"chArUco+", None))

        self.checkBox_isFish.setText(QCoreApplication.translate("MainWindow", u"fishEyeLens", None))
        self.pushButton_saveParameter.setText(QCoreApplication.translate("MainWindow", u"save(0)", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_show.setText("")
        self.pushButton_output.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_calib), QCoreApplication.translate("MainWindow", u"Calib", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"number_X:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"print_height(cm):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"print_width(cm):", None))
        self.lineEdit_numX.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"number_Y:", None))
        self.lineEdit_numY.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dict:", None))
        self.lineEdit_printY.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"squareSize(cm):", None))
        self.lineEdit_printX.setText(QCoreApplication.translate("MainWindow", u"29.7", None))
        self.lineEdit_squareSize.setText(QCoreApplication.translate("MainWindow", u"2.5", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"DPI:", None))
        self.lineEdit_DPI.setText(QCoreApplication.translate("MainWindow", u"96", None))
        self.pushButton_create.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Create), QCoreApplication.translate("MainWindow", u"CreateChess", None))
        self.label_showCamera.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_camera), QCoreApplication.translate("MainWindow", u"Camera", None))
    # retranslateUi

