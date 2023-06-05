from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import cv2
import os
import pickle
import random as rnd
import webbrowser
from getWeatherData import *

#옷장!
class Picture_closet(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(1000,1000)
        self.setFixedSize(1000, 1000)
        self.setWindowTitle("너의 코디는")
        cloth_type = ['Outer','Top(long)','Top(short)','Pants','Skirt','Ops']
        for i in range(len(cloth_type)):
            cloth_type[i] = QLabel(cloth_type[i], self)
            cloth_type[i].setFont(QFont('Arial', 20))
            cloth_type[i].move(40 + 170 * i, 30)

        list = ['Outer','Top(long)','Top(short)','Pants','Skirt','Ops']
        listA = [['padding','coat','jacket','zipup'],['tee','mtm','hood','shirt','knit'],['tee','shirt'],['long','short'],['long','short'],['long','short']]
        listB = [['Outer_padding','Outer_coat','Outer_jacket','Outer_zipup'],['Top(long)_tee','Top(long)_mtm','Top(long)_hood','Top(long)_shirt','Top(long)_knit'],['Top(short)_tee','Top(short)_shirt'],['Pants_long','Pants_short'],['Skirt_long','Skirt_short'],['Ops_long','Ops_short']]
        cloth_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        num = 0
        num2 = 0
        for i in range(len(list)):
            for k in range(len(listA[i])):
                cloth_list[num] = []
                cnt = 0
                cnt += len(os.listdir('./{}/{}'.format(list[i],listA[i][k])))
                for t in range(cnt):
                    cloth_list[num].append(QLabel(self))
                    pixmap_rec = QPixmap('{}/{}/{}{}.jpg'.format(list[i],listA[i][k],listB[i][k],t))
                    pixmap_rec = pixmap_rec.scaledToWidth(100)
                    cloth_list[num][t].setPixmap(pixmap_rec)
                    cloth_list[num][t].move(20 + i * 170, 70 + 170 * num2)
                    num2 += 1
                num += 1
            num2 = 0

#아우터
class Picture_Outer_padding(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Outer_padding을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

        def closeEvent(self, event):
            self.deleteLater()


    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('./Outer/padding/Outer_padding{}.jpg'.format(len(os.listdir('./Outer/padding'))), img_color) ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_O_p.close()

class Picture_Outer_coat(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Outer_coat을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Outer/coat/Outer_coat{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Outer/coat'))), img_color)  ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_O_c.close()

class Picture_Outer_jacket(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Outer_jacket을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Outer/jacket/Outer_jacket{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Outer/jacket'))), img_color)  ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_O_j.close()

class Picture_Outer_zipup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Outer_zipup을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Outer/zipup/Outer_zipup{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Outer/zipup'))), img_color) ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_O_z.close()

#긴팔
class Picture_Top_long_tee(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Top(long)_tee을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Top(long)/tee/Top(long)_tee{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(long)/tee'))), img_color)  ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_T_l_t.close()

class Picture_Top_long_mtm(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Top(long)_mtm을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Top(long)/mtm/Top(long)_mtm{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(long)/mtm'))), img_color)  ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_T_l_m.close()

class Picture_Top_long_hood(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Top(long)_hood을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Top(long)/hood/Top(long)_hood{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(long)/hood'))), img_color) ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_T_l_h.close()

class Picture_Top_long_shirt(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Top(long)_shirt을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Top(long)/shirt/Top(long)_shirt{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(long)/shirt'))), img_color) ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_T_l_s.close()

class Picture_Top_long_knit(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Top(long)_knit을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Top(long)/knit/Top(long)_knit{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(long)/knit'))), img_color) ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_T_l_k.close()

#반팔
class Picture_Top_short_tee(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Top(short)_tee을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Top(short)/tee/Top(short)_tee{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(short)/tee'))), img_color) ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_T_s_t.close()

class Picture_Top_short_shirt(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Top(short)_shirt을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Top(short)/shirt/Top(short)_shirt{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(short)/shirt'))), img_color)  ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_T_s_s.close()

#바지
class Picture_Pants_long(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Pants_long을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Pants/long/Pants_long{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Pants/long'))), img_color) ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_P_l.close()

class Picture_Pants_short(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Pants_short을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Pants/short/Pants_short{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Pants/short'))), img_color) ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_P_s.close()

#스커트
class Picture_Skirt_long(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Skirt_long을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Skirt/long/Skirt_long{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Skirt/long'))), img_color) ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_S_l.close()

class Picture_Skirt_short(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Skirt_short을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Skirt/short/Skirt_short{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Skirt/short'))), img_color) ##check
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_S_s.close()

#원피스
class Picture_Ops_long(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Ops_long을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Ops/long/Ops_long{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Ops/long'))), img_color) ##check





        event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_O_l.close()

class Picture_Ops_short(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("너의 코디는")

        ex = QLabel('Ops_short을 드레그해주세요!')

        AddButton = QPushButton("나가기")
        AddButton.clicked.connect(self.EXIT)

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(AddButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/Ops/short/Ops_short{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Ops/short'))), img_color) ##check





        event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def EXIT(self):
        P_O_s.close()

class Option_c(QWidget):
    global P_O_l
    global P_O_s
    global P_S_l
    global P_S_s
    global P_P_l
    global P_P_s
    global P_T_s_s
    global P_T_s_t
    global P_T_l_t
    global P_T_l_m
    global P_T_l_h
    global P_T_l_s
    global P_T_l_k
    global P_O_p
    global P_O_c
    global P_O_j
    global P_O_z
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('너의 코디는')

        # QHBoxLayout 만들기
        self.hbox0 = QHBoxLayout()  # 등록할 옷의 카테고리를 설정해주세요.
        self.hbox1 = QHBoxLayout()  # 아우터, 상의
        self.hbox2 = QHBoxLayout()  # 하의
        self.hbox3 = QHBoxLayout()  # 등록 버튼
        self.hbox4 = QHBoxLayout()  # 알림창(예외상황 발생시 사용 ex)카테고리를 두개 설정했을 경우

        # hbox0 구성
        self.hbox0.addStretch(1)
        self.hbox0.addWidget(QLabel('등록할 옷의 카테고리를 설정해주세요.'))
        self.hbox0.addStretch(1)

        # hbox1 구성
        self.hbox1.addWidget(QLabel('Outer:'))
        self.outer_input = QComboBox()
        self.outer_input.addItem('none')
        self.outer_input.addItem('padding')
        self.outer_input.addItem('coat')
        self.outer_input.addItem('jacket')
        self.outer_input.addItem('zipup')
        self.hbox1.addWidget(self.outer_input)

        self.hbox1.addWidget(QLabel('Top(long):'))
        self.topl_input = QComboBox()
        self.topl_input.addItem('none')
        self.topl_input.addItem('tee')
        self.topl_input.addItem('mtm')
        self.topl_input.addItem('hood')
        self.topl_input.addItem('shirt')
        self.topl_input.addItem('knit')
        self.hbox1.addWidget(self.topl_input)

        self.hbox1.addWidget(QLabel('Top(short):'))
        self.tops_input = QComboBox()
        self.tops_input.addItem('none')
        self.tops_input.addItem('tee')
        self.tops_input.addItem('shirt')
        self.hbox1.addWidget(self.tops_input)

        # hbox2 구성
        self.hbox2.addWidget(QLabel('Pants:'))
        self.pants_input = QComboBox()
        self.pants_input.addItem('none')
        self.pants_input.addItem('long')
        self.pants_input.addItem('short')
        self.hbox2.addWidget(self.pants_input)

        self.hbox2.addWidget(QLabel('Skirt:'))
        self.skirt_input = QComboBox()
        self.skirt_input.addItem('none')
        self.skirt_input.addItem('long')
        self.skirt_input.addItem('short')
        self.hbox2.addWidget(self.skirt_input)

        self.hbox2.addWidget(QLabel('Ops:'))
        self.ops_input = QComboBox()
        self.ops_input.addItem('none')
        self.ops_input.addItem('long')
        self.ops_input.addItem('short')
        self.hbox2.addWidget(self.ops_input)

        # hbox3 구성
        self.addButton = QPushButton("Add Your Cloth!")
        self.addButton.clicked.connect(self.dialog_open)
        self.hbox3.addWidget(self.addButton)

        # hbox4 구성
        self.notifi = QLineEdit()
        self.hbox4.addWidget(self.notifi)


        # QVBoxLayout 만들기
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)

        self.setLayout(self.vbox)



    def dialog_open(self):
        key = [self.outer_input.currentText(), self.topl_input.currentText(),
               self.tops_input.currentText(), self.pants_input.currentText(),
               self.skirt_input.currentText(), self.ops_input.currentText()]
        cnt = 0
        for k in range(len(key)):
            if key[k] == 'none':
                cnt += 1
            else:
                self.cloth_key = key[k]
                self.num = k
        if 0 <= cnt <= 4:
            self.notifi.setText("카테고리를 하나만 설정해주세요.")
        if cnt == 6:
            self.notifi.setText("등록할 옷의 카테고리를 설정해주세요.")
        if cnt == 5:
            self.notifi.clear()
            if self.num == 5:
                if self.cloth_key == "long":
                    P_O_l.show()
                elif self.cloth_key == "short":
                    P_O_s.show()
            elif self.num == 4:
                if self.cloth_key == "long":
                    P_S_l.show()
                elif self.cloth_key == "short":
                    P_S_s.show()
            elif self.num == 3:
                if self.cloth_key == "long":
                    P_P_l.show()
                elif self.cloth_key == "short":
                    P_P_s.show()
            elif self.num == 2:
                if self.cloth_key == "tee":
                    P_T_s_t.show()
                elif self.cloth_key == "shirt":
                    P_T_s_s.show()
            elif self.num == 1:
                if self.cloth_key == "tee":
                    P_T_l_t.show()
                elif self.cloth_key == "mtm":
                    P_T_l_m.show()
                elif self.cloth_key == "hood":
                    P_T_l_h.show()
                elif self.cloth_key == "shirt":
                    P_T_l_s.show()
                else:
                    P_T_l_k.show()
            else:
                if self.cloth_key == "padding":
                    P_O_p.show()
                elif self.cloth_key == "coat":
                    P_O_c.show()
                elif self.cloth_key == "jacket":
                    P_O_j.show()
                else:
                    P_O_z.show()

#사용자가 남자일 때
class CMainWindow_M(QWidget):
    global o
    global P_C

    def __init__(self):
        super().__init__()
        self.dbfilenames = 'user.dat'
        self.user = []
        self.weather = Weather()
        self.initUI()

    def initUI(self):
        # 창 설정
        self.setGeometry(750, 250, 500, 600)
        self.setWindowTitle('너의 코디는')
        self.weather.setArea("정릉제1동")
        self.weather.setJson()

        try:
            now_temp = self.weather.getTemp()  # 오늘의 기온
        except:
            self.weather.setArea("정릉제1동")
            now_temp = self.weather.getTemp()

        # QHBoxLayout 만들기
        self.hbox0 = QHBoxLayout()  # 주소지
        self.hbox1 = QHBoxLayout()  # 날씨 그림 & 온도 표시
        self.hbox2 = QHBoxLayout()  # 추천 이유
        self.hbox3 = QHBoxLayout()  # 추천조합
        self.hbox4 = QHBoxLayout()  # 쇼핑몰 바로가기

        # hbox0 : Area Name
        label_area = QLabel("정릉동", self)
        font_area = label_area.font()
        font_area.setPointSize(15)
        font_area.setBold(True)
        label_area.setFont(font_area)
        self.hbox0.addWidget(label_area)

        # hbox1 : weather PNG
        weather_vbox = QVBoxLayout()
        label_png = QLabel(self)
        # weather = getWeather()
        now_weather = self.weather.getWeather()
        if now_weather == 1:
            pixmap = QPixmap('png/sunny2.png')
        elif now_weather == 3:
            pixmap = QPixmap('png/cloudy.png')
        elif now_weather == 4:
            pixmap = QPixmap('png/cloud-sunny.png')
        if self.weather.isRain() == True:
            pixmap = QPixmap('png/rainy.png')
        pixmap = pixmap.scaledToHeight(150)
        label_png.setPixmap(pixmap)
        weather_vbox.addWidget(label_png)

        label_temp = QLabel("  " + str(now_temp) + '°C')
        temp_font = label_temp.font()
        temp_font.setPointSize(35)
        temp_font.setBold(True)
        label_temp.setFont(temp_font)
        weather_vbox.addWidget(label_temp)

        self.hbox1.addStretch(1)
        self.hbox1.addLayout(weather_vbox)
        self.hbox1.addStretch(1)

        # hbox2 구성
        recommend = {
            5: "바람이 많이 불어 날씨가 춥습니다. 패딩과 코트같이 두꺼운 옷을 입을 필요가 있다고 생각합니다. 추위를 잘 느끼시면 목도리나 장갑같은 아이템을 착용하는 것도 좋다는 생각이 듭니다. 완벽 무장을 하고 나갈 필요가 있습니다:D",
            16: '낮에 따듯하더라도 아침, 저녁으로 쌀쌀하니 얇은 겉옷을 챙기는 게 좋을 것 같습니다. 갑자기 추워진 지금 일교차가 크니 감기 조심하세요!',
            23: '날씨가 선선해지면서 긴팔을 꺼내 입을 날이 되었습니다. 추위를 잘 느끼신다면 기모가 들어간 옷을 입어도 좋을 것 같습니다.',
            27: '날씨가 덥긴 하지만 그리 못 버틸 더위는 아닙니다. 오히려 밤에는 시원할 수 있기 때문에 상의는 반팔, 하의는 긴바지를 추천합니다.',
            100: '습하고 햇빛이 강력해서 서있는 것 만으로도 땀이 나고 숨이 막힐 더위가 예상됩니. 더위 때문에 예민할 수 밖에 없는 날씨에 이 조합을 추천합니다~'}
        for key, val in recommend.items():
            if now_temp <= key:
                Text = val
                break

        msgbox = QTextBrowser(self)
        msgbox.append(Text)
        AddButton = QPushButton("자신의 옷 저장하기")
        Add2Button = QPushButton("자신의 옷장 보기")
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(AddButton)
        self.hbox2.addWidget(msgbox)
        self.hbox2.addWidget(Add2Button)
        self.hbox2.addStretch(1)

        AddButton.clicked.connect(self.new)
        Add2Button.clicked.connect(self.new2)

        # hbox3 구성 : 옷 추천 # 고정되잇는값
        rec_layout1 = QVBoxLayout()
        rec_layout2 = QVBoxLayout()
        rec_layout3 = QVBoxLayout()
        rec_layout1.addWidget(QLabel("추천 조합 1", self))
        rec_layout2.addWidget(QLabel("추천 조합 2", self))
        rec_layout3.addWidget(QLabel("추천 조합 3", self))

        #추천 옷 세트 1
        label_rec1 = []
        if now_temp<= 16:
            #Outer
            label_rec1.append(QLabel(self))
            if now_temp <= 5:
                n = rnd.randint(0, 2)
            else:
                n = rnd.randint(1,2)
            tmp_list = ['coat', 'padding', 'jacket', 'zipup']
            db_cnt = len(os.listdir('./Outer/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Outer/{}/Outer_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[0].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_rec1[0])

            #Top
            label_rec1.append(QLabel(self))
            n = rnd.randint(0, 4)
            tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
            db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n],tmp_list[n],n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[1].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_rec1[1])

            #Pants & Skirt
            label_rec1.append(QLabel(self))
            db_cnt = len(os.listdir('./Pants/long'))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[2].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_rec1[2])
        else:
            if now_temp <= 23:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 4)
                tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
                db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[1])

            elif now_temp <= 27:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[1])

            else:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/short'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/short/Pants_short{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[1])

        # 추천 옷 세트 2
        label_rec1 = []
        if now_temp <= 16:
            # Outer
            label_rec1.append(QLabel(self))
            if now_temp <= 5:
                n = rnd.randint(0, 2)
            else:
                n = rnd.randint(1, 2)
            tmp_list = ['coat', 'padding', 'jacket', 'zipup']
            db_cnt = len(os.listdir('./Outer/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Outer/{}/Outer_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[0].setPixmap(pixmap_rec)
            rec_layout2.addWidget(label_rec1[0])

            # Top
            label_rec1.append(QLabel(self))
            n = rnd.randint(0, 4)
            tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
            db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[1].setPixmap(pixmap_rec)
            rec_layout2.addWidget(label_rec1[1])

            # Pants & Skirt
            label_rec1.append(QLabel(self))
            db_cnt = len(os.listdir('./Pants/long'))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[2].setPixmap(pixmap_rec)
            rec_layout2.addWidget(label_rec1[2])
        else:
            if now_temp <= 23:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 4)
                tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
                db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[1])

            elif now_temp <= 27:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[1])

            else:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/short'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/short/Pants_short{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[1])

        # 추천 옷 세트 3
        label_rec1 = []
        if now_temp <= 16:
            # Outer
            label_rec1.append(QLabel(self))
            if now_temp <= 5:
                n = rnd.randint(0, 2)
            else:
                n = rnd.randint(1, 2)
            tmp_list = ['coat', 'padding', 'jacket', 'zipup']
            db_cnt = len(os.listdir('./Outer/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Outer/{}/Outer_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[0].setPixmap(pixmap_rec)
            rec_layout3.addWidget(label_rec1[0])

            # Top
            label_rec1.append(QLabel(self))
            n = rnd.randint(0, 4)
            tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
            db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[1].setPixmap(pixmap_rec)
            rec_layout3.addWidget(label_rec1[1])

            # Pants & Skirt
            label_rec1.append(QLabel(self))
            db_cnt = len(os.listdir('./Pants/long'))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[2].setPixmap(pixmap_rec)
            rec_layout3.addWidget(label_rec1[2])
        else:
            if now_temp <= 23:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 4)
                tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
                db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[1])

            elif now_temp <= 27:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[1])

            else:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/short'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/short/Pants_short{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[1])

        self.hbox3.addLayout(rec_layout1)
        self.hbox3.addLayout(rec_layout2)
        self.hbox3.addLayout(rec_layout3)

        # hbox4 구성 : url 버튼 만들기

        shmall = QPushButton("쇼핑몰 추천받기", self)
        shmall.clicked.connect(self.sh_url)
        self.hbox4.addWidget(shmall)

        # QVBoxLayout 만들기
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)

        self.setLayout(self.vbox)

    def sh_url(self):
        url1 = 'https://store.musinsa.com/app/?c=y'
        webbrowser.open(url1)

    def new(self):
        o.show()

    def new2(self):
        P_C.show()

    def readDB(self):
        try:
            fH = open('./user.dat', 'rb')
        except FileNotFoundError as e:
            self.user = []
            return
        try:
            self.user = pickle.load(fH)
        except:
            pass
        fH.close()

#사용자가 여자일 때
class CMainWindow_W(QWidget):
    global o
    global P_C

    def __init__(self):
        super().__init__()
        self.dbfilenames = 'user.dat'
        self.user = []
        self.weather = Weather()
        self.initUI()

    def initUI(self):
        # 창 설정
        self.setGeometry(750, 250, 500, 600)
        self.setWindowTitle('너의 코디는')
        self.weather.setArea("정릉제1동")
        self.weather.setJson()

        try:
            now_temp = self.weather.getTemp()  # 오늘의 기온
        except:
            self.weather.setArea("정릉제1동")
            now_temp = self.weather.getTemp()

        # QHBoxLayout 만들기
        self.hbox0 = QHBoxLayout()  # 주소지
        self.hbox1 = QHBoxLayout()  # 날씨 그림 & 온도 표시
        self.hbox2 = QHBoxLayout()  # 추천 이유
        self.hbox3 = QHBoxLayout()  # 추천조합
        self.hbox4 = QHBoxLayout()  # 쇼핑몰 바로가기

        # hbox0 : Area Name
        label_area = QLabel("정릉동", self)
        font_area = label_area.font()
        font_area.setPointSize(15)
        font_area.setBold(True)
        label_area.setFont(font_area)
        self.hbox0.addWidget(label_area)

        # hbox1 : weather PNG
        weather_vbox = QVBoxLayout()
        label_png = QLabel(self)
        # weather = getWeather()
        now_weather = self.weather.getWeather()
        if now_weather == 1:
            pixmap = QPixmap('png/sunny2.png')
        elif now_weather == 3:
            pixmap = QPixmap('png/cloudy.png')
        elif now_weather == 4:
            pixmap = QPixmap('png/cloud-sunny.png')
        if self.weather.isRain() == True:
            pixmap = QPixmap('png/rainy.png')
        pixmap = pixmap.scaledToHeight(150)
        label_png.setPixmap(pixmap)
        weather_vbox.addWidget(label_png)

        label_temp = QLabel("  " + str(now_temp) + '°C')
        temp_font = label_temp.font()
        temp_font.setPointSize(35)
        temp_font.setBold(True)
        label_temp.setFont(temp_font)
        weather_vbox.addWidget(label_temp)

        self.hbox1.addStretch(1)
        self.hbox1.addLayout(weather_vbox)
        self.hbox1.addStretch(1)

        # hbox2 구성
        recommend = {
            5: "바람이 많이 불어 날씨가 춥습니다. 패딩과 코트같이 두꺼운 옷을 입을 필요가 있다고 생각합니다. 추위를 잘 느끼시면 목도리나 장갑같은 아이템을 착용하는 것도 좋다는 생각이 듭니다. 완벽 무장을 하고 나갈 필요가 있습니다:D",
            16: '낮에 따듯하더라도 아침, 저녁으로 쌀쌀하니 얇은 겉옷을 챙기는 게 좋을 것 같습니다. 갑자기 추워진 지금 일교차가 크니 감기 조심하세요!',
            23: '날씨가 선선해지면서 긴팔을 꺼내 입을 날이 되었습니다. 추위를 잘 느끼신다면 기모가 들어간 옷을 입어도 좋을 것 같습니다.',
            27: '날씨가 덥긴 하지만 그리 못 버틸 더위는 아닙니다. 오히려 밤에는 시원할 수 있기 때문에 상의는 반팔, 하의는 긴바지를 추천합니다.',
            100: '습하고 햇빛이 강력해서 서있는 것 만으로도 땀이 나고 숨이 막힐 더위가 예상됩니. 더위 때문에 예민할 수 밖에 없는 날씨에 이 조합을 추천합니다~'}
        for key, val in recommend.items():
            if now_temp <= key:
                Text = val
                break

        msgbox = QTextBrowser(self)
        msgbox.append(Text)
        AddButton = QPushButton("자신의 옷 저장하기")
        Add2Button = QPushButton("자신의 옷장 보기")
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(AddButton)
        self.hbox2.addWidget(msgbox)
        self.hbox2.addWidget(Add2Button)
        self.hbox2.addStretch(1)

        AddButton.clicked.connect(self.new)
        Add2Button.clicked.connect(self.new2)

        # hbox3 구성 : 옷 추천 # 고정되잇는값
        rec_layout1 = QVBoxLayout()
        rec_layout2 = QVBoxLayout()
        rec_layout3 = QVBoxLayout()
        rec_layout1.addWidget(QLabel("추천 조합 1", self))
        rec_layout2.addWidget(QLabel("추천 조합 2", self))
        rec_layout3.addWidget(QLabel("추천 조합 3", self))

        #추천 옷 세트 1
        label_rec1 = []
        if now_temp<= 16:
            #Outer
            label_rec1.append(QLabel(self))
            if now_temp <= 5:
                n = rnd.randint(0, 2)
            else:
                n = rnd.randint(1,2)
            tmp_list = ['coat', 'padding', 'jacket', 'zipup']
            db_cnt = len(os.listdir('./Outer/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Outer/{}/Outer_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[0].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_rec1[0])

            #Top
            label_rec1.append(QLabel(self))
            n = rnd.randint(0, 4)
            tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
            db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n],tmp_list[n],n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[1].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_rec1[1])

            #Pants & Skirt
            label_rec1.append(QLabel(self))
            db_cnt = len(os.listdir('./Pants/long'))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[2].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_rec1[2])
        else:
            if now_temp <= 23:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 4)
                tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
                db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[1])

            elif now_temp <= 27:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[1])

            else:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/short'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/short/Pants_short{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout1.addWidget(label_rec1[1])

        # 추천 옷 세트 2
        label_rec1 = []
        if now_temp <= 16:
            # Outer
            label_rec1.append(QLabel(self))
            if now_temp <= 5:
                n = rnd.randint(0, 2)
            else:
                n = rnd.randint(1, 2)
            tmp_list = ['coat', 'padding', 'jacket', 'zipup']
            db_cnt = len(os.listdir('./Outer/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Outer/{}/Outer_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[0].setPixmap(pixmap_rec)
            rec_layout2.addWidget(label_rec1[0])

            # Top
            label_rec1.append(QLabel(self))
            n = rnd.randint(0, 4)
            tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
            db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[1].setPixmap(pixmap_rec)
            rec_layout2.addWidget(label_rec1[1])

            # Pants & Skirt
            label_rec1.append(QLabel(self))
            db_cnt = len(os.listdir('./Pants/long'))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[2].setPixmap(pixmap_rec)
            rec_layout2.addWidget(label_rec1[2])
        else:
            if now_temp <= 23:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 4)
                tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
                db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[1])

            elif now_temp <= 27:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[1])

            else:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/short'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/short/Pants_short{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout2.addWidget(label_rec1[1])

        # 추천 옷 세트 3
        label_rec1 = []
        if now_temp <= 16:
            # Outer
            label_rec1.append(QLabel(self))
            if now_temp <= 5:
                n = rnd.randint(0, 2)
            else:
                n = rnd.randint(1, 2)
            tmp_list = ['coat', 'padding', 'jacket', 'zipup']
            db_cnt = len(os.listdir('./Outer/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Outer/{}/Outer_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[0].setPixmap(pixmap_rec)
            rec_layout3.addWidget(label_rec1[0])

            # Top
            label_rec1.append(QLabel(self))
            n = rnd.randint(0, 4)
            tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
            db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[1].setPixmap(pixmap_rec)
            rec_layout3.addWidget(label_rec1[1])

            # Pants & Skirt
            label_rec1.append(QLabel(self))
            db_cnt = len(os.listdir('./Pants/long'))
            n_2 = rnd.randint(0, db_cnt - 1)
            pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[2].setPixmap(pixmap_rec)
            rec_layout3.addWidget(label_rec1[2])
        else:
            if now_temp <= 23:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 4)
                tmp_list = ['hood', 'knit', 'mtm', 'shirt', 'tee']
                db_cnt = len(os.listdir('./Top(long)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(long)/{}/Top(long)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[1])

            elif now_temp <= 27:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/long'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/long/Pants_long{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[1])

            else:
                # Top
                label_rec1.append(QLabel(self))
                n = rnd.randint(0, 1)
                tmp_list = ['shirt', 'tee']
                db_cnt = len(os.listdir('./Top(short)/{}'.format(tmp_list[n])))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Top(short)/{}/Top(short)_{}{}.jpg'.format(tmp_list[n], tmp_list[n], n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[0].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[0])

                # Pants & Skirt
                label_rec1.append(QLabel(self))
                db_cnt = len(os.listdir('./Pants/short'))
                n_2 = rnd.randint(0, db_cnt - 1)
                pixmap_rec = QPixmap('./Pants/short/Pants_short{}.jpg'.format(n_2))
                pixmap_rec = pixmap_rec.scaledToWidth(100)
                label_rec1[1].setPixmap(pixmap_rec)
                rec_layout3.addWidget(label_rec1[1])

        self.hbox3.addLayout(rec_layout1)
        self.hbox3.addLayout(rec_layout2)
        self.hbox3.addLayout(rec_layout3)

        # hbox4 구성 : url 버튼 만들기

        shmall = QPushButton("쇼핑몰 추천받기", self)
        shmall.clicked.connect(self.sh_url)
        self.hbox4.addWidget(shmall)

        # QVBoxLayout 만들기
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)

        self.setLayout(self.vbox)

    def sh_url(self):
        url1 = 'https://store.musinsa.com/app/?c=y'
        webbrowser.open(url1)

    def new(self):
        o.show()

    def new2(self):
        P_C.show()

    def readDB(self):
        try:
            fH = open('./user.dat', 'rb')
        except FileNotFoundError as e:
            self.user = []
            return
        try:
            self.user = pickle.load(fH)
        except:
            pass
        fH.close()

####
class Mainwindow(QWidget):
    global Cmain_M
    global Cmain_W
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'user.dat'
        self.user = []
        self.readDB()


    def initUI(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('너의 코디는')
        self.show()
        # QHBoxLayout 만들기
        self.hbox0 = QHBoxLayout()  # '너의 코디는'
        self.hbox1 = QHBoxLayout()  # 사용자 이름
        self.hbox2 = QHBoxLayout()  # 비밀번호
        self.hbox3 = QHBoxLayout()  # 지역명
        self.hbox4 = QHBoxLayout()  # 성별
        self.hbox5 = QHBoxLayout()  # go 버

        # hbox0 구성
        label1 = QLabel('너의 코디는', self)
        label1.setAlignment(Qt.AlignCenter)

        font1 = label1.font()
        font1.setPointSize(20)
        label1.setFont(font1)

        self.hbox0.addWidget(label1)

        # hbox1 구성
        self.hbox1.addWidget(QLabel('사용자 이름 : '))
        self.username_input = QLineEdit()
        self.hbox1.addWidget(self.username_input)

        # hbox2 구성
        self.hbox2.addWidget(QLabel('    비밀번호 : '))
        self.usercode_input = QLineEdit()
        self.usercode_input.setEchoMode(QLineEdit.Password)
        self.hbox2.addWidget(self.usercode_input)

        # hbox4 구성
        self.man = QRadioButton('남자')
        self.woman = QRadioButton('여자')

        self.hbox4.addWidget(QLabel('성별:'))
        self.hbox4.addWidget(self.man)
        self.hbox4.addWidget(self.woman)

        # hbox5 구성
        self.goButton = QPushButton("GO")
        self.hbox5.addWidget(self.goButton)
        self.goButton.clicked.connect(self.mb)

        # QVBoxLayout 만들기
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)

        self.setLayout(self.vbox)


    def closeEvent(self, event):
        self.writeDB()

    def readDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.user = []
            return
        try:
            self.user = pickle.load(fH)
        except:
            pass
        fH.close()

    def writeDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.user, fH)
        fH.close()

    def mb(self, event):
        iusname = str(self.username_input)
        iuscode = str(self.usercode_input)

        if self.username_input.text() == '' or iusname.isdigit() == True:
            reply = QMessageBox.question(self, '알림창', '사용자 이름을 바르게 입력하세요.',
                                         QMessageBox.Yes)
        if self.usercode_input.text() == '':
            reply = QMessageBox.question(self, '알림창', '비밀번호를 입력하세요.',
                                         QMessageBox.Yes)

        else:
            self.dialog_open()

    def dialog_open(self):
        if self.man.isChecked():
            name = self.username_input.text()
            pw = self.usercode_input.text()
            sex = 'man'

            for u in self.user:
                if u['Name'] == name and u['Pw'] == pw:
                    name = u['Name']
                    pw = u['Pw']
                    sex = u['Sex']

            else:
                record = dict(Name=name, Pw=pw, Sex=sex)
                self.user += [record]



            Cmain_M.show()
            Main.close()

        if self.woman.isChecked():
            name = self.username_input.text()
            pw = self.usercode_input.text()
            sex = 'woman'

            for u in self.user:
                if u['Name'] == name and u['Pw'] == pw:
                    name = u['Name']
                    pw = u['Pw']
                    sex = u['Sex']

            else:
                record = dict(Name=name, Pw=pw, Sex=sex)
                self.user += [record]

            Cmain_W.show()
            Main.close()

#####
app = QApplication(sys.argv)
Cmain_M = CMainWindow_M()
Cmain_W = CMainWindow_W()
Main = Mainwindow()
o = Option_c()
P_O_p = Picture_Outer_padding()
P_O_c = Picture_Outer_coat()
P_O_j = Picture_Outer_jacket()
P_O_z = Picture_Outer_zipup()
P_T_l_t = Picture_Top_long_tee()
P_T_l_m = Picture_Top_long_mtm()
P_T_l_h = Picture_Top_long_hood()
P_T_l_s = Picture_Top_long_shirt()
P_T_l_k = Picture_Top_long_knit()
P_T_s_t = Picture_Top_short_tee()
P_T_s_s = Picture_Top_short_shirt()
P_P_l = Picture_Pants_long()
P_P_s = Picture_Pants_short()
P_S_l = Picture_Skirt_long()
P_S_s = Picture_Skirt_short()
P_O_l = Picture_Ops_long()
P_O_s = Picture_Ops_short()
P_C = Picture_closet()
sys.exit(app.exec_())