
import doubleagent
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
import webbrowser
import time
from multiprocessing import Process, Queue,Pool
from allmaker import allmaker
from autionmaker import autionmaker
from nummaker import nummaker
from pricemaker import pricemaker
import pyperclip
from multigo import multigo
from callee import *
import traceback
class MainWindow(QMainWindow):
    
    def __init__(self):
        self.thread = {}
        super(MainWindow, self).__init__()
        self.centralwidget = QWidget(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.centralwidgetLayout = QVBoxLayout(self.centralwidget)
        self.buttonWidget = QWidget()
# ##########################################################
        self.first = QWidget()
        self.firstlabel = QLabel(
            '메모장', self.first)
        self.firstlabel.setStyleSheet("font-size: 25px;"
                                  "font-weight:bold;")
        self.firstLayout = QGridLayout(self.first)
        self.firstLayout.addWidget(
            self.firstlabel,          0, 0)
        self.firstlabel.setStyleSheet("font-size: 25px;"
                                  "font-weight:bold;")
##############################################################
        self.onecounter = QLabel('')
        self.twocounter = QLabel('')
        self.threecounter = QLabel('')
##############################################################
        self.twoinput = QWidget()
        self.twoinputLayout = QGridLayout(self.twoinput)
        self.one = QLineEdit(self.twoinput)


        self.twoinputLayout.addWidget(
            self.one,          0, 0)        

        self.twoinputLayout.addWidget(
            self.onecounter,          1, 0)        

        self.one.setStyleSheet("width:200px; border:0.5px solid gray;")
        self.two = QLineEdit(self.twoinput)
        self.three = QLineEdit(self.twoinput)

        self.twoinputLayout.addWidget(
            self.two,          2, 0)        
        self.twoinputLayout.addWidget(
            self.twocounter,          3, 0)   
        self.twoinputLayout.addWidget(
            self.three,          4, 0)   
        self.twoinputLayout.addWidget(
            self.threecounter,        5 , 0)   


        self.two.setStyleSheet("width:200px; border:0.5px solid gray;")
        self.three.setStyleSheet("width:200px; border:0.5px solid gray;")

################################################################### 

        self.keywordlimit = QLabel('리미트')
        self.keywordlimit.setStyleSheet(" font-size: 15px")
        self.limitinputwiget = QWidget()
        self.limitinput = QLineEdit(self.limitinputwiget)
        self.keywordlimitLayout = QGridLayout(self.limitinputwiget)
        self.limitinput.setStyleSheet("width:80px; border:0.5px solid gray;") 
        self.keywordlimitLayout.addWidget(
            self.limitinput,          0, 0)  

############################################################################
        self.connection = QPlainTextEdit()
        self.connection.setMaximumSize(250, 100)
        self.importexted = QPlainTextEdit()
        self.importexted.setMaximumSize(250, 100)
        self.subimportexted = QPlainTextEdit()
        self.subimportexted.setMaximumSize(250, 100)  
        self.subtexted = QPlainTextEdit()
        self.subtexted.setMaximumSize(250, 100)  
############################################################################  

        self.price = QLabel('B/A')
        self.price.setStyleSheet(" font-size: 15px")

############################################################################
        self.textcounter = QLabel('')


############################################################################    
        self.pricewiget = QWidget()
        self.priceLayout = QGridLayout(self.pricewiget)
        self.origine = QLineEdit(self.pricewiget)
        self.selling = QLineEdit(self.pricewiget)
        self.origine.setStyleSheet("width:80px; border:0.5px solid gray;")
        self.selling.setStyleSheet("width:80px; border:0.5px solid gray;")
        self.priceLayout.addWidget(
            self.origine,          0, 0)        
        self.priceLayout.addWidget(
            self.selling,          0, 1)   
############################################################################
        self.calculator = QLabel('')

############################################################################
        self.link = QLabel('링크')
        self.link.setStyleSheet("font-size: 15px")
############################################################################
        self.linkinput = QLineEdit()
        self.linkinput.setStyleSheet("width:80px; border:0.5px solid gray;")

############################################################################
        self.linkbutton = QPushButton('LINK', self)

        self.linkbutton.setStyleSheet("margin-top: 20px; width:255px; height:50px")
 
        self.copybutton = QPushButton('COPY', self)
        self.copybutton.setStyleSheet("width:250px; height:50px")
############################################################################
        self.sink = QLabel('')
############################################################################
        self.centralwidgetLayout.addWidget(self.first,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.twoinput,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.connection,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.importexted,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.subimportexted,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.subtexted,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.textcounter,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.sink,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.keywordlimit,alignment=Qt.AlignmentFlag.AlignCenter)  
        self.centralwidgetLayout.addWidget(self.limitinputwiget,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.price,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.pricewiget,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.calculator,alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.link,alignment=Qt.AlignmentFlag.AlignCenter)    
        self.centralwidgetLayout.addWidget(self.linkinput,alignment=Qt.AlignmentFlag.AlignCenter)  
        self.centralwidgetLayout.addWidget(self.linkinput,alignment=Qt.AlignmentFlag.AlignCenter)  
        self.centralwidgetLayout.addWidget(self.linkbutton,alignment=Qt.AlignmentFlag.AlignCenter)  
        self.centralwidgetLayout.addWidget(self.copybutton,alignment=Qt.AlignmentFlag.AlignCenter) 
        
############################################################################ 
        self.selling.textChanged.connect(self.calcuchange) 
        self.origine.textChanged.connect(self.calcuchange)  
        self.linkbutton.clicked.connect(self.linkgo)    
        self.importexted.textChanged.connect(self.checker)
        self.connection.textChanged.connect(self.checker)
        self.subimportexted.textChanged.connect(self.checker)
        self.subtexted.textChanged.connect(self.checker)
        self.copybutton.clicked.connect(self.listLayoutChildWidgets)
        self.setCentralWidget(self.centralwidget)
###########################################################################       
        self.one.textChanged.connect(self.onecount) 

        self.two.textChanged.connect(self.twocount) 
        self.three.textChanged.connect(self.threecount) 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def onecount(self):
        t =self.one.text()
        length=len(t.encode('euc-kr'))
        
        self.onecounter.setText(str(length))
    def twocount(self):
        t =self.two.text()
        length=len(t.encode('euc-kr'))
        self.twocounter.setText(str(length))

    def threecount(self):
        t =self.three.text()

        length=len((t).encode('euc-kr'))
        self.threecounter.setText(str(length))


    def calcuchange(self):
        try:
            margin = round(int(self.selling.text())*0.87) - \
                int(self.origine.text())
            self.calculator.setText(str(margin))

        except Exception as e:
            print(e)
            pass
    def checker(self):
        try:
            t =self.one.text()
            t1 = self.importexted.toPlainText()
            t2 = self.subtexted.toPlainText()
            con = self.connection.toPlainText()
            si = self.subimportexted.toPlainText()
            con = con.replace('\n',' ')
            allt = t1+t2+t+con+si
            length=len(allt)

            self.textcounter.setText(str(length))

        except Exception as e:
            print(e)
            pass

    def linkgo(self):
        num = self.linkinput.text()

        try:

            if self.thread[2].is_running == True:
                self.thread[2].terminate()
                self.thread[2].wait()

        except:

            pass

        self.thread[2] = urlworker(index=num)

        self.thread[2].start()

    def listLayoutChildWidgets(self):
        t1 = self.one.text()
        t2 = self.two.text()
        t3 = self.three.text()

        t2a = t2
        t3a = t3


        try:
            if len(t1) == 0 or len(t2) == 0  or len(t3) == 0 :
                print(nontext)
        except Exception as e:
                print(e)

        num = self.linkinput.text()
        important = self.importexted.toPlainText()
        sub = self.subtexted.toPlainText()
        subim = self.subimportexted.toPlainText()
        connected = self.connection.toPlainText()
        if '' == self.limitinput.text():
            limitinput =99
        limitinput = self.limitinput.text()
  
        dic={'price':[self.origine.text(),self.selling.text()],'first_ch':[t1,t2a,t3a],'num':num,'important':important,'sub':sub,'connected':connected,'subimportant':subim,'limitinput':limitinput}


        try:

            if self.thread[1].is_running == True:
                self.thread[1].terminate()
                self.thread[1].wait()

        except:

            pass

        self.thread[1] = keywordworker(index=dic)
        keywordworkerman = self.thread[1]
        keywordworkerman.signal1.connect(self.signal1_emitted)

        self.thread[1].start()
        self.modi = False
    @pyqtSlot(int)
    def signal1_emitted(self,value):
        self.sink.setText(str(value))


def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    app.exec()
class urlworker(QThread):

    def __init__(self,  index=0):
        super(urlworker, self).__init__()
        self.index = index

        self.is_running = True

    def run(self):

        num = self.index


        num = str(num)
        intcounter = len(num)
        if intcounter < 4:
            plus0 = 4 - intcounter
            for li in range(0,plus0):
                num = str(0) + num
        headers = {
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',

                    }

        t = requests.get(
            'http://www.msgood4u.com/html/search/search.php?skey=all&directsearch=y&searchTerm=&sword='+str(num)+'',headers=headers).text
        htmlchunk_lst = t.split("<div class='space'>")[1:]

        for htmlchunk in htmlchunk_lst:
            link = htmlchunk.split("<div class='code'>")[1].split('상품코드 <span>')[1].split('</span>')[0]
            if link == num:
                targetchunk = htmlchunk
                break
        try:
            link = targetchunk.split("<a href='")[1].split('>')[0]
            webbrowser.open(link)
        except:
            pass

class keywordworker(QThread):
    signal1 = pyqtSignal(int)
    def __init__(self,  index=0):
        super(keywordworker, self).__init__()
        self.index = index

        self.is_running = True

    def run(self):

        try:

        #{'origineprice': '60', 'sellingprice': '600', 'first_ch': ['fds', 'dsf', 'sdf'], 'num': '600', 'important': 'sdf', 'sub': 'sdf', 'connected': 'sdf'}
            price = self.index['price']
            limitinput =self.index['limitinput']
            connected = self.index['connected']
            numberid = self.index['num']
            numberid = numberid.replace(' ','')
            firstkeyword = self.index['first_ch']
            subim = self.index['subimportant']
            firstkeywordaf = []
            important = self.index['important']
            sub = self.index['sub']
            for li in firstkeyword:
                tt = li.split(' ')
                lili = []
                for li2 in tt:
                    if not li2 == '':
                        lili.append(li2)
                firstkeywordaf.append(lili)
            importantaf = []
            subimportant = subim
            subimportantaf = []
            subimportant = subimportant.split(' ')
            important = important.split(' ')
            connected = connected.split('\n')
            if isinstance(connected,list) == False:
                 connected = doubleagent.s2l(connected)
            connectedaf = []
            for li in subimportant:
                if not li[0] == ' ' or not li[-1] == ' ':
                    subimportantaf.append(li)    
            for li in connected:
                if not li[0] == ' ' or not li[-1] == ' ':
                    connectedaf.append(li)   

            for li in important:
                if not li == '':
                    importantaf.append(li)    
            subaf = []
            sub = sub.split(' ')
            for li in sub:
                if not li == '':
                    subaf.append(li)   
            overlap = connectedaf[:]
            overlap_li = []
            for li in overlap:
                overlap_li.append(li.split(' '))
            overlap_li = doubleagent.ll2l(overlap_li)
            for li in connectedaf:
                checker = len(firstkeyword[0])
                checker2 = len(firstkeyword[0].replace(li,''))
                connectedsplited = li.split(' ')
                print(checker)
                print(checker2)
                if checker == checker2:
                    ob = firstkeyword[0].split(' ')
                    lenob = len(ob)
                    checker = [x for x in ob if x not in connectedsplited]
                    if not lenob == len(checker):
                        print(firstkeyword에connected중복키워드가있습니다)
            for li in connectedaf:
                checker = len(firstkeyword[1])
                checker2 = len(firstkeyword[1].replace(li,''))
                connectedsplited = li.split(' ')
                if checker == checker2:
                    ob = firstkeyword[1].split(' ')
                    lenob = len(ob)
                    checker = [x for x in ob if x not in connectedsplited]
                    if not lenob == len(checker):
                        print(firstkeyword에connected중복키워드가있습니다)
            for li in connectedaf:
                checker = len(firstkeyword[2])
                checker2 = len(firstkeyword[2].replace(li,''))
                connectedsplited = li.split(' ')
                if checker == checker2:
                    ob = firstkeyword[2].split(' ')
                    lenob = len(ob)
                    checker = [x for x in ob if x not in connectedsplited]
                    if not lenob == len(checker):
                        print(firstkeyword에onnected중복키워드가있습니다)
            if doubleagent.overlapchecker(importantaf) == True:
                importantaf =list(dict.fromkeys(importantaf))
            if doubleagent.overlapchecker(connectedaf) == True:
                connectedaf =list(dict.fromkeys(connectedaf))
            if doubleagent.overlapchecker(subimportantaf) == True:
                subimportantaf =list(dict.fromkeys(subimportantaf))
            if doubleagent.overlapchecker(subaf) == True:
                subaf =list(dict.fromkeys(subaf))
            testset = importantaf[:]
            testset.extend(subaf)
        
            if doubleagent.overlapchecker(testset) == True:
               subaf = [x for x in subaf if x not in importantaf]
            importantaf = [x for x in importantaf if x not in overlap_li]
            subaf = [x for x in subaf if x not in overlap_li]
            subimportantaf = [x for x in subimportantaf if x not in overlap_li]


            allkey = {'firstkeywordaf':firstkeywordaf,'connectedaf':connectedaf,'importantaf':importantaf,'subaf':subaf,'subimportantaf':subimportantaf}



            
            allmaker_result = Queue()

            nummaker_result = Queue()
            pricemaker_result = Queue()

            th1 = Process(target=pricemaker, args=(
                price[0], price[1], pricemaker_result))
            th2 = Process(target=nummaker, args=(numberid, nummaker_result))
            th3 = Process(target=allmaker, args=(
                allkey,limitinput, allmaker_result))

            th1.start()
            th2.start()
            th3.start()

            th1.join()
            th2.join()
            th3.join()

            pricemakerrt = (pricemaker_result.get())
            nummaker_resultrt = (nummaker_result.get())

            modified = (allmaker_result.get())


            col_list = []

            for priceori, priceosel, num, allmakerr, autionm in zip(pricemakerrt[0], pricemakerrt[1], nummaker_resultrt,
                                                                    modified[1], modified[0]):
                col = str(num)+'\t'+autionm+'\t'+allmakerr + \
                    '\t'+priceosel+'\t'+priceori
                col_list.append(col)
            col_list = '\n'.join(col_list)
            pyperclip.copy(col_list)
            a=modified[1][0].split(' ')
            b = modified[1][1].split(' ')
            a = len([x for x in a if x not in b])

            self.signal1.emit(a)
        except Exception as e :
            print(traceback.format_exc())


if __name__ == '__main__':
    main()
