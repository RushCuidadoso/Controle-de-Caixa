# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmparametros.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmparametros(object):
    def setupUi(self, frmparametros):
        frmparametros.setObjectName("frmparametros")
        frmparametros.resize(742, 147)
        self.groupBox = QtWidgets.QGroupBox(frmparametros)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 721, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btnconta = QtWidgets.QPushButton(self.groupBox)
        self.btnconta.setGeometry(QtCore.QRect(500, 20, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnconta.setFont(font)
        self.btnconta.setObjectName("btnconta")
        self.btnbanco = QtWidgets.QPushButton(self.groupBox)
        self.btnbanco.setGeometry(QtCore.QRect(20, 20, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnbanco.setFont(font)
        self.btnbanco.setObjectName("btnbanco")
        self.btnfornecedor = QtWidgets.QPushButton(self.groupBox)
        self.btnfornecedor.setGeometry(QtCore.QRect(260, 20, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnfornecedor.setFont(font)
        self.btnfornecedor.setObjectName("btnfornecedor")

        self.retranslateUi(frmparametros)
        QtCore.QMetaObject.connectSlotsByName(frmparametros)
        frmparametros.setTabOrder(self.btnbanco, self.btnconta)

    def retranslateUi(self, frmparametros):
        _translate = QtCore.QCoreApplication.translate
        frmparametros.setWindowTitle(_translate("frmparametros", "Seleccionar um parametro"))
        self.groupBox.setTitle(_translate("frmparametros", "Contas"))
        self.btnconta.setText(_translate("frmparametros", "Abrir Contas"))
        self.btnbanco.setText(_translate("frmparametros", "Abrir Bancos"))
        self.btnfornecedor.setText(_translate("frmparametros", "Abrir Fornecedores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmparametros = QtWidgets.QWidget()
    ui = Ui_frmparametros()
    ui.setupUi(frmparametros)
    frmparametros.show()
    sys.exit(app.exec_())
