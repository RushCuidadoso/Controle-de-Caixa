# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmcaixa.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmcaixa(object):
    def setupUi(self, frmcaixa):
        frmcaixa.setObjectName("frmcaixa")
        frmcaixa.resize(888, 258)
        self.groupBox = QtWidgets.QGroupBox(frmcaixa)
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
        self.txtnomcaixa = QtWidgets.QLineEdit(self.groupBox)
        self.txtnomcaixa.setEnabled(False)
        self.txtnomcaixa.setGeometry(QtCore.QRect(152, 59, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtnomcaixa.setFont(font)
        self.txtnomcaixa.setObjectName("txtnomcaixa")
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
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(18, 101, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtsaldo = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.txtsaldo.setEnabled(False)
        self.txtsaldo.setGeometry(QtCore.QRect(150, 100, 251, 31))
        self.txtsaldo.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.txtsaldo.setMinimum(-99999999999.99)
        self.txtsaldo.setMaximum(99999999999.99)
        self.txtsaldo.setObjectName("txtsaldo")
        self.btneditar.raise_()
        self.btnnovo.raise_()
        self.btnguardar.raise_()
        self.btneliminar.raise_()
        self.txtcod.raise_()
        self.txtnomcaixa.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.btncancelar.raise_()
        self.label_3.raise_()
        self.txtsaldo.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(frmcaixa)
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

        self.retranslateUi(frmcaixa)
        self.tabla.cellClicked['int','int'].connect(self.lblindice.setNum)
        QtCore.QMetaObject.connectSlotsByName(frmcaixa)
        frmcaixa.setTabOrder(self.txtcod, self.txtnomcaixa)
        frmcaixa.setTabOrder(self.txtnomcaixa, self.txtsaldo)
        frmcaixa.setTabOrder(self.txtsaldo, self.btnnovo)
        frmcaixa.setTabOrder(self.btnnovo, self.btnguardar)
        frmcaixa.setTabOrder(self.btnguardar, self.btneditar)
        frmcaixa.setTabOrder(self.btneditar, self.btneliminar)
        frmcaixa.setTabOrder(self.btneliminar, self.btncancelar)
        frmcaixa.setTabOrder(self.btncancelar, self.tabla)

    def retranslateUi(self, frmcaixa):
        _translate = QtCore.QCoreApplication.translate
        frmcaixa.setWindowTitle(_translate("frmcaixa", "Registro de Caixas"))
        self.btnnovo.setText(_translate("frmcaixa", "Nuevo"))
        self.btnguardar.setText(_translate("frmcaixa", "Guardar"))
        self.btneliminar.setText(_translate("frmcaixa", "Eliminar"))
        self.btneditar.setText(_translate("frmcaixa", "Editar"))
        self.label.setText(_translate("frmcaixa", "Codigo:"))
        self.label_2.setText(_translate("frmcaixa", "Nome:"))
        self.btncancelar.setText(_translate("frmcaixa", "Cancelar"))
        self.label_3.setText(_translate("frmcaixa", "Saldo inicial:"))
        self.lblsinreg.setText(_translate("frmcaixa", "Sin Registros"))
        self.lblindice.setText(_translate("frmcaixa", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmcaixa = QtWidgets.QWidget()
    ui = Ui_frmcaixa()
    ui.setupUi(frmcaixa)
    frmcaixa.show()
    sys.exit(app.exec_())
