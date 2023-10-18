
import typing
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget
from game import Game
from PyQt6.QtWidgets import QMessageBox
from style import GameStyle
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

class GameWindow(QMainWindow):    
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./icons/tic_icon.png"))
        self.setWindowTitle("Tic Tac Toe 0.0.1")
        self.btns = [self.btnOne, self.btnTwo,
                     self.btnThree,self.btnFour,
                     self.btnFive,self.btnSix,
                     self.btnSeven, self.btnEight,
                     self.btnNine]
        
        self.media = QMediaPlayer(self)
        self.audio = QAudioOutput(self)
        self.media.setAudioOutput(self.audio)
        self.game_timer = 30
        self.timeBar.setMaximum(self.game_timer)
        self.timeBar.setMinimum(0)
        self.tmr = QtCore.QTimer(self)
        self.gm = Game(self.btns)
        self.cur_gamer = 'x'
        if self.cur_gamer == 'x':
            self.lblLeftGamer.setStyleSheet(GameStyle.active_style())
            self.lblRightGamer.setStyleSheet(GameStyle.disactive_style())
        else:
            self.lblRightGamer.setStyleSheet(GameStyle.active_style())
            self.lblLeftGamer.setStyleSheet(GameStyle.disactive_style())
        self.disable_change()
        self.startBtn.clicked.connect(self.start_slot)
        self.stopBtn.clicked.connect(self.disable_change)
        self.btnOne.clicked.connect(lambda x:self.click_btns(0))
        self.btnTwo.clicked.connect(lambda x:self.click_btns(1))
        self.btnThree.clicked.connect(lambda x:self.click_btns(2))
        self.btnFour.clicked.connect(lambda x:self.click_btns(3))
        self.btnFive.clicked.connect(lambda x:self.click_btns(4))
        self.btnSix.clicked.connect(lambda x:self.click_btns(5))
        self.btnSeven.clicked.connect(lambda x:self.click_btns(6))
        self.btnEight.clicked.connect(lambda x:self.click_btns(7))
        self.btnNine.clicked.connect(lambda x:self.click_btns(8))
        self.tmr.setInterval(1000)
        self.tmr.timeout.connect(self.timout_slot)
        
    def timout_slot(self):
        if self.game_timer == 0:
            self.clear_btns()
            self.disable_change()
            self.cur_gamer = 'x'
            self.game_timer = 150
            self.timeBar.repaint()
            self.timeBar.setMaximum(self.game_timer)
            self.timeBar.setMinimum(0)
            self.timeBar.setValue(self.game_timer)
            if self.media.isAvailable():
                self.media.stop()
            self.media.setSource(QtCore.QUrl.fromLocalFile("./sounds/finish.mp3"))
            self.media.play()
            QMessageBox.information(self, 'Game Over', f'Afsuski o\'yin tugadi')
            self.tmr.stop()
        else:
            self.game_timer -= 1
            self.timeBar.setValue(self.game_timer)
            
    #Maydondagi btnlar
    def click_btns(self, ind:int):
        if self.cur_gamer == 'x':
            if self.media.isAvailable():
                self.media.stop()
            self.media.setSource(QtCore.QUrl.fromLocalFile("./sounds/xsound.mp3"))
            self.media.play()
            self.btns[ind].setText('X')
            self.btns[ind].setEnabled(False)
            self.cur_gamer = 'o'
        else:
            if self.media.isAvailable():
                self.media.stop()
            self.media.setSource(QtCore.QUrl.fromLocalFile("./sounds/osound.mp3"))
            self.media.play()
            self.btns[ind].setText('O')
            self.btns[ind].setEnabled(False)
            self.cur_gamer = 'x'
        ans = self.gm.check_all()
        if self.cur_gamer == 'x':
            self.lblLeftGamer.setStyleSheet(GameStyle.active_style())
            self.lblRightGamer.setStyleSheet(GameStyle.disactive_style())
        else:
            self.lblRightGamer.setStyleSheet(GameStyle.active_style())
            self.lblLeftGamer.setStyleSheet(GameStyle.disactive_style())
        if ans != False:
            if self.media.isAvailable():
                self.media.stop()
            self.media.setSource(QtCore.QUrl.fromLocalFile("./sounds/finish.mp3"))
            self.media.play()
            QMessageBox.information(self, 'Win', f'{ans} siz golib keldingiz')
            self.clear_btns()
            self.disable_change()
            self.cur_gamer = 'x'
            self.game_timer = 30
            
    def clear_btns(self):
        for btn in self.btns:
            btn.setText('')        
        
    def disable_change(self):
        for btn in self.btns:
            btn.setEnabled(False)
    
    def start_slot(self):
        if self.cur_gamer == 'x':
            self.lblLeftGamer.setStyleSheet(GameStyle.active_style())
            self.lblRightGamer.setStyleSheet(GameStyle.disactive_style())
        else:
            self.lblRightGamer.setStyleSheet(GameStyle.active_style())
            self.lblLeftGamer.setStyleSheet(GameStyle.disactive_style())
        for btn in self.btns:
            btn.setEnabled(True)
        self.timeBar.setValue(self.game_timer)
        self.tmr.start()     
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 507)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblLeftGamer = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblLeftGamer.setMinimumSize(QtCore.QSize(60, 200))
        self.lblLeftGamer.setMaximumSize(QtCore.QSize(80, 800))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lblLeftGamer.setFont(font)
        self.lblLeftGamer.setObjectName("lblLeftGamer")
        self.horizontalLayout_5.addWidget(self.lblLeftGamer)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOne = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOne.sizePolicy().hasHeightForWidth())
        self.btnOne.setSizePolicy(sizePolicy)
        self.btnOne.setMinimumSize(QtCore.QSize(80, 80))
        self.btnOne.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.btnOne.setFont(font)
        self.btnOne.setText("")
        self.btnOne.setObjectName("btnOne")
        self.horizontalLayout.addWidget(self.btnOne)
        self.btnTwo = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTwo.sizePolicy().hasHeightForWidth())
        self.btnTwo.setSizePolicy(sizePolicy)
        self.btnTwo.setMinimumSize(QtCore.QSize(80, 80))
        self.btnTwo.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.btnTwo.setFont(font)
        self.btnTwo.setText("")
        self.btnTwo.setObjectName("btnTwo")
        self.horizontalLayout.addWidget(self.btnTwo)
        self.btnThree = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnThree.sizePolicy().hasHeightForWidth())
        self.btnThree.setSizePolicy(sizePolicy)
        self.btnThree.setMinimumSize(QtCore.QSize(80, 80))
        self.btnThree.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.btnThree.setFont(font)
        self.btnThree.setText("")
        self.btnThree.setObjectName("btnThree")
        self.horizontalLayout.addWidget(self.btnThree)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnFour = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFour.sizePolicy().hasHeightForWidth())
        self.btnFour.setSizePolicy(sizePolicy)
        self.btnFour.setMinimumSize(QtCore.QSize(80, 80))
        self.btnFour.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.btnFour.setFont(font)
        self.btnFour.setText("")
        self.btnFour.setObjectName("btnFour")
        self.horizontalLayout_2.addWidget(self.btnFour)
        self.btnFive = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFive.sizePolicy().hasHeightForWidth())
        self.btnFive.setSizePolicy(sizePolicy)
        self.btnFive.setMinimumSize(QtCore.QSize(80, 80))
        self.btnFive.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.btnFive.setFont(font)
        self.btnFive.setText("")
        self.btnFive.setObjectName("btnFive")
        self.horizontalLayout_2.addWidget(self.btnFive)
        self.btnSix = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSix.sizePolicy().hasHeightForWidth())
        self.btnSix.setSizePolicy(sizePolicy)
        self.btnSix.setMinimumSize(QtCore.QSize(80, 80))
        self.btnSix.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.btnSix.setFont(font)
        self.btnSix.setText("")
        self.btnSix.setObjectName("btnSix")
        self.horizontalLayout_2.addWidget(self.btnSix)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnSeven = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSeven.sizePolicy().hasHeightForWidth())
        self.btnSeven.setSizePolicy(sizePolicy)
        self.btnSeven.setMinimumSize(QtCore.QSize(80, 80))
        self.btnSeven.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.btnSeven.setFont(font)
        self.btnSeven.setText("")
        self.btnSeven.setObjectName("btnSeven")
        self.horizontalLayout_3.addWidget(self.btnSeven)
        self.btnEight = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEight.sizePolicy().hasHeightForWidth())
        self.btnEight.setSizePolicy(sizePolicy)
        self.btnEight.setMinimumSize(QtCore.QSize(80, 80))
        self.btnEight.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.btnEight.setFont(font)
        self.btnEight.setText("")
        self.btnEight.setObjectName("btnEight")
        self.horizontalLayout_3.addWidget(self.btnEight)
        self.btnNine = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNine.sizePolicy().hasHeightForWidth())
        self.btnNine.setSizePolicy(sizePolicy)
        self.btnNine.setMinimumSize(QtCore.QSize(80, 80))
        self.btnNine.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.btnNine.setFont(font)
        self.btnNine.setText("")
        self.btnNine.setObjectName("btnNine")
        self.horizontalLayout_3.addWidget(self.btnNine)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.lblRightGamer = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblRightGamer.setMinimumSize(QtCore.QSize(60, 200))
        self.lblRightGamer.setMaximumSize(QtCore.QSize(80, 800))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lblRightGamer.setFont(font)
        self.lblRightGamer.setObjectName("lblRightGamer")
        self.horizontalLayout_5.addWidget(self.lblRightGamer)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.startBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startBtn.setMinimumSize(QtCore.QSize(120, 50))
        self.startBtn.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.startBtn.setFont(font)
        self.startBtn.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(85, 85, 255);\n"
