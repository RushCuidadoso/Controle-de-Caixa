# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmconta.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmconta(object):
    def setupUi(self, frmconta):
        frmconta.setObjectName("frmconta")
        frmconta.resize(888, 259)
        self.groupBox = QtWidgets.QGroupBox(frmconta)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 411, 241))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btnnovo = QtWidgets.QPushButton(self.groupBox)
        self.btnnovo.setGeometry(QtCore.QRect(10, 200, 91, 23))
        self.btnnovo.setObjectName("btnnovo")
        self.btnguardar = QtWidgets.QPushButton(self.groupBox)
        self.btnguardar.setGeometry(QtCore.QRect(110, 200, 91, 23))
        self.btnguardar.setObjectName("btnguardar")
        self.btneliminar = QtWidgets.QPushButton(self.groupBox)
        self.btneliminar.setGeometry(QtCore.QRect(210, 200, 91, 23))
        self.btneliminar.setObjectName("btneliminar")
        self.btneditar = QtWidgets.QPushButton(self.groupBox)
        self.btneditar.setGeometry(QtCore.QRect(110, 200, 91, 23))
        self.btneditar.setObjectName("btneditar")
        self.txtcod = QtWidgets.QLineEdit(self.groupBox)
        self.txtcod.setEnabled(False)
        self.txtcod.setGeometry(QtCore.QRect(270, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtcod.setFont(font)
        self.txtcod.setObjectName("txtcod")
        self.txtnomconta = QtWidgets.QLineEdit(self.groupBox)
        self.txtnomconta.setEnabled(False)
        self.txtnomconta.setGeometry(QtCore.QRect(92, 59, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtnomconta.setFont(font)
        self.txtnomconta.setObjectName("txtnomconta")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 46, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btncancelar = QtWidgets.QPushButton(self.groupBox)
        self.btncancelar.setGeometry(QtCore.QRect(310, 200, 91, 23))
        self.btncancelar.setObjectName("btncancelar")
        self.cbobanco = QtWidgets.QComboBox(self.groupBox)
        self.cbobanco.setGeometry(QtCore.QRect(180, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbobanco.setFont(font)
        self.cbobanco.setObjectName("cbobanco")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 103, 46, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtcodbanco = QtWidgets.QLineEdit(self.groupBox)
        self.txtcodbanco.setEnabled(False)
        self.txtcodbanco.setGeometry(QtCore.QRect(140, 100, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtcodbanco.setFont(font)
        self.txtcodbanco.setObjectName("txtcodbanco")
        self.btneditar.raise_()
        self.btnnovo.raise_()
        self.btnguardar.raise_()
        self.btneliminar.raise_()
        self.txtcod.raise_()
        self.txtnomconta.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.btncancelar.raise_()
        self.cbobanco.raise_()
        self.label_3.raise_()
        self.txtcodbanco.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(frmconta)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 10, 451, 241))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tabla = QtWidgets.QTableWidget(self.groupBox_2)
        self.tabla.setGeometry(QtCore.QRect(10, 10, 431, 221))
        self.tabla.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.tabla.verticalHeader().setVisible(False)
        self.lblsinreg = QtWidgets.QLabel(self.groupBox_2)
        self.lblsinreg.setGeometry(QtCore.QRect(190, 110, 91, 16))
        self.lblsinreg.setObjectName("lblsinreg")
        self.lblindice = QtWidgets.QLabel(self.groupBox_2)
        self.lblindice.setGeometry(QtCore.QRect(290, 10, 46, 13))
        self.lblindice.setObjectName("lblindice")

        self.retranslateUi(frmconta)
        self.tabla.cellClicked['int','int'].connect(self.lblindice.setNum)
        QtCore.QMetaObject.connectSlotsByName(frmconta)
        frmconta.setTabOrder(self.btnnovo, self.txtnomconta)
        frmconta.setTabOrder(self.txtnomconta, self.cbobanco)
        frmconta.setTabOrder(self.cbobanco, self.btnguardar)
        frmconta.setTabOrder(self.btnguardar, self.btneditar)
        frmconta.setTabOrder(self.btneditar, self.btneliminar)
        frmconta.setTabOrder(self.btneliminar, self.btncancelar)
        frmconta.setTabOrder(self.btncancelar, self.txtcod)
        frmconta.setTabOrder(self.txtcod, self.tabla)
        frmconta.setTabOrder(self.tabla, self.txtcodbanco)

    def retranslateUi(self, frmconta):
        _translate = QtCore.QCoreApplication.translate
        frmconta.setWindowTitle(_translate("frmconta", "Registro de Contas"))
        self.btnnovo.setText(_translate("frmconta", "Nuevo"))
        self.btnguardar.setText(_translate("frmconta", "Guardar"))
        self.btneliminar.setText(_translate("frmconta", "Eliminar"))
        self.btneditar.setText(_translate("frmconta", "Editar"))
        self.label.setText(_translate("frmconta", "Codigo"))
        self.label_2.setText(_translate("frmconta", "Nome"))
        self.btncancelar.setText(_translate("frmconta", "Cancelar"))
        self.label_3.setText(_translate("frmconta", "Banco"))
        self.lblsinreg.setText(_translate("frmconta", "Sin Registros"))
        self.lblindice.setText(_translate("frmconta", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmconta = QtWidgets.QWidget()
    ui = Ui_frmconta()
    ui.setupUi(frmconta)
    frmconta.show()
    sys.exit(app.exec_())