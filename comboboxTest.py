import time
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from multiprocessing import Process, Queue
import requests
import webbrowser
import multiprocessing


class gui(QWidget):
    thread_signal_1 = pyqtSignal(str)

    def __init__(self):

        super().__init__()
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        void = QLabel()
        void.setMaximumHeight(30)
        self.number = QLabel('품번')
        self.number.setAlignment(Qt.AlignBottom)
        self.number.setStyleSheet("font-size: 15px;"
                                  "font-weight:bold;")
        self.number.setMaximumHeight(50)
        self.qle = QTextEdit(self)
        self.qle.setMaximumSize(100, 25)

        bottom = QLabel()
        texted = QTextEdit()
        texted.setMaximumSize(250, 250)
        empty = QLabel('키워드 메이커', self)
        empty.setAlignment(Qt.AlignCenter)
        empty.setStyleSheet("font-size: 35px;"
                            "font-weight:bold;")

        empty.setMaximumHeight(60)

        price = QLabel('원가/판매가')
        self.calculator = QLabel('')
        self.calculator.setStyleSheet("font-size: 15px;")
        price.setStyleSheet("font-size: 15px;"
                            "font-weight:bold;")
        price.setMaximumHeight(50)
        price.setAlignment(Qt.AlignBottom)
        empty.setMaximumHeight(30)
        self.originalprice = QTextEdit(self)
        self.originalprice.setMaximumSize(120, 25)
        self.originalprice.setStyleSheet("margin-left: 40px;")
        self.originalprice.textChanged.connect(self.calcuchange)
        self.sellprice = QTextEdit(self)
        self.sellprice.setMaximumSize(120, 25)
        self.sellprice.setStyleSheet("margin-right: 40px;")
        self.sellprice.textChanged.connect(self.calcuchange)
        self.linkbutton = QPushButton('LINK', self)
        self.linkbutton.clicked.connect(self.send_signal)
        self.linkbutton.setStyleSheet("margin-top: 30px;")
        self.linkbutton.setMinimumHeight(100)
        copybutton = QPushButton('COPY', self)
        # copybutton.setStyleSheet("margin-top: 30px;")
        copybutton.setMinimumHeight(70)
        grid_layout.addWidget(empty, 0, 0)
        grid_layout.addWidget(void, 1, 0)
        grid_layout.addWidget(texted, 2, 0)
        grid_layout.addWidget(self.number, 3, 0, alignment=Qt.AlignHCenter)
        grid_layout.addWidget(self.qle, 4, 0, alignment=Qt.AlignHCenter)
        grid_layout.addWidget(price, 5, 0, alignment=Qt.AlignHCenter)

        grid_layout.addWidget(self.originalprice, 6, 0,
                              alignment=Qt.AlignLeft)

        grid_layout.addWidget(self.sellprice, 6, 0, alignment=Qt.AlignRight)
        grid_layout.addWidget(self.calculator, 7, 0, alignment=Qt.AlignHCenter)
        grid_layout.addWidget(self.linkbutton, 8, 0)
        grid_layout.addWidget(copybutton, 9, 0)
        grid_layout.addWidget(bottom, 10, 0)
        self.setGeometry(500, 100, 260, 450)

    def send_signal(self):
        self.thread_signal_1.emit('st')

    def calcuchange(self):
        try:
            margin = round(int(self.sellprice.toPlainText())*0.87) - \
                int(self.originalprice.toPlainText())
            self.calculator.setText(str(margin))
        except Exception as e:
            print(e)
            pass


# class urlworker(QObject):

#     def __init__(self, parent=None):
#         super(self.__class__, self).__init__(parent)
#         print(1)

#     def go(self):
#         time.sleep(2)
#         print(2)


class urlworker(QThread):

    any_signal = pyqtSignal(int)

    def __init__(self,  index=0):
        super(urlworker, self).__init__()
        self.index = index

        print(self.index)
        self.is_running = True

    def run(self):

        num = self.index
        t = requests.get(
            'http://mscoop.co.kr/site/estore/mscoop1/index.php?CID=goods_search&cPage=1&pageSize=40&orderby_type=6&FrontPageType=1&srh_keyfield=name&srh_keyword='+str(num)+'').text

        t = t.split('<div class="thumbnailG_70BMA">')
        t = t[1:]
        t = t[-1]

        q = t.split('<a href=')[1].split("'")[1]
        url = 'http://mscoop.co.kr/site/estore/mscoop1/index.php'+q
        webbrowser.open(url)

    def stop(self):
        self.is_running = False
        print('Stopping thread...', self.index)
        self.terminate()


class keywordworker(QThread):

    any_signal = pyqtSignal(int)

    def __init__(self,  index=0):
        super(keywordworker, self).__init__()
        self.index = index

        print(self.index)
        self.is_running = True

    def run(self):
        t = Queue()
        num = self.index
        t = requests.get(
            'http://mscoop.co.kr/site/estore/mscoop1/index.php?CID=goods_search&cPage=1&pageSize=40&orderby_type=6&FrontPageType=1&srh_keyfield=name&srh_keyword='+str(num)+'').text

        t = t.split('<div class="thumbnailG_70BMA">')
        t = t[1:]
        t = t[-1]

        q = t.split('<a href=')[1].split("'")[1]
        url = 'http://mscoop.co.kr/site/estore/mscoop1/index.php'+q
        webbrowser.open(url)

    def stop(self):
        self.is_running = False
        print('Stopping thread...', self.index)
        self.terminate()


class controler(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.gui = gui()

        self._connectSignals()
        self.thread = {}
        self.gui.show()

    def _connectSignals(self):
        self.gui.linkbutton.clicked.connect(self.urlworkerport)

    def urlworkerport(self):
        try:

            if self.thread[1].is_running == True:
                self.thread[1].terminate()
                self.thread[1].wait()

        except:

            pass
        self.thread[1] = urlworker(index=1)

        self.thread[1].start()

    def keywordworkerport(self):
        try:

            if self.thread[1].is_running == True:
                self.thread[1].terminate()
                self.thread[1].wait()

        except:

            pass
        self.thread[1] = urlworker(index=1)

        self.thread[1].start()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    controler = controler(app)

    sys.exit(app.exec_())
