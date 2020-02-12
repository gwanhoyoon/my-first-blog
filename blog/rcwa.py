# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
import re
import time
import scipy.linalg as splinalg
import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class AddRow(QDialog):                  # Dialog window widget for 'Add row x N'
    def __init__(self):
        super().__init__()
        self.setFont(QFont('Consolas',11))
        self.setupUI()
        self.num = 0

    def setupUI(self):
        self.setGeometry(700, 400, 200, 100)
        self.setWindowTitle('Add Row')
        label1 = QLabel('Number: ')
        self.lineEdit1 = QLineEdit()
        self.pushButton1= QPushButton('Add')
        self.pushButton1.clicked.connect(self.pushButtonClicked)
        layout = QVBoxLayout()
        layout_up = QHBoxLayout()
        layout_up.addWidget(label1)
        layout_up.addWidget(self.lineEdit1)
        layout.addLayout(layout_up)
        layout.addWidget(self.pushButton1)
        self.setLayout(layout)

    def pushButtonClicked(self):
        self.num = self.lineEdit1.text()
        self.close()

class RemRow(QDialog):                  # Dialog window widget for 'Remove row x N'
    def __init__(self):
        super().__init__()
        self.setFont(QFont('Consolas',11))
        self.setupUI()
        self.num = 0

    def setupUI(self):
        self.setGeometry(700, 400, 200, 100)
        self.setWindowTitle('Remove Row')
        label1 = QLabel('Number: ')
        self.lineEdit1 = QLineEdit()
        self.pushButton1= QPushButton('Remove')
        self.pushButton1.clicked.connect(self.pushButtonClicked)
        layout = QVBoxLayout()
        layout_up = QHBoxLayout()
        layout_up.addWidget(label1)
        layout_up.addWidget(self.lineEdit1)
        layout.addLayout(layout_up)
        layout.addWidget(self.pushButton1)
        self.setLayout(layout)

    def pushButtonClicked(self):
        self.num = self.lineEdit1.text()
        self.close()

class Exit_confirm(QDialog):                  # Exit confirmation
    def __init__(self):
        super().__init__()
        self.setFont(QFont('Consolas',11))
        self.setupUI()
        self.ans = None
    def setupUI(self):
        self.setGeometry(700, 400, 200, 100)
        self.setWindowTitle('Exit')
        label1 = QLabel('Are you sure?')
        self.pushButton1= QPushButton('Yes')
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2= QPushButton('No')
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout_down = QHBoxLayout()
        layout_down.addWidget(self.pushButton1)
        layout_down.addWidget(self.pushButton2)
        layout.addLayout(layout_down)
        self.setLayout(layout)
    def pushButton1Clicked(self):
        self.ans = True
        self.close()
    def pushButton2Clicked(self):
        self.ans = False
        self.close()
        
class Reset_confirm(QDialog):                  # Reset confirmation
    def __init__(self):
        super().__init__()
        self.setFont(QFont('Consolas',11))
        self.setupUI()
        self.ans = None
    def setupUI(self):
        self.setGeometry(700, 400, 200, 100)
        self.setWindowTitle('Reset')
        label1 = QLabel('Are you sure?')
        self.pushButton1= QPushButton('Yes')
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2= QPushButton('No')
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout_down = QHBoxLayout()
        layout_down.addWidget(self.pushButton1)
        layout_down.addWidget(self.pushButton2)
        layout.addLayout(layout_down)
        self.setLayout(layout)
    def pushButton1Clicked(self):
        self.ans = True
        self.close()
    def pushButton2Clicked(self):
        self.ans = False
        self.close()

