from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from binary_clock_gui import Ui_MainWindow

import datetime
import sys
import time


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Post_Init_Steps()
        self.While_Loop = False
        return

    def Post_Init_Steps(self):
        self.ui.pushButton_Start.clicked.connect(self.Event_PushButton_Show_Time)
        return

    def Event_PushButton_Show_Time(self):
        if not self.While_Loop:
            self.While_Loop = True
            self.ui.pushButton_Start.setText('Stop')
            while self.While_Loop:
                Date_Time = datetime.datetime.now()
                Date_Str = Date_Time.strftime('%Y-%m-%d %H:%M:%S')
                Binary_Str = "{0:064b}".format(int(Date_Time.timestamp()))
                self.ui.label_Current_Time_Str.setText(Date_Str)
                self.Show_Binary_Clock(Binary_Str)
                QtWidgets.QApplication.processEvents()
                time.sleep(1)
        else:
            self.While_Loop = False
            self.ui.pushButton_Start.setText('Start')
            Date_Str = self.ui.label_Current_Time_Str.text()
            Date_Str = Date_Str + " (STOPPED)"
            self.ui.label_Current_Time_Str.setText(Date_Str)

    def Show_Binary_Clock(self, Binary_Str=None):
        if Binary_Str:
            Binary_Str = Binary_Str[::-1]
            Loop = 1
            Ctr = 1
            for idx, i in enumerate(Binary_Str):
                if i == '1':
                    ss = 'self.ui.label_0%d_0%d.setStyleSheet("background-color: #00FF00;")' % (Loop, Ctr)
                    eval(ss)
                else:
                    ss = 'self.ui.label_0%d_0%d.setStyleSheet("background-color: #000000;")' % (Loop, Ctr)
                    eval(ss)
                if (idx+1) % 8 == 0:
                    Loop += 1
                    Ctr = 1
                else:
                    Ctr += 1

    def closeEvent(self, event):
        self.While_Loop = False
        event.accept()
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
