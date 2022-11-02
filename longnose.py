import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import time
from PyQt5.QtCore import QThread


class Worker(QObject):
    # object는 보통 클레스라고 생각하면 된다
    # 여기서는 스레드에 돌릴 알고리즘을 만드는 용도로 사용했다
    sig_numbers = pyqtSignal(int)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

    @pyqtSlot()
    def startWork(self):
        _cnt = 0
        for _cnt in range(1, 10):
            _cnt += 1
            self.sig_numbers.emit(_cnt)
            print(_cnt)
            time.sleep(1)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.button_start = QPushButton('Start', self)
        self.button_cancel = QPushButton('Cancel', self)
        self.label_status = QLabel('status!!', self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button_start)
        layout.addWidget(self.button_cancel)
        layout.addWidget(self.label_status)

        self.setFixedSize(400, 200)

    # @pyqtSlot(int)
    def updateStatus(self, status):
        self.label_status.setText('{}'.format(status))


class Example(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.gui = Window()
        self.worker = Worker()               # 백그라운드에서 돌아갈 인스턴스 소환
        self.worker_thread = QThread()       # 따로 돌아갈 thread를 하나 생성
        self.worker.moveToThread(self.worker_thread)  # worker를 만들어둔 쓰레드에 넣어줍니다
        self.worker_thread.start()           # 쓰레드를 실행합니다.

        self._connectSignals()
        self.gui.show()

    def _connectSignals(self):
        self.gui.button_start.clicked.connect(self.forceWorkerReset)
        self.gui.button_start.clicked.connect(self.worker.startWork)

        self.worker.sig_numbers.connect(self.gui.updateStatus)

        self.gui.button_cancel.clicked.connect(self.forceWorkerReset)

    def forceWorkerReset(self):
        if self.worker_thread.isRunning():
            self.worker_thread.terminate()
            print(self.worker_thread.isRunning())
            self.worker_thread.wait()
            print(self.worker_thread.isRunning())
            self.worker_thread.start()
            print(self.worker_thread.isRunning())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example(app)
    sys.exit(app.exec_())
