from PyQt5 import QtCore, QtGui, QtWidgets
import string

from PyQt5.QtWidgets import QTableWidgetItem


class Ui_outputWindow(object):
    def setupUi(self, outputWindow, roots, numberOfEquations, methodIndex):
        outputWindow.setObjectName("MainWindow")
        outputWindow.resize(557, 437)
        self.centralwidget = QtWidgets.QWidget(outputWindow)

        # Font Setting
        font = QtGui.QFont()
        font.setPointSize(10)

        # TableWidget Initialization
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 557, 221))
        # Set Rows & Columns numbers
        self.tableWidget.setColumnCount(numberOfEquations)
        if methodIndex == 4:
            self.tableWidget.setRowCount(4)
        else:
            self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)

        # Label Initialization
        self.methodLabel = QtWidgets.QLabel(self.centralwidget)
        self.methodLabel.setGeometry(QtCore.QRect(130, 30, 271, 31))
        self.methodLabel.setFont(font)
        self.methodLabel.setAlignment(QtCore.Qt.AlignCenter)

        outputWindow.setCentralWidget(self.centralwidget)

        # Insert Data into the Table
        self.setData(roots, methodIndex)

        self.retranslateUi(outputWindow)
        QtCore.QMetaObject.connectSlotsByName(outputWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("outputWindow", "outputWindow"))

    def setData(self, data, index):
        header = string.ascii_lowercase
        header2 = []
        if index == 0:
            method = "Gaussian-elimination"
        elif index == 1:
            method = "LU decomposition"
        elif index == 2:
            method = "Gaussian-jordan"
        elif index == 3:
            method = "Gauss-seidel"
        else:
            method = "All Methods"
        self.methodLabel.setText(method)
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                newItem = QTableWidgetItem(str(round(data[i][j], 9)))
                self.tableWidget.setItem(i, j, newItem)
                if index != 4:
                    header2.append(header[j])
            header2.append(header[i])
        if index == 4:
            self.tableWidget.setVerticalHeaderLabels(["Gaussian-elimination", "LU decomposition", "Gaussian-jordan", "Gauss-seidel"])
        else:
            self.tableWidget.setVerticalHeaderLabels([method])
        self.tableWidget.setHorizontalHeaderLabels(header2)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