"    color: rgb(255, 255, 255);\n"
"  border:2px solid rgb(0, 0, 0);\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 255);\n"
"  border:2px solid rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"}\n"
"")
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_4.addWidget(self.startBtn)
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.stopBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stopBtn.setMinimumSize(QtCore.QSize(120, 50))
        self.stopBtn.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.stopBtn.setFont(font)
        self.stopBtn.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(85, 85, 255);\n"
"    color: rgb(255, 255, 255);\n"
"  border:2px solid rgb(0, 0, 0);\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 255);\n"
"  border:2px solid rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"}\n"
"")
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout_4.addWidget(self.stopBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.timeBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.timeBar.setProperty("value", 24)
        self.timeBar.setObjectName("timeBar")
        self.verticalLayout_2.addWidget(self.timeBar)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(parent=self.menubar)
        self.menuGame.setObjectName("menuGame")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLow = QtGui.QAction(parent=MainWindow)
        self.actionLow.setObjectName("actionLow")
        self.actionMeduim = QtGui.QAction(parent=MainWindow)
        self.actionMeduim.setObjectName("actionMeduim")
        self.actionHigh = QtGui.QAction(parent=MainWindow)
        self.actionHigh.setObjectName("actionHigh")
        self.actionE_xit = QtGui.QAction(parent=MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.actionAbout_us = QtGui.QAction(parent=MainWindow)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.menuGame.addAction(self.actionLow)
        self.menuGame.addAction(self.actionMeduim)
        self.menuGame.addAction(self.actionHigh)
        self.menuGame.addAction(self.actionE_xit)
        self.menuAbout.addAction(self.actionAbout_us)
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblLeftGamer.setText(_translate("MainWindow", "X"))
        self.lblRightGamer.setText(_translate("MainWindow", "O"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.menuGame.setTitle(_translate("MainWindow", "Game"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionLow.setText(_translate("MainWindow", "Low"))
        self.actionMeduim.setText(_translate("MainWindow", "Meduim"))
        self.actionHigh.setText(_translate("MainWindow", "High"))
        self.actionE_xit.setText(_translate("MainWindow", "E&xit"))
        self.actionAbout_us.setText(_translate("MainWindow", "About us"))

