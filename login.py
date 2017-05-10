# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created: Sat Apr 22 10:59:07 2017
#      by: Paul Cyryl
#

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(803, 499)
        Login.setStyleSheet(_fromUtf8("QDialog{background-color: rgb(0, 170, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(0, 85, 255, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"}\n"
"\n"
""))
        self.topLabel = QtGui.QLabel(Login)
        self.topLabel.setGeometry(QtCore.QRect(210, 110, 351, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic Medium"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.topLabel.setFont(font)
        self.topLabel.setTextFormat(QtCore.Qt.LogText)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.Name = QtGui.QLabel(Login)
        self.Name.setGeometry(QtCore.QRect(220, 190, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Franklin Gothic Demi Cond"))
        font.setPointSize(11)
        font.setItalic(True)
        self.Name.setFont(font)
        self.Name.setObjectName(_fromUtf8("Name"))
        self.Password = QtGui.QLabel(Login)
        self.Password.setGeometry(QtCore.QRect(220, 250, 91, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Franklin Gothic Demi Cond"))
        font.setPointSize(11)
        font.setItalic(True)
        self.Password.setFont(font)
        self.Password.setObjectName(_fromUtf8("Password"))
        self.PasswordEntry = QtGui.QLineEdit(Login)
        self.PasswordEntry.setGeometry(QtCore.QRect(330, 250, 211, 20))
        self.PasswordEntry.setObjectName(_fromUtf8("PasswordEntry"))
        self.NameEntry = QtGui.QLineEdit(Login)
        self.NameEntry.setGeometry(QtCore.QRect(330, 190, 211, 21))
        self.NameEntry.setObjectName(_fromUtf8("NameEntry"))
        self.LoginButton = QtGui.QPushButton(Login)
        self.LoginButton.setGeometry(QtCore.QRect(370, 300, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rage Italic"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LoginButton.setFont(font)
        self.LoginButton.setObjectName(_fromUtf8("LoginButton"))
        self.pushButton = QtGui.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(350, 350, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rage Italic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Login Page", None))
        self.topLabel.setText(_translate("Login", "Egerton University Mortuary Management System", None))
        self.Name.setText(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Demi Cond\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Staff Number</p></body></html>", None))
        self.Password.setText(_translate("Login", "Password", None))
        self.LoginButton.setText(_translate("Login", "Login", None))
        self.pushButton.setText(_translate("Login", "Forgot Password", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Login = QtGui.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