class Coordinate(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        self.setWindowTitle('Coordinate Information')
        img = QLabel()
        pixmap = QPixmap('images\\Coordinate.png')
        img.setPixmap(pixmap)
        img.resize(pixmap.width()/2,pixmap.height()/2)
        layout = QVBoxLayout()
        layout.addWidget(img)
        self.setLayout(layout)

class MyRCWA(QWidget):                  # Object to generate table
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.result_op1 = False
        self.result_op2 = False
        
        self.setFont(QFont('Consolas'))
        self.table = self.makeTable()
        self.table2 = self.makeTable()
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setVerticalHeaderLabels(['Values'])
        self.table.verticalHeaderItem(0).setTextAlignment(Qt.AlignCenter)
        
        grp_schedule = QGroupBox(' Schedule ')
        lay_schedule = QHBoxLayout()
        lay_schedule.addWidget(self.table)
        grp_schedule.setLayout(lay_schedule)
        
        self.fig1 = plt.Figure()
        self.canvas1 = FigureCanvas(self.fig1)
        self.fig2 = plt.Figure()
        self.canvas2 = FigureCanvas(self.fig2)
        self.fig3 = plt.Figure()
        self.canvas3 = FigureCanvas(self.fig3)
        self.fig4 = plt.Figure()
        self.canvas4 = FigureCanvas(self.fig4)
        self.fig5 = plt.Figure()
        self.canvas5 = FigureCanvas(self.fig5)
        self.fig6 = plt.Figure()
        self.canvas6 = FigureCanvas(self.fig6)
        self.fig7 = plt.Figure()
        self.canvas7 = FigureCanvas(self.fig7)
        self.fig8 = plt.Figure()
        self.canvas8 = FigureCanvas(self.fig8)
        self.fig9 = plt.Figure()
        self.canvas9 = FigureCanvas(self.fig9)
        self.fig10 = plt.Figure()
        self.canvas10 = FigureCanvas(self.fig10)
        self.fig11 = plt.Figure()
        self.canvas11 = FigureCanvas(self.fig11)
        self.fig12 = plt.Figure()
        self.canvas12 = FigureCanvas(self.fig12)
        
        grp_field = QGroupBox(' Field Visualization ')
        grid2 = QGridLayout()
        grid2.addWidget(self.canvas1,0,0)
        grid2.addWidget(self.canvas2,1,0)
        grid2.addWidget(self.canvas3,2,0)
        grid2.addWidget(self.canvas4,0,1)
        grid2.addWidget(self.canvas5,1,1)
        grid2.addWidget(self.canvas6,2,1)
        grid2.addWidget(self.canvas7,0,2)
        grid2.addWidget(self.canvas8,1,2)
        grid2.addWidget(self.canvas9,2,2)
        grid2.addWidget(self.canvas10,0,3)
        grid2.addWidget(self.canvas11,1,3)
        grid2.addWidget(self.canvas12,2,3)
        grp_field.setLayout(grid2)
        
        lay_N = QVBoxLayout()
        lay_N.addWidget(grp_schedule)
        lay_N.addWidget(grp_field)
        
        grp_schedule_S = QGroupBox(' Schedule ')
        lay_schedule_S = QVBoxLayout()
        lay_schedule_S.addWidget(self.table2)
        grp_schedule_S.setLayout(lay_schedule_S)
        
        lay_S = QVBoxLayout()
        lay_S.addWidget(grp_schedule_S)
        
        tab1 = QWidget()
        tab1.setLayout(lay_N)
        tab2 = QWidget()
        tab2.setLayout(lay_S)
        tabs = QTabWidget()
        tabs.addTab(tab1, 'Normal Mode')
        tabs.addTab(tab2, 'Sweep Mode')
        
        lay_tot = QVBoxLayout()
        lay_tot.addWidget(tabs)
        self.setLayout(lay_tot)
        self.tabs = tabs
        
    def makeTable(self):
        table = QTableWidget()
        table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        table.setColumnCount(10)
        table.setRowCount(1)
        table.setHorizontalHeaderLabels(["wavelength", "theta", "phi", "psi", "nx", "ny", "tx", "ty", "ni", "nf"])
        table.setVerticalHeaderLabels(['# 1'])
        
        table.horizontalHeaderItem(0).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(0).setToolTip('Wavelength\n\nUnit: nm')
        table.horizontalHeaderItem(1).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(1).setToolTip('Incident angle\n\nUnit: deg')
        table.horizontalHeaderItem(2).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(2).setToolTip('Angle phi\n\nUnit: deg')
        table.horizontalHeaderItem(3).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(3).setToolTip('Polarization angle\n\nUnit: deg')
        table.horizontalHeaderItem(4).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(4).setToolTip('Number of Fourier harmonics in X-direction\n\n*\'nx=0\' means 1D grating in Y-direction')
        table.horizontalHeaderItem(5).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(5).setToolTip('Number of Fourier harmonics in Y-direction\n\n*\'ny=0\' means 1D grating in X-direction')
        table.horizontalHeaderItem(6).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(6).setToolTip('Periodicity in X-direction\n\nUnit: nm')
        table.horizontalHeaderItem(7).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(7).setToolTip('Periodicity in Y-direction\n\nUnit: nm')
        table.horizontalHeaderItem(8).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(8).setToolTip('Refractive index of input medium\n\n[example]\n\'1\', \'2+0.1j\', \'SiO2\'\n\n[possible mateiral list]\nAg\nAl\nAl2O3\naSiH\nAu\ncSi\nCu\nHfO2\nSiO2\nTiO2')
        table.horizontalHeaderItem(9).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(9).setToolTip('Refractive index of output medium\n\n[example]\n\'1\', \'2+0.1j\', \'SiO2\'\n\n[possible mateiral list]\nAg\nAl\nAl2O3\naSiH\nAu\ncSi\nCu\nHfO2\nSiO2\nTiO2')
        table.verticalHeaderItem(0).setFont(QFont('Consolas'))
        
        item_wl = QTableWidgetItem('532')
        item_wl.setTextAlignment(Qt.AlignCenter)
        item_wl.setFont(QFont('Consolas'))
        item_theta = QTableWidgetItem('0')
        item_theta.setTextAlignment(Qt.AlignCenter)
        item_theta.setFont(QFont('Consolas'))
        item_phi = QTableWidgetItem('0')
        item_phi.setTextAlignment(Qt.AlignCenter)
        item_phi.setFont(QFont('Consolas'))
        item_psi = QTableWidgetItem('0')
        item_psi.setTextAlignment(Qt.AlignCenter)
        item_psi.setFont(QFont('Consolas'))
        item_nx = QTableWidgetItem('5')
        item_nx.setTextAlignment(Qt.AlignCenter)
        item_nx.setFont(QFont('Consolas'))
        item_ny = QTableWidgetItem('5')
        item_ny.setTextAlignment(Qt.AlignCenter)
        item_ny.setFont(QFont('Consolas'))
        item_tx = QTableWidgetItem('300')
        item_tx.setTextAlignment(Qt.AlignCenter)
        item_tx.setFont(QFont('Consolas'))
        item_ty = QTableWidgetItem('300')
        item_ty.setTextAlignment(Qt.AlignCenter)
        item_ty.setFont(QFont('Consolas'))
        item_ni = QTableWidgetItem('SiO2')
        item_ni.setTextAlignment(Qt.AlignCenter)
        item_ni.setFont(QFont('Consolas'))
        item_nf = QTableWidgetItem('1')
        item_nf.setTextAlignment(Qt.AlignCenter)
        item_nf.setFont(QFont('Consolas'))
        table.setItem(0, 0, item_wl)
        table.setItem(0, 1, item_theta)
        table.setItem(0, 2, item_phi)
        table.setItem(0, 3, item_psi)
        table.setItem(0, 4, item_nx)
        table.setItem(0, 5, item_ny)
        table.setItem(0, 6, item_tx)
        table.setItem(0, 7, item_ty)
        table.setItem(0, 8, item_ni)
        table.setItem(0, 9, item_nf)
        table.setAlternatingRowColors(True)
        table.resizeColumnsToContents()
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        table.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
        return table
    

class MyMain(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont('Consolas'))
        self.rcwa = MyRCWA(self)
        self.initUI()
        self.setCentralWidget(self.rcwa)
        self.toolbar_setup()
    
    def initUI(self):
        QToolTip.setFont(QFont('Consolas', 10))
        self.setWindowIcon(QIcon('images\\icon.png'))
        self.setWindowTitle('Maxim')
        self.setWindowState(Qt.WindowMaximized)
        self.rcwa.tabs.currentChanged.connect(self.tabChange)
        self.statusBar = QStatusBar()
        self.statusMessage1 = QLabel(' Made by Gwanho Yoon [https://sites.google.com/site/gwanhoyoon] ')
        self.statusMessage1.setFont(QFont('Consolas'))
        self.statusMessage2 = QLabel(' '+os.getcwd()+' ')
        self.statusMessage2.setFont(QFont('Consolas'))
        self.statusMessage3 = QLabel(' Ready ')
        self.statusMessage3.setFont(QFont('Consolas'))
        self.statusBar.addWidget(self.statusMessage1)
        self.statusBar.addWidget(self.statusMessage2)
        self.statusBar.addWidget(self.statusMessage3)
        self.setStatusBar(self.statusBar)
        copyShortcut = QShortcut(QKeySequence.Copy,self)
        pasteShortcut = QShortcut(QKeySequence.Paste,self)
        deleteShortcut = QShortcut(QKeySequence.Delete,self)
        copyShortcut.activated.connect(self.copy)
        pasteShortcut.activated.connect(self.paste)
        deleteShortcut.activated.connect(self.delete)
        
    def toolbar_setup(self):
        self.toolbar = self.addToolBar('Structure Edit')
        exitAction = QAction(QIcon('images\\exit.png'), 'Exit', self)
        exitAction.triggered.connect(self.exit_btn_clicked)
        saveAction = QAction(QIcon('images\\save.png'), 'Save', self)
        saveAction.triggered.connect(self.save)
        infoAction = QAction(QIcon('images\\info.png'), 'Coordinate\nInformation', self)
        infoAction.triggered.connect(self.info_btn_clicked)
        
        btn1Action = QAction(QIcon('images\\film.png'), 'Add Film (F1)', self)
        btn1Action.triggered.connect(self.btn1_clicked)
        btn2Action = QAction(QIcon('images\\rect.png'), 'Add Rect (F2)', self)
        btn2Action.triggered.connect(self.btn2_clicked)
        btn3Action = QAction(QIcon('images\\circ.png'), 'Add Circ (F3)', self)
        btn3Action.triggered.connect(self.btn3_clicked)
        btn4Action = QAction(QIcon('images\\del.png'), 'Delete (F4)', self)
        btn4Action.triggered.connect(self.btn4_clicked)
        btn5Action = QAction(QIcon('images\\tabwiz2.png'), 'Table Wizard (F5)', self)
        btn5Action.triggered.connect(self.btn5_clicked)
        btn6Action = QAction(QIcon('images\\addrow.png'), 'Add Row (F6)', self)
        btn6Action.triggered.connect(self.btn6_clicked)
        btn6_N_Action = QAction(QIcon('images\\addrow_N.png'), 'Add Row X N', self)
        btn6_N_Action.triggered.connect(self.btn6_N_clicked)
        btn7Action = QAction(QIcon('images\\remrow.png'), 'Remove Row (F7)', self)
        btn7Action.triggered.connect(self.btn7_clicked)
        btn7_N_Action = QAction(QIcon('images\\remrow_N.png'), 'Remove Row X N', self)
        btn7_N_Action.triggered.connect(self.btn7_N_clicked)
        btn8Action = QAction(QIcon('images\\reset.png'), 'Reset (F8)', self)
        btn8Action.triggered.connect(self.btn8_clicked)
        btn9Action = QAction(QIcon('images\\run.png'), 'Run (F9)', self)
        btn9Action.triggered.connect(self.btn9_clicked)
        
        self.spacer1 = QLabel(' ')
        self.spacer2 = QLabel(' ')
        self.spacer11 = QLabel(' ')
        self.spacer22 = QLabel(' ')
        
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(infoAction)
        self.toolbar.addWidget(self.spacer1)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.spacer2)
        self.toolbar.addAction(btn1Action)
        self.toolbar.addAction(btn2Action)
        self.toolbar.addAction(btn3Action)
        self.toolbar.addAction(btn4Action)
        self.toolbar.addAction(btn5Action)
        self.toolbar.addAction(btn6Action)
        self.toolbar.addAction(btn6_N_Action)
        self.toolbar.addAction(btn7Action)
        self.toolbar.addAction(btn7_N_Action)
        self.toolbar.addAction(btn8Action)
        self.toolbar.addAction(btn9Action)
        self.toolbar.setIconSize(QSize(50,50))
        self.toolbar.addWidget(self.spacer11)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.spacer22)
        
        btn1Action.setShortcut('F1')
        btn2Action.setShortcut('F2')
        btn3Action.setShortcut('F3')
        btn4Action.setShortcut('F4')
        btn5Action.setShortcut('F5')
        btn6Action.setShortcut('F6')
        btn7Action.setShortcut('F7')
        btn8Action.setShortcut('F8')
        btn9Action.setShortcut('F9')
        btn5Action.setEnabled(False)
        btn6Action.setEnabled(False)
        btn6_N_Action.setEnabled(False)
        btn7Action.setEnabled(False)
        btn7_N_Action.setEnabled(False)
        
        self.btn5Action = btn5Action
        self.btn6Action = btn6Action
        self.btn6_N_Action = btn6_N_Action
        self.btn7Action = btn7Action
        self.btn7_N_Action = btn7_N_Action
        self.btn8Action = btn8Action
        
        self.pbar = QProgressBar()
        self.pbar.setValue(0)
        
        self.run_time_label = QLabel()
        self.run_time_label.setAlignment(Qt.AlignCenter)
        font1 = self.run_time_label.font()
        font1.setPointSize(10)
        self.run_time_label.setFont(font1)
        
        self.spacer3 = QLabel(' ')
        self.spacer4 = QLabel('  ')
        self.spacer5 = QLabel('  ')
        
        grp_tbar1 = QGroupBox(' Progress ')
        lay_tbar1 = QHBoxLayout()
        lay_tbar1.addWidget(self.pbar)
        grp_tbar1.setLayout(lay_tbar1)
        
        grp_tbar2 = QGroupBox(' Run Time ')
        lay_tbar2 = QHBoxLayout()
        lay_tbar2.addWidget(self.run_time_label)
        grp_tbar2.setLayout(lay_tbar2)
        
        self.toolbar.addWidget(self.spacer3)
        self.toolbar.addWidget(grp_tbar1)
        self.toolbar.addWidget(self.spacer4)
        self.toolbar.addWidget(grp_tbar2)
        self.toolbar.addWidget(self.spacer5)
    
    @pyqtSlot()
    def tabChange(self):
        if self.rcwa.tabs.currentIndex() == 0:
            self.btn5Action.setEnabled(False)
            self.btn6Action.setEnabled(False)
            self.btn6_N_Action.setEnabled(False)
            self.btn7Action.setEnabled(False)
            self.btn7_N_Action.setEnabled(False)
        else:
            self.btn5Action.setEnabled(True)
            self.btn6Action.setEnabled(True)
            self.btn6_N_Action.setEnabled(True)
            self.btn7Action.setEnabled(True)
            self.btn7_N_Action.setEnabled(True)
    
    @pyqtSlot()
    def keyPressEvent(self,event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter :
            if self.rcwa.tabs.currentIndex() == 0:
                i = self.rcwa.table.currentRow()
                j = self.rcwa.table.currentColumn()+1
                self.rcwa.table.setCurrentCell(i,j)
            elif self.rcwa.tabs.currentIndex() == 1:
                i = self.rcwa.table2.currentRow()+1
                j = self.rcwa.table2.currentColumn()
                self.rcwa.table2.setCurrentCell(i,j)
            event.accept()

    @pyqtSlot()
    def copy(self):
        if self.rcwa.tabs.currentIndex() == 0:
            table = self.rcwa.table
        elif self.rcwa.tabs.currentIndex() == 1:
            table = self.rcwa.table2
            
        selectedRangeList = table.selectedRanges()
        if selectedRangeList == [] :
            return
        text = ""
        selectedRange = selectedRangeList[0]
        for i in range(selectedRange.rowCount()):
            if i > 0:
                text += "\n"
            for j in range(selectedRange.columnCount()):
                if j > 0:
                    text += "\t"
                itemA = table.item(selectedRange.topRow()+i,selectedRange.leftColumn()+j)
                if itemA :
                    text += itemA.text()
        text += '\n'
        QApplication.clipboard().setText(text)
    
    @pyqtSlot()
    def paste(self):
        if self.rcwa.tabs.currentIndex() == 0:
            table = self.rcwa.table
        elif self.rcwa.tabs.currentIndex() == 1:
            table = self.rcwa.table2
        
        n_col = table.columnCount()
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_')
        m = p.match(last_item)
        if last_item == 'R_Ez':
            table.removeColumn(n_col-1)
            table.removeColumn(n_col-2)
            table.removeColumn(n_col-3)
            table.removeColumn(n_col-4)
            table.removeColumn(n_col-5)
            table.removeColumn(n_col-6)
            table.removeColumn(n_col-7)
            table.removeColumn(n_col-8)
        
        text = QApplication.clipboard().text()
        rows = text.split('\n')
        numRows = len(rows)-1
        numColumns = rows[0].count('\t')+1
        if table.currentRow()+numRows > table.rowCount():
            prevRowCount = table.rowCount()
            table.setRowCount(table.currentRow()+numRows)
            for i in range(prevRowCount,table.currentRow()+numRows):
                for kk in range(table.columnCount()):
                    item = QTableWidgetItem()
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setFont(QFont('Consolas'))
                    table.setItem(i,kk,item)
        for i in range(numRows):
            columns = rows[i].split('\t')
            for j in range(numColumns):
                row = table.currentRow()+i
                column = table.currentColumn()+j
                if column < table.columnCount():
                    table.item(row,column).setText(columns[j])
        table.resizeColumnsToContents()
    
    @pyqtSlot()
    def delete(self):
        if self.rcwa.tabs.currentIndex() == 0:
            table = self.rcwa.table
        elif self.rcwa.tabs.currentIndex() == 1:
            table = self.rcwa.table2
        
        temp = table.selectedRanges()
        top_row = QTableWidgetSelectionRange.topRow(temp[0])
        bot_row = QTableWidgetSelectionRange.bottomRow(temp[0])
        left_col = QTableWidgetSelectionRange.leftColumn(temp[0])
        right_col = QTableWidgetSelectionRange.rightColumn(temp[0])
        
        for ir in range(top_row,bot_row+1):
            for ic in range(left_col,right_col+1):
                item = QTableWidgetItem()
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont('Consolas'))
                table.setItem(ir, ic, item)
        table.resizeColumnsToContents()
        
    @pyqtSlot()
    def save(self):
        Fdir = QFileDialog.getExistingDirectory(self,'Select Directory')
        realpath = os.path.realpath(Fdir)
        if self.rcwa.tabs.currentIndex() == 0 and self.rcwa.result_op1 == True:
            self.Result_table.to_csv(realpath+'\\result_table.csv')
            np.savetxt(realpath+'\\x_xz.csv', self.rcwa.x_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\y_yz.csv', self.rcwa.y_yz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\z.csv', self.rcwa.z, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Ex_xz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Ey_xz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Ez_xz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Hx_xz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Hy_xz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Hz_xz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Ex_yz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Ey_yz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Ez_yz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Hx_yz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Hy_yz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
            np.savetxt(realpath+'\\Hz_yz.csv', self.rcwa.Ex_xz, delimiter=',', fmt='%.4e')
        elif self.rcwa.tabs.currentIndex() == 1 and self.rcwa.result_op2 == True:
            self.Result_table.to_csv(realpath+'\\result_table.csv')
            
    @pyqtSlot()
    def exit_btn_clicked(self):
        dlg = Exit_confirm()
        dlg.exec_()
        ans = dlg.ans
        if ans == True:
            qApp.quit()
    
    @pyqtSlot()
    def info_btn_clicked(self):
        dlg = Coordinate()
        dlg.exec_()
            
    @pyqtSlot()                                 # Add Film
    def btn1_clicked(self):
        if self.rcwa.tabs.currentIndex() == 0:
            table = self.rcwa.table
        elif self.rcwa.tabs.currentIndex() == 1:
            table = self.rcwa.table2
        
        n_col = table.columnCount()
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_')
        m = p.match(last_item)
        if last_item == 'R_Ez':
            table.removeColumn(n_col-1)
            table.removeColumn(n_col-2)
            table.removeColumn(n_col-3)
            table.removeColumn(n_col-4)
            table.removeColumn(n_col-5)
            table.removeColumn(n_col-6)
            table.removeColumn(n_col-7)
            table.removeColumn(n_col-8)
        n_col = table.columnCount()
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_')
        m = p.match(last_item)
        if m == None:
            num = 0
        else:
            temp = m.group()
            num = int(last_item.replace(temp, ""))+1
        table.setColumnCount(n_col+3)
        table.setHorizontalHeaderLabels(labels+[f'type_{num}',f'laythick_{num}',f'n_{num}'])
        table.horizontalHeaderItem(n_col).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col).setToolTip('Type of structure\n\nfilm: homogeneous film\nrect: rectangular structure\ncirc: circular pillar')
        table.horizontalHeaderItem(n_col+1).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+1).setToolTip('Thickness of film\n\nUnit: nm')
        table.horizontalHeaderItem(n_col+2).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+2).setToolTip('Refractive index of film\n\n[example]\n\'1\', \'2+0.1j\', \'SiO2\'\n\n[possible mateiral list]\nAg\nAl\nAl2O3\naSiH\nAu\ncSi\nCu\nHfO2\nSiO2\nTiO2')
        n_row = table.rowCount()
        for ir in range(n_row):
            item_type = QTableWidgetItem('film')
            item_type.setTextAlignment(Qt.AlignCenter)
            item_type.setFont(QFont('Consolas'))
            item_laythick = QTableWidgetItem()
            item_laythick.setTextAlignment(Qt.AlignCenter)
            item_laythick.setFont(QFont('Consolas'))
            item_n = QTableWidgetItem()
            item_n.setTextAlignment(Qt.AlignCenter)
            item_n.setFont(QFont('Consolas'))
            table.setItem(ir, len(labels), item_type)
            table.setItem(ir, len(labels)+1, item_laythick)
            table.setItem(ir, len(labels)+2, item_n)
        table.resizeColumnsToContents()
    
    @pyqtSlot()                                 # Add Rect
    def btn2_clicked(self):
        if self.rcwa.tabs.currentIndex() == 0:
            table = self.rcwa.table
        elif self.rcwa.tabs.currentIndex() == 1:
            table = self.rcwa.table2
        
        n_col = table.columnCount()
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_')
        m = p.match(last_item)
        if last_item == 'R_Ez':
            table.removeColumn(n_col-1)
            table.removeColumn(n_col-2)
            table.removeColumn(n_col-3)
            table.removeColumn(n_col-4)
            table.removeColumn(n_col-5)
            table.removeColumn(n_col-6)
            table.removeColumn(n_col-7)
            table.removeColumn(n_col-8)
        n_col = table.columnCount()
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_')
        m = p.match(last_item)
        if m == None:
            num = 0
        else:
            temp = m.group()
            num = int(last_item.replace(temp, ""))+1
        table.setColumnCount(n_col+7)
        table.setHorizontalHeaderLabels(labels+[f'type_{num}',f'laythick_{num}',f'wx_{num}',f'wy_{num}',f'angle_{num}',f'ng_{num}',f'nb_{num}'])
        table.horizontalHeaderItem(n_col).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col).setToolTip('Type of structure\n\nfilm: homogeneous film\nrect: rectangular structure\ncirc: circular pillar')
        table.horizontalHeaderItem(n_col+1).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+1).setToolTip('Thickness of rectangular structure\n\nUnit: nm')
        table.horizontalHeaderItem(n_col+2).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+2).setToolTip('X-direction width of rectangular structure\n\nUnit: nm')
        table.horizontalHeaderItem(n_col+3).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+3).setToolTip('Y-direction width of rectangular structure\n\nUnit: nm')
        table.horizontalHeaderItem(n_col+4).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+4).setToolTip('Rotation angle of rectangular structure\n\nUnit: deg')
        table.horizontalHeaderItem(n_col+5).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+5).setToolTip('Refractive index of rectangular structure\n\n[example]\n\'1\', \'2+0.1j\', \'SiO2\'\n\n[possible mateiral list]\nAg\nAl\nAl2O3\naSiH\nAu\ncSi\nCu\nHfO2\nSiO2\nTiO2')
        table.horizontalHeaderItem(n_col+6).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+6).setToolTip('Refractive index of background\n\n[example]\n\'1\', \'2+0.1j\', \'SiO2\'\n\n[possible mateiral list]\nAg\nAl\nAl2O3\naSiH\nAu\ncSi\nCu\nHfO2\nSiO2\nTiO2')
        n_row = table.rowCount()
        for ir in range(n_row):
            item_type = QTableWidgetItem('rect')
            item_type.setTextAlignment(Qt.AlignCenter)
            item_type.setFont(QFont('Consolas'))
            item_laythick = QTableWidgetItem()
            item_laythick.setTextAlignment(Qt.AlignCenter)
            item_laythick.setFont(QFont('Consolas'))
            item_wx = QTableWidgetItem()
            item_wx.setTextAlignment(Qt.AlignCenter)
            item_wx.setFont(QFont('Consolas'))
            item_wy = QTableWidgetItem()
            item_wy.setTextAlignment(Qt.AlignCenter)
            item_wy.setFont(QFont('Consolas'))
            item_angle = QTableWidgetItem()
            item_angle.setTextAlignment(Qt.AlignCenter)
            item_angle.setFont(QFont('Consolas'))
            item_ng = QTableWidgetItem()
            item_ng.setTextAlignment(Qt.AlignCenter)
            item_ng.setFont(QFont('Consolas'))
            item_nb = QTableWidgetItem()
            item_nb.setTextAlignment(Qt.AlignCenter)
            item_nb.setFont(QFont('Consolas'))
            table.setItem(ir, len(labels), item_type)
            table.setItem(ir, len(labels)+1, item_laythick)
            table.setItem(ir, len(labels)+2, item_wx)
            table.setItem(ir, len(labels)+3, item_wy)
            table.setItem(ir, len(labels)+4, item_angle)
            table.setItem(ir, len(labels)+5, item_ng)
            table.setItem(ir, len(labels)+6, item_nb)
        table.resizeColumnsToContents()
    
    @pyqtSlot()                                 # Add Circ
    def btn3_clicked(self):
        if self.rcwa.tabs.currentIndex() == 0:
            table = self.rcwa.table
        elif self.rcwa.tabs.currentIndex() == 1:
            table = self.rcwa.table2
        
        n_col = table.columnCount()
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_')
        m = p.match(last_item)
        if last_item == 'R_Ez':
            table.removeColumn(n_col-1)
            table.removeColumn(n_col-2)
            table.removeColumn(n_col-3)
            table.removeColumn(n_col-4)
            table.removeColumn(n_col-5)
            table.removeColumn(n_col-6)
            table.removeColumn(n_col-7)
            table.removeColumn(n_col-8)
        n_col = table.columnCount()
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_')
        m = p.match(last_item)
        if m == None:
            num = 0
        else:
            temp = m.group()
            num = int(last_item.replace(temp, ""))+1
        table.setColumnCount(n_col+5)
        table.setHorizontalHeaderLabels(labels+[f'type_{num}',f'laythick_{num}',f'r_{num}',f'ng_{num}',f'nb_{num}'])
        table.horizontalHeaderItem(n_col).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col).setToolTip('Type of structure\n\nfilm: homogeneous film\nrect: rectangular structure\ncirc: circular pillar')
        table.horizontalHeaderItem(n_col+1).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+1).setToolTip('Thickness of circular pillar\n\nUnit: nm')
        table.horizontalHeaderItem(n_col+2).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+2).setToolTip('Radius of circular pillar\n\nUnit: nm')
        table.horizontalHeaderItem(n_col+3).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+3).setToolTip('Refractive index of circular pillar\n\n[example]\n\'1\', \'2+0.1j\', \'SiO2\'\n\n[possible mateiral list]\nAg\nAl\nAl2O3\naSiH\nAu\ncSi\nCu\nHfO2\nSiO2\nTiO2')
        table.horizontalHeaderItem(n_col+4).setFont(QFont('Consolas'))
        table.horizontalHeaderItem(n_col+4).setToolTip('Refractive index of background\n\n[example]\n\'1\', \'2+0.1j\', \'SiO2\'\n\n[possible mateiral list]\nAg\nAl\nAl2O3\naSiH\nAu\ncSi\nCu\nHfO2\nSiO2\nTiO2')
        n_row = table.rowCount()
        for ir in range(n_row):
            item_type = QTableWidgetItem('circ')
            item_type.setTextAlignment(Qt.AlignCenter)
            item_type.setFont(QFont('Consolas'))
            item_laythick = QTableWidgetItem()
            item_laythick.setTextAlignment(Qt.AlignCenter)
            item_laythick.setFont(QFont('Consolas'))
            item_r = QTableWidgetItem()
            item_r.setTextAlignment(Qt.AlignCenter)
            item_r.setFont(QFont('Consolas'))
            item_ng = QTableWidgetItem()
            item_ng.setTextAlignment(Qt.AlignCenter)
            item_ng.setFont(QFont('Consolas'))
            item_nb = QTableWidgetItem()
            item_nb.setTextAlignment(Qt.AlignCenter)
            item_nb.setFont(QFont('Consolas'))
            table.setItem(ir, len(labels), item_type)
            table.setItem(ir, len(labels)+1, item_laythick)
            table.setItem(ir, len(labels)+2, item_r)
            table.setItem(ir, len(labels)+3, item_ng)
            table.setItem(ir, len(labels)+4, item_nb)
        table.resizeColumnsToContents()
    
    @pyqtSlot()                                 # Delete
    def btn4_clicked(self):
        if self.rcwa.tabs.currentIndex() == 0:
            table = self.rcwa.table
        elif self.rcwa.tabs.currentIndex() == 1:
            table = self.rcwa.table2
        
        n_col = table.columnCount()
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p1 = re.compile('\w+_\d+')
        m1 = p1.match(last_item)
        p2 = re.compile('\w+_')
        m2 = p2.match(last_item)
        if m1 != None:
            temp = m2.group()
            num = int(last_item.replace(temp, ""))
            p2 = re.compile(f'\w+_{num}')
            for i in range(len(labels)):
                if p2.match(labels[i]) != None:
                    table.removeColumn(table.columnCount()-1)
        elif last_item == 'R_Ez':
            table.removeColumn(n_col-1)
            table.removeColumn(n_col-2)
            table.removeColumn(n_col-3)
            table.removeColumn(n_col-4)
            table.removeColumn(n_col-5)
            table.removeColumn(n_col-6)
            table.removeColumn(n_col-7)
            table.removeColumn(n_col-8)
            
    
    @pyqtSlot()                                 # Table Wizard
    def btn5_clicked(self):
        def is_digit(str):
            try:
                tmp = complex(str)
                return True
            except ValueError:
                return False
        
        def is_int(x):
            if int(x) == x:
                return True
            else:
                return False
        
        if self.rcwa.tabs.currentIndex() == 0:
            table = self.rcwa.table
        elif self.rcwa.tabs.currentIndex() == 1:
            table = self.rcwa.table2
        
        n_col = table.columnCount()
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_')
        m = p.match(last_item)
        if last_item == 'R_Ez':
            table.removeColumn(n_col-1)
            table.removeColumn(n_col-2)
            table.removeColumn(n_col-3)
            table.removeColumn(n_col-4)
            table.removeColumn(n_col-5)
            table.removeColumn(n_col-6)
            table.removeColumn(n_col-7)
            table.removeColumn(n_col-8)
        
        n_row = table.rowCount()
        temp = table.selectedRanges()
        top_row = QTableWidgetSelectionRange.topRow(temp[0])
        bot_row = QTableWidgetSelectionRange.bottomRow(temp[0])
        left_col = QTableWidgetSelectionRange.leftColumn(temp[0])
        right_col = QTableWidgetSelectionRange.rightColumn(temp[0])
        cur_col = table.currentColumn()
        top_item = QTableWidgetItem.text(table.item(top_row,cur_col))
        bot_item = QTableWidgetItem.text(table.item(bot_row,cur_col))
        
        if left_col == right_col:
            if is_digit(top_item) == True:
                if top_row == bot_row:
                    for i in range(top_row,n_row):
                        item = QTableWidgetItem(top_item)
                        item.setTextAlignment(Qt.AlignCenter)
                        item.setFont(QFont('Consolas'))
                        table.setItem(i, cur_col, item)
                elif top_row+1 == bot_row:
                    delta = float(bot_item)-float(top_item)
                    for i in range(top_row,n_row):
                        item = QTableWidgetItem(str(round(float(top_item)+delta*i,2)))
                        item.setTextAlignment(Qt.AlignCenter)
                        item.setFont(QFont('Consolas'))
                        table.setItem(i, cur_col, item)
                elif top_row+1 < bot_row:
                    if float(bot_item) != float(top_item):
                        delta = (float(bot_item)-float(top_item))/(bot_row-top_row)
                        for i in range(top_row,bot_row+1):
                            item = QTableWidgetItem(str(round(float(top_item)+delta*i,2)))
                            item.setTextAlignment(Qt.AlignCenter)
                            item.setFont(QFont('Consolas'))
                            table.setItem(i, cur_col, item)
                    else:
                        for i in range(top_row,bot_row+1):
                            item = QTableWidgetItem(top_item)
                            item.setTextAlignment(Qt.AlignCenter)
                            item.setFont(QFont('Consolas'))
                            table.setItem(i, cur_col, item)
            else:
                if top_row == bot_row:
                    for i in range(top_row,n_row):
                        item = QTableWidgetItem(top_item)
                        item.setTextAlignment(Qt.AlignCenter)
                        item.setFont(QFont('Consolas'))
                        table.setItem(i, cur_col, item)
                else:
                    for i in range(top_row,bot_row+1):
                        item = QTableWidgetItem(top_item)
                        item.setTextAlignment(Qt.AlignCenter)
                        item.setFont(QFont('Consolas'))
                        table.setItem(i, cur_col, item)
        else:
            if top_row == bot_row:
                for ic in range(left_col,right_col+1):
                    top_item = QTableWidgetItem.text(table.item(top_row,ic))
                    for ir in range(top_row,n_row):
                        item = QTableWidgetItem(top_item)
                        item.setTextAlignment(Qt.AlignCenter)
                        item.setFont(QFont('Consolas'))
                        table.setItem(ir, ic, item)
            else:
                for ic in range(left_col,right_col+1):
                    top_item = QTableWidgetItem.text(table.item(top_row,ic))
                    for ir in range(top_row,bot_row+1):
                        item = QTableWidgetItem(top_item)
                        item.setTextAlignment(Qt.AlignCenter)
                        item.setFont(QFont('Consolas'))
                        table.setItem(ir, ic, item)
                        
        table.resizeColumnsToContents()
    
    @pyqtSlot()                                 # Add Row
    def btn6_clicked(self):
        table = self.rcwa.table2
        n_col = table.columnCount()
        
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_')
        m = p.match(last_item)
        if last_item == 'R_Ez':
            table.removeColumn(n_col-1)
            table.removeColumn(n_col-2)
            table.removeColumn(n_col-3)
            table.removeColumn(n_col-4)
            table.removeColumn(n_col-5)
            table.removeColumn(n_col-6)
            table.removeColumn(n_col-7)
            table.removeColumn(n_col-8)
            
        n_col = table.columnCount()
        n_row = table.rowCount()
        vlabels = []
        for i in range(n_row):
            vlabels.append(QTableWidgetItem.text(table.verticalHeaderItem(i)))
        table.setRowCount(n_row+1)
        table.setVerticalHeaderLabels(vlabels+[f'# {n_row+1}'])
        table.verticalHeaderItem(n_row).setFont(QFont('Consolas'))
        for i in range(n_col):
            item = QTableWidgetItem(table.item(n_row-1,i))
            table.setItem(n_row, i, item)
    
    @pyqtSlot()                                 # Add Row x N
    def btn6_N_clicked(self):
        table = self.rcwa.table2
        n_col = table.columnCount()
        dlg = AddRow()
        dlg.exec_()
        num = int(dlg.num)
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_')
        m = p.match(last_item)
        if last_item == 'R_Ez':
            table.removeColumn(n_col-1)
            table.removeColumn(n_col-2)
            table.removeColumn(n_col-3)
            table.removeColumn(n_col-4)
            table.removeColumn(n_col-5)
            table.removeColumn(n_col-6)
            table.removeColumn(n_col-7)
            table.removeColumn(n_col-8)
        
        n_col = table.columnCount()
        n_row = table.rowCount()
        vlabels = []
        for i in range(n_row):
            vlabels.append(QTableWidgetItem.text(table.verticalHeaderItem(i)))
        table.setRowCount(n_row+num)
        add_vlabels = []
        for i in range(num):
            add_vlabels.append(f'# {n_row+1+i}')
        table.setVerticalHeaderLabels(vlabels+add_vlabels)
        for i in range(num):
            table.verticalHeaderItem(n_row+i).setFont(QFont('Consolas'))
        for ic in range(n_col):
            for ir in range(num):
                item = QTableWidgetItem(table.item(n_row-1,ic))
                table.setItem(n_row+ir, ic, item)
    
    @pyqtSlot()                                 # Remove Row
    def btn7_clicked(self):
        table = self.rcwa.table2
        n_row = table.rowCount()
        if n_row > 1:
            table.removeRow(n_row-1)
    
    @pyqtSlot()                                 # Remove Row x N
    def btn7_N_clicked(self):
        table = self.rcwa.table2
        n_row = table.rowCount()
        dlg = RemRow()
        dlg.exec_()
        num = int(dlg.num)
        if n_row-num > 0:
            for i in range(num+1):
                table.removeRow(n_row-i)
        else:
            for i in range(n_row):
                table.removeRow(n_row-i)
    
    @pyqtSlot()                                 # Reset
    def btn8_clicked(self):
        if self.rcwa.tabs.currentIndex() == 0:
            table = self.rcwa.table
        elif self.rcwa.tabs.currentIndex() == 1:
            table = self.rcwa.table2
        
        dlg = Reset_confirm()
        dlg.exec_()
        ans = dlg.ans
        
        if ans == True:
            table.clearContents()
            n_col = table.columnCount()
            labels = []
            for i in range(n_col):
                labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
            last_item = labels[-1]
            p1 = re.compile('\w+_\d')
            for i in range(len(labels)):
                if p1.match(labels[i]) != None:
                    table.removeColumn(table.columnCount()-1)
            n_row = table.rowCount()
            while n_row > 1:
                table.removeRow(n_row-1)
                n_row = n_row-1
            n_col = table.columnCount()
            for ic in range(n_col):
                item_reset = QTableWidgetItem()
                item_reset.setTextAlignment(Qt.AlignCenter)
                item_reset.setFont(QFont('Consolas'))
                table.setItem(0, ic, item_reset)
    
    ###################################### RCWA calculation #######################################
    @pyqtSlot()                                 # Run
    def btn9_clicked(self):
        tic = time.time()
        self.statusMessage3.setText(' Busy ')
        if self.rcwa.tabs.currentIndex() == 0:
            table = self.rcwa.table
        elif self.rcwa.tabs.currentIndex() == 1:
            table = self.rcwa.table2
            
        n_col = table.columnCount()
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_')
        m = p.match(last_item)
        if last_item == 'R_Ez':
            table.removeColumn(n_col-1)
            table.removeColumn(n_col-2)
            table.removeColumn(n_col-3)
            table.removeColumn(n_col-4)
            table.removeColumn(n_col-5)
            table.removeColumn(n_col-6)
            table.removeColumn(n_col-7)
            table.removeColumn(n_col-8)
        
        n_col = table.columnCount()
        n_row = table.rowCount()
        
        labels = []
        for i in range(n_col):
            labels.append(QTableWidgetItem.text(table.horizontalHeaderItem(i)))
        last_item = labels[-1]
        p = re.compile('\w+_\d+')
        m_str_exist = p.match(last_item)
        
        df_data0 = pd.DataFrame(index=range(n_row),columns=range(n_col))
        
        for ic in range(n_col):
            vname = QTableWidgetItem.text(table.horizontalHeaderItem(ic))
            df_data0.rename(columns={ic:vname}, inplace = True)
            for ir in range(n_row):
                df_data0[vname][ir] = QTableWidgetItem.text(table.item(ir,ic))
        
        if m_str_exist == None:
            df_data0['type_0'] = 'film'
            df_data0['laythick_0'] = '0'
            df_data0['n_0'] = '1'
        
        table.setColumnCount(n_col+8)
        table.setHorizontalHeaderLabels(labels+['T','R','T_Ex','T_Ey','T_Ez','R_Ex','R_Ey','R_Ez'])
        for ic in range(8):
            table.horizontalHeaderItem(n_col+ic).setFont(QFont('Consolas'))
            for ir in range(n_row):
                item = QTableWidgetItem()
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont('Consolas'))
                table.setItem(ir, n_col+ic, item)
        
        # Value conversion to number
        def is_digit(str):
            try:
                tmp = complex(str)
                return True
            except ValueError:
                return False
        
        def is_int(x):
            if int(x) == x:
                return True
            else:
                return False
        
        var = list(df_data0.columns)
        N_swp = df_data0.shape[0]
        
        for i1 in range(len(var)):
            for i2 in range(N_swp):
                if is_digit(df_data0[var[i1]][i2]) == True:
                    if complex(df_data0[var[i1]][i2]).imag != 0:
                        df_data0[var[i1]][i2] = complex(df_data0[var[i1]][i2])
                    elif is_int(float(df_data0[var[i1]][i2])) == True:
                        df_data0[var[i1]][i2] = int(float(df_data0[var[i1]][i2]))
                    else:
                        df_data0[var[i1]][i2] = float(df_data0[var[i1]][i2])
        
        temp = ' '.join(df_data0.columns)
        Nlay = temp.count('type_')
        pi = np.pi
        data = pd.DataFrame.to_dict(df_data0)
        
        def index_finder(material,wavelength):
            nk = np.loadtxt(f'py_mat\\{material}.txt')
            nk_wl = nk[:,0]
            nk_n = nk[:,1]
            nk_k = nk[:,2]
            i1 = np.nonzero(nk_wl<wavelength)[0][-1]
            i2 = np.nonzero(nk_wl>wavelength)[0][0]
            nn = nk_n[i2] + (nk_n[i1]-nk_n[i2])*(nk_wl[i2]-wavelength)/(nk_wl[i2]-nk_wl[i1])
            kk = nk_k[i2] + (nk_k[i1]-nk_k[i2])*(nk_wl[i2]-wavelength)/(nk_wl[i2]-nk_wl[i1])
            y = round(nn,4) + round(kk,4)*1j
            return y
        
        # Index conversion
        for i in range(N_swp):
            for ii in range(Nlay):
                if data[f'type_{ii}'][i] == 'film':
                    if type(data[f'n_{ii}'][i]) == str:
                        data[f'n_{ii}'][i] = index_finder(data[f'n_{ii}'][i],data['wavelength'][i])
                else:
                    if type(data[f'ng_{ii}'][i]) == str:
                        data[f'ng_{ii}'][i] = index_finder(data[f'ng_{ii}'][i],data['wavelength'][i])
                    elif type(data[f'nb_{ii}'][i]) == str:
                        data[f'nb_{ii}'][i] = index_finder(data[f'nb_{ii}'][i],data['wavelength'][i])
            if type(data['ni'][i]) == str:
                data['ni'][i] = index_finder(data['ni'][i],data['wavelength'][i])
            elif type(data['nf'][i]) == str:
                data['nf'][i] = index_finder(data['nf'][i],data['wavelength'][i])
        df_data = pd.DataFrame(data)
        
        result = {'T':[0]*N_swp,
                  'R':[0]*N_swp,
                  'T_Ex':[0]*N_swp,
                  'T_Ey':[0]*N_swp,
                  'R_Ex':[0]*N_swp,
                  'R_Ey':[0]*N_swp}
        df_result = pd.DataFrame(result)
        
        # Main calculation
        for n_swp in range(N_swp):
            if N_swp > 1:
                pnum = 100*(n_swp+1)/N_swp
                self.pbar.setValue(pnum)
            
            # Preallocation
            df = df_data.loc[n_swp]
            wl = df['wavelength']*1e-9
            theta = df['theta']*pi/180
            phi = df['phi']*pi/180
            psi = df['psi']*pi/180
            nx = df['nx']
            ny = df['ny']
            tx = df['tx']*1e-9
            ty = df['ty']*1e-9
            ni = df['ni']
            nf = df['nf']
            
            c0 = 299792458
            eps0 = 1/(36*pi)*1e-9
            mu0 = 4*pi*1e-7
            eta0 = 120*pi
            k0 = 2*pi/wl
            w0 = c0*k0
            kx0 = k0*np.sin(theta)*np.cos(phi)
            ky0 = k0*np.sin(theta)*np.sin(phi)
            kz0 = k0*np.cos(theta)
            nFx = 2*nx + 1
            nFy = 2*ny + 1
            nSx = 4*nx + 1
            nSy = 4*ny + 1
            
            k_inc = k0*ni
            kx_inc = kx0*ni
            ky_inc = ky0*ni
            kz_inc = k_inc*np.cos(theta)
            k_ref = k0*ni
            kx_ref = kx0*ni
            ky_ref = ky0*ni
            kz_ref = k_ref*np.cos(theta)
            k_tra = k0*nf
            kx_tra = kx0*nf
            ky_tra = ky0*nf
            kz_tra = k_tra*np.cos(theta)
            N = nFx*nFy
            
            # Fourier coefficient
            def rect_2D_FT(m,n,tx,ty,wx,wy):
                f1 = (wx/tx)*np.sinc(wx*m/tx)
                f2 = (wy/ty)*np.sinc(wy*n/ty)
                y = f1*f2
                return y
            
            def rot_rect_2D_FT(nx,ny,tx,ty,wx,wy,angle):    # angle unit is degree
                nSx = 4*nx + 1
                nSy = 4*ny + 1
                NSx = 30*(nSx-1)+1
                NSy = 30*(nSy-1)+1
        
                xx = np.arange(-(NSx-1)/2,(NSx-1)/2+1)*tx/(NSx-1)
                yy = np.flipud(xx)
                [x,y] = np.meshgrid(xx,yy)
            
                x[abs(x)<=wx/2] = 0
                x[abs(x)>wx/2] = -1
                x = x+1
                y[abs(y)<=wy/2] = 0
                y[abs(y)>wy/2] = -1
                y = y+1
        
                U = x*y
                U = scipy.ndimage.rotate(U,-angle, reshape=False, prefilter=False)
                U[U>=0.5] = 1
                U[U<0.5] = 0
                
                y = np.fft.fftshift(np.fft.fft2(np.fft.fftshift(U)))
                y = y/(NSx*NSy)
                y = y[int((NSx-1)/2-(nSx-1)/2):int((NSx-1)/2+1+(nSx-1)/2),int((NSx-1)/2-(nSy-1)/2):int((NSx-1)/2+1+(nSy-1)/2)]
                y = y.T
                return y
            
            def circ_2D_FT(r,tx,nx,ny):
                nSx = 4*nx + 1
                nSy = 4*ny + 1
                NSx = 10*(nSx-1)+1
                NSy = 10*(nSy-1)+1
                if r == 0:
                    temp = np.zeros([nSx,nSy])
                    temp[int((nSx-1)/2),int((nSy-1)/2)] = 1
                    y = temp.copy()
                else:
                    xx = np.arange(-(NSx-1)/2,(NSx-1)/2+1)*tx/(NSx-1)
                    yy = np.flipud(xx)
                    [x,y] = np.meshgrid(xx,yy)
            
                    U = np.sqrt(x**2+y**2)
                    U[U>r] = -1
                    U[U>=0] = 0
                    U = U + 1
            
                    y = np.fft.fftshift(np.fft.fft2(np.fft.fftshift(U)))
                    y = y/(NSx*NSy)
                    y = y[int((NSx-1)/2-(nSx-1)/2):int((NSx-1)/2+1+(nSx-1)/2),int((NSx-1)/2-(nSy-1)/2):int((NSx-1)/2+1+(nSy-1)/2)]
                return y
        
            my, mx = np.meshgrid(np.arange(-nFy+1,-nFy+nSy+1,1),np.arange(-nFx+1,-nFx+nSx+1,1))
            
            pfeprxx = [[]]*Nlay
            pfepryy = [[]]*Nlay
            pfeprzz = [[]]*Nlay
            pfmurxx = [[]]*Nlay
            pfmuryy = [[]]*Nlay
            pfmurzz = [[]]*Nlay
            pfaprxx = [[]]*Nlay
            pfapryy = [[]]*Nlay
            pfaprzz = [[]]*Nlay
            pfburxx = [[]]*Nlay
            pfburyy = [[]]*Nlay
            pfburzz = [[]]*Nlay
            
            for i in range(Nlay):
                if df['type_%d'%i] == 'rect':
                    eprgxx = df[f'ng_{i}']**2
                    eprgyy = df[f'ng_{i}']**2
                    eprgzz = df[f'ng_{i}']**2
                    murgxx = 1
                    murgyy = 1
                    murgzz = 1
                    eprbxx = df[f'nb_{i}']**2
                    eprbyy = df[f'nb_{i}']**2
                    eprbzz = df[f'nb_{i}']**2
                    murbxx = 1
                    murbyy = 1
                    murbzz = 1
                    
                    if nx == 0:
                        wxi = tx
                        wyi = df['wy_%d'%i]*1e-9
                    elif ny == 0:
                        wxi = df['wx_%d'%i]*1e-9
                        wyi = ty
                    else:
                        wxi, wyi = (df['wx_%d'%i]*1e-9, df['wy_%d'%i]*1e-9)
                    
                    if df['angle_%d'%i] == 0:
                        pfeprxx[i] = eprgxx*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + eprbxx*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                        pfepryy[i] = eprgyy*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + eprbyy*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                        pfeprzz[i] = eprgzz*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + eprbzz*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                        pfmurxx[i] = murgxx*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + murbxx*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                        pfmuryy[i] = murgyy*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + murbyy*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                        pfmurzz[i] = murgzz*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + murbzz*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                        pfaprxx[i] = (1/eprgxx)*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + (1/eprbxx)*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                        pfapryy[i] = (1/eprgyy)*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + (1/eprbyy)*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                        pfaprzz[i] = (1/eprgzz)*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + (1/eprbzz)*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                        pfburxx[i] = (1/murgxx)*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + (1/murbxx)*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                        pfburyy[i] = (1/murgyy)*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + (1/murbyy)*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                        pfburzz[i] = (1/murgzz)*rect_2D_FT(mx,my,tx,ty,wxi,wyi) + (1/murbzz)*(rect_2D_FT(mx,my,tx,ty,tx,ty) - rect_2D_FT(mx,my,tx,ty,wxi,wyi))
                    else:
                        angle = df['angle_%d'%i]
                        pfeprxx[i] = eprgxx*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + eprbxx*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))
                        pfepryy[i] = eprgyy*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + eprbyy*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))
                        pfeprzz[i] = eprgzz*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + eprbzz*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))
                        pfmurxx[i] = murgxx*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + murbxx*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))
                        pfmuryy[i] = murgyy*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + murbyy*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))
                        pfmurzz[i] = murgzz*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + murbzz*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))
                        pfaprxx[i] = (1/eprgxx)*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + (1/eprbxx)*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))
                        pfapryy[i] = (1/eprgyy)*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + (1/eprbyy)*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))
                        pfaprzz[i] = (1/eprgzz)*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + (1/eprbzz)*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))
                        pfburxx[i] = (1/murgxx)*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + (1/murbxx)*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))
                        pfburyy[i] = (1/murgyy)*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + (1/murbyy)*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))
                        pfburzz[i] = (1/murgzz)*rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle) + (1/murbzz)*(rot_rect_2D_FT(nx,ny,tx,ty,tx,ty,0) - rot_rect_2D_FT(nx,ny,tx,ty,wxi,wyi,angle))  
                
                elif df['type_%d'%i] == 'circ':
                    eprgxx = df[f'ng_{i}']**2
                    eprgyy = df[f'ng_{i}']**2
                    eprgzz = df[f'ng_{i}']**2
                    murgxx = 1
                    murgyy = 1
                    murgzz = 1
                    eprbxx = df[f'nb_{i}']**2
                    eprbyy = df[f'nb_{i}']**2
                    eprbzz = df[f'nb_{i}']**2
                    murbxx = 1
                    murbyy = 1
                    murbzz = 1
                    
                    r = df['r_%d'%i]*1e-9
                    pfeprxx[i] = eprgxx*circ_2D_FT(r,tx,nx,ny) + eprbxx*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    pfepryy[i] = eprgyy*circ_2D_FT(r,tx,nx,ny) + eprbyy*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    pfeprzz[i] = eprgzz*circ_2D_FT(r,tx,nx,ny) + eprbzz*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    pfmurxx[i] = murgxx*circ_2D_FT(r,tx,nx,ny) + murbxx*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    pfmuryy[i] = murgyy*circ_2D_FT(r,tx,nx,ny) + murbyy*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    pfmurzz[i] = murgzz*circ_2D_FT(r,tx,nx,ny) + murbzz*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    pfaprxx[i] = (1/eprgxx)*circ_2D_FT(r,tx,nx,ny) + (1/eprbxx)*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    pfapryy[i] = (1/eprgyy)*circ_2D_FT(r,tx,nx,ny) + (1/eprbyy)*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    pfaprzz[i] = (1/eprgzz)*circ_2D_FT(r,tx,nx,ny) + (1/eprbzz)*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    pfburxx[i] = (1/murgxx)*circ_2D_FT(r,tx,nx,ny) + (1/murbxx)*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    pfburyy[i] = (1/murgyy)*circ_2D_FT(r,tx,nx,ny) + (1/murbyy)*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    pfburzz[i] = (1/murgzz)*circ_2D_FT(r,tx,nx,ny) + (1/murbzz)*(circ_2D_FT(0,tx,nx,ny) - circ_2D_FT(r,tx,nx,ny))
                    
                elif df['type_%d'%i] == 'film':
                    eprxx = df[f'n_{i}']**2
                    epryy = df[f'n_{i}']**2
                    eprzz = df[f'n_{i}']**2
                    murxx = 1
                    muryy = 1
                    murzz = 1
                    
                    exx = np.zeros([nSx,nSy],dtype=complex)
                    eyy = np.zeros([nSx,nSy],dtype=complex)
                    ezz = np.zeros([nSx,nSy],dtype=complex)
                    mxx = np.zeros([nSx,nSy],dtype=complex)
                    myy = np.zeros([nSx,nSy],dtype=complex)
                    mzz = np.zeros([nSx,nSy],dtype=complex)
                    axx = np.zeros([nSx,nSy],dtype=complex)
                    ayy = np.zeros([nSx,nSy],dtype=complex)
                    azz = np.zeros([nSx,nSy],dtype=complex)
                    bxx = np.zeros([nSx,nSy],dtype=complex)
                    byy = np.zeros([nSx,nSy],dtype=complex)
                    bzz = np.zeros([nSx,nSy],dtype=complex)
                    
                    exx[nFx-1,nFy-1] = eprxx
                    eyy[nFx-1,nFy-1] = epryy
                    ezz[nFx-1,nFy-1] = eprzz
                    mxx[nFx-1,nFy-1] = murxx
                    myy[nFx-1,nFy-1] = muryy
                    mzz[nFx-1,nFy-1] = murzz
                    axx[nFx-1,nFy-1] = (1/eprxx)
                    ayy[nFx-1,nFy-1] = (1/epryy)
                    azz[nFx-1,nFy-1] = (1/eprzz)
                    bxx[nFx-1,nFy-1] = (1/murxx)
                    byy[nFx-1,nFy-1] = (1/muryy)
                    bzz[nFx-1,nFy-1] = (1/murzz)
                    
                    pfeprxx[i] = exx
                    pfepryy[i] = eyy
                    pfeprzz[i] = ezz
                    pfmurxx[i] = mxx
                    pfmuryy[i] = myy
                    pfmurzz[i] = mzz
                    pfaprxx[i] = axx
                    pfapryy[i] = ayy
                    pfaprzz[i] = azz
                    pfburxx[i] = bxx
                    pfburyy[i] = byy
                    pfburzz[i] = bzz
                    
            # Toeplitz matrix
            j = np.arange(1,N+1,1).reshape(1,N)
            my1 = -((j-1) % nFy) + nFy
            mx1 = np.int32((np.fliplr(j)-my1)/nFy + 1)
            indx = mx1 - mx1.T + nFx
            indy = my1 - my1.T + nFy
            ind = np.dot((indy-1),nSx) + indx
            ind_temp = np.squeeze(ind.reshape(1,N*N))
            
            Exx = [[]]*Nlay
            Eyy = [[]]*Nlay
            Ezz = [[]]*Nlay
            Gxx = [[]]*Nlay
            Gyy = [[]]*Nlay
            Gzz = [[]]*Nlay
            Axx = [[]]*Nlay
            Ayy = [[]]*Nlay
            Azz = [[]]*Nlay
            Bxx = [[]]*Nlay
            Byy = [[]]*Nlay
            Bzz = [[]]*Nlay
            
            for i in range(Nlay):
                pfeprxx_temp = np.squeeze(pfeprxx[i].T.reshape(1,nSx*nSy))
                pfepryy_temp = np.squeeze(pfepryy[i].T.reshape(1,nSx*nSy))
                pfeprzz_temp = np.squeeze(pfeprzz[i].T.reshape(1,nSx*nSy))
                pfmurxx_temp = np.squeeze(pfmurxx[i].T.reshape(1,nSx*nSy))
                pfmuryy_temp = np.squeeze(pfmuryy[i].T.reshape(1,nSx*nSy))
                pfmurzz_temp = np.squeeze(pfmurzz[i].T.reshape(1,nSx*nSy))
                pfaprxx_temp = np.squeeze(pfaprxx[i].T.reshape(1,nSx*nSy))
                pfapryy_temp = np.squeeze(pfapryy[i].T.reshape(1,nSx*nSy))
                pfaprzz_temp = np.squeeze(pfaprzz[i].T.reshape(1,nSx*nSy))
                pfburxx_temp = np.squeeze(pfburxx[i].T.reshape(1,nSx*nSy))
                pfburyy_temp = np.squeeze(pfburyy[i].T.reshape(1,nSx*nSy))
                pfburzz_temp = np.squeeze(pfburzz[i].T.reshape(1,nSx*nSy))
                Exx[i] = pfeprxx_temp[ind_temp-1].reshape(N,N)
                Eyy[i] = pfepryy_temp[ind_temp-1].reshape(N,N)
                Ezz[i] = pfeprzz_temp[ind_temp-1].reshape(N,N)
                Gxx[i] = pfmurxx_temp[ind_temp-1].reshape(N,N)
                Gyy[i] = pfmuryy_temp[ind_temp-1].reshape(N,N)
                Gzz[i] = pfmurzz_temp[ind_temp-1].reshape(N,N)
                Axx[i] = pfaprxx_temp[ind_temp-1].reshape(N,N)
                Ayy[i] = pfapryy_temp[ind_temp-1].reshape(N,N)
                Azz[i] = pfaprzz_temp[ind_temp-1].reshape(N,N)
                Bxx[i] = pfburxx_temp[ind_temp-1].reshape(N,N)
                Byy[i] = pfburyy_temp[ind_temp-1].reshape(N,N)
                Bzz[i] = pfburzz_temp[ind_temp-1].reshape(N,N)
        
            # Toeplitz (vacuum)
            mx2 = np.arange(1,nFx+1,1).reshape(1,nFx)
            my2 = np.arange(1,nFy+1,1).reshape(1,nFy)
            
            kxf0 = kx0 + (mx2.T-(nx+1))*(2*pi/tx)
            kyf0 = ky0 + (my2-(ny+1))*(2*pi/ty)
            kzf0 = k0**2 - kxf0**2 - kyf0**2
            kzf0 = np.sqrt(kzf0.astype(complex))
            Kx0 = np.tile(kxf0/k0,(1,nFy))
            Kx0 = np.diag(np.squeeze(Kx0.reshape(1,nFx*nFy)))
            Ky0 = np.tile(kyf0/k0,(nFx,1))
            Ky0 = np.diag(np.squeeze(Ky0.reshape(1,nFx*nFy)))
            temp0_11 = ((np.dot(kxf0,kyf0))/kzf0)
            temp0_12 = ((kzf0**2 + np.tile(kxf0**2,(1,nFy)))/kzf0)
            temp0_21 = -((kzf0**2 + np.tile(kyf0**2,(nFx,1)))/kzf0)
            temp0_22 = -temp0_11
            K0_11 = np.diag(np.squeeze(temp0_11.reshape(1,nFx*nFy)))
            K0_12 = np.diag(np.squeeze(temp0_12.reshape(1,nFx*nFy)))
            K0_21 = np.diag(np.squeeze(temp0_21.reshape(1,nFx*nFy)))
            K0_22 = np.diag(np.squeeze(temp0_22.reshape(1,nFx*nFy)))
            K0 = np.block([[K0_11,K0_12],[K0_21,K0_22]])
            
            # Toeplitz (incident)
            kxf_inc = kx_inc + (mx2.T-(nx+1))*(2*pi/tx)
            kyf_inc = ky_inc + (my2-(ny+1))*(2*pi/ty)
            kzf_inc = k_inc**2 - kxf_inc**2 - kyf_inc**2
            kzf_inc = np.sqrt(kzf_inc.astype(complex))
            temp_inc_11 = ((np.dot(kxf_inc,kyf_inc))/kzf_inc)
            temp_inc_12 = ((kzf_inc**2 + np.tile(kxf_inc**2,(1,nFy)))/kzf_inc)
            temp_inc_21 = -((kzf_inc**2 + np.tile(kyf_inc**2,(nFx,1)))/kzf_inc)
            temp_inc_22 = -temp_inc_11
            K_inc_11 = np.diag(np.squeeze(temp_inc_11.reshape(1,nFx*nFy)))
            K_inc_12 = np.diag(np.squeeze(temp_inc_12.reshape(1,nFx*nFy)))
            K_inc_21 = np.diag(np.squeeze(temp_inc_21.reshape(1,nFx*nFy)))
            K_inc_22 = np.diag(np.squeeze(temp_inc_22.reshape(1,nFx*nFy)))
            K_inc = np.block([[K_inc_11,K_inc_12],[K_inc_21,K_inc_22]])
            
            # Toeplitz (reflection)
            kxf_ref = kx_ref + (mx2.T-(nx+1))*(2*pi/tx)
            kyf_ref = ky_ref + (my2-(ny+1))*(2*pi/ty)
            kzf_ref = k_ref**2 - kxf_ref**2 - kyf_ref**2
            kzf_ref = np.sqrt(kzf_ref.astype(complex))
            temp_ref_11 = ((np.dot(kxf_ref,kyf_ref))/kzf_ref)
            temp_ref_12 = ((kzf_ref**2 + np.tile(kxf_ref**2,(1,nFy)))/kzf_ref)
            temp_ref_21 = -((kzf_ref**2 + np.tile(kyf_ref**2,(nFx,1)))/kzf_ref)
            temp_ref_22 = -temp_ref_11
            K_ref_11 = np.diag(np.squeeze(temp_ref_11.reshape(1,nFx*nFy)))
            K_ref_12 = np.diag(np.squeeze(temp_ref_12.reshape(1,nFx*nFy)))
            K_ref_21 = np.diag(np.squeeze(temp_ref_21.reshape(1,nFx*nFy)))
            K_ref_22 = np.diag(np.squeeze(temp_ref_22.reshape(1,nFx*nFy)))
            K_ref = np.block([[K_ref_11,K_ref_12],[K_ref_21,K_ref_22]])
            
            # Toeplitz (transmission)
            kxf_tra = kx_tra + (mx2.T-(nx+1))*(2*pi/tx)
            kyf_tra = ky_tra + (my2-(ny+1))*(2*pi/ty)
            kzf_tra = k_tra**2 - kxf_tra**2 - kyf_tra**2
            kzf_tra = np.sqrt(kzf_tra.astype(complex))
            temp_tra_11 = ((np.dot(kxf_tra,kyf_tra))/kzf_tra)
            temp_tra_12 = ((kzf_tra**2 + np.tile(kxf_tra**2,(1,nFy)))/kzf_tra)
            temp_tra_21 = -((kzf_tra**2 + np.tile(kyf_tra**2,(nFx,1)))/kzf_tra)
            temp_tra_22 = -temp_tra_11
            K_tra_11 = np.diag(np.squeeze(temp_tra_11.reshape(1,nFx*nFy)))
            K_tra_12 = np.diag(np.squeeze(temp_tra_12.reshape(1,nFx*nFy)))
            K_tra_21 = np.diag(np.squeeze(temp_tra_21.reshape(1,nFx*nFy)))
            K_tra_22 = np.diag(np.squeeze(temp_tra_22.reshape(1,nFx*nFy)))
            K_tra = np.block([[K_tra_11,K_tra_12],[K_tra_21,K_tra_22]])
            
            if N_swp == 1:
                self.pbar.setValue(10)
            
            # Block S-matrix
            Wh = np.eye(2*N)
            Vh = K0/(w0*mu0)
            inv_Vh = np.linalg.inv(Vh)
            
            sTa = [[]]*Nlay
            sRa = [[]]*Nlay
            sTb = [[]]*Nlay
            sRb = [[]]*Nlay
            
            sCa = [[]]*Nlay
            sCb = [[]]*Nlay
            
            pevalue = [[]]*Nlay
            mevalue = [[]]*Nlay
            
            pfEy = [[]]*Nlay
            pfEx = [[]]*Nlay
            pfEz = [[]]*Nlay
            pfHy = [[]]*Nlay
            pfHx = [[]]*Nlay
            pfHz = [[]]*Nlay
            mfEy = [[]]*Nlay
            mfEx = [[]]*Nlay
            mfEz = [[]]*Nlay
            mfHy = [[]]*Nlay
            mfHx = [[]]*Nlay
            mfHz = [[]]*Nlay
            
            # Input media
            Vh_inc = K_inc/(w0*mu0)
            Vh_ref = -K_ref/(w0*mu0)
            inv_Vh_ref = np.linalg.inv(Vh_ref)
            sTa_in = np.linalg.solve((Wh-np.dot(inv_Vh_ref,Vh)),(Wh-np.dot(inv_Vh_ref,Vh_inc)))
            sRa_in = np.linalg.solve(-(Wh-np.dot(inv_Vh,Vh_ref)),(Wh-np.dot(inv_Vh,Vh_inc)))
            sTb_in = 2*np.linalg.inv(Wh-np.dot(inv_Vh,Vh_ref))
            sRb_in = np.linalg.solve(-(Wh-np.dot(inv_Vh_ref,Vh)),(Wh+np.dot(inv_Vh_ref,Vh)))
            
            # Output media
            Vh_tra = K_tra/(w0*mu0)
            inv_Vh_tra = np.linalg.inv(Vh_tra)
            sTa_out = 2*np.linalg.inv(Wh+np.dot(inv_Vh,Vh_tra))
            sRa_out = np.linalg.solve(-(Wh+np.dot(inv_Vh_tra,Vh)),(Wh-np.dot(inv_Vh_tra,Vh)))
            sTb_out = np.linalg.solve((Wh+np.dot(inv_Vh_tra,Vh)),(Wh+np.dot(inv_Vh_tra,Vh_tra)))
            sRb_out = np.linalg.solve(-(Wh+np.dot(inv_Vh,Vh_tra)),(Wh-np.dot(inv_Vh,Vh_tra)))
            
            # Grating
            for i in range(Nlay):
                inv_Ezz = np.linalg.inv(Ezz[i]);
                inv_Gzz = np.linalg.inv(Gzz[i]);
                
                SA = np.block([[np.dot(np.dot(Ky0,inv_Ezz),Kx0), Gxx[i] - np.dot(np.dot(Ky0,inv_Ezz),Ky0)],[-Gyy[i] + np.dot(np.dot(Kx0,inv_Ezz),Kx0), np.dot(np.dot(-Kx0,inv_Ezz),Ky0)]])
                SB = np.block([[np.dot(np.dot(Ky0,inv_Gzz),Kx0), Exx[i] - np.dot(np.dot(Ky0,inv_Gzz),Ky0)],[-Eyy[i] + np.dot(np.dot(Kx0,inv_Gzz),Kx0), np.dot(np.dot(-Kx0,inv_Gzz),Ky0)]])
                
                St11 = np.dot(np.dot(np.dot(Ky0,inv_Ezz),Kx0),np.dot(np.dot(Ky0,inv_Gzz),Kx0)) + np.dot((Gxx[i] - np.dot(np.dot(Ky0,inv_Ezz),Ky0)),(-Eyy[i] + np.dot(np.dot(Kx0,inv_Gzz),Kx0)))
                St12 = np.dot(np.dot(np.dot(Ky0,inv_Ezz),Kx0),(Exx[i]-np.dot(np.dot(Ky0,inv_Gzz),Ky0))) + np.dot((Gxx[i] - np.dot(np.dot(Ky0,inv_Ezz),Ky0)),-np.dot(np.dot(Kx0,inv_Gzz),Ky0))
                St21 = np.dot((-Gyy[i] + np.dot(np.dot(Kx0,inv_Ezz),Kx0)),np.dot(np.dot(Ky0,inv_Gzz),Kx0)) + np.dot(-np.dot(np.dot(Kx0,inv_Ezz),Ky0),(-Eyy[i] + np.dot(np.dot(Kx0,inv_Gzz),Kx0)))
                St22 = np.dot((-Gyy[i] + np.dot(np.dot(Kx0,inv_Ezz),Kx0)),(Exx[i] - np.dot(np.dot(Ky0,inv_Gzz),Ky0))) + np.dot(-np.dot(np.dot(Kx0,inv_Ezz),Ky0),-np.dot(np.dot(Kx0,inv_Gzz),Ky0))
                
                St = np.block([[St11, St12],[St21, St22]])*(k0**2)
                
                eig_val, W = splinalg.eig(St)
                
                for ii in range(2*N):
                    eig_val[ii] = eig_val[ii]**0.5
                    if eig_val[ii].real > 0:
                        eig_val[ii] = -eig_val[ii]
            
                pevalue[i] = eig_val
                mevalue[i] = -eig_val
                pW = W
                mW = W
                
                pQ = np.diag(pevalue[i])
                mQ = np.diag(mevalue[i])
                pV = np.dot(np.linalg.inv(SA),np.dot(pW,pQ/k0))
                mV = np.dot(np.linalg.inv(SA),np.dot(mW,mQ/k0))
                
                pfEy[i] = pW[:N,:]
                pfEx[i] = pW[N:,:]
                pfHy[i] = pV[:N,:]
                pfHx[i] = pV[N:,:]
                
                pfEz[i] = np.dot(inv_Ezz,(1j*np.dot(Ky0,pfHx[i])-1j*np.dot(Kx0,pfHy[i])))
                pfHz[i] = np.dot(inv_Gzz,(1j*np.dot(Ky0,pfEx[i])-1j*np.dot(Kx0,pfEy[i])))
                
                pfHy[i] = (1j/eta0)*pfHy[i]
                pfHx[i] = (1j/eta0)*pfHx[i]
                pfHz[i] = (1j/eta0)*pfHz[i]
                
                mfEy[i] = mW[:N,:]
                mfEx[i] = mW[N:,:]
                mfHy[i] = mV[:N,:]
                mfHx[i] = mV[N:,:]
                
                mfEz[i] = np.dot(inv_Ezz,(1j*np.dot(Ky0,mfHx[i])-1j*np.dot(Kx0,mfHy[i])))
                mfHz[i] = np.dot(inv_Gzz,(1j*np.dot(Ky0,mfEx[i])-1j*np.dot(Kx0,mfEy[i])))
                
                mfHy[i] = (1j/eta0)*mfHy[i]
                mfHx[i] = (1j/eta0)*mfHx[i]
                mfHz[i] = (1j/eta0)*mfHz[i]
                
                zm = 0
                zp = df['laythick_%d'%i]*1e-9
                
                p_temp = np.tile(pevalue[i].reshape(1,2*N),(2*N,1))
                m_temp = np.tile(mevalue[i].reshape(1,2*N),(2*N,1))
                
                Wp_zp = pW*np.exp(p_temp*(zp-zm))
                Wm_zp = mW*np.exp(m_temp*(zp-zp))
                Vp_zp = 1j/eta0*pV*np.exp(p_temp*(zp-zm))
                Vm_zp = 1j/eta0*mV*np.exp(m_temp*(zp-zp))
                
                Wp_zm = pW*np.exp(p_temp*(zm-zm))
                Wm_zm = mW*np.exp(m_temp*(zm-zp))
                Vp_zm = 1j/eta0*pV*np.exp(p_temp*(zm-zm))
                Vm_zm = 1j/eta0*mV*np.exp(m_temp*(zm-zp))
                
                U = np.eye(2*N)
                O = np.zeros((2*N,2*N))
                
                Da = np.block([[2*U],[O]])
                Db = np.block([[O],[2*U]])
                
                temp = np.block([[np.dot(Wh,Wp_zm)+np.dot(inv_Vh,Vp_zm), np.dot(Wh,Wm_zm)+np.dot(inv_Vh,Vm_zm)],[np.dot(Wh,Wp_zp)-np.dot(inv_Vh,Vp_zp), np.dot(Wh,Wm_zp)-np.dot(inv_Vh,Vm_zp)]])
                inv_temp = np.linalg.inv(temp)
                
                sCa[i] = np.dot(inv_temp,Da)
                sCb[i] = np.dot(inv_temp,Db)
                
                sCa_temp = sCa[i]
                sCb_temp = sCb[i]
                
                Cap = sCa_temp[:2*N,:]
                Cam = sCa_temp[2*N:,:]
                Cbp = sCb_temp[:2*N,:]
                Cbm = sCb_temp[2*N:,:]
                
                sTa[i] = np.dot(Wh,(np.dot(Wp_zp,Cap)+np.dot(Wm_zp,Cam)))
                sRa[i] = np.dot(Wh,(np.dot(Wp_zm,Cap)+np.dot(Wm_zm,Cam)-Wh))
                sTb[i] = np.dot(Wh,(np.dot(Wp_zm,Cbp)+np.dot(Wm_zm,Cbm)))
                sRb[i] = np.dot(Wh,(np.dot(Wp_zp,Cbp)+np.dot(Wm_zp,Cbm)-Wh))    # check
            
            # Total S-matrix
            def Redheffer_RT(T1a, R1a, T1b, R1b, T2a, R2a, T2b, R2b):
                inv_1b2a = np.linalg.inv(np.eye(len(T1a),len(T1a))-np.dot(R1b,R2a))
                inv_2a1b = np.linalg.inv(np.eye(len(T1a),len(T1a))-np.dot(R2a,R1b))
                Ta = np.dot(np.dot(T2a,inv_1b2a),T1a)
                Ra = R1a + np.dot(np.dot(np.dot(T1b,inv_2a1b),R2a),T1a)
                Tb = np.dot(np.dot(T1b,inv_2a1b),T2b)
                Rb = R2b + np.dot(np.dot(np.dot(T2a,inv_1b2a),R1b),T2b)
                return Ta, Ra, Tb, Rb
            
            def Redheffer_C(T1a, R1a, T1b, R1b, T2a, R2a, T2b, R2b, C1a, C1b, C2a, C2b):
                inv_1b2a = np.linalg.inv(np.eye(len(T1a),len(T1a))-np.dot(R1b,R2a))
                inv_2a1b = np.linalg.inv(np.eye(len(T1a),len(T1a))-np.dot(R2a,R1b))
                laynt = len(C1a)
                tCa = [[]]*(laynt+1)
                tCb = [[]]*(laynt+1)
                for m in range(laynt+1):
                    if m < laynt:
                        tCa[m] = C1a[m] + np.dot(np.dot(np.dot(C1b[m],inv_2a1b),R2a),T1a)
                        tCb[m] =          np.dot(np.dot(C1b[m],inv_2a1b),T2b)
                    else:
                        tCa[m] =       np.dot(np.dot(C2a,inv_1b2a),T1a)
                        tCb[m] = C2b + np.dot(np.dot(np.dot(C2a,inv_1b2a),R1b),T2b)
                return tCa, tCb
        
            def Redheffer_C_in(T1a, R1a, T1b, R1b, T2a, R2a, T2b, R2b, Ca_prev, Cb_prev):
                inv_1b2a = np.linalg.inv(np.eye(len(T1a),len(T1a))-np.dot(R1b,R2a))
                laynt = len(Ca_prev)
                tCa = [[]]*laynt
                tCb = [[]]*laynt
                for m in range(laynt):
                    tCa[m] =              np.dot(np.dot(Ca_prev[m],inv_1b2a),T1a)
                    tCb[m] = Cb_prev[m] + np.dot(np.dot(np.dot(Ca_prev[m],inv_1b2a),R1b),T2b)
                return tCa, tCb
        
            def Redheffer_C_out(T1a, R1a, T1b, R1b, T2a, R2a, T2b, R2b, Ca_prev, Cb_prev):
                inv_2a1b = np.linalg.inv(np.eye(len(T1a),len(T1a))-np.dot(R2a,R1b))
                laynt = len(Ca_prev)
                tCa = [[]]*laynt
                tCb = [[]]*laynt
                for m in range(laynt):
                    tCa[m] = Ca_prev[m] + np.dot(np.dot(np.dot(Cb_prev[m],inv_2a1b),R2a),T1a)
                    tCb[m] =              np.dot(np.dot(Cb_prev[m],inv_2a1b),T2b)
                return tCa, tCb
            
            if N_swp == 1:
                self.pbar.setValue(30)
        
            TTa = sTa[0]
            RRa = sRa[0]
            TTb = sTb[0]
            RRb = sRb[0]
            CCa = [sCa[0]]
            CCb = [sCb[0]]
        
            if Nlay > 1:
                for i in range(1,Nlay):
                    Ta_temp = TTa
                    Ra_temp = RRa
                    Tb_temp = TTb
                    Rb_temp = RRb
                    TTa, RRa, TTb, RRb = Redheffer_RT(TTa, RRa, TTb, RRb, sTa[i], sRa[i], sTb[i], sRb[i])
                    CCa, CCb = Redheffer_C(Ta_temp, Ra_temp, Tb_temp, Rb_temp, sTa[i], sRa[i], sTb[i], sRb[i], CCa, CCb, sCa[i], sCb[i])
        
            Ta_temp, Ra_temp, Tb_temp, Rb_temp = Redheffer_RT(sTa_in, sRa_in, sTb_in, sRb_in, TTa, RRa, TTb, RRb)
            Ca_temp, Cb_temp = Redheffer_C_in(sTa_in, sRa_in, sTb_in, sRb_in, TTa, RRa, TTb, RRb, CCa, CCb)
            Ta, Ra, Tb, Rb = Redheffer_RT(Ta_temp, Ra_temp, Tb_temp, Rb_temp, sTa_out, sRa_out, sTb_out, sRb_out)
            Ca, Cb = Redheffer_C_out(Ta_temp, Ra_temp, Tb_temp, Rb_temp, sTa_out, sRa_out, sTb_out, sRb_out, Ca_temp, Cb_temp)
            
            if N_swp == 1:
                self.pbar.setValue(40)
        
            # Field coefficient
            Ux = np.cos(psi)*np.cos(theta)*np.cos(phi) - np.sin(psi)*np.sin(phi)
            Uy = np.cos(psi)*np.cos(theta)*np.sin(phi) + np.sin(psi)*np.cos(phi)
            Uz = -np.cos(psi)*np.sin(theta)
            
            Einc = np.zeros([2*N,1])
            Einc[nx*nFy+ny,0] = Uy
            Einc[N+nx*nFy+ny,0] = Ux
            Hinc = np.dot(Vh_inc,Einc)
            
            Vy = Hinc[nx*nFy+ny,0]
            Vx = Hinc[N+nx*nFy+ny,0]
            Vz = -(kx_inc*Vx + ky_inc*Vy)/kz_inc
            
            ET2_temp = np.dot(Ta,Einc)
            HT2_temp = np.dot(Vh_tra,ET2_temp)
            ET1_temp = np.dot(Ra,Einc)
            HT1_temp = np.dot(Vh_ref,ET1_temp)
            
            C_p = np.zeros([2*N,Nlay], dtype=complex)
            C_n = np.zeros([2*N,Nlay], dtype=complex)
            
            for laynt in range(Nlay):
                C_temp = np.dot(Ca[laynt],Einc)
                C_p[:,laynt] = C_temp[:2*N,0]
                C_n[:,laynt] = C_temp[2*N:,0]
        
            ET1_y = ET1_temp[:N]
            ET1_x = ET1_temp[N:]
            HT1_y = HT1_temp[:N]
            HT1_x = HT1_temp[N:]
            ET2_y = ET2_temp[:N]
            ET2_x = ET2_temp[N:]
            HT2_y = HT2_temp[:N]
            HT2_x = HT2_temp[N:]
            
            ET1y_cof = ET1_y.reshape([nFx,nFy])
            ET1x_cof = ET1_x.reshape([nFx,nFy])
            ET1z_cof = (ET1x_cof*np.tile(kxf_ref,[1,nFy]) + ET1y_cof*np.tile(kyf_ref,[nFx,1]))/kzf_ref
            HT1y_cof = HT1_y.reshape([nFx,nFy])
            HT1x_cof = HT1_x.reshape([nFx,nFy])
            HT1z_cof = (HT1x_cof*np.tile(kxf_ref,[1,nFy]) + HT1y_cof*np.tile(kyf_ref,[nFx,1]))/kzf_ref
            ET2y_cof = ET2_y.reshape([nFx,nFy])
            ET2x_cof = ET2_x.reshape([nFx,nFy])
            ET2z_cof = -(ET2x_cof*np.tile(kxf_tra,[1,nFy]) + ET2y_cof*np.tile(kyf_tra,[nFx,1]))/kzf_tra
            HT2y_cof = HT2_y.reshape([nFx,nFy])
            HT2x_cof = HT2_x.reshape([nFx,nFy])
            HT2z_cof = -(HT2x_cof*np.tile(kxf_tra,[1,nFy]) + HT2y_cof*np.tile(kyf_tra,[nFx,1]))/kzf_tra
            
            DEt1 = (np.conj(ET1x_cof)*ET1x_cof + np.conj(ET1y_cof)*ET1y_cof + np.conj(ET1z_cof)*ET1z_cof)*np.real(kzf_ref)/kz_ref
            DEt2 = (nf/ni)*(np.conj(ET2x_cof)*ET2x_cof + np.conj(ET2y_cof)*ET2y_cof + np.conj(ET2z_cof)*ET2z_cof)*np.real(kzf_tra)/kz_tra
            T = np.real(np.sum(DEt2))
            R = np.real(np.sum(DEt1))
            
            # Data save
            T = np.round(T,4)
            R = np.round(R,4)
            T_Ex = np.round(np.sqrt(nf/ni)*ET2x_cof[nx,ny],4)
            T_Ey = np.round(np.sqrt(nf/ni)*ET2y_cof[nx,ny],4)
            T_Ez = np.round(np.sqrt(nf/ni)*ET2z_cof[nx,ny],4)
            R_Ex = np.round(ET1x_cof[nx,ny],4)
            R_Ey = np.round(ET1y_cof[nx,ny],4)
            R_Ez = np.round(ET1z_cof[nx,ny],4)
            
            df_result.loc[n_swp,'T'] = T
            df_result.loc[n_swp,'R'] = R
            df_result.loc[n_swp,'T_Ex'] = T_Ex
            df_result.loc[n_swp,'T_Ey'] = T_Ey
            df_result.loc[n_swp,'T_Ez'] = T_Ez
            df_result.loc[n_swp,'R_Ex'] = R_Ex
            df_result.loc[n_swp,'R_Ey'] = R_Ey
            df_result.loc[n_swp,'R_Ez'] = R_Ez
            
            def rm_para(x):
                x = x.replace('(','')
                x = x.replace(')','')
                return x
            
            table.item(n_swp,n_col).setText(str(T))
            table.item(n_swp,n_col+1).setText(str(R))
            table.item(n_swp,n_col+2).setText(rm_para(str(T_Ex)))
            table.item(n_swp,n_col+3).setText(rm_para(str(T_Ey)))
            table.item(n_swp,n_col+4).setText(rm_para(str(T_Ez)))
            table.item(n_swp,n_col+5).setText(rm_para(str(R_Ex)))
            table.item(n_swp,n_col+6).setText(rm_para(str(R_Ey)))
            table.item(n_swp,n_col+7).setText(rm_para(str(R_Ez)))
            table.resizeColumnsToContents()
        
            # Field visualization
            if N_swp == 1 and self.rcwa.tabs.currentIndex() == 0:
                laythick = [0]
                for i in range(Nlay):
                    laythick.append(df['laythick_%d'%i]*1e-9)
                
                laythick_c = np.cumsum(laythick)
                height = np.sum(laythick)
                
                xx_x = np.linspace(-tx/2, tx/2, 100)
                xx_x = xx_x.reshape([len(xx_x),1])
                yy_x = np.linspace(0, 0, 1)
                yy_x = yy_x.reshape([1,len(yy_x)])
                
                xx_y = np.linspace(0, 0, 1)
                xx_y = xx_y.reshape([len(xx_y),1])
                yy_y = np.linspace(-ty/2, ty/2, 100)
                yy_y = yy_y.reshape([1,len(yy_y)])
                
                zz = np.linspace(-200e-9, height+300e-9, 300)
                
                rgGn = [[]]*Nlay
                zz1 = zz[zz<=0]
                zz2 = zz[zz>height]
                zzG = [[]]*Nlay
                
                for i in range(Nlay):
                    zzG[i] = zz[np.logical_and(zz>laythick_c[i],zz<=laythick_c[i+1])]
                    rgGn[i] = len(zzG[i])
        
                # input region
                Ey_xyz1_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz1)], dtype=complex)
                Ex_xyz1_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz1)], dtype=complex)
                Ez_xyz1_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz1)], dtype=complex)
                Hy_xyz1_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz1)], dtype=complex)
                Hx_xyz1_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz1)], dtype=complex)
                Hz_xyz1_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz1)], dtype=complex)
                y1_x, x1_x, z1_x = np.meshgrid(yy_x, xx_x, zz1)
                Ey_xyz1_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz1)], dtype=complex)
                Ex_xyz1_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz1)], dtype=complex)
                Ez_xyz1_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz1)], dtype=complex)
                Hy_xyz1_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz1)], dtype=complex)
                Hx_xyz1_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz1)], dtype=complex)
                Hz_xyz1_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz1)], dtype=complex)
                y1_y, x1_y, z1_y = np.meshgrid(yy_y, xx_y, zz1)
                
                for fx in range(nFx):
                    for fy in range(nFy):
                        Ey_xyz1_x = Ey_xyz1_x + ET1y_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_x + kyf_ref[0,fy]*y1_x - kzf_ref[fx,fy]*z1_x))
                        Ex_xyz1_x = Ex_xyz1_x + ET1x_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_x + kyf_ref[0,fy]*y1_x - kzf_ref[fx,fy]*z1_x))
                        Ez_xyz1_x = Ez_xyz1_x + ET1z_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_x + kyf_ref[0,fy]*y1_x - kzf_ref[fx,fy]*z1_x))
                        Hy_xyz1_x = Hy_xyz1_x + HT1y_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_x + kyf_ref[0,fy]*y1_x - kzf_ref[fx,fy]*z1_x))
                        Hx_xyz1_x = Hx_xyz1_x + HT1x_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_x + kyf_ref[0,fy]*y1_x - kzf_ref[fx,fy]*z1_x))
                        Hz_xyz1_x = Hz_xyz1_x + HT1z_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_x + kyf_ref[0,fy]*y1_x - kzf_ref[fx,fy]*z1_x))
                        Ey_xyz1_y = Ey_xyz1_y + ET1y_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_y + kyf_ref[0,fy]*y1_y - kzf_ref[fx,fy]*z1_y))
                        Ex_xyz1_y = Ex_xyz1_y + ET1x_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_y + kyf_ref[0,fy]*y1_y - kzf_ref[fx,fy]*z1_y))
                        Ez_xyz1_y = Ez_xyz1_y + ET1z_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_y + kyf_ref[0,fy]*y1_y - kzf_ref[fx,fy]*z1_y))
                        Hy_xyz1_y = Hy_xyz1_y + HT1y_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_y + kyf_ref[0,fy]*y1_y - kzf_ref[fx,fy]*z1_y))
                        Hx_xyz1_y = Hx_xyz1_y + HT1x_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_y + kyf_ref[0,fy]*y1_y - kzf_ref[fx,fy]*z1_y))
                        Hz_xyz1_y = Hz_xyz1_y + HT1z_cof[fx,fy]*np.exp(1j*(kxf_ref[fx,0]*x1_y + kyf_ref[0,fy]*y1_y - kzf_ref[fx,fy]*z1_y))
        
                Ey_xyz1_x = Ey_xyz1_x + Uy*np.exp(1j*(kx_inc*x1_x + ky_inc*y1_x + kz_inc*z1_x))
                Ex_xyz1_x = Ex_xyz1_x + Ux*np.exp(1j*(kx_inc*x1_x + ky_inc*y1_x + kz_inc*z1_x))
                Ez_xyz1_x = Ez_xyz1_x + Uz*np.exp(1j*(kx_inc*x1_x + ky_inc*y1_x + kz_inc*z1_x))
                Hy_xyz1_x = Hy_xyz1_x + Vy*np.exp(1j*(kx_inc*x1_x + ky_inc*y1_x + kz_inc*z1_x))
                Hx_xyz1_x = Hx_xyz1_x + Vx*np.exp(1j*(kx_inc*x1_x + ky_inc*y1_x + kz_inc*z1_x))
                Hz_xyz1_x = Hz_xyz1_x + Vz*np.exp(1j*(kx_inc*x1_x + ky_inc*y1_x + kz_inc*z1_x))
                Ey_xyz1_y = Ey_xyz1_y + Uy*np.exp(1j*(kx_inc*x1_y + ky_inc*y1_y + kz_inc*z1_y))
                Ex_xyz1_y = Ex_xyz1_y + Ux*np.exp(1j*(kx_inc*x1_y + ky_inc*y1_y + kz_inc*z1_y))
                Ez_xyz1_y = Ez_xyz1_y + Uz*np.exp(1j*(kx_inc*x1_y + ky_inc*y1_y + kz_inc*z1_y))
                Hy_xyz1_y = Hy_xyz1_y + Vy*np.exp(1j*(kx_inc*x1_y + ky_inc*y1_y + kz_inc*z1_y))
                Hx_xyz1_y = Hx_xyz1_y + Vx*np.exp(1j*(kx_inc*x1_y + ky_inc*y1_y + kz_inc*z1_y))
                Hz_xyz1_y = Hz_xyz1_y + Vz*np.exp(1j*(kx_inc*x1_y + ky_inc*y1_y + kz_inc*z1_y))
                
                if N_swp == 1:
                    self.pbar.setValue(60)
                
                # output region xz-plane
                Ey_xyz2_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz2)], dtype=complex)
                Ex_xyz2_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz2)], dtype=complex)
                Ez_xyz2_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz2)], dtype=complex)
                Hy_xyz2_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz2)], dtype=complex)
                Hx_xyz2_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz2)], dtype=complex)
                Hz_xyz2_x = np.zeros([np.size(xx_x),np.size(yy_x),np.size(zz2)], dtype=complex)
                y2_x, x2_x, z2_x = np.meshgrid(yy_x, xx_x, zz2)
                Ey_xyz2_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz2)], dtype=complex)
                Ex_xyz2_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz2)], dtype=complex)
                Ez_xyz2_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz2)], dtype=complex)
                Hy_xyz2_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz2)], dtype=complex)
                Hx_xyz2_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz2)], dtype=complex)
                Hz_xyz2_y = np.zeros([np.size(xx_y),np.size(yy_y),np.size(zz2)], dtype=complex)
                y2_y, x2_y, z2_y = np.meshgrid(yy_y, xx_y, zz2)
                
                for fx in range(nFx):
                    for fy in range(nFy):
                        Ey_xyz2_x = Ey_xyz2_x + ET2y_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_x + kyf_tra[0,fy]*y2_x + kzf_tra[fx,fy]*(z2_x-height)))
                        Ex_xyz2_x = Ex_xyz2_x + ET2x_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_x + kyf_tra[0,fy]*y2_x + kzf_tra[fx,fy]*(z2_x-height)))
                        Ez_xyz2_x = Ez_xyz2_x + ET2z_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_x + kyf_tra[0,fy]*y2_x + kzf_tra[fx,fy]*(z2_x-height)))
                        Hy_xyz2_x = Hy_xyz2_x + HT2y_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_x + kyf_tra[0,fy]*y2_x + kzf_tra[fx,fy]*(z2_x-height)))
                        Hx_xyz2_x = Hx_xyz2_x + HT2x_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_x + kyf_tra[0,fy]*y2_x + kzf_tra[fx,fy]*(z2_x-height)))
                        Hz_xyz2_x = Hz_xyz2_x + HT2z_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_x + kyf_tra[0,fy]*y2_x + kzf_tra[fx,fy]*(z2_x-height)))
                        Ey_xyz2_y = Ey_xyz2_y + ET2y_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_y + kyf_tra[0,fy]*y2_y + kzf_tra[fx,fy]*(z2_y-height)))
                        Ex_xyz2_y = Ex_xyz2_y + ET2x_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_y + kyf_tra[0,fy]*y2_y + kzf_tra[fx,fy]*(z2_y-height)))
                        Ez_xyz2_y = Ez_xyz2_y + ET2z_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_y + kyf_tra[0,fy]*y2_y + kzf_tra[fx,fy]*(z2_y-height)))
                        Hy_xyz2_y = Hy_xyz2_y + HT2y_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_y + kyf_tra[0,fy]*y2_y + kzf_tra[fx,fy]*(z2_y-height)))
                        Hx_xyz2_y = Hx_xyz2_y + HT2x_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_y + kyf_tra[0,fy]*y2_y + kzf_tra[fx,fy]*(z2_y-height)))
                        Hz_xyz2_y = Hz_xyz2_y + HT2z_cof[fx,fy]*np.exp(1j*(kxf_tra[fx,0]*x2_y + kyf_tra[0,fy]*y2_y + kzf_tra[fx,fy]*(z2_y-height)))
                
                if N_swp == 1:
                    self.pbar.setValue(80)
                        
                # grating region
                sG = np.sum(rgGn).astype(int)
                nG = rgGn.copy()
                nG.insert(0,0)
                nG = np.cumsum(nG)
            
                Ey_xyzG_x = np.zeros([np.size(xx_x),np.size(yy_x),sG], dtype=complex)
                Ex_xyzG_x = np.zeros([np.size(xx_x),np.size(yy_x),sG], dtype=complex)
                Ez_xyzG_x = np.zeros([np.size(xx_x),np.size(yy_x),sG], dtype=complex)
                Hy_xyzG_x = np.zeros([np.size(xx_x),np.size(yy_x),sG], dtype=complex)
                Hx_xyzG_x = np.zeros([np.size(xx_x),np.size(yy_x),sG], dtype=complex)
                Hz_xyzG_x = np.zeros([np.size(xx_x),np.size(yy_x),sG], dtype=complex)
                Ey_xyzG_y = np.zeros([np.size(xx_y),np.size(yy_y),sG], dtype=complex)
                Ex_xyzG_y = np.zeros([np.size(xx_y),np.size(yy_y),sG], dtype=complex)
                Ez_xyzG_y = np.zeros([np.size(xx_y),np.size(yy_y),sG], dtype=complex)
                Hy_xyzG_y = np.zeros([np.size(xx_y),np.size(yy_y),sG], dtype=complex)
                Hx_xyzG_y = np.zeros([np.size(xx_y),np.size(yy_y),sG], dtype=complex)
                Hz_xyzG_y = np.zeros([np.size(xx_y),np.size(yy_y),sG], dtype=complex)
                
                X = np.zeros([2*N,2*N]).astype(complex)
                X_inv = np.zeros([2*N,2*N]).astype(complex)
        
                for i in range(Nlay):
                    for znt in range(len(zzG[i])):   
                        for k in range(2*N):
                            X[k,k] = np.exp(pevalue[i][k]*(zzG[i][znt]-laythick_c[i]))
                            X_inv[k,k] = np.exp(mevalue[i][k]*(zzG[i][znt]-laythick_c[i+1]))
                
                        tmp1 = np.dot(X,C_p[:,i])
                        pf_Ex = np.dot(pfEx[i],tmp1)
                        pf_Ey = np.dot(pfEy[i],tmp1)
                        pf_Ez = np.dot(pfEz[i],tmp1)
                        pf_Hx = np.dot(pfHx[i],tmp1)
                        pf_Hy = np.dot(pfHy[i],tmp1)
                        pf_Hz = np.dot(pfHz[i],tmp1)
                        
                        tmp2 = np.dot(X_inv,C_n[:,i])
                        mf_Ex = np.dot(mfEx[i],tmp2)
                        mf_Ey = np.dot(mfEy[i],tmp2)
                        mf_Ez = np.dot(mfEz[i],tmp2)
                        mf_Hx = np.dot(mfHx[i],tmp2)
                        mf_Hy = np.dot(mfHy[i],tmp2)
                        mf_Hz = np.dot(mfHz[i],tmp2)
                
                        for fx in range(nFx):
                            for fy in range(nFy):
                                Ey_xyzG_x[:,:,nG[i]+znt] = Ey_xyzG_x[:,:,nG[i]+znt] +(pf_Ey[fx*nFy+fy] + mf_Ey[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_x + kyf0[0,fy]*yy_x))
                                Ex_xyzG_x[:,:,nG[i]+znt] = Ex_xyzG_x[:,:,nG[i]+znt] +(pf_Ex[fx*nFy+fy] + mf_Ex[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_x + kyf0[0,fy]*yy_x))
                                Ez_xyzG_x[:,:,nG[i]+znt] = Ez_xyzG_x[:,:,nG[i]+znt] +(pf_Ez[fx*nFy+fy] + mf_Ez[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_x + kyf0[0,fy]*yy_x))
                                Hy_xyzG_x[:,:,nG[i]+znt] = Hy_xyzG_x[:,:,nG[i]+znt] +(pf_Hy[fx*nFy+fy] + mf_Hy[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_x + kyf0[0,fy]*yy_x))
                                Hx_xyzG_x[:,:,nG[i]+znt] = Hx_xyzG_x[:,:,nG[i]+znt] +(pf_Hx[fx*nFy+fy] + mf_Hx[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_x + kyf0[0,fy]*yy_x))
                                Hz_xyzG_x[:,:,nG[i]+znt] = Hz_xyzG_x[:,:,nG[i]+znt] +(pf_Hz[fx*nFy+fy] + mf_Hz[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_x + kyf0[0,fy]*yy_x))
                                
                                Ey_xyzG_y[:,:,nG[i]+znt] = Ey_xyzG_y[:,:,nG[i]+znt] +(pf_Ey[fx*nFy+fy] + mf_Ey[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_y + kyf0[0,fy]*yy_y))
                                Ex_xyzG_y[:,:,nG[i]+znt] = Ex_xyzG_y[:,:,nG[i]+znt] +(pf_Ex[fx*nFy+fy] + mf_Ex[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_y + kyf0[0,fy]*yy_y))
                                Ez_xyzG_y[:,:,nG[i]+znt] = Ez_xyzG_y[:,:,nG[i]+znt] +(pf_Ez[fx*nFy+fy] + mf_Ez[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_y + kyf0[0,fy]*yy_y))
                                Hy_xyzG_y[:,:,nG[i]+znt] = Hy_xyzG_y[:,:,nG[i]+znt] +(pf_Hy[fx*nFy+fy] + mf_Hy[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_y + kyf0[0,fy]*yy_y))
                                Hx_xyzG_y[:,:,nG[i]+znt] = Hx_xyzG_y[:,:,nG[i]+znt] +(pf_Hx[fx*nFy+fy] + mf_Hx[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_y + kyf0[0,fy]*yy_y))
                                Hz_xyzG_y[:,:,nG[i]+znt] = Hz_xyzG_y[:,:,nG[i]+znt] +(pf_Hz[fx*nFy+fy] + mf_Hz[fx*nFy+fy])*np.exp(1j*(kxf0[fx,0]*xx_y + kyf0[0,fy]*yy_y))
                
                Ex_xyz_x = np.dstack((Ex_xyz1_x,Ex_xyzG_x,Ex_xyz2_x))
                Ey_xyz_x = np.dstack((Ey_xyz1_x,Ey_xyzG_x,Ey_xyz2_x))
                Ez_xyz_x = np.dstack((Ez_xyz1_x,Ez_xyzG_x,Ez_xyz2_x))
                Hx_xyz_x = np.dstack((Hx_xyz1_x,Hx_xyzG_x,Hx_xyz2_x))
                Hy_xyz_x = np.dstack((Hy_xyz1_x,Hy_xyzG_x,Hy_xyz2_x))
                Hz_xyz_x = np.dstack((Hz_xyz1_x,Hz_xyzG_x,Hz_xyz2_x))
                E_xyz_x = np.sqrt(np.conj(Ex_xyz_x)*Ex_xyz_x + np.conj(Ey_xyz_x)*Ey_xyz_x + np.conj(Ez_xyz_x)*Ez_xyz_x)
                H_xyz_x = np.sqrt(np.conj(Hx_xyz_x)*Hx_xyz_x + np.conj(Hy_xyz_x)*Hy_xyz_x + np.conj(Hz_xyz_x)*Hz_xyz_x)
                Ex_xyz_y = np.dstack((Ex_xyz1_y,Ex_xyzG_y,Ex_xyz2_y))
                Ey_xyz_y = np.dstack((Ey_xyz1_y,Ey_xyzG_y,Ey_xyz2_y))
                Ez_xyz_y = np.dstack((Ez_xyz1_y,Ez_xyzG_y,Ez_xyz2_y))
                Hx_xyz_y = np.dstack((Hx_xyz1_y,Hx_xyzG_y,Hx_xyz2_y))
                Hy_xyz_y = np.dstack((Hy_xyz1_y,Hy_xyzG_y,Hy_xyz2_y))
                Hz_xyz_y = np.dstack((Hz_xyz1_y,Hz_xyzG_y,Hz_xyz2_y))
                E_xyz_y = np.sqrt(np.conj(Ex_xyz_y)*Ex_xyz_y + np.conj(Ey_xyz_y)*Ey_xyz_y + np.conj(Ez_xyz_y)*Ez_xyz_y)
                H_xyz_y = np.sqrt(np.conj(Hx_xyz_y)*Hx_xyz_y + np.conj(Hy_xyz_y)*Hy_xyz_y + np.conj(Hz_xyz_y)*Hz_xyz_y)
                
                self.rcwa.x_xz = np.squeeze(xx_x)
                self.rcwa.y_yz = np.squeeze(yy_y)
                self.rcwa.z = np.squeeze(zz)
                self.rcwa.Ex_xz = np.squeeze(Ex_xyz_x[:,0,:])
                self.rcwa.Ey_xz = np.squeeze(Ey_xyz_x[:,0,:])
                self.rcwa.Ez_xz = np.squeeze(Ez_xyz_x[:,0,:])
                self.rcwa.Hx_xz = np.squeeze(Hx_xyz_x[:,0,:])
                self.rcwa.Hy_xz = np.squeeze(Hy_xyz_x[:,0,:])
                self.rcwa.Hz_xz = np.squeeze(Hz_xyz_x[:,0,:])
                self.rcwa.E_xz = np.squeeze(E_xyz_x[:,0,:])
                self.rcwa.H_xz = np.squeeze(E_xyz_x[:,0,:])
                self.rcwa.Ex_yz = np.squeeze(Ex_xyz_y[0,:,:])
                self.rcwa.Ey_yz = np.squeeze(Ey_xyz_y[0,:,:])
                self.rcwa.Ez_yz = np.squeeze(Ez_xyz_y[0,:,:])
                self.rcwa.Hx_yz = np.squeeze(Hx_xyz_y[0,:,:])
                self.rcwa.Hy_yz = np.squeeze(Hy_xyz_y[0,:,:])
                self.rcwa.Hz_yz = np.squeeze(Hz_xyz_y[0,:,:])
                self.rcwa.E_yz = np.squeeze(E_xyz_y[0,:,:])
                self.rcwa.H_yz = np.squeeze(E_xyz_y[0,:,:])
                
                if N_swp == 1:
                    self.pbar.setValue(90)
                
                color_map1 = 'bwr'
                color_map2 = 'rainbow'
                font = 'Consolas' # ex) 'fontname=font'
                
                def color_limit(field):
                    Max = field.max()
                    Min = field.min()
                    if abs(Max) >= abs(Min):
                        y = abs(Max)
                    else:
                        y = abs(Min)
                    return y
                
                self.rcwa.fig1.clear()
                ax1 = self.rcwa.fig1.add_subplot(111)
                vlim1 = color_limit(np.real(Ex_xyz_x[:,0,:]))
                im1 = ax1.pcolormesh(zz*1e9,xx_x*1e9,np.real(Ex_xyz_x[:,0,:]),cmap=color_map1,vmax=vlim1,vmin=-vlim1)
                ax1.set_xlabel('z (nm)')
                ax1.set_ylabel('x (nm)')
                ax1.set_title('Ex')
                cbar1 = self.rcwa.fig1.colorbar(im1, ax=ax1, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar1.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig1.tight_layout()
                self.rcwa.canvas1.draw()
                
                self.rcwa.fig2.clear()
                ax2 = self.rcwa.fig2.add_subplot(111)
                vlim2 = color_limit(np.real(Ey_xyz_x[:,0,:]))
                im2 = ax2.pcolormesh(zz*1e9,xx_x*1e9,np.real(Ey_xyz_x[:,0,:]),cmap=color_map1,vmax=vlim2,vmin=-vlim2)
                ax2.set_xlabel('z (nm)')
                ax2.set_ylabel('x (nm)')
                ax2.set_title('Ey')
                cbar2 = self.rcwa.fig2.colorbar(im2, ax=ax2, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar2.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig2.tight_layout()
                self.rcwa.canvas2.draw()
                
                self.rcwa.fig3.clear()
                ax3 = self.rcwa.fig3.add_subplot(111)
                im3 = ax3.pcolormesh(zz*1e9,xx_x*1e9,np.abs(E_xyz_x[:,0,:]),cmap=color_map2)
                ax3.set_xlabel('z (nm)')
                ax3.set_ylabel('x (nm)')
                ax3.set_title('|E|')
                cbar3 = self.rcwa.fig3.colorbar(im3, ax=ax3, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar3.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig3.tight_layout()
                self.rcwa.canvas3.draw()
                
                self.rcwa.fig4.clear()
                ax4 = self.rcwa.fig4.add_subplot(111)
                vlim4 = color_limit(np.real(Hx_xyz_x[:,0,:]))
                im4 = ax4.pcolormesh(zz*1e9,xx_x*1e9,np.real(Hx_xyz_x[:,0,:]),cmap=color_map1,vmax=vlim4,vmin=-vlim4)
                ax4.set_xlabel('z (nm)')
                ax4.set_ylabel('x (nm)')
                ax4.set_title('Hx')
                cbar4 = self.rcwa.fig4.colorbar(im4, ax=ax4, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar4.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig4.tight_layout()
                self.rcwa.canvas4.draw()
                
                self.rcwa.fig5.clear()
                ax5 = self.rcwa.fig5.add_subplot(111)
                vlim5 = color_limit(np.real(Hy_xyz_x[:,0,:]))
                im5 = ax5.pcolormesh(zz*1e9,xx_x*1e9,np.real(Hy_xyz_x[:,0,:]),cmap=color_map1,vmax=vlim5,vmin=-vlim5)
                ax5.set_xlabel('z (nm)')
                ax5.set_ylabel('x (nm)')
                ax5.set_title('Hy')
                cbar5 = self.rcwa.fig5.colorbar(im5, ax=ax5, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar5.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig5.tight_layout()
                self.rcwa.canvas5.draw()
                
                self.rcwa.fig6.clear()
                ax6 = self.rcwa.fig6.add_subplot(111)
                im6 = ax6.pcolormesh(zz*1e9,xx_x*1e9,np.abs(H_xyz_x[:,0,:]),cmap=color_map2)
                ax6.set_xlabel('z (nm)')
                ax6.set_ylabel('x (nm)')
                ax6.set_title('|H|')
                cbar6 = self.rcwa.fig6.colorbar(im6, ax=ax6, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar6.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig6.tight_layout()
                self.rcwa.canvas6.draw()
                
                self.rcwa.fig7.clear()
                ax7 = self.rcwa.fig7.add_subplot(1,1,1)
                vlim7 = color_limit(np.real(Ex_xyz_y[0,:,:]))
                im7 = ax7.pcolormesh(zz*1e9,np.squeeze(yy_y)*1e9,np.real(Ex_xyz_y[0,:,:]),cmap=color_map1,vmax=vlim7,vmin=-vlim7)
                ax7.set_xlabel('z (nm)')
                ax7.set_ylabel('y (nm)')
                ax7.set_title('Ex')
                cbar7 = self.rcwa.fig7.colorbar(im7, ax=ax7, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar7.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig7.tight_layout()
                self.rcwa.canvas7.draw()
                
                self.rcwa.fig8.clear()
                ax8 = self.rcwa.fig8.add_subplot(111)
                vlim8 = color_limit(np.real(Ey_xyz_y[0,:,:]))
                im8 = ax8.pcolormesh(zz*1e9,np.squeeze(yy_y)*1e9,np.real(Ey_xyz_y[0,:,:]),cmap=color_map1,vmax=vlim8,vmin=-vlim8)
                ax8.set_xlabel('z (nm)')
                ax8.set_ylabel('y (nm)')
                ax8.set_title('Ey')
                cbar8 = self.rcwa.fig8.colorbar(im8, ax=ax8, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar8.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig8.tight_layout()
                self.rcwa.canvas8.draw()
                
                self.rcwa.fig9.clear()
                ax9 = self.rcwa.fig9.add_subplot(111)
                im9 = ax9.pcolormesh(zz*1e9,np.squeeze(yy_y)*1e9,np.abs(E_xyz_y[0,:,:]),cmap=color_map2)
                ax9.set_xlabel('z (nm)')
                ax9.set_ylabel('y (nm)')
                ax9.set_title('|E|')
                cbar9 = self.rcwa.fig9.colorbar(im9, ax=ax9, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar9.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig9.tight_layout()
                self.rcwa.canvas9.draw()
                
                self.rcwa.fig10.clear()
                ax10 = self.rcwa.fig10.add_subplot(111)
                vlim10 = color_limit(np.real(Hx_xyz_y[0,:,:]))
                im10 = ax10.pcolormesh(zz*1e9,np.squeeze(yy_y)*1e9,np.real(Hx_xyz_y[0,:,:]),cmap=color_map1,vmax=vlim10,vmin=-vlim10)
                ax10.set_xlabel('z (nm)')
                ax10.set_ylabel('y (nm)')
                ax10.set_title('Hx')
                cbar10 = self.rcwa.fig10.colorbar(im10, ax=ax10, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar10.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig10.tight_layout()
                self.rcwa.canvas10.draw()
                
                self.rcwa.fig11.clear()
                ax11 = self.rcwa.fig11.add_subplot(111)
                vlim11 = color_limit(np.real(Hy_xyz_y[0,:,:]))
                im11 = ax11.pcolormesh(zz*1e9,np.squeeze(yy_y)*1e9,np.real(Hy_xyz_y[0,:,:]),cmap=color_map1,vmax=vlim11,vmin=-vlim11)
                ax11.set_xlabel('z (nm)')
                ax11.set_ylabel('y (nm)')
                ax11.set_title('Hy')
                cbar11 = self.rcwa.fig11.colorbar(im11, ax=ax11, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar11.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig11.tight_layout()
                self.rcwa.canvas11.draw()
                
                self.rcwa.fig12.clear()
                ax12 = self.rcwa.fig12.add_subplot(111)
                im12 = ax12.pcolormesh(zz*1e9,np.squeeze(yy_y)*1e9,np.abs(H_xyz_y[0,:,:]),cmap=color_map2)
                ax12.set_xlabel('z (nm)')
                ax12.set_ylabel('y (nm)')
                ax12.set_title('|H|')
                cbar12 = self.rcwa.fig12.colorbar(im12, ax=ax12, format=ticker.ScalarFormatter(useMathText=True),aspect=12)
                cbar12.formatter.set_powerlimits((-2, 2))
                self.rcwa.fig12.tight_layout()
                self.rcwa.canvas12.draw()
                
                self.rcwa.result_op1 = True
                
                if N_swp == 1:
                    self.pbar.setValue(100)
        
        toc = time.time()
        tt = np.round(toc-tic)
        hour = int(tt//3600)
        minute = int((tt%3600)//60)
        second = int(round((tt%3600)%60))
        if hour == 0 and minute == 0:
            elapsed = f'{second} s'
        elif hour == 0:
            elapsed = f'{minute} m  {second} s'
        else:
            elapsed = f'{hour} h  {minute} m  {second} s'
        self.run_time_label.setText(elapsed)
        self.rcwa.result_op2 = True
        self.pbar.setValue(0)
        self.statusMessage3.setText(' Ready ')
        self.Result_table = pd.concat([df_data,df_result], axis=1)
        
        if m_str_exist == None:
            del self.Result_table["type_0"]
            del self.Result_table["laythick_0"]
            del self.Result_table["n_0"]
                
        header = list(self.Result_table)
        n_row = self.Result_table.shape[0]
        n_col = self.Result_table.shape[1]
        for ir in range(n_row):
            for ic in range(n_col):
                temp1 = str(self.Result_table[header[ic]][ir])
                temp2 = temp1.replace('(','')
                temp3 = temp2.replace(')','')
                self.Result_table.loc[ir,header[ic]] = temp3
