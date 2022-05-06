import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Worker(QThread):
    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        # while True:
        #     print("안녕하세요")
        #     self.sleep(1)
        for lil in range(0, 10000):
            print(lil)

    def resume(self):
        self.running = False

    def pause(self):
        self.running = False


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()

        btn1 = QPushButton("resume", self)
        btn1.move(10, 10)
        btn2 = QPushButton("pause", self)
        btn2.move(10, 50)

        # 시그널-슬롯 연결하기
        btn1.clicked.connect(self.pause)
        btn1.clicked.connect(self.resume)
        btn2.clicked.connect(self.pause)

    def resume(self):

        self.worker.start()

    def pause(self):
        self.worker.terminate()
        self.worker.wait()
        self.worker.start()


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
