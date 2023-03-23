from PyQt5 import QtCore, QtGui, QtWidgets
from signUpWindow_hr import Ui_signUpWindow_hr
from signUpWindow_emp import Ui_signUpWindow_emp
from loginWindow_hr import Ui_loginWindow_hr
from loginWindow_emp import Ui_loginWindow_emp
class Ui_MainWindow(object):
    def openSignUpWindow_hr(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_signUpWindow_hr()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openLoginWindow_hr(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_loginWindow_hr()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openSignUpWindow_emp(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_signUpWindow_emp()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openLoginWindow_emp(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_loginWindow_emp()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("HR Helping Hand")
        MainWindow.resize(522, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 521, 351))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../images/hr-analysis.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 370, 171, 121))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox,clicked=lambda:self.openLoginWindow_hr())
        self.pushButton.setGeometry(QtCore.QRect(0, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox,clicked=lambda:self.openSignUpWindow_hr())
        self.pushButton_2.setGeometry(QtCore.QRect(0, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 370, 171, 121))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2,clicked=lambda:self.openLoginWindow_emp())
        self.pushButton_3.setGeometry(QtCore.QRect(0, 30, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2,clicked=lambda:self.openSignUpWindow_emp())
        self.pushButton_4.setGeometry(QtCore.QRect(0, 80, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "For HR Manager and Team"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Regesiter"))
        self.groupBox_2.setTitle(_translate("MainWindow", "For Employees and Members"))
        self.pushButton_3.setText(_translate("MainWindow", "Login"))
        self.pushButton_4.setText(_translate("MainWindow", "Regesiter"))

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# why data is split into 70-30
# add theory of models

