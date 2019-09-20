#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pymysql
import traceback
from pymysql.cursors import DictCursor

connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='egais',
            charset='utf8mb4',
            cursorclass=DictCursor)

#глобальные переменные
cursor=connection.cursor()
result=[]
cursor.execute('SELECT* FROM kassa_kassir ')
for row1 in cursor: result.append(row1)
spisok_prodavc=[]
for i in result:
    if i.get("current")==1:
        spisok_prodavc.insert(0,i['fio'])
    else:
        
        spisok_prodavc.append(i['fio'])
    

cursor=connection.cursor()
organizac=[]
ul=[]
cursor.execute("SELECT ul_id FROM kassa_ulonsaleplace")
for row1 in cursor: ul.append(row1)

for i in range (0,len(ul)):
    cursor.execute('SELECT shortname, address, fsrar FROM kassa_ul where id ='+str(ul[i].get('ul_id')))
    for row1 in cursor: organizac.append(row1)
spisok_origanizac=[]
for i in range(0,len(organizac)):
    spisok_origanizac.append(organizac[i].get('shortname'))


cursor=connection.cursor()
kategor=[]
cursor.execute("SELECT name FROM kassa_categ")
for row1 in cursor: kategor.append(row1)
for i in range(0,len(kategor)):
    kategor[i]=kategor[i].get("name")
kategor=kategor[2:len(kategor)-1]

try:
    cursor=connection.cursor()
    cursor.execute("SELECT number_kassa FROM kassa_basket")
except:
    cursor=connection.cursor()
    cursor.execute("ALTER TABLE kassa_basket ADD number_kassa int")

    connection.commit()

#библиотеки
from itertools import groupby
from collections import Counter
import sip
import urllib.request
import xml.etree.ElementTree as xml
import sys 
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import threading
#from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem,QCheckBox
import sys
import time
import requests
import datetime
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,  QToolBox,QPushButton, QGridLayout,QTableWidgetItem, QLineEdit,QInputDialog,QApplication,QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout,QComboBox,QLineEdit
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from time import strftime
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber
from PyQt5.QtCore import QThread, pyqtSignal
import sip
from PyQt5.QtCore import QBasicTimer
import ntplib
import time
import os
LastStateRole = QtCore.Qt.UserRole



from win32api import GetSystemMetrics

a=GetSystemMetrics(0)
b=GetSystemMetrics(1)

#дизайны
if a<1000 or b<1000:
    import design_pip as design_gl_ekran # Это наш конвертированный файл дизайна
else:
    import designnewnewnew as design_gl_ekran
import design_new_dop_okno
from design_new_dop_okno import Ui_Dialog as Form
import design_okno_opl
import gurnal_pr
import vnesenie
import design_add_tovar
import design_podbor
from okno_pred import NameClass


#драйвера
try:
    from driver_atol import Driver_Atol
    from driver_viki import Driver_Viki
    from driver_shtrih import Driver_Shtrih
    flag_kass=True
    
except :
    flag_kass=False
    
print(flag_kass)

def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:n'.format(ex_cls.__name__, ex)

    text += ''.join(traceback.format_tb(tb))

    print(text)
    QtWidgets.QMessageBox.critical(None, 'Error', text)

    sys.exit()

sys.excepthook = log_uncaught_exceptions


class MyThread(QtCore.QThread):
    mysignal = QtCore .pyqtSignal(str) 
    def __init__ ( self, parent=None):
        QtCore.QThread.__init__(self, parent )
        self.running = False
        self.count =0  
    def run(self):
        self.running=True
        while self.running:

            try:
                client = ntplib.NTPClient()
                response = client.request('pool.ntp.org',timeout=40)
                #os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
                if time.strftime('%H')!=time.strftime('%H',time.localtime(response.tx_time)) or int(time.strftime('%M'))-int(time.strftime('%M',time.localtime(response.tx_time)))>10:
                    self.a="Установленное на компьютере время не верно. Необходимо исправить!"
                else:
                    self.a=''
                
            except:
                self.a="НЕТ ИНТЕРНЕТА"
    
                
            self.mysignal.emit(self.a)
            self.sleep(1) 
    
           
            
'''

def thread(my_func):
    """
    Запускает функцию в отдельном потоке
    """
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper
 
@thread
def processing(signal):
    """
    Эмулирует обработку (скачивание) каких-то данных
    """
    try:
        response=urllib.request.urlopen('http://vk.com',timeout=40)
            
        a=True
    except urllib.request.URLError as err: a=False
    
              
    signal.emit(a)  # Посылаем сигнал в котором передаём полученные данные
    
'''

class dop_okno_viemka(QtWidgets.QDialog, vnesenie.Ui_Dialog):

    def __init__(self,parent):
        super().__init__()
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.setupUi(self)
        

        self.initUi()

    def initUi(self):
        window=QtWidgets.QWidget()
        desktop=QtWidgets.QApplication.desktop()
        x=(desktop.width()-window.width())//2
        y=(desktop.height()-window.height())//2
        self.label.clear()
        ex=Example()

        #a=driver.summa_nalich()
        #self.label.setText("Введите сумму, которую хотите изъять"+"n"+"Максимально воможная сумма  "+str(a))
        self.label.clear()
        self.label.setText("Введите сумму, которую хотите изъять:")

class dop_okno_vnesenie(QtWidgets.QDialog, vnesenie.Ui_Dialog):

    def __init__(self,parent):
        super().__init__()
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.setupUi(self)
        

        self.initUi()

    def initUi(self):
        window=QtWidgets.QWidget()
        desktop=QtWidgets.QApplication.desktop()
        x=(desktop.width()-window.width())//2
        y=(desktop.height()-window.height())//2
        

'''
Журнал продаж
'''
class gurnal_pr(QtWidgets.QMainWindow, gurnal_pr.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # Это здесь нужно для доступа к переменным, методам
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        window=QtWidgets.QWidget()
        desktop=QtWidgets.QApplication.desktop()
        x=(desktop.width()-window.width())//2
        y=(desktop.height()-window.height())//2
        self.comboBox.addItems(spisok_origanizac) 
        self.label.setText("c")
        self.dateEdit.setDate(datetime.datetime.now().date())
        self.dateEdit_2.setDate(datetime.datetime.now().date())
        self.label_2.setText("по")
        self.label_3.setText("номер смены")
        self.table = self.tableWidget
        self.table.setColumnCount(6)
        self.table.setGridStyle(0)
        self.table.setHorizontalHeaderLabels(["№ смены","Дата/Время", "Продукция","Сумма чека","ФИО кассира","Оплата"])
        fnt = self.table.font()
        fnt.setPointSize(30)

        for i in range(0,6):
            self.table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)

        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        #колонки по размерности текста
        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        #колонка названия товара растягивается максимально
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        for i in range(4,6):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        indices = int(self.table.selectionModel().currentIndex().row())
        
        self.pushButton.clicked.connect(self.zapoln_tabl)

        self.zapoln_tabl()
        #time = datetime.datetime.now().time()
        #value=times[0].get("begintime")
        #time_morning=(datetime.datetime.min + value).time()

    def zapoln_tabl(self):
        self.table.clear()
        self.table.setRowCount( 0)
        self.table.setColumnCount(6)
        self.table.setGridStyle(0)
        
        self.table.setHorizontalHeaderLabels(["№ смены","Дата/Время", "Продукция","Сумма чека","ФИО кассира","Оплата"])
        a=self.dateEdit.text().replace('.','-')
        
        #print(a[6:]+a[2:6]+a[0:2]+" 00:00:00")
        b=self.dateEdit_2.text().replace('.','-')
        id_ul=[]
        cursor=connection.cursor() 
        cursor.execute("SELECT id FROM kassa_ul where shortname ='"+self.comboBox.currentText()+"'")
        for row1 in cursor:id_ul.append(row1)
        
        kassa_check=[]
        #если номер смены не установлен
        if self.lineEdit.text()=='':
            cursor2=connection.cursor()   
            cursor2.execute("""SELECT ID,DT_CLOSE,SMENA,KASSIR_FIO,MODE FROM KASSA_CHECK WHERE DT_CLOSE>='"""+
            a[6:]+a[2:6]+a[0:2]+" 00:00:00'"+" AND DT_CLOSE<='"""+b[6:]+b[2:6]+b[0:2]+" 23:59:59'"+"AND kassa_ulonsaleplace_id="+str(id_ul[0].get("id")))
            for row1 in cursor2:kassa_check.append(row1)
            #print(self.comboBox.currentText())
        #если установлен
        else:
            cursor2=connection.cursor()   
            cursor2.execute("""SELECT ID,DT_CLOSE,SMENA,KASSIR_FIO,MODE FROM KASSA_CHECK WHERE SMENA="""+self.lineEdit.text()+""" AND DT_CLOSE>='"""+
            a[6:]+a[2:6]+a[0:2]+" 00:00:00'"+" AND DT_CLOSE<='"""+b[6:]+b[2:6]+b[0:2]+" 23:59:59'"+"AND kassa_ulonsaleplace_id="+str(id_ul[0].get("id")))
            for row1 in cursor2:kassa_check.append(row1)            
        
        kassa_check_positions=[]
        price=[]
        for i in kassa_check:
            cursor2=connection.cursor() 
            cursor2.execute("""SELECT KASSA_CHECK_ID,KASSA_GOODS_ID,MARKA,FULLNAME,PRICE FROM kassa_check_positions WHERE KASSA_CHECK_ID="""+str(i.get("ID")))
            for row1 in cursor2:kassa_check_positions.append(row1)
            cursor2=connection.cursor() 
            cursor2.execute("""SELECT SUM(PRICE)  FROM kassa_check_positions WHERE KASSA_CHECK_ID="""+str(i.get("ID"))+" GROUP BY KASSA_CHECK_ID")
            for row1 in cursor2:price.append(row1)
        
        ##print(kassa_check_positions) 
        spisok_fullname=[]
        full=[]
        param=[]
        A=[]
        B=[]
        for i in kassa_check:
            cursor2=connection.cursor() 
            cursor2.execute("""SELECT kassa_check_id,FULLNAME,price, shtrih, marka,param FROM kassa_check_positions WHERE KASSA_CHECK_ID="""+str(i.get("ID")))
            for i in cursor2: full.append(i)
        connection.commit()        
        for i in kassa_check:       
            
            cursor=connection.cursor()
            cursor.execute("""SELECT param FROM kassa_check_positions WHERE KASSA_CHECK_ID="""+str(i.get("ID")))            
            for i in cursor: param.append(i)

        for i in range(0,len(full)):
            full[i]=full[i].values()
        for i in range(0,len(full)):
            full[i]=list(full[i])
        a=[]
        c=[]
        #стурктура информации о продукции
        for i in range(0,len(full)):
            a.append(str(full[i][1]))
            a.append("Объём: "+param[i].get("param")[13:param[i].get("param").find(",")-1])
            a.append("Цена: "+str(full[i][2])+" Руб.")
            a.append('\n')
            a.append("Штрих-код: "+full[i][3])
            a.append('\n')
            if full[i][4]!='':
                a.append("Марка: "+full[i][4])
            else: a.append(" ")
            a.append('\n')
            a.append('                    ')
            b='  '.join(a)
            c.append(full[i][0])
            c.append(b)
            full[i]=c
            a=[]
            c=[]
 
        sorted_vehicles=full
        A=[] 
        #группировка по чеку (когда несколько продукции в чеке)
        for key, group in groupby(sorted_vehicles, lambda make: make[0]):
            for make, model in group:
                
                A.append(model)
                ##print('{model} is made by {make}'.format(model=model, make=make))

            B.append(A)
            A=[]
        for i in range(0,len(B)):

            B[i]= '\n'.join(B[i])   
                
        
        #заполнение таблицы
            
        for i in range(0,len(price)):
        
            self.table.insertRow(i) 

            self.table.setRowHeight(i,60) 


            self.table.setItem(i, 0, QTableWidgetItem(str(kassa_check[i].get('SMENA'))))     
            self.table.setItem(i, 1, QTableWidgetItem(str(kassa_check[i].get('DT_CLOSE'))) ) 
            self.table.setItem(i, 2, QTableWidgetItem(B[i] ) )
            self.table.setItem(i, 3, QTableWidgetItem(str(price[i].get('SUM(PRICE)')) +" Руб.") )
            self.table.setItem(i, 4, QTableWidgetItem(str(kassa_check[i].get('KASSIR_FIO')))) 
            if kassa_check[i].get('MODE')==1:
                self.table.setItem(i, 5, QTableWidgetItem("карта") )
            else:
                self.table.setItem(i, 5, QTableWidgetItem("наличные") )
                
            #цвет нечётных=жёлтый
            if i%2!=0:
                self.table.item(i, 0).setBackground(QtGui.QColor(255, 255, 255))
                self.table.item(i, 1).setBackground(QtGui.QColor(255, 255, 255))
                self.table.item(i, 2).setBackground(QtGui.QColor(255, 255, 255))
                self.table.item(i, 3).setBackground(QtGui.QColor(255, 255, 255))
                self.table.item(i, 4).setBackground(QtGui.QColor(255, 255, 255))
                self.table.item(i, 5).setBackground(QtGui.QColor(255, 255, 255))
            self.table.item(i,0).setFlags(QtCore.Qt.ItemIsEnabled )
            self.table.item(i,1).setFlags(QtCore.Qt.ItemIsEnabled)
            self.table.item(i,2).setFlags(QtCore.Qt.ItemIsEnabled)
            self.table.item(i,3).setFlags(QtCore.Qt.ItemIsEnabled)
            self.table.item(i,4).setFlags(QtCore.Qt.ItemIsEnabled)
            self.table.item(i,5).setFlags(QtCore.Qt.ItemIsEnabled)
         

        
        self.table.resizeRowsToContents () 
        self.table.resizeColumnsToContents()
        
'''
окно оплаты
'''

class dop_okno_opl(QtWidgets.QDialog, design_okno_opl.Ui_Dialog):

    def __init__(self,parent,number_check,vozvrat):
        super().__init__()
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.setupUi(self)
        

        self.initUi(number_check,vozvrat)

    def initUi(self,number_check,vozvrat):
        print(vozvrat,"ВОВРАТ ИЛИ НЕТ??")
        window=QtWidgets.QWidget()
        desktop=QtWidgets.QApplication.desktop()
        x=(desktop.width()-window.width())//2
        y=(desktop.height()-window.height())//2
        
        ex=Example()
        a=number_check
        print(a)
        self.a=a[5:] #номер чека из лэйбла (надпись над таблицей)
        #self.pushButton.clicked.connect(lambda:self.createXML("a.xml",a))
        oplata=[]
        cursor2=connection.cursor()
        cursor2.execute("SELECT id,price,fullname,number_kassa,quantity,shtrih,kassa_ulonsaleplace_id,kassa_goods_id,marka FROM kassa_basket where number_kassa="
                        +str(self.a))
        for row1 in cursor2:oplata.append(row1)
        if oplata!=[]:

            kolvo_alc_prod=0
            for i in range(0,len(oplata)):
                if oplata[i].get("marka")!=" ":
                    kolvo_alc_prod+=1


            print(oplata)
            organizac_opl=[]
            kolvo_kassa_ulonsaleplace_id=[]
            for i in oplata:
                kolvo_kassa_ulonsaleplace_id.append(i.get("kassa_ulonsaleplace_id"))
            c = Counter(kolvo_kassa_ulonsaleplace_id)

            spis_pok=c.values()

            spis_pok=list(spis_pok)
            c=list(c)
            print(c)

            if len(c)>=2:
                self.label.setText("Предупреждение! Оплата будет произведена в "+str(len(c))+" этапа")

            #for i in range (0,len(c)):
            cursor.execute('SELECT id,shortname, address, fsrar FROM kassa_ul where id ='+str(min(c)))
            for row1 in cursor: organizac_opl.append(row1)

            self.label_2.setText("Организация: "+organizac_opl[0].get("shortname")) 
            #print(c)
            #print(organizac)


            price_pok=[]
            cursor2=connection.cursor()
            cursor2.execute("SELECT SUM(price*quantity) FROM kassa_basket where number_kassa="+str(self.a))
            for row1 in cursor2:price_pok.append(row1)
            self.label_3.setText("Итоговая сумма: "+str(self.toFixed(price_pok[0].get("SUM(price*quantity)"))))
            #self.oplnal.clicked.connect(lambda: self.oplata_nalich(oplata))
            if vozvrat==False:
                self.oplnal.clicked.connect(lambda: self.opl(self.toFixed(price_pok[0].get("SUM(price*quantity)")),oplata,c))
                print("продажа")
            else:
                self.oplnal.clicked.connect(lambda: self.oplata_nalich(c,1,price_pok[0].get("SUM(price*quantity)"),vozvrat))
                print("возврат")
        
    def toFixed(self,numObj, digits=2):
        return f"{numObj:.{digits}f}"
              
    def createXML(self,oplata):
        """
        Создаем XML файл.
        """
        filename="cheque.xml"
        #oplata=[]
        #cursor2=connection.cursor()
        #cursor2.execute("SELECT id,price,fullname,number_kassa,kassa_ulonsaleplace_id,marka FROM kassa_basket where number_kassa="+str(a)+" AND marka!=' '")
        #for row1 in cursor2:oplata.append(row1)
        alc_harakter=[]
        alc_id=[]
        
        for i in range (0,len(oplata)):

            cursor1=connection.cursor()
            cursor1.execute("SELECT CAPACITY,ALCVOLUME,KASSA_GOODS_ID FROM kassa_GOODS_ALC where kassa_goods_id="
                            +str(oplata[i].get('kassa_goods_id')))
            for row1 in cursor1:alc_harakter.append(row1)
        #print(alc_harakter)
        for i in alc_harakter:
            alc_id.append(i.get("KASSA_GOODS_ID"))
        print(alc_id)
        date=datetime.datetime.now().strftime('%d%m')+datetime.datetime.now().strftime('%Y')[2:]+datetime.datetime.now().strftime('%H%M')
        root = xml.Element(u'Cheque'.encode('utf-8').decode('utf-8'),inn="1660287087".encode('utf-8').decode('utf-8'),datetime=date.encode('utf-8').decode('utf-8'),kpp="162945015".encode('utf-8').decode('utf-8'),kassa="45664".encode('utf-8').decode('utf-8'),address=u"г. Москва, ул. Никопольская,4".encode('utf-8').decode('utf-8'),name=u"Гармония".encode('utf-8').decode('utf-8'),number="45".encode('utf-8').decode('utf-8'),shift="1".encode('utf-8').decode('utf-8'))
        
        for i in range(0,len(oplata)):
            title = xml.SubElement(root,"Bottle".encode('utf-8').decode('utf-8'),
            barcode=oplata[i].get("marka").encode('utf-8').decode('utf-8'),
            ean=oplata[i].get("shtrih").encode('utf-8').decode('utf-8'),price=str(oplata[i].get("price")).encode('utf-8').decode('utf-8'),
            volume=str(alc_harakter[i].get("ALCVOLUME")).encode('utf-8').decode('utf-8'))

            tree = xml.ElementTree(root)

        with open(filename, "wb" ) as fh:
            tree.write(fh,encoding="utf-8",xml_declaration=True)
            
    def c_xml(self):
        headers = {
            'cache-control': "no-cache",
        }
        cookies = {
        }
        data = {

        }
        files = {
            'xml_file': open('Cheque.xml', 'rb')
        }
                  

        r = requests.post("http://192.168.2.67:8080/xml", headers=headers, cookies=cookies, data=data, files=files)
        return r.text

            
    def opl(self,S,oplata,c):
        self.oplnal.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.summa = QtWidgets.QLineEdit()
        self.summa.setStyleSheet("font: 8pt \"Microsoft YaHei\";\n" "background-color: rgb(255, 255, 205);")
                    
        self.summa.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.summa.setObjectName("summa")
        self.summa.setStyleSheet("font: 18pt \"Microsoft YaHei\";")
        self.summa.textChanged.connect(lambda: self.doSomething(S))
        
        
        val_kolvo=QtGui.QRegExpValidator(QtCore.QRegExp("[0-9][0-9][0-9][0-9][0-9]") )
        self.summa.setValidator(val_kolvo) 
           
            
        self.verticalLayout.insertWidget(3,self.summa)
        self.lab=QtWidgets.QLabel()
        self.lab.setStyleSheet("font: 18pt \"Microsoft YaHei\";")
        self.lab.setText("Внесено: ")
        self.verticalLayout.insertWidget(3,self.lab)
        
        self.sd=QtWidgets.QLabel()
        self.sd.setStyleSheet("font: 18pt \"Microsoft YaHei\";")
        self.sd.setText("Сдача: ")
        self.verticalLayout.addWidget(self.sd)
        
        self.gridLayout_money = QtWidgets.QGridLayout() 
        self.gridLayout_money.setVerticalSpacing(60)
        self.d1 = QtWidgets.QPushButton()
        self.d1.setStyleSheet("font: 10pt \"Microsoft YaHei\";\n"
        "background-color: rgb(255, 214, 143);")
        self.d1.setText("10")
        self.d1.clicked.connect(lambda: self.set_money_d(self.d1.text()))
        
        self.d2 = QtWidgets.QPushButton()
        self.d2.setStyleSheet("font: 10pt \"Microsoft YaHei\";\n"
        "background-color: rgb(255, 214, 143);")
        self.d2.setText("50")
        self.d2.clicked.connect(lambda: self.set_money_d(self.d2.text()))
        self.d3 = QtWidgets.QPushButton()
        self.d3.setStyleSheet("font: 10pt \"Microsoft YaHei\";\n"
        "background-color: rgb(255, 214, 143);")
        self.d3.setText("100")
        self.d3.clicked.connect(lambda: self.set_money_d(self.d3.text()))
        self.d4 = QtWidgets.QPushButton()
        self.d4.setStyleSheet("font: 10pt \"Microsoft YaHei\";\n"
        "background-color: rgb(255, 214, 143);")
        self.d4.setText("200")
        self.d4.clicked.connect(lambda: self.set_money_d(self.d4.text()))
        self.d5 = QtWidgets.QPushButton()
        self.d5.setStyleSheet("font: 10pt \"Microsoft YaHei\";\n"
        "background-color: rgb(255, 214, 143);")
        self.d5.setText("500")
        self.d5.clicked.connect(lambda: self.set_money_d(self.d5.text()))
        self.d6 = QtWidgets.QPushButton()
        self.d6.setStyleSheet("font: 10pt \"Microsoft YaHei\";\n"
        "background-color: rgb(255, 214, 143);")
        self.d6.setText("1000")
        self.d6.clicked.connect(lambda: self.set_money_d(self.d6.text()))
        self.d7 = QtWidgets.QPushButton()
        self.d7.setStyleSheet("font: 10pt \"Microsoft YaHei\";\n"
        "background-color: rgb(255, 214, 143);")
        self.d7.setText("2000")
        self.d7.clicked.connect(lambda: self.set_money_d(self.d7.text()))
        self.d8 = QtWidgets.QPushButton()
        self.d8.setStyleSheet("font: 10pt \"Microsoft YaHei\";\n"
        "background-color: rgb(255, 214, 143);")
        self.d8.setText("5000")
        self.d8.clicked.connect(lambda: self.set_money_d(self.d8.text()))
        self.gridLayout_money.addWidget(self.d1, 0, 0, 1, 1)
        self.gridLayout_money.addWidget(self.d2, 0, 1, 1, 1)
        self.gridLayout_money.addWidget(self.d3, 0, 2, 1, 1)
        self.gridLayout_money.addWidget(self.d4, 0, 3, 1, 1)
        self.gridLayout_money.addWidget(self.d5, 0, 4, 1, 1)
        self.gridLayout_money.addWidget(self.d6, 0, 5, 1, 1)
        self.gridLayout_money.addWidget(self.d7, 0, 6, 1, 1)
        self.gridLayout_money.addWidget(self.d8, 0,7, 1, 1)
        self.gridLayout_money.setVerticalSpacing(60)
        
        self.verticalLayout.addLayout(self.gridLayout_money)
            
        
        self.gridLayout_opl = QtWidgets.QGridLayout()     
        self.oplnalich = QtWidgets.QPushButton()
        self.oplnalich.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
        "background-color: rgb(255, 214, 143);")
        self.oplnalich.setText("ОПЛАТА")
        #self.verticalLayout.addWidget(self.oplnalich)
        self.oplnalich.clicked.connect(lambda: self.oplata_nalich(c,1,S,False))
        
        self.oplnalich_no_check = QtWidgets.QPushButton()
        self.oplnalich_no_check.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
        "background-color: rgb(255, 214, 143);")
        self.oplnalich_no_check.setText("ОПЛАТА без печати чека")
        #self.verticalLayout.addWidget(self.oplnalich)
        self.oplnalich_no_check.clicked.connect(lambda: self.oplata_nalich(c,0,False))
        self.gridLayout_opl.addWidget(self.oplnalich, 0, 0, 1, 1)
        self.gridLayout_opl.addWidget(self.oplnalich_no_check, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_opl)
        
        
    def set_money_d(self,kn):
        if self.summa.text()!='':
            self.summa.setText(str(float(self.summa.text())+float(kn)))
        else:
            self.summa.setText(str(float(kn)))
                               

            
    def oplata_nalich(self,c,fl,summa,vozvrat):
        ex=Example()
        a=ex.label_number_chek.text()
        a=a[5:] #номер чека из лэйбла (надпись над таблицей)
        oplata=[]
        cursor2=connection.cursor()
        cursor2.execute("SELECT id,price,fullname,number_kassa,shtrih,quantity,kassa_ulonsaleplace_id,marka,kassa_goods_id FROM kassa_basket where number_kassa="+str(self.a)+
                        " AND kassa_ulonsaleplace_id="+str(min(c)))
        for row1 in cursor2:oplata.append(row1)
            
        oplata1=[]
        cursor2=connection.cursor()
        cursor2.execute("SELECT id,price,fullname,number_kassa,shtrih,quantity,kassa_ulonsaleplace_id,marka,kassa_goods_id FROM kassa_basket where number_kassa="+str(self.a)+
                        " AND kassa_ulonsaleplace_id="+str(min(c))+" AND marka!=' '")
        for row1 in cursor2:oplata1.append(row1)
        

        if oplata1==[]:
            ex=Example()
            if ex.number_driver==1:self.check_print_atol(oplata,c,self.a,fl,0,summa,vozvrat)
            elif ex.number_driver==2: self.check_print_viki(oplata,c,self.a,fl,0,summa,vozvrat)
            elif ex.number_driver==3: self.check_print_shtrih(oplata,c,self.a,fl,0,summa,vozvrat)
            
        
        else:
            self.createXML(oplata1)
            b=self.c_xml()
            print(b)

            if b[:57]=='<?xml version="1.0" encoding="UTF-8" standalone="no"?><A>':
                ex=Example()
                print("получили подпись")
                if ex.number_driver==1:self.check_print_atol(oplata,c,self.a,fl,1,summa,vozvrat,b[b.find("<url>")+5:b.find("</url>")])
                elif ex.number_driver==2: self.check_print_viki(oplata,c,self.a,fl,1,summa,vozvrat,b[b.find("<url>")+5:b.find("</url>")])

            
    def check_print_viki(self,oplata,c,a,fl,alc):
        name_kassir=[]
        cursor2=connection.cursor()
        cursor2.execute("SELECT fio FROM kassa_kassir where current=1")
        for i in cursor2: name_kassir.append(i)
        self1=Example()
        self1.driver.annulir()
        #driver.kassir_registration(name_kassir[0].get("fio"),"548675")
        if fl==1:

            self1.driver.open_check(name_kassir[0].get("fio"))
        else:

            text,ok = QInputDialog.getText(self, 'Оплата без печати чека',
                    'Ввдите email или тел.номер покупателя:')

            if ok:
                self1.driver.open_elekrt_check(text)

        for i in range(0,len(oplata)):
            print(oplata[i].get("fullname"),oplata[i].get("shtrih"),str(oplata[i].get("price"))+'0',str(oplata[i].get("quantity")))
            self1.driver.registration_pos(oplata[i].get("fullname"),oplata[i].get("shtrih"),str(oplata[i].get("price"))+'0',str(oplata[i].get("quantity")))
        if alc==1:
            info_org=[]
            cursor2=connection.cursor()
            cursor2.execute("SELECT fullname,inn,kpp,address FROM kassa_ul where id="+str(min(c)))
            for row1 in cursor2:info_org.append(row1)            
            
            self1.driver.recvisit(info_org[0].get("fullname"))
            self1.driver.recvisit("ИНН: "+info_org[0].get("inn"))
            self1.driver.recvisit("КПП: "+info_org[0].get("kpp"))
            self1.driver.recvisit("АДРЕС: "+info_org[0].get("address"))
            
            self1.driver.itog()
            self1.driver.oplata_nalich(self.summa.text())
            self1.driver.close_check()
            
        else:
            
            self1.driver.itog()
            self1.driver.oplata_nalich(self.summa.text())
            self1.driver.close_check()

        print(self.label_2.text()[13:])
        id_org=ul[spisok_origanizac.index(self.label_2.text()[13:])]
        print(id_org)
        cursor=connection.cursor()
        cursor.execute("""
        DELETE FROM kassa_basket WHERE kassa_ulonsaleplace_id="""+str(id_org.get('ul_id'))+" AND number_kassa="+str(a))
        connection.commit()
        self.accept()        
            
    def check_print_atol(self,oplata,c,a,fl,alc,summa,vozvrat,*args):
        print("/////////////////")
        name_kassir=[]
        cursor2=connection.cursor()
        cursor2.execute("SELECT fio FROM kassa_kassir where current=1")
        for i in cursor2: name_kassir.append(i)
        self1=Example()
        self1.driver.kassir_registration(name_kassir[0].get("fio"),"548675")
        if fl==1:
            if vozvrat==False:
                

                self1.driver.open_check(name_kassir[0].get("fio"),"548675")
            else:
                self1.driver.open_check_vozvr(name_kassir[0].get("fio"),"548675")
        else:

            text,ok = QInputDialog.getText(self, 'Оплата без печати чека',
                    'Ввдите email или тел.номер покупателя:')

            if ok:
                self1.driver.open_elekrt_check(text)

        for i in range(0,len(oplata)):
            self1.driver.registration_pos(oplata[i].get("fullname"),abs(oplata[i].get("price")),oplata[i].get("quantity"))

        self1.driver.oplata_nalich(abs(float(summa)))
        if alc==1:
            print("ого куда ушло")
            self1.driver.QR_code(*args)
            self1.driver.stroka(*args)
                  
        self1.driver.close_check()

        print(self.label_2.text()[13:])
        id_org=ul[spisok_origanizac.index(self.label_2.text()[13:])]
        print(id_org)
        cursor=connection.cursor()
        cursor.execute("""
        DELETE FROM kassa_basket WHERE kassa_ulonsaleplace_id="""+str(c[0])+" AND number_kassa="+str(a))
        connection.commit()
        self.accept()
        
        
    def check_print_shtrih(self,oplata,c,a,fl,alc):
        
        name_kassir=[]
        cursor2=connection.cursor()
        cursor2.execute("SELECT fio FROM kassa_kassir where current=1")
        for i in cursor2: name_kassir.append(i)
        self1=Example()
        self1.driver.info_check()
        #self1.driver.annulir()
        #self1.driver.kassir_registration(name_kassir[0].get("fio"),"548675")
        if fl==1:

            self1.driver.open_check_dr()
        else:

            text,ok = QInputDialog.getText(self, 'Оплата без печати чека',
                    'Ввдите email или тел.номер покупателя:')

            if ok:
                #self1.driver.open_elekrt_check(text)
                pass

        for i in range(0,len(oplata)):
            print((oplata[i].get("fullname"),int(oplata[i].get("price"))*100,int(oplata[i].get("quantity"))*1000))
            self1.driver.registration_pos((oplata[i].get("fullname"),int(oplata[i].get("price"))*100,int(oplata[i].get("quantity"))*1000),tax1=1)
        self1.driver.close_check_dr(int(float(self.summa.text()))*100)
        self1.driver.cut_dr()


        print(self.label_2.text()[13:])
        id_org=ul[spisok_origanizac.index(self.label_2.text()[13:])]
        print(id_org)
        cursor=connection.cursor()
        cursor.execute("""
        DELETE FROM kassa_basket WHERE kassa_ulonsaleplace_id="""+str(c[0])+" AND number_kassa="+str(a))
        connection.commit()
        self.accept()
        
        
    def doSomething(self,S):
        if self.summa.text()!='':
            if float(self.summa.text())>=float(S):
                self.sd.clear()
                self.sd.setText("Сдача: "+str(float(self.summa.text())-float(S)))
            else: 
                self.sd.clear()
                self.sd.setText("Сдача: ")


# In[27]:


'''
Окно выбора корзины
'''
class dop_okno_korz(QtWidgets.QDialog, design_new_dop_okno.Ui_Dialog):

    def __init__(self,parent):
        super().__init__()
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        window=QtWidgets.QWidget()
        desktop=QtWidgets.QApplication.desktop()
        x=(desktop.width()-window.width())//2
        y=(desktop.height()-window.height())//2
        
        #размерности экрана
        w=desktop.width()/2
        h=desktop.height()
        self.setGeometry(desktop.width()/8,desktop.height()/4, desktop.width()/4,desktop.height()/2)
        self.table1=self.tableWidget
        self.label.setText("Выберите чек")
        self.table1.setColumnCount(1)
        self.table1.setGridStyle(0)

        #выделенная строка

        self.table1.setHorizontalHeaderLabels([""])
        
         
        fnt = self.table1.font()
        fnt.setPointSize(20)

        #заголовки по центру
        name=[]
        self.table1.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        indices = self.table1.selectionModel().currentIndex().row()
                
        header = self.table1.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        kassa=[]


        connection.commit()
        for i in range(0,len(ul)):
            cursor2=connection.cursor()
            cursor2.execute("SELECT price,number_kassa FROM kassa_basket")
        for row1 in cursor2: kassa.append(row1)
        a=0
        
        
        kassa_number=[]
        for i in kassa:
            kassa_number.append(i.get("number_kassa"))
        

        c = Counter(kassa_number)
        
        spis_pok=c.values()
        
        spis_pok=list(spis_pok)
        c=list(c)
        
            
        
        #заполнить таблицу кнопками
        for i in range(0,len(c)): 
            self.table1.insertRow(i) #указательно что новую строку нужно в начало
            self.table1.setRowHeight(i,60)
            btnd = QPushButton(self)
         
            btnd.setText("                                    Чек №"+str(c[i])+"      количество позиций    "+str(spis_pok[i])+"                                                                                               ")
            
            self.table1.setCellWidget(i, 0, btnd) 
            btnd.clicked.connect(self.accept)
            #self.table1.setItem(i, 1, QTableWidgetItem(info_pokupka[i].get('fullname')))
                        
        ''' 
        for i in range(0,len(kassa)-1):
            if kassa[i].get("number_kassa")==kassa[i+1].get("number_kassa"):
                
                a+=kassa[i].get("price")
                
            elif i==len(kassa)-1:
                kassa_cen.append(a)

            else:
                kassa_cen.append(a)
                a=0
        #print("цена каждой корзины",kassa_cen)
                
        
        
        
        product1=[]
        product2=[]
        for i in range(0,len(product)):
            if len(product[i].get("shtrih"))<7:
                product1.append(product[i])

        for i in range(0,len(product1)): 
            self.table1.insertRow(i) #указательно что новую строку нужно в начало
            self.table1.setRowHeight(i,60)
            btnd = QPushButton(self)
         
            btnd.setText(product1[i].get('fullname'))
            
            self.table1.setCellWidget(i, 0, btnd) 
            btnd.clicked.connect(self.accept)
            #self.table1.setItem(i, 1, QTableWidgetItem(info_pokupka[i].get('fullname')))        

      
        '''
'''
окно быстрого подбора товаров (с кол-вом цифр в штрихкодe <=6)
'''
class dop_okno_podbor(QtWidgets.QDialog, design_podbor.Ui_Dialog):

    def __init__(self,parent):
        super().__init__()
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.setupUi(self)
        

        self.initUi()

    def initUi(self):
        window=QtWidgets.QWidget()
        desktop=QtWidgets.QApplication.desktop()
        x=(desktop.width()-window.width())//2
        y=(desktop.height()-window.height())//2
        
        #размерности экрана
        w=desktop.width()/2
        h=desktop.height()
        self.setGeometry(desktop.width()/8,desktop.height()/4, desktop.width()/4,desktop.height()/2)
        self.table1=self.tableWidget
        self.label.setText("Выберите товар из списка.")

        #self.table1.setGridStyle(0)

        #выделенная строка

        self.table1.setHorizontalHeaderLabels([' ',"    наименование    "])
        
         
        fnt = self.table1.font()
        fnt.setPointSize(20)

        #заголовки по центру
        name=[]
        self.table1.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        indices = self.table1.selectionModel().currentIndex().row()
                
        header = self.table1.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        kassa_goods_id=[]
        product=[]
        connection.commit()
        for i in range(0,len(ul)):
            cursor2=connection.cursor()
            cursor2.execute("SELECT kassa_goods_id FROM kassa_rests where kassa_ulonsaleplace_id="+str(ul[i].get('ul_id')))
            for row1 in cursor2: kassa_goods_id.append(row1)
        for i in range(0,len(kassa_goods_id)):                    
            cursor2=connection.cursor()
            cursor2.execute("SELECT id, shtrih, fullname FROM kassa_goods where alc!=1 and marka!=1 and markatovar!=1 and id="+str(kassa_goods_id[i].get('kassa_goods_id')))
            for row1 in cursor2: product.append(row1) 
        
        product1=[]
        product2=[]
        for i in range(0,len(product)):
            if len(product[i].get("shtrih"))<7:
                product1.append(product[i])


        
        self.label_2.hide()
        for i in range(0,len(product1)): 
            self.table1.insertRow(i) #указательно что новую строку нужно в начало
            self.table1.setRowHeight(i,60)
            btnd = QPushButton(self)
         
            btnd.setText(product1[i].get('fullname'))
            self.table1.setItem(i, 0, QTableWidgetItem(str(product1[i].get('id'))))
            self.table1.setCellWidget(i, 1, btnd) 
            btnd.clicked.connect(self.accept)
            #self.table1.setItem(i, 1, QTableWidgetItem(info_pokupka[i].get('fullname')))
            

            self.table1.item(i, 0).setBackground(QtGui.QColor(250, 239, 214))
            self.table1.item(i, 0).setForeground(QBrush(QColor(250, 239, 214)))
                        
            self.table1.item(i,0).setFlags(QtCore.Qt.ItemIsEnabled)
        #self.pushButton.clicked.connect(lambda:self.create(product1))
        self.lineEdit.textChanged.connect(lambda:self.create(product1))
            
            
    def create(self,l):
        pr=[]
        pr_id=[]
        self.table1.setRowCount( 0)
        for i in l:
            if i.get('fullname').lower().find(self.lineEdit.text().lower())!=-1:
                pr.append(i.get('fullname'))
                pr_id.append(i.get('id'))
        if pr==[]:
            self.label_2.show()
        else:
            self.label_2.hide()
                  
                  
        for i in range(0,len(pr)):
            self.table1.insertRow(i) #указательно что новую строку нужно в начало
            self.table1.setRowHeight(i,60)
            btnd = QPushButton(self)
         
            btnd.setText(pr[i])
            self.table1.setItem(i, 0, QTableWidgetItem(str(pr_id[i])))
            self.table1.setCellWidget(i, 1, btnd) 
            btnd.clicked.connect(self.accept)
            #self.table1.setItem(i, 1, QTableWidgetItem(info_pokupka[i].get('fullname')))
            

            self.table1.item(i, 0).setBackground(QtGui.QColor(250, 239, 214))
            self.table1.item(i, 0).setForeground(QBrush(QColor(250, 239, 214)))
                        
            self.table1.item(i,0).setFlags(QtCore.Qt.ItemIsEnabled)                  
            
        
    def zapisat(self):
        

        
        self.hide()
 
'''
окно, когда назначено несколько штрих кодов ВОЗВРАТ
'''

class dop_okno_vozvrat(QtWidgets.QDialog, design_new_dop_okno.Ui_Dialog):
    def __init__(self,parent,info_pokupka):
        super().__init__()
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.setupUi(self)
        

        self.initUi(info_pokupka)

    def initUi(self,info_pokupka):
        window=QtWidgets.QWidget()
        desktop=QtWidgets.QApplication.desktop()
        x=(desktop.width()-window.width())//2
        y=(desktop.height()-window.height())//2
        self.setGeometry(desktop.width()/8,desktop.height()/4, desktop.width()/4,desktop.height()/2)
        
        #размерности экрана
        w=desktop.width()/2
        h=desktop.height()
        self.table1=self.tableWidget
        self.label.setText("Товар с этим штрих кодом назначен на несколько групп товаров. Выберите товар из списка.")
        
        self.table1.setGridStyle(0)

        #выделенная строка

        self.table1.setHorizontalHeaderLabels(["наименование"])
         
        fnt = self.table1.font()
        fnt.setPointSize(20)
        alc_haracter=[]
        alc_id=[]
        spisok_cen=[]
        spisok_name=[]
                  
        for i in range (0,len(info_pokupka)):
            if info_pokupka[i].get("price") not in spisok_cen:
                  spisok_cen.append(info_pokupka[i].get("price"))
                  spisok_name.append(info_pokupka[i].get("fullname"))


        #заголовки по центру
        name=[]
        #self.table1.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        indices = self.table1.selectionModel().currentIndex().row()
                
        header = self.table1.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        c=0
        for i in range(0,len(spisok_cen)): 
            self.table1.insertRow(i) #указательно что новую строку нужно в начало
            self.table1.setRowHeight(i,60)
            btnd = QPushButton(self)
            btnd.setText(spisok_name[i]+' '+str(spisok_cen[i])+ ' Р')               
            self.table1.setCellWidget(i, 0, btnd) 
            btnd.clicked.connect(self.accept)
            #self.table1.setItem(i, 1, QTableWidgetItem(info_pokupka[i].get('fullname')))
            
            
    def zapisat(self,info_pokupka):

        
        self.hide()#скрыть окно
                  
        
'''
окно, когда назначено несколько штрих кодов
'''

class dop_okno(QtWidgets.QDialog, design_new_dop_okno.Ui_Dialog):
    def __init__(self,parent,info_pokupka):
        super().__init__()
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.setupUi(self)
        

        self.initUi(info_pokupka)

    def initUi(self,info_pokupka):
        window=QtWidgets.QWidget()
        desktop=QtWidgets.QApplication.desktop()
        x=(desktop.width()-window.width())//2
        y=(desktop.height()-window.height())//2
        self.setGeometry(desktop.width()/8,desktop.height()/4, desktop.width()/4,desktop.height()/2)
        
        #размерности экрана
        w=desktop.width()/2
        h=desktop.height()
        self.table1=self.tableWidget
        self.label.setText("Этот штрих-код назначен на несколько товаров. Выберите товар из списка.")
        
        self.table1.setGridStyle(0)

        #выделенная строка

        self.table1.setHorizontalHeaderLabels(["наименование"])
         
        fnt = self.table1.font()
        fnt.setPointSize(20)
        alc_haracter=[]
        alc_id=[]
                  
        for i in range (0,len(info_pokupka)):

            cursor1=connection.cursor()
            cursor1.execute("SELECT CAPACITY,ALCVOLUME,KASSA_GOODS_ID FROM kassa_GOODS_ALC where kassa_goods_id="+str(info_pokupka[i].get('id')))
            for row1 in cursor1:alc_haracter.append(row1)
        print(alc_haracter)
        for i in alc_haracter:
            alc_id.append(i.get("KASSA_GOODS_ID"))
        print(alc_id)

        #заголовки по центру
        name=[]
        #self.table1.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        indices = self.table1.selectionModel().currentIndex().row()
                
        header = self.table1.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        c=0
        for i in range(0,len(info_pokupka)): 
            self.table1.insertRow(i) #указательно что новую строку нужно в начало
            self.table1.setRowHeight(i,60)
            btnd = QPushButton(self)
            if info_pokupka[i].get('kassa_goods_id') in alc_id:
                btnd.setText(info_pokupka[i].get('fullname')+alc_haracter[c].get("CAPACITY")+alc_haracter[c].get("ALCVOLUME"))
                c+=1
            else:
                  btnd.setText(info_pokupka[i].get('fullname'))               
            self.table1.setCellWidget(i, 0, btnd) 
            btnd.clicked.connect(self.accept)
            #self.table1.setItem(i, 1, QTableWidgetItem(info_pokupka[i].get('fullname')))
            
            
    def zapisat(self,info_pokupka):

        
        self.hide()#скрыть окно


# In[28]:


'''
Окно ввода нового товара
'''
class Vvod_new_tovar(QtWidgets.QDialog,design_add_tovar.Ui_Dialog):
    def __init__(self, parent):
        super().__init__() 
        self.setupUi(self)
        self.build()

    def build(self):
        window=QtWidgets.QWidget()
        desktop=QtWidgets.QApplication.desktop()
        x=(desktop.width()-window.width())//2
        y=(desktop.height()-window.height())//2
        #appearance = self.palette()
        #appearance.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,QtGui.QColor("white"))
        #self.setPalette(appearance)
        w=desktop.width()/2
        h=desktop.height()

        

        #self.mainLayout = QtWidgets.QVBoxLayout()
        self.setGeometry(w*3/8, h/4,w/4,h/1.6)
        self.setWindowTitle('Добавить товар')
        self.setFont(QtGui.QFont("Times", 12))
        
        w0=w*3/8
        h0=h/4
        w1=w/4
        h1=h/2

        
        self.vnt0=self.label
        #self.vnt0.setGeometry(w0*0.05, 0.05*h0, 0.5*w0, 0.1*h0) 
        
        self.vnt1=self.label_2
        #self.vnt1.setGeometry(w0*0.05, 0.3*h0, 0.5*w0, 0.1*h0) 
        
        self.vnt2=self.label_3
        #self.vnt2.setGeometry(w0*0.05, 0.5*h0, 0.55*w0, 0.1*h0) 
        
        
        self.vnt3=self.label_4
        #self.vnt3.setGeometry(w0*0.05, 0.75*h0, 0.55*w0, 0.1*h0) 
        
        self.vnt4=self.label_5
        #self.vnt4.setGeometry(w0*0.05, h0, 0.55*w0, 0.1*h0) 
        
        self.vnt5=self.label_6
        #self.vnt5.setGeometry(w0*0.05, 1.25*h0, 0.5*w0, 0.1*h0)
        
        self.vnt6=self.label_7
        #self.vnt6.setGeometry(w0*0.05, 1.45*h0, 0.5*w0, 0.1*h0)
        


        #все поля для ввода
        
        self.vnt_pole0 = self.lineEdit
        #self.vnt_pole0.setGeometry(w0*0.05, 0.15*h0, 0.55*w0, 0.1*h0)
        
        self.vnt_pole1 =self.lineEdit_2
        #self.vnt_pole1.setGeometry(w0*0.05, 0.4*h0, 0.55*w0, 0.1*h0)
        
        self.vnt_pole2 = self.lineEdit_3
        #self.vnt_pole2.setGeometry(w0*0.05, 0.6*h0, 0.55*w0, 0.1*h0)
        
        self.vnt_pole3 = self.lineEdit_4
        #self.vnt_pole3.setGeometry(w0*0.05, 1.35*h0, 0.55*w0, 0.1*h0)
        

        #self.vnt_pole4.setGeometry(w0*0.05, 1.9*h0, 0, 0)
        
        #выпадающий список
        self.combo_vnt1 = self.comboBox
        #self.combo_vnt1.setGeometry(w0*0.05, 0.85*h0, 0.55*w0, 0.1*h0)
        self.combo_vnt1.addItems(["шт","л","кг"]) 
        #выпадающий список с категориями товара
        
        self.combo_vnt3 =self.comboBox_3
        #self.combo_vnt3.setGeometry(w0*0.05, 1.55*h0, 0.55*w0, 0.1*h0)
        self.combo_vnt3.addItems(kategor) 
        
        #выпадающий список со списками организаций

        self.combo_vnt2 = self.comboBox_2
        #self.combo_vnt2.setGeometry(w0*0.05, 1.1*h0, 0.55*w0, 0.1*h0)
        self.combo_vnt2.addItems(spisok_origanizac) 
        
        self.cb = self.checkBox
        #self.cb.toggle()
        #self.cb.setGeometry(w0*0.05, 1.7*h0, 0.55*w0, 0.1*h0)
        #self.cb.stateChanged.connect(self.changeOkno)
        
        
        self.btn1_vnt = self.pushButton

        self.btn1_vnt.clicked.connect(self.BD) #срабатывающая фукнци

        
                
        self.btn2_vnt = self.pushButton_2

        self.btn2_vnt.clicked.connect(self.otmena)
        self.lbl9=self.label_8
        self.lbl10=self.label_9
        self.lbl9.hide()
        self.lbl10.hide()

        self.vnt_pole0.textChanged.connect(self.doSomething)
        
        self.vnt_pole1.textChanged.connect(self.doSomething1)
        self.vnt_pole3.textChanged.connect(self.doSomething2)

        

        
    #колво цифр в штрихкоде
    def doSomething(self):
        if len(self.vnt_pole0.text())<3 or self.vnt_pole0.text().isdigit()==False :
            
            self.lbl9.show()
            self.vnt_pole0.setStyleSheet("color: red;")
            self.vnt_pole0.setFont(QtGui.QFont("Microsoft YaHei", 12))

        else:
            self.vnt_pole0.setStyleSheet("color: black;")
            self.vnt_pole0.setFont(QtGui.QFont("Microsoft YaHei", 12))
            self.lbl9.hide()
            
    #проверка на введение алкогольнрй продукци
    
    def doSomething1(self):
        a=self.vnt_pole1.text().lower()
        #spisok_zapr=["пив","водка","ликёр","вино","винн","сигарет","коньяк","водка"]
        if a.find("пив")!=-1 or a.find("водка")!=-1 or a.find("винн")!=-1 or a.find("вино")!=-1 or a.find("сигарет")!=-1 or a.find("настойка")!=-1 or a.find("ликёр")!=-1  or a.find("коньяк")!=-1 or a.find("виски")!=-1 or a.find("ром")!=-1:
            self.lbl10.show()
            self.vnt_pole1.setStyleSheet("color:  red;")
            self.vnt_pole1.setFont(QtGui.QFont("Microsoft YaHei", 12))
            self.lbl10.setStyleSheet("color: red;")
            self.lbl10.setFont(QtGui.QFont("Microsoft YaHei", 12))
        else:
            self.vnt_pole1.setStyleSheet("color: black;")
            self.vnt_pole1.setFont(QtGui.QFont("Microsoft YaHei", 12))
            self.lbl10.hide()


        
    #цвет, если поля пустые
    def doSomething2(self):
        if self.vnt_pole3.text().isdigit()==False:
            self.vnt_pole3.setStyleSheet("background-color: pink;")
            self.vnt_pole3.setFont(QtGui.QFont("Times", 12))
        else:
            self.vnt_pole3.setStyleSheet("background-color: white;")
            self.vnt_pole3.setFont(QtGui.QFont("Times", 12))

            
            
    """
    функция автоматического заполнения при обнаружении товара
    """

    def dobavlenie_new_tovar(self):
        connection.commit()
        cursor=connection.cursor()
        info_pokupka=[]
        price=[]
        if cursor.execute("SELECT name FROM egais_allshtrih where shtrih="+str(self.vnt_pole0.text()))!=0:
            for row1 in cursor: info_pokupka.append(row1)
            self.vnt_pole1.setText(info_pokupka[0].get("name"))
            self.vnt_pole2.setText(info_pokupka[0].get("name"))
            self.vnt_pole3.setFocus(0)
    #щапись в таблицу kassa_goods гиформации о новом товаре 

    def BD(self,state):
        if self.vnt_pole0.text()!='' and self.vnt_pole1.text()!='' and self.vnt_pole3.text()!='':
            connection.commit()
            cursor=connection.cursor()
            id_kategor=[]
            cursor.execute("SELECT id FROM kassa_categ where name= '"+self.combo_vnt3.currentText()+"'" )
            for row1 in cursor: id_kategor.append(row1)
            id_org=ul[spisok_origanizac.index(self.combo_vnt2.currentText())]

            ed_izm=[["шт","л","кг"],[0,1,2],["ed","l","kg"]]
            typ_id=ed_izm[1][ed_izm[0].index(self.combo_vnt1.currentText())]
            edizm_id=ed_izm[2][ed_izm[0].index(self.combo_vnt1.currentText())]
            if self.cb.isChecked():
                markatovar=1
            else: markatovar=0
            
            #запись в БД
            cursor=connection.cursor()
            cursor.execute("""

            INSERT INTO kassa_goods (fullname,fullname2,categ_id,shtrih,kod,alc,typ_id,edizm_id,
            maker_ulid,marka,nalog,mercury,sync,shtrih2,markatovar)values ('"""+str(self.vnt_pole1.text())+
            "',''," +str(id_kategor[0].get("id"))+","+str(self.vnt_pole0.text())+",'','0'," +str(typ_id)+",'"+
            str(edizm_id)+"','0','0','0','0','0','',"+str(markatovar)+")")
            
            connection.commit()

            max_id=[]
            cursor=connection.cursor()
            cursor.execute("SELECT MAX(ID)FROM KASSA_GOODS")
            for row1 in cursor: max_id.append(row1)
            #print("!!",max_id)
            print("организации",id_org)
                
            max_id_kp=[]
            cursor=connection.cursor()
            cursor.execute("SELECT MAX(ID)FROM KASSA_price")
            for row1 in cursor: max_id_kp.append(row1)
            #получение даты
            today = datetime.datetime.today()
            a= today.strftime("%Y-%m-%d %H:%M:%S")
            
            cursor=connection.cursor()
            
            cursor.execute("""
            INSERT INTO kassa_price (dt,kassa_wb_id,price,kassa_goods_id)values ('"""+
            str(a)+
            "','0'," +str(self.vnt_pole3.text())+","+str(max_id[0].get("MAX(ID)"))+")")
            
            cursor=connection.cursor()
            cursor.execute("""
            INSERT INTO kassa_rests (quantity,kassa_price_id,kassa_ulonsaleplace_id,kassa_goods_id)values ("""
            +"'-1',"+str(max_id_kp[0].get("MAX(ID)"))+","+str(id_org.get("ul_id"))+","+
            str(max_id[0].get("MAX(ID)"))+")")
            connection.commit()

            connection.commit()
            self.vnt_pole0.clear()
            self.vnt_pole1.clear()
            self.vnt_pole2.clear()
            self.vnt_pole3.clear()

            self.switch()
        else:
            if self.vnt_pole0.text()=='':
                self.vnt_pole0.setStyleSheet("background-color: pink;")
            if self.vnt_pole1.text()=='':
                self.vnt_pole1.setStyleSheet("background-color: pink;")
            if self.vnt_pole3.text()=='':
                self.vnt_pole3.setStyleSheet("background-color: pink;")
                

    def switch(self):
        self.hide()
        info_pokupka=[]
        cursor=connection.cursor()
        L=[]
        connection.commit()
        cursor=connection.cursor()
        cursor.execute("""SELECT max(id) from kassa_goods""")
        for row1 in cursor: L.append(row1)
        cursor=connection.cursor()
        cursor.execute("SELECT id,shtrih,fullname,fullname2 FROM kassa_goods where id="+str(L[0].get("max(id)")))    
        for row1 in cursor: info_pokupka.append(row1)


        info_pokupka[0].get('fullname')
        price=[]
        cursor1=connection.cursor()
        cursor1.execute("SELECT id,price FROM kassa_price where kassa_goods_id="+str(info_pokupka[0].get('id')))
        for row1 in cursor1: price.append(row1)
        quantity=[]
        cursor2=connection.cursor()
        cursor2.execute("SELECT id,quantity,kassa_ulonsaleplace_id FROM kassa_rests where kassa_goods_id="+str(info_pokupka[0].get('id')))
        for row1 in cursor2:quantity.append(row1)
        pole="000001111"
        self.accept()

    #при нажатии на кнопку отмена очистка полей
    def otmena(self):

        self.vnt_pole0.clear()
        self.vnt_pole1.clear()
        self.vnt_pole2.clear()
        self.vnt_pole3.clear()

   
        self.cls_w()


    def keyReleaseEvent(self, e):
        #нажатие на кнопку enter автоматическое заполенние, если возможно
        if (e.key()==16777220 ) and str(self.vnt_pole0.text())!='':
            #print("нажат!!!")
            self.dobavlenie_new_tovar()
 

    #закрыть окно
    def cls_w(self):
        

        self.close()


# In[29]:


"""
Окно кассы
"""


class Example(QtWidgets.QMainWindow, design_gl_ekran.Ui_MainWindow):
    my_signal = QtCore.pyqtSignal(bool, name='my_signal')
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.secondWin = None
        self.vvodnewtovarWin = None
        self.dop_oknoWin = None
        self.gurnal_prWin = None

        self.initUI()

 

    def initUI(self):
        window=QtWidgets.QWidget()
        
        '''
        
        s, ok = QtWidgets.QInputDialog.getItem(self, "Это заголовок окна",
        "Это текст подсказки", [ "Пункт 1", "Пункт 2", "Пункт З"] ,
        current=1 , editable=False)
        if ok :
            print ("Teкcт выбранного пункта : ", s)
            
        '''
        desktop=QtWidgets.QApplication.desktop()
        x=(desktop.width()-window.width())//2
        y=(desktop.height()-window.height())//2

        #размерности экрана
        w=desktop.width()/2
        h=desktop.height()
        self.setGeometry(0, 0, 100,200)
        self.setWindowTitle('ОБЛАКО')
        
        
        
        
        #список элементов!
        #driver=Driver_Atol()
        #driver.open_smena("gkdfgdkfgjkdfg","797897")

        self.table = self.tableWidget 
        self.qle=self.lineEdit
        self.qle.setCursorPosition(0)
        self.qle.setClearButtonEnabled(True)
        self.qle1=self.lineEdit_2
        self.qle1.setCursorPosition(0)
        self.qle1.setClearButtonEnabled(True)
        self.combo=self.comboBox
        
        self.btn1_tovar =self.pushButton_5
        self.btn1_tovar.clicked.connect(self.tovar)
        
        self.btn2_n_tovar =self.pushButton_6
        self.btn2_n_tovar.clicked.connect(self.open_dialog_3)
        
        self.btn_dop_kn =self.pushButton_8
        self.btn_dop_kn.clicked.connect(self.dop_kn)
       
        
        self.btn_podbor =self.pushButton_7
        self.btn_podbor.clicked.connect(self.open_dialog2)
        
        
        self.btn_opl=self.pushButton_23
        self.btn_opl.clicked.connect(lambda:self.open_dialog_5(False))


        self.label_number_chek=self.label_4

        self.vnesenie=self.pushButton_24
        self.vnesenie.clicked.connect(self.open_win7)

        self.vozvrat=self.pushButton_25

        self.viemka=self.pushButton_26
        self.viemka.clicked.connect(self.open_win8)

        self.x_otchet=self.pushButton_27
        self.x_otchet.clicked.connect(lambda: self.x_otch())

        self.z_otchet=self.pushButton_28
        self.z_otchet.clicked.connect(lambda:self.z_otch())

        self.g_pr=self.pushButton_29
        self.g_pr.clicked.connect(self.open_dialog_6)
                
        self.btn_delete_chek=self.pushButton_31
        self.btn_delete_chek.clicked.connect(self.open_dialog_4)
                
        self.btn_otl_chek=self.pushButton_30
        self.btn_otl_chek.clicked.connect(self.new_kassa_chek_butt)
        
        self.skr_dop_okno=self.pushButton_9
        self.skr_dop_okno.clicked.connect(self.zakr_okno)

                  
        # При нажатии на кнопку запускаем обработку данных
        #processing(self.my_signal)
 
        # Обработчик сигнала
        #self.my_signal.connect(self.mySignalHandler, QtCore.Qt.QueuedConnection)
 
        
                  
        
        self.vozvr=self.pushButton_32
        self.vozvr.clicked.connect(lambda:self.open_dialog_5(True))
                  
                  
        self.show_vozvr=self.pushButton_25
        self.show_vozvr.clicked.connect(self.regim_vozvrat)
    
        self.otmena_vozvr_b=self.pushButton_10
        self.otmena_vozvr_b.clicked.connect(self.otmena_vozvr)
                  

                  
        self.mythread = MyThread()
                  
        print("Запуск потока",self.mythread.isRunning())
        if not self.mythread.isRunning() :
            self.mythread.start() # Запускаем поток 
            print(" Запускаем поток ",self.mythread.isRunning())
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
                  
        print(organizac)
        name_org=[]
        for i in organizac:
            name_org.append(i.get("shortname")+" "+i.get("address")+" "+i.get("fsrar")+" ")
        

        print(name_org)
        if name_org!=[]:
            
            self.label.setText(name_org[0])
    
        now = QDate.currentDate() 
        self.label_2.setText(now.toString(Qt.ISODate))
        self.label_3.setText("кассир:")

        spisok_prodavc.append("ДОБАВИТЬ КАССИРА")
        self.comboBox.addItems(spisok_prodavc) 
        self.combo.activated.connect(self.combo_new_kassir)
        #self.lbl4=self.label_4
        #self.label_4.setText("Чек №1")
        
        #self.btn_udal = self.pushButton_7

        #self.btn_udal.clicked.connect(self.otmena_vvoda)
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime() 
        self.table.setColumnCount(8)
        self.table.setGridStyle(0) 
        #self.qle1=QLineEdit(self)
        self.qle.setFocus(0)


        #self.lbl6=QLabel(self)
        #self.lbl6.setStyleSheet("color:#FF0000;")
        #self.lbl6.setFont(QtGui.QFont("Times", 25))
        
        #self.table.cellChanged.connect(self.onCellChanged)
        #self.tableWidget_2.deleteLater()
        #self.lineEdit_2.deleteLater()
        A=[]
        connection.commit()
        cursor1=connection.cursor()
        cursor1.execute("SELECT COUNT(*) FROM kassa_basket")
        for row1 in cursor1: A.append(row1)


        self.comboBox.currentTextChanged.connect(self.on_combobox_changed_fio)      

        self.table.cellChanged.connect(self.onCellChanged)
        
                  
        self.regim_vozvr=False
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_9.setEnabled(False)        
        self.pushButton_9.hide()
        self.pushButton_24.hide()
        self.pushButton_25.hide()
        self.pushButton_26.hide()
        self.pushButton_27.hide()
        self.pushButton_28.hide()
        self.pushButton_29.hide()
        self.pushButton_30.hide()
        self.pushButton_31.hide()
        self.label_6.hide()
        self.pushButton_32.hide()
        self.pushButton_10.hide()
        self.lineEdit_2.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()

        shortcut =QShortcut(QKeySequence("Ctrl+O"), self)
        shortcut.activated.connect(self.qle.setFocus)
        # Обработчик сигнала
                  
        #self.btn4.clicked.connect(lambda: processing(self.my_signal))
        number_chek=[]
        number_chek1=[]
        self.message=self.label_9


           
        #self.comboBox_kassa_sklad = QtWidgets.QComboBox(self.centralwidget)
        #self.comboBox_kassa_sklad.setStyleSheet("font: 14pt \"Microsoft YaHei\";")
        #self.comboBox_kassa_sklad.setObjectName("comboBox")
        #self.comboBox_kassa_sklad.addItems(['                                       КАССА                                       ','                                       СКЛАД                                       ']) 
        #self.comboBox_kassa_sklad.setAlignment(QtCore.Qt.AlignCenter)
        #self.verticalLayout.insertWidget(0,self.comboBox_kassa_sklad)            
        #self.verticalLayout.insertWidget(0,self.lbl9)  
        if A[0].get('COUNT(*)')!=0:
            connection.commit()
            cursor1=connection.cursor()
            cursor1.execute("SELECT number_kassa FROM kassa_basket")
            for row1 in cursor1: number_chek.append(row1)
            for i in number_chek:
                number_chek1.append(i.get("number_kassa"))
            number_chek1=list(set(number_chek1))
            self.label_number_chek.setText("Чек №"+str(number_chek1[0]))
            self.zapolnenie(number_chek1[0])
            
            

                
        else:
            self.table.setHorizontalHeaderLabels(["","НАИМЕНОВАНИЕ", "КОЛ-ВО"," ","  ЦЕНА   "," ОСТАТОК ","   СУММА   "," "])
            fnt = self.table.font()
            fnt.setPointSize(40)
            #заголовки по центру
            for i in range(0,8):
                self.table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)
            header = self.table.horizontalHeader() 
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
            self.label_5.setText("итого: 0 "+'Р')
            self.label_number_chek.setText("Чек №1")
            
     
        kassa_model=[]
        

        connection.commit()
        cursor1=connection.cursor()
        cursor1.execute("SELECT model FROM kassa_ulonsaleplace")
        for row1 in cursor1: kassa_model.append(row1)
        if kassa_model==[] or flag_kass==False:
            self.number_driver=0
            self.message.setText("Отсутсвует информация о модели кассы! Обратитесь в тех.поддержку")
        elif kassa_model[0].get("model")=="atol":
            self.driver=Driver_Atol()
            if self.driver.proverka_podkl()==False:
                print("сработалдо")
                self.message.setText("Отсутсвует поключение к кассе! Обратитесь в тех.поддержку.")
                self.number_driver=0
                self.message.show()
            else:   
                #self.driver.info_smena_open()
                self.number_driver=1
                if self.internet_on()==False:
                    self.message.setText("НЕТ ИНТЕРНЕТА")
                    self.message.show()
                else:self.message.hide()


        elif kassa_model[0].get("model")=="viki": 
            self.driver=Driver_Viki()
            if self.driver.proverka_podkl()==False:
                print("сработалдо")
                self.message.setText("Отсутсвует поключение к кассе! Обратитесь в тех.поддержку.")
                self.number_driver=0
                self.message.show()
            else:   
                #self.driver.info_smena_open()
                self.number_driver=2
                if self.internet_on()==False:
                    self.message.setText("НЕТ ИНТЕРНЕТА")
                    self.message.show()
                else:self.message.hide()


        elif kassa_model[0].get("model")=="shtrih": 
            self.driver=Driver_Shtrih()
            if self.driver.proverka_podkl()==False:
                print("сработалдо")
                self.message.setText("Отсутсвует поключение к кассе! Обратитесь в тех.поддержку.")
                self.number_driver=0
                self.message.show()
            else:   
                self.driver.info_smena_open()
                self.number_driver=3
                if self.internet_on()==False:
                    self.message.setText("НЕТ ИНТЕРНЕТА")
                    self.message.show()
                else:self.message.hide()
        else:
            self.number_driver=0
            self.message.setText("Отсутсвует информация о модели кассы! Обратитесь в тех.поддержку")                  
        
        
        
            
        self.btn_set_0=self.pushButton_20
        self.btn_set_0.clicked.connect(lambda: self.set_number(self.btn_set_0.text()))
        self.btn_set_1=self.pushButton_12
        self.btn_set_1.clicked.connect(lambda: self.set_number(self.btn_set_1.text()))
        self.btn_set_2=self.pushButton_18
        self.btn_set_2.clicked.connect(lambda: self.set_number(self.btn_set_2.text()))     
        self.btn_set_3=self.pushButton_19
        self.btn_set_3.clicked.connect(lambda: self.set_number(self.btn_set_3.text()))
        self.btn_set_4=self.pushButton_13
        self.btn_set_4.clicked.connect(lambda: self.set_number(self.btn_set_4.text()))        
        self.btn_set_5=self.pushButton_15
        self.btn_set_5.clicked.connect(lambda: self.set_number(self.btn_set_5.text()))        
        self.btn_set_6=self.pushButton_16
        self.btn_set_6.clicked.connect(lambda: self.set_number(self.btn_set_6.text()))
        self.btn_set_7=self.pushButton_17
        self.btn_set_7.clicked.connect(lambda: self.set_number(self.btn_set_7.text()))       
        self.btn_set_8=self.pushButton_11
        self.btn_set_8.clicked.connect(lambda: self.set_number(self.btn_set_8.text()))        
        self.btn_set_9=self.pushButton_14
        self.btn_set_9.clicked.connect(lambda: self.set_number(self.btn_set_9.text()))
        self.btn_set=self.pushButton_21
        self.btn_set.clicked.connect(lambda: self.set_number(self.btn_set.text()))    
        self.btn_del=self.pushButton_22
        self.btn_del.clicked.connect(lambda: self.delete_number()) 
    def on_change ( self, s ) :

        if s!='':
            self.message.setText(s)
            self.message.show()
        else:
            self.message.hide()
                  
        
    def set_number(self,text):
        if str(type(self.focusWidget()))=="<class 'PyQt5.QtWidgets.QLineEdit'>":
                  
            self.focusWidget().setText(self.focusWidget().text()+text)
            self.itogo()
    def delete_number(self):
        if self.focusWidget().text()!='':
            self.focusWidget().setText(self.focusWidget().text()[:len(self.focusWidget().text())-1])
                  
                  
    
    #проверка на наличин интернета
    def internet_on(self):
        try:
            response=urllib.request.urlopen('http://vk.com',timeout=40)
            
            return True
        except urllib.request.URLError as err: pass
        return False
              

    #время 
    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.lcdNumber.display(text)
    def combo_new_kassir(self):
        if self.combo.currentText()=="ДОБАВИТЬ КАССИРА":

            text,ok = QInputDialog.getText(self, 'Новый кассир',
                'Введите имя:')

            if ok:
                cursor=connection.cursor()
                cursor.execute("""

                INSERT INTO kassa_kassir (fio,current)values ('"""+str(text)+"','0')")

                
                connection.commit()
                self.combo.clear()
                
                spisok_prodavc.insert(0,text)
                self.comboBox.addItems(spisok_prodavc) 
                

          
            
        
    '''
        
    def new_kassa_chek(self,*args):
        connection.commit()
        cursor1=connection.cursor()
        number_chek=[]
        number_chek1=[]
        cursor1.execute("SELECT number_kassa FROM kassa_basket")
        for row1 in cursor1: number_chek.append(row1)
        for i in number_chek:
            number_chek1.append(i.get("number_kassa"))
        number_chek1=list(set(number_chek1))
        
        #print(str(*args) )  
        if str(*args)=='':
            btn_kassa = QPushButton(str(int(self.verticalLayout_4.itemAt(self.verticalLayout_4.count()-1).widget().text())+1),self)
        #self.btn1_vnt.setGeometry(w0*0.2, 2.3*h0, 0.25*w0, 0.2*h0)
        else: 
            btn_kassa = QPushButton(str(*args),self)

        #self.btn1_vnt.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        self.verticalLayout_4.insertWidget(-1,btn_kassa) 
        a=btn_kassa.text()
        btn_kassa.clicked.connect(lambda:self.new_kassa_chek_butt_1(a, btn_kassa)) #срабатывающая фукнци
        self.new_kassa_chek_butt(int(a))
                


        
        
    def new_kassa_chek_butt_1(self,numb, btn_kassa):
        #numb=self.btn_kassa.text()
        self.label_number_chek.setText("Чек №"+str(numb))       
        
        c=0
        for i in range(self.verticalLayout_4.count()):
            c+=1

        
        position=[]
        number_chek1=[]
        connection.commit()
        cursor1=connection.cursor()
        cursor1.execute("SELECT COUNT(*) FROM kassa_basket WHERE NUMBER_KASSA="+str(numb))
        for row1 in cursor1: position.append(row1)
        for i in position:
            number_chek1.append(i.get("number_kassa"))
        number_chek1=list(set(number_chek1))                

            
                    
        for i in range(self.verticalLayout_4.count()):   
             #layout.itemAt(i).widget().deleteLater()    
            if self.verticalLayout_4.itemAt(i).widget().text()==self.label.text()[5:]:
            
                #print("название кнопки",numb)
                #print("индекс",i)
                effect = QGraphicsDropShadowEffect( self.verticalLayout_4.itemAt(i).widget() )
                effect.setOffset(0, 0)
                effect.setBlurRadius(20)
                self.verticalLayout_4.itemAt(i).widget().setGraphicsEffect(effect)
                
        for i in range(self.verticalLayout_4.count()):   
             #layout.itemAt(i).widget().deleteLater()    
            if self.verticalLayout_4.itemAt(i).widget().text()!=self.label.text()[5:]:
            
                #print("название кнопки",numb)
                #print("индекс",i)
                effect = QGraphicsDropShadowEffect( self.verticalLayout_4.itemAt(i).widget() )
                effect.setOffset(0, 0)
                effect.setBlurRadius(0)
                self.verticalLayout_4.itemAt(i).widget().setGraphicsEffect(effect)                
                
                
        if position[0].get('COUNT(*)')!=0:
                self.table.setRowCount(0)
                self.zapolnenie(numb)
                #self.table.cellChanged.connect(self.onCellChanged)
                
               
        else: 

            
            self.table.setRowCount(0)
            #self.table.cellChanged.connect(self.onCellChanged)
            
     
    def delete_korsina(self):
        a=self.label_number_chek.text()
        a=a[len(a)-1]

        #удаление из корзины по id 
        cursor=connection.cursor()
        cursor.execute("""
        DELETE FROM kassa_basket WHERE number_kassa="""+str(a))
        connection.commit()
        self.table.setRowCount(0)
        self.qle.setFocus(0)
        
 
        spisok_kass=[]
    
        for i in range(self.verticalLayout_4.count()): 
            #print(i)
            #layout.itemAt(i).widget().deleteLater()    
            if self.verticalLayout_4.itemAt(i).widget().text()==self.label.text()[5:]:
                effect = QGraphicsDropShadowEffect( self.verticalLayout_4.itemAt(i).widget() )
                effect.setOffset(0, 0)
                effect.setBlurRadius(0)
                self.verticalLayout_4.itemAt(i).widget().setGraphicsEffect(effect)    
                

                #effect = QGraphicsDropShadowEffect( self.verticalLayout_4.itemAt(i).widget() )
                self.verticalLayout_2.removeWidget(self.verticalLayout_4.itemAt(i).widget())
                sip.delete(self.verticalLayout_4.itemAt(i).widget())
                if self.verticalLayout_4.itemAt(0)!=None: 
                    self.new_kassa_chek_butt(self.verticalLayout_4.itemAt(0).widget().text())
                else:
                    self.label_5.setText("итого: 0 "+'Р')
                    self.new_kassa_chek(1)

                #self.verticalLayout_4.itemAt(i).widget() = None
                break
                


  
        #print("список касса",self.verticalLayout_4.count())       
        self.itogo()
        
        
    '''  
    def dop_kn(self):
        #self.btn_dop_kn.setEnabled(False)
        #driver=Driver_Atol()
        self.btn_dop_kn.hide()
        #print("1 фукнция")
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(True)
        self.pushButton.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.pushButton_4.show()
        
        self.pushButton_24.show()


        self.pushButton_25.show()

        self.pushButton_26.show()
        self.pushButton_9.show()

        self.pushButton_27.show()

        self.pushButton_28.show()

        
        self.pushButton_29.show()

        self.pushButton_30.show()
        self.pushButton_31.show()

        self.skr_dop_okno.show()

        

        
    
    def zakr_okno(self):
        self.pushButton_9.setEnabled(False)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.show()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_9.hide()
        self.pushButton_24.hide()
        self.pushButton_25.hide()
        self.pushButton_26.hide()
        self.pushButton_27.hide()
        self.pushButton_28.hide()
        self.pushButton_29.hide()
        self.pushButton_30.hide()
        self.pushButton_31.hide()  
        #self.btn_dop_kn.clicked.connect(self.dop_kn)

     
    def z_otch(self):
        reply = QMessageBox.question(self, 'Предупреждение',"Вы уверенны что хотите снять Z отчёт и ЗАКРЫТЬ СМЕНУ?", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)

            
        if reply == QMessageBox.Yes:
            if self.number_driver==3:
                self.driver.closed_smen()
            elif self.number_driver!=0:
                self.driver.closed_smen(self.comboBox.currentText(),"1")


    def x_otch(self):    
        if self.number_driver==1 or self.number_driver==3:
            self.driver.X_otchet()
        elif self.number_driver==2: 
            self.driver.X_otchet(self.comboBox.currentText())
        
    def new_kassa_chek_butt(self):
        #numb=self.btn_kassa.text()
        kassa=[]
        for i in range(0,len(ul)):
            cursor2=connection.cursor()
            cursor2.execute("SELECT price,number_kassa FROM kassa_basket")
        for row1 in cursor2: kassa.append(row1)
        a=0
        
        
        kassa_number=[]
        for i in kassa:
            kassa_number.append(i.get("number_kassa"))
            
        if kassa_number!=[]:
            
            self.label_number_chek.setText("Чек №"+str(max(kassa_number)+1))

        self.table.setRowCount(0)
        #self.table.cellChanged.connect(self.onCellChanged)
        
    def tovar(self):
        desktop=QtWidgets.QApplication.desktop()
        w=desktop.width()/2
        h=desktop.height()
        
        #self.table.setGeometry(0, 0.3*h,w,0.4*h)
        self.table.setHorizontalHeaderLabels(["","НАИМЕНОВАНИЕ", "КОЛИЧЕСТВО","   ЦЕНА   "," ОСТАТОК ","   СУММА   "," "])
        fnt = self.table.font()
        fnt.setPointSize(40)
        #заголовки по центру
        for i in range(0,7):
            self.table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)


        #колонки по размерности текста
        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #колонка названия товара растягивается максимально
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for i in range(2,8):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)


        indices = int(self.table.selectionModel().currentIndex().row())
        connection.commit()
        cursor=connection.cursor()
        info_pokupka=[]
        cursor.execute("SELECT id,shtrih,fullname,fullname2,edizm_id,marka FROM kassa_goods where shtrih=00000011111")
        for row1 in cursor: info_pokupka.append(row1)

            
        if info_pokupka==[]:
            cursor=connection.cursor()
            cursor.execute("""INSERT INTO KASSA_GOODS (fullname,fullname2,categ_id,shtrih,kod,alc,typ_id,edizm_id,
            maker_ulid,marka,nalog,mercury,sync,shtrih2,markatovar) VALUES ('Товар','','0','00000011111',
                           '','0','0','ed','0','0','0','0','0','','0')""")
            connection.commit()  
            cursor=connection.cursor()
            info_pokupka=[]
            cursor.execute("SELECT id,shtrih,fullname,fullname2,edizm_id,marka FROM kassa_goods where shtrih=00000011111")                  
            for row1 in cursor: info_pokupka.append(row1)
        print(info_pokupka)
        price=[]
        cursor1=connection.cursor()
        cursor1.execute("SELECT id,price FROM kassa_price where kassa_goods_id="+str(info_pokupka[0].get('id')))
        for row1 in cursor1: price.append(row1)
        quantity=[]
        cursor2=connection.cursor()
        cursor2.execute("SELECT id,quantity,kassa_ulonsaleplace_id FROM kassa_rests where kassa_goods_id="+str(info_pokupka[0].get('id')))
        for row1 in cursor2:quantity.append(row1)
        if quantity==[]:
           cursor=connection.cursor()
           cursor.execute("""INSERT INTO KASSA_rests (quantity,kassa_price_id,kassa_ulonsaleplace_id,kassa_goods_id)
           VALUES ('-1','0',"""+str(ul[0].get("ul_id"))+","+str(info_pokupka[0].get("id"))+')')
           connection.commit() 
           quantity=[]
           cursor2=connection.cursor()
           cursor2.execute("SELECT id,quantity,kassa_ulonsaleplace_id FROM kassa_rests where kassa_goods_id="+str(info_pokupka[0].get('id')))
           for row1 in cursor2:quantity.append(row1)
            
        pole="000001111"
        #установка фокуса
        #self.qle.setFocus(0)
        #добавление в таблицу
        self.new_stroka(info_pokupka,quantity,pole,'0',"0"," ","0",[])
        

    def toFixed(self,numObj, digits=0):
        return f"{numObj:.{digits}f}"
                  
    def proverka_mrc(self,cena,widj):
        indices = int(self.table.selectionModel().currentIndex().row())
        #print("проверка мрц",self.table.cellWidget(indices,4).text(),float(cena))
        try:
            if float(widj.text())<float(cena):
                QToolTip.setFont(QFont('SansSerif', 10))

                #self.setToolTip('Минимальная розничная цена '+str(cena)+" Р")                

                widj.setToolTip('Минимальная розничная цена '+str(cena)+" Р")
                widj.setStyleSheet("border: 1px solid red;")
            else:
                widj.setStyleSheet("border: 0px solid red;")

        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
             
                  
    #подсчёт суммы по одному товару
    def summa_kolvo(self):
        indices =  int(self.table.selectionModel().currentIndex().row()) #выделенная строка
        try:
            if indices>=0 and  self.table.cellWidget(indices,2).text()!='' and self.table.cellWidget(indices,4).text()!='':
                #расчёт цены колво*цену
                a= self.toFixed(float(self.table.cellWidget(indices,2).text())*float(self.table.cellWidget(indices,4).text()),2)
                ##print("СЧИТАЕМ",str(float(self.table.cellWidget(indices,2).text())*float(self.table.cellWidget(indices,4).text())))
                self.table.setItem(indices, 6, QTableWidgetItem(str(a)))
                self.table.item(indices,6).setFlags(QtCore.Qt.ItemIsEnabled)

            if indices>=0 and  self.table.cellWidget(indices,2).text()=='':
                self.table.cellWidget(indices,2).setStyleSheet("border: 1px solid red;")
            elif indices>=0 and self.table.cellWidget(indices,2).text()!='' and float(self.table.cellWidget(indices,2).text())==float('0'):
                self.table.cellWidget(indices,2).setStyleSheet("border: 1px solid red;")
            elif indices>=0 and  self.table.item(indices,5).text()!='---':
                if float(self.table.cellWidget(indices,2).text())>float(self.table.item(indices,5).text()):

                    self.table.cellWidget(indices,2).setStyleSheet("border: 1px solid red;")
                else:
                    self.table.cellWidget(indices,2).setStyleSheet("border: 0px solid red;")
                  
            elif indices>=0  :
                self.table.cellWidget(indices,2).setStyleSheet("border: 0px solid red;")
                  
        except:
            self.table.cellWidget(indices,2).setStyleSheet("border: 1px solid red;")

            
    def summa_price(self):
        indices =  int(self.table.selectionModel().currentIndex().row()) #выделенная строка
        try:
            if indices>=0 and  self.table.cellWidget(indices,2).text()!='' and self.table.cellWidget(indices,4).text()!='':
                #расчёт цены колво*цену
                #print("СЧИТАЕМ",str(float(self.table.cellWidget(indices,2).text())*float(self.table.cellWidget(indices,4).text())))
                a= self.toFixed(float(self.table.cellWidget(indices,2).text())*float(self.table.cellWidget(indices,4).text()),2)
                self.table.setItem(indices, 6, QTableWidgetItem(str(a)))
                self.table.item(indices,6).setFlags(QtCore.Qt.ItemIsEnabled)

            if indices>=0 and  self.table.cellWidget(indices,4).text()=='':
                self.table.cellWidget(indices,4).setStyleSheet("border: 1px solid red;")

            elif indices>=0 and self.table.cellWidget(indices,4).text()!='' and int(float(self.table.cellWidget(indices,4).text()))==0:
                self.table.cellWidget(indices,4).setStyleSheet("border: 1px solid red;")
            elif indices>=0:
                self.table.cellWidget(indices,4).setStyleSheet("border: 0px solid red;")
        except:
            self.table.cellWidget(indices,4).setStyleSheet("border: 1px solid red;")            

    #подсчёт итоговой суммы корзины
    def itogo(self):
        try:
            a=self.label_number_chek.text()
            a=a[len(a)-1]
            summa_price=[]
            summa_price2=[]
            rowPosition = self.table.rowCount()
            connection.commit()   
            cursor2=connection.cursor()
            cursor2.execute("SELECT SUM(PRICE*QUANTITY) from kassa_basket WHERE ROZLIV!=1 AND NUMBER_KASSA="+str(a))
            for row1 in cursor2:summa_price.append(row1)

            cursor2=connection.cursor()
            cursor2.execute("SELECT SUM(PRICE) from kassa_basket WHERE ROZLIV=1 AND NUMBER_KASSA="+str(a))
            for row1 in cursor2:summa_price2.append(row1)
            if summa_price[0].get("SUM(PRICE*QUANTITY)")!=None and summa_price2[0].get("SUM(PRICE)")!=None:
                s=summa_price[0].get("SUM(PRICE*QUANTITY)")+summa_price2[0].get("SUM(PRICE)")
            elif summa_price[0].get("SUM(PRICE*QUANTITY)")!=None and summa_price2[0].get("SUM(PRICE)")==None:
                s=summa_price[0].get("SUM(PRICE*QUANTITY)")
            elif summa_price[0].get("SUM(PRICE*QUANTITY)")==None and summa_price2[0].get("SUM(PRICE)")!=None:
                s=summa_price2[0].get("SUM(PRICE)")
            else:
                s=0
                
                
                #s=s[:s.find('.')+3]

            self.label_5.setText("  Итого:  "+self.toFixed(float(s),digits=2)+' '+'Р ')
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
        
    def shtrih_kod(self):
        #print("ФУНКЦИЯ ШТРИХ КОДА")
        desktop=QtWidgets.QApplication.desktop()
        w=desktop.width()/2
        h=desktop.height()

        
        

        self.table.setHorizontalHeaderLabels(["","НАИМЕНОВАНИЕ", "КОЛИЧЕСТВО"," ","   ЦЕНА   "," ОСТАТОК ","   СУММА   "," "])
        for i in range(0,8):
            self.table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)


        #колонки по размерности текста
        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #колонка названия товара растягивается максимально
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for i in range(2,8):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        pole=str(self.qle.text())
        #словарь если отсканировали при русской расскладке, транслит текста
        layout = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'),
                            "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'))
        pole=pole.translate(layout)
        print(pole)
                  

        quantity=[]
        #если длинны поля 68-это марка
        if len(pole)==68:
            self.marka(pole)
        #если дляинна поля 150-это марка
        elif len(pole)==150:
            self.marka(pole)
        #иначе штрих код
        elif len(pole)>=3 and pole.isdigit()==True:
            
            cursor=connection.cursor()
            connection.commit()
            info_pokupka=[]
            #если не нашли в бд запись с таким штрих кодом, товар отсутствует
            if cursor.execute("SELECT id,fullname,alc,shtrih,fullname2,edizm_id,marka,markatovar FROM kassa_goods where shtrih="+str(pole))==0:
                self.tovar_ots(w,h)
                
                
            else:
                #заполняем в список информацию о покупке
                for row1 in cursor: info_pokupka.append(row1)
                if len(info_pokupka)>1:
                    self.open_dialog(info_pokupka)
                else:
                    self.alone_shtrich(info_pokupka)
                    
        elif len(pole)!=0 and len(pole)<3 or pole.isdigit()==False:
            self.tovar_never_vvod()
            

       #если ввдено 0 1 2 символа неверный ввод                     

       
            
    def alone_shtrich(self,info_pokupka):
        #print("ФУНКЦИЯ ЕДНСТВЕННЫЙ ШТРИХ КОД")
        self.lbl6=QLabel(self)
        self.lbl6.setStyleSheet("color:#FF0000;")
        self.lbl6.setFont(QtGui.QFont("Times", 25))
        desktop=QtWidgets.QApplication.desktop()
        w=desktop.width()/2
        h=desktop.height()
        rozliv=[]
        quantity=[]
        #смотрим информацию о остатках
        times=[]
        cursor2=connection.cursor()   
        cursor2.execute("SELECT begintime,endtime FROM egais_config")
        for row1 in cursor2:times.append(row1)
                
        time = datetime.datetime.now().time()
        value=times[0].get("begintime")
        time_morning=(datetime.datetime.min + value).time()
        value=times[0].get("endtime")
        time_evn=(datetime.datetime.min + value).time()
        #last_night = datetime.time(str(times[0].get("begintime"))[:2],str(times[0].get("begintime"))[3:5])
        
        connection.commit()
        cursor2=connection.cursor()
        for i in ul:
            cursor2.execute("SELECT id,quantity,kassa_ulonsaleplace_id FROM kassa_rests where kassa_ulonsaleplace_id="+str(i.get("ul_id"))+" and kassa_goods_id="+str(info_pokupka[0].get('id')))
            for row1 in cursor2:quantity.append(row1)
        #если список пустой, то нет информации о колве
        if quantity==[]:
            self.tovar_net_kolvo(w,h)
           
        #если остатки нулевые-товар отсутсвует
        elif quantity[0].get('quantity')==0.0:
            #self._update_timer =  QBasicTimer()
            #print("НАЛИЧИЕ ТОВАРА")
            self.tovar_nalich(w,h)
            #self.tovar_ots(w,h)
        elif info_pokupka[0].get('shtrih')=='00000011111':
            self.tovar()
        
        
        elif info_pokupka[0].get("alc")==1 and time<time_morning or info_pokupka[0].get("alc")==1 and time>time_evn :
            self.tovar_alc_time()
            

           

        else:
                        
            if info_pokupka[0].get('marka')==1:
                #self.hbox.insertLayout (3,self.vbox8)
                self.lineEdit_2.show()

                self.qle1=self.lineEdit_2
                            
                self.qle.setDisabled(True)
                self.qle1.setFocus(0)

            #если есть товарная марка открываем поле для ввода товарной марки
            elif info_pokupka[0].get('markatovar')==1:
                self.lineEdit_2.show()

                self.qle1=self.lineEdit_2
                            
                self.qle.setDisabled(True)
                self.qle1.setFocus(0)
            else: 
                #находим цену товара
                price=[]
                cursor1=connection.cursor()
                pole=str(self.qle.text())
                cursor1.execute("SELECT id,price FROM kassa_price where kassa_goods_id="+str(info_pokupka[0].get('id')))
                for row1 in cursor1: price.append(row1)
                #если цена не назначена пишем это
                if price==[]:
                    #self.tovar_net_cena(w,h)
                    self.new_stroka(info_pokupka,quantity,pole,'0','0',' ','0',[])
                #добавление в таблицу    
                else:

                    self.new_stroka(info_pokupka,quantity,pole,str(price[0].get('price')),price[0].get("id"),' ',price[0].get("price"),[])
                                

    #функция добавление записи в таблицу и в бд
    def new_stroka(self,info_pokupka,quantity,pole,price_tov,price,qle1,cena,rozliv):
        self.btn_opl.setEnabled(True)
        self.btn_delete_chek.setEnabled(True)
        self.qle1.clear()
        self.qle1.hide()
        a=self.label_number_chek.text()
        a=a[len(a)-1]
        #print("номер кассы",a)
        desktop=QtWidgets.QApplication.desktop()
        w=desktop.width()/2
        h=desktop.height()
        print(rozliv)
        if rozliv!=[]:
            rozliv_fl=1
            self.zapis_BD(info_pokupka,quantity,price,qle1,cena,rozliv_fl,rozliv[0].get("edizmcode"))
        else: 
            rozliv_fl=0
            self.zapis_BD(info_pokupka,quantity,price,qle1,cena,rozliv_fl)
        #выделенная строка
        #self.table.setGeometry(0, 0.3*h,w,0.4*h)
        self.table.setHorizontalHeaderLabels(["","НАИМЕНОВАНИЕ", "КОЛ-ВО","-","  ЦЕНА   "," ОСТАТОК ","   СУММА   "," "])
        fnt = self.table.font()
        #fnt.setPointSize(80)
        #заголовки по центру
        for i in range(0,8):
            self.table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)

        if info_pokupka[0].get('edizm_id')=="ed":
            ed_izm="шт    "
                
        if info_pokupka[0].get('edizm_id')=="l":
            ed_izm="л    "
        if info_pokupka[0].get('edizm_id')=="kg":
            ed_izm="кг    "
        #колонки по размерности текста
        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #колонка названия товара растягивается максимально
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for i in range(2,8):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        indices = int(self.table.selectionModel().currentIndex().row())
        rowPosition = self.table.rowCount()
        self.table.insertRow(0) #указательно что новую строку нужно в начало
        #кнопка удаления товара
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        btn1 = QPushButton(self)
        val_kolvo=QtGui.QRegExpValidator(QtCore.QRegExp("[0-9][0-9][0-9][0-9][0-9]") )
        val_kolvo_decimal=QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+(\.[0-9][0-9][0-9]?)?") )
        val_price = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+(\.[0-9][0-9]?)?") )
        pole_vv_text = QTextEdit(self)
        pole_vv_text.setReadOnly(True)            
        pole_vv_text.setStyleSheet("border: 0px solid red;")
        pole_vv_text.setMaximumHeight(90)
                  
        #кнопку в седбмой столбец
        self.table.setCellWidget(0, 7, btn1)
        self.table.setRowHeight(0,60)
        pole_vv_kolvo = QLineEdit(self)
        pole_vv_kolvo.setMaxLength(7)
        pole_vv_kolvo.setText("1")
        pole_vv_kolvo.setAlignment(QtCore.Qt.AlignCenter)
            
        pole_vv_price = QLineEdit(self)
        pole_vv_price.setMaxLength(7)
        pole_vv_price.setAlignment(QtCore.Qt.AlignCenter)
            
        pole_vv_price.setText(str(price_tov))
        pole_vv_kolvo.textChanged.connect(self.summa_kolvo)
        pole_vv_price.textChanged.connect(self.summa_price)
        pole_vv_price.setValidator(val_price)
        
        pole_vv_kolvo.setStyleSheet("border: 0px solid red;")
        if price_tov=='0':
            pole_vv_price.setStyleSheet("border: 1px solid red;")
        else:
            pole_vv_price.setStyleSheet("border: 0px solid red;")
        
        combo_v = QComboBox(self)
        #self.combo_vnt1.setGeometry(w0*0.05, 0.85*h0, 0.55*w0, 0.1*h0)

        alc_haracter=[]
        cursor1=connection.cursor()
        cursor1.execute("SELECT PRODUCTVCODE,CAPACITY,ALCVOLUME,KASSA_GOODS_ID FROM kassa_GOODS_ALC where kassa_goods_id="+str(info_pokupka[0].get('id')))
        for row1 in cursor1:alc_haracter.append(row1)

        a1="""
                <html><head>
                  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                  <title>Текст</title> <style>colortext {color: Grey;  font-size:10pt;}</head><body> <p>"""
        b1="</p> </body></html>"
           
                

        rozliv_volume=[]
        #название
        print(alc_haracter)
        if alc_haracter==[]:
                  
            pole_vv_text.setText(a1+info_pokupka[0].get('fullname')+"<br/>"+'<colortext>'+
                                 info_pokupka[0].get('shtrih')+"<br/>"+str(qle1)+
                                    "</colortext>"+b1)
        else:
            if rozliv==[]:
                pole_vv_price.textChanged.connect(lambda:self.proverka_mrc(alc_mrc[0].get('price'),pole_vv_price))
                pole_vv_text.setText(a1+info_pokupka[0].get('fullname')+" "+str(alc_haracter[0].get("ALCVOLUME"))+"% "+
                        str(alc_haracter[0].get("CAPACITY"))+"<br/>"+'<colortext>'+
                    info_pokupka[0].get('shtrih')+"<br/>"+
                                     str(qle1)+"</colortext>"+b1)
            else:
                  
                alc_mrc=[]
                cursor1=connection.cursor()
                cursor1.execute("SELECT price FROM egais_mrc where PRODUCTVCODE="+str(alc_haracter[0].get('PRODUCTVCODE')))
                for row1 in cursor1:alc_mrc.append(row1)
                pole_vv_text.setText(a1+"РОЗЛИВ: "+info_pokupka[0].get('fullname')+" "+str(alc_haracter[0].get("ALCVOLUME"))+"% "+
                        str(alc_haracter[0].get("CAPACITY"))+"<br/>"+'<colortext>'+
                    info_pokupka[0].get('shtrih')+"<br/>"+
                                     str(qle1)+"</colortext>"+b1)
                  
                  
            
        self.table.setCellWidget(0,1, pole_vv_text)
        #self.table.setItem(0, 1, QTableWidgetItem(info_pokupka[0].get('fullname')+'n'+str(info_pokupka[0].get('shtrih'))+'n'+str(qle1)))
        #self.table.setItem(0, 1, QTableWidgetItem(info_pokupka[0].get('fullname')))
        #колво
        if rozliv==[]:
            self.table.setCellWidget(0, 2, pole_vv_kolvo)
            if info_pokupka[0].get('marka')==1 or info_pokupka[0].get('markatov')==1:
                pole_vv_kolvo.setReadOnly(True)
            if info_pokupka[0].get('shtrih')=='00000011111':
                  pole_vv_price.setStyleSheet("border: 1px solid red;")
                  pole_vv_price.setText("")
                  pole_vv_price.setFocus(0)
                  
            if info_pokupka[0].get('edizm_id')=="ed" and info_pokupka[0].get('shtrih')!='00000011111':

                pole_vv_kolvo.setValidator(val_kolvo) 
            else:
 
                pole_vv_kolvo.setValidator(val_kolvo_decimal) 
            
        else:
            for i in rozliv:
                rozliv_volume.append(str(i.get("volume")))
                
            combo_v.addItems(rozliv_volume)       
            self.table.setCellWidget(0, 2, combo_v)
            combo_v.currentTextChanged.connect(lambda:self.on_combobox_changed(rozliv,combo_v))
        #ед.изм
        if rozliv==[]:
            self.table.setItem(0, 3, QTableWidgetItem(ed_izm))
        else:
            self.table.setItem(0, 3, QTableWidgetItem(rozliv[0].get("edizmcode")))
            
        #цена
        if rozliv==[]:
            #self.table.setItem(0, 4, QTableWidgetItem(price_tov))
            self.table.setCellWidget(0, 4, pole_vv_price)
        else:
            cena=rozliv[0].get("price")
            self.table.setItem(0, 4, QTableWidgetItem(str(rozliv[0].get("price"))))
        #колво на складе
        if str(quantity[0].get('quantity'))=='-1.0':
            self.table.setItem(0, 5, QTableWidgetItem('---'))
        else:
            self.table.setItem(0, 5, QTableWidgetItem(str(quantity[0].get('quantity')-1)))
        #сумма
        if rozliv==[]:
            self.table.setItem(0, 6, QTableWidgetItem(price_tov))
        else:
            self.table.setItem(0, 6, QTableWidgetItem(str(rozliv[0].get("price"))))
            
        

        self.qle.clear()
        

        indices = int( self.table.rowCount())-1
        #self.save_izm(pole,quantity[0].get('id'),price[0].get('id'),self.qle1.text(),info_pokupka )

       # grid_layout = QGridLayout() 
        #grid_layout.addWidget(self.table, 0, 0)   # Добавляем таблицу в сетку
        id_pok=[]
        #запись в бд корзину
        rowPosition = self.table.rowCount()

        id_pok=[]
        #в таблице хранб id из бд
        connection.commit()
        cursor=connection.cursor()
        cursor.execute("SELECT id FROM kassa_basket where NUMBER_kassa="+str(a))
        for row1 in cursor: id_pok.append(row1)  
        self.table.setItem(0, 0, QTableWidgetItem(str(id_pok[len(id_pok)-1].get("id"))))
        self.table.item(0, 0).setBackground(QtGui.QColor(0,0,0))
        #делаю поле невозможным для просмотра
        self.table.item(0, 0).setFlags(QtCore.Qt.ItemIsEnabled) 
        #self.table.item(0, 1).setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.item(0, 3).setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.item(0,5).setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.item(0,6).setFlags(QtCore.Qt.ItemIsEnabled)
        
        
        self.table.item(0, 0).setBackground(QtGui.QColor(250, 239, 214))
        self.table.item(0, 0).setForeground(QBrush(QColor(250, 239, 214)))

        self.table.resizeRowsToContents () 
   
        
        #self.table.cellChanged.connect(self.onCellChanged)
                  
        icon_b = QtGui.QIcon()
        icon_b.addPixmap(QtGui.QPixmap("delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        btn1.setIcon(icon_b)
        btn1.setIconSize(QtCore.QSize(60, 60))
        #функия в кнопку удаления
        btn1.clicked.connect(self.delete_stroka)
        

        #self.summa()
        self.itogo()
        
    #записать в касса баскет    
    def zapis_BD(self,info_pokupka,quantity,price_id,qle1,cena,rozliv,*args):
        rowPosition = self.table.rowCount()
        a=self.label_number_chek.text()
        a=a[len(a)-1]


        if info_pokupka!=[]:
            if rozliv!=1:
                cursor=connection.cursor()
                cursor.execute(
                r"""INSERT INTO kassa_basket (pos,kassa_goods_id,quantity,kassa_price_id,
                kassa_rests_id,kassa_ulonsaleplace_id,price,fullname,typ_id,
                edizm_id,shtrih,marka,alcnotsendedegais,markatovar,number_kassa,rozliv) values("""
                    +str(rowPosition)+","+str(info_pokupka[0].get('id'))+",'1',"+str(price_id)
                    +','+str(quantity[0].get('id'))+","+str(quantity[0].get("kassa_ulonsaleplace_id"))+","
                    +str(cena)+",'"+str(info_pokupka[0].get('fullname'))+"','3','"+str(info_pokupka[0].get('edizm_id'))+"','"+
                    str(info_pokupka[0].get('shtrih'))+"','"
                    +str(qle1)+"','1',' ',"+str(a)+","+str(rozliv)+")")
                connection.commit()
            
                cursor=connection.cursor()
                cursor.execute(
                r"""update kassa_rests set quantity=quantity-1 where quantity!=-1 and quantity!=0 and kassa_goods_id="""+str(info_pokupka[0].get('id')))

                connection.commit()
            else:
                cursor=connection.cursor()
                cursor.execute(
                r"""INSERT INTO kassa_basket (pos,kassa_goods_id,quantity,kassa_price_id,
                kassa_rests_id,kassa_ulonsaleplace_id,price,fullname,typ_id,
                edizm_id,shtrih,marka,alcnotsendedegais,markatovar,number_kassa,rozliv) values("""
                    +str(rowPosition)+","+str(info_pokupka[0].get('id'))+",'1',"+str(price_id)
                    +','+str(quantity[0].get('id'))+","+str(quantity[0].get("kassa_ulonsaleplace_id"))+","
                    +str(cena)+",'"+str(info_pokupka[0].get('fullname'))+"','3','"+str(*args)+"','"+
                    str(info_pokupka[0].get('shtrih'))+"','"
                    +str(qle1)+"','1',' ',"+str(a)+","+str(rozliv)+")")
                connection.commit()
                  
 
            
    def tovar_ots(self,w,h): 
        #print("функция 1")
        self.label_7.show()
        self.label_7.setText("Товар с таким штрих-кодом не обнаружен!")

        QTimer.singleShot(3000, self.skr)
        self.qle.clear()
        self.qle.setDisabled(False)
        self.qle.setFocus(0)
        
    def tovar_nalich(self,w,h): 
        #print("функция 2")
        self.label_7.show()
        self.label_7.setText("Товара нет в налчии!")
        QTimer.singleShot(3000, self.skr)
       
        self.qle.clear()
        self.qle.setDisabled(False)
        self.qle.setFocus(0)
                
    def tovar_net_cena(self,w,h):
        #print("функция 3")
        self.label_7.show()
        self.label_7.setText("Цена не назначена!")
        QTimer.singleShot(3000, self.skr)
        self.qle.clear()
        self.qle.setDisabled(False)
        self.qle.setFocus(0)
                
    def tovar_net_kolvo(self,w,h):
        #print("функция 4")
        self.label_7.show()
        self.label_7.setText("Количество не назначено!")
        QTimer.singleShot(3000, self.skr)
        self.qle.clear()
        self.qle.setDisabled(False)
        self.qle.setFocus(0)
                
    def tovar_alc_time(self):
        #print("функция 4")
        self.label_7.show()
        self.label_7.setText("Вы пытаетесь продать алкоголь в недоступное время!")
        QTimer.singleShot(3000, self.skr)
        self.qle.clear()
        self.qle.setDisabled(False)
        self.qle.setFocus(0)
        
        
    def tovar_never_vvod(self):
        self.label_7.show()
        self.label_7.setText("Неверный ввод!")
        
        QTimer.singleShot(3000, self.skr)
        self.qle.clear()
        self.qle.setDisabled(False)
        self.qle.setFocus(0)


    def skr(self):
        self.label_7.hide()

                
        
    #срабатываемые функции при нажатии на кнопки
    def keyReleaseEvent(self, e):
        rowPosition = self.table.rowCount()

        #нажимая на кнопку enter срабатывает функция штрих кода, если поле не пусто
        
        if (e.key()==16777220 or e.key()==16777221 ) and self.qle.hasFocus()==True and self.qle.text()!='':
            if self.regim_vozvr==False:
                self.shtrih_kod()
            else:
                self.regim_vozvr_shtrih(self.qle.text())
                  
    
        elif (e.key()==16777220 or e.key()==16777221 ) and self.qle1!=None and self.qle1.hasFocus()==True:
            #if len(self.qle1.text())==68:
            
            if self.regim_vozvr==False:
                self.marka(self.qle1.text())
            else:
                self.regim_vozvr_marka(self.qle1.text())
   
            
        elif e.type() == 7 and rowPosition>=0:
            
            #self.summa()
            self.itogo()
                  
    def keyPressEvent(self, e):
        print(e.key())
    '''
    
           
    def keyPressEvent(self, event):
        print("AAAAAAAAAAAAA")
        print(event.key())
        if self.qle.hasFocus()==True and self.qle.text()=="Штрих-Код / Марка":
            self.qle.clear()
        else:
            self.qle.setText("Штрих-Код / Марка")
    '''
            
    def marka(self,qle1):

        
        
        print("ФУНКЦИЯ МАРКИ")

        desktop=QtWidgets.QApplication.desktop()
        w=desktop.width()/2
        h=desktop.height()
        #pole=str(self.qle.text())
        rowPosition = self.table.rowCount()
        layout = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'),
                            "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'))
        qle1=qle1.translate(layout)
        
        quantity=[]
        if len(qle1)==68:
            fl=0
            kassa_good_id=[]
            sh=[]
            pole=qle1
            
            #марка старого образца достаём алкокод из неё
            alcocod='0'+self.convert_base(pole[7:19],to_base=10, from_base=36)
            #print("alcocod",alcocod)
            #определяем есть ли запись с таким алкокодом в бд
            connection.commit()
            cursor=connection.cursor()
            cursor.execute("""
            SELECT kassa_goods_id 
            FROM  kassa_goods_alc 
            WHERE  AlcCode LIKE '"""+alcocod+"'ORDER BY  kassa_goods_alc. id ASC ")
            for row1 in cursor:kassa_good_id.append(row1)
            #определяем штрих код
            if len(kassa_good_id)==1:

                #print("штрих",sh)
                rozliv=[]
                cursor1=connection.cursor()
                for i in range(0,len(organizac)):
                    cursor1.execute("SELECT price, volume,edizmcode FROM egais_rozliv where FSRAR='"+
                    str( organizac[i].get('fsrar'))+"' AND ALCCODE='"+str(alcocod)+"'")
                    for row1 in cursor1: rozliv.append(row1)
                if rozliv==[]:
                  
                    cursor2=connection.cursor()
                    check=[]
                    cursor2.execute("SELECT kassa_check_id FROM kassa_check_positions where marka='"+str(qle1)+"'")                                                                                                 
                    for row1 in cursor2:check.append(row1)
                    if check!=[]:
                        chek_data=[]
                        cursor2.execute("SELECT dt_close FROM kassa_check where id="+str(check[0].get("kassa_check_id")))                                                                                                 
                        for row1 in cursor2:chek_data.append(row1)
                        self.error(" ДАННАЯ МАРКА БЫЛА ПРОДАНА "+str(chek_data[0].get('dt_close')))
                    else:
                        self.opredel_sh(kassa_good_id[0].get("kassa_goods_id"),qle1,pole,0)
                                            
                    
                else:
                    self.rozliv(qle1,alcocod,rozliv)
               


            elif len(kassa_good_id)==0: 
                cursor2=connection.cursor()
                check=[]
                cursor2.execute("SELECT kassa_check_id FROM kassa_check_positions where marka='"+str(qle1)+"'")                                                                                                 
                for row1 in cursor2:check.append(row1)
                if check!=[]:
                    chek_data=[]
                    cursor2.execute("SELECT dt_close FROM kassa_check where id="+str(check[0].get("kassa_check_id")))                                                                                                 
                    for row1 in cursor2:chek_data.append(row1)
                    self.error(" ДАННАЯ МАРКА БЫЛА ПРОДАНА "+str(chek_data[0].get('dt_close')))
                  
                
                else:
                    self.error("НАРУШЕНИЕ СТРУКТУРЫ ТАБЛИЦ! ОБРАТИТЕСЬ В ТЕХ.ПОДДЕРЖКУ")
                
        elif len(qle1)==150:
            #print("1")
            alccod=[]
            kassa_good_id=[]
            data_egais=[]
            sh=[]   
            fl=1
            amc=[]
            pole=qle1
            #марка нового образца проверка на дату
            connection.commit()
            cursor2=connection.cursor()
            cursor2.execute("SELECT alccode,dt_sendtoegais FROM egais_restsshop_stockposition_amc where amc='"+qle1+"'")                                                                                                 
            for row1 in cursor2:data_egais.append(row1)
            print(data_egais)
    
            rozliv=[]
            cursor1=connection.cursor()
            for i in range(0,len(organizac)):
                cursor1.execute("SELECT price, volume,edizmcode FROM egais_rozliv where FSRAR='"+
                str( organizac[i].get('fsrar'))+"' AND ALCCODE='"+str(data_egais[0].get("alccode"))+"'")
                for row1 in cursor1: rozliv.append(row1)
                  
            if data_egais==[]:
                self.marka_ots()
            elif rozliv!=[]:
                    self.rozliv(qle1,data_egais[0].get("alccode"),rozliv)
                  
                #print("2")
                
                
            elif data_egais[0].get("dt_sendtoegais")!='0000-00-00 00:00:00':
                    egais_acts=[]
                    cursor2=connection.cursor()
                    cursor2.execute("""
                    SELECT * FROM  egais_acts WHERE status IN (1,2) AND type='ActWriteOff_v3' AND 
                    id in (SELECT egais_Acts_id FROM  egais_acts_position WHERE id IN (SELECT egais_Acts_position_id 
                    FROM  egais_acts_position_amc WHERE amc='""" +qle1+"'))")
                    for row1 in cursor2:egais_acts.append(row1)

                    if egais_acts!=[]:
                        self.error(" ДАННАЯ МАРКА БЫЛА СПИСАНА "+str(egais_acts[0].get("dt")))

                    elif egais_acts==[]:
                        cursor2=connection.cursor()
                        check=[]
                        cursor2.execute("SELECT kassa_check_id FROM kassa_check_positions where marka='"+str(qle1)+"'")                                                                                                 
                        for row1 in cursor2:check.append(row1)
                        if check!=[]:
                            chek_data=[]
                            cursor2.execute("SELECT dt_close FROM kassa_check where id="+str(check[0].get("kassa_check_id")))                                                                                                 
                            for row1 in cursor2:chek_data.append(row1)
                            self.error(" ДАННАЯ МАРКА БЫЛА ПРОДАНА "+str(chek_data[0].get('dt_close')))
                        else:
                            self.error(" ИНФОРМАЦИЯ ПО МАРКЕ НЕ НАЙДЕНА, ОБРАТИТЕСЬ В ТЕХ.ПОДДЕРЖКУ! ")
                                            
                    #self.qle1.clear()
                    #print("3")
            else:

         
                #опреляем штрих код
                connection.commit()
                cursor=connection.cursor()
                #print("6")
                cursor.execute("""
                SELECT kassa_goods_id 
                FROM  kassa_goods_alc 
                WHERE  AlcCode LIKE '"""+data_egais[0].get("alccode")+"'ORDER BY  kassa_goods_alc. id ASC ")

                for row1 in cursor:kassa_good_id.append(row1)
               
                if len(kassa_good_id)==1:
                    #print("8")

                    self.opredel_sh(kassa_good_id[0].get("kassa_goods_id"),qle1,pole,0)

                elif len(kassa_good_id)==0: 
                    self.error("ИНФОРМАЦИЯ ПО МАРКЕ НЕ НАЙДЕНА! ОБРАТИТЕСЬ В ТЕХ.ПОДДЕРЖКУ")
                else:
                    self.error("НАРУШЕНИЕ СТРУКТУРЫ ТАБЛИЦ! ОБРАТИТЕСЬ В ТЕХ.ПОДДЕРЖКУ")
                                            
        
        elif len(qle1)>17:
            sigaret=[]
            check_data=[]
            connection.commit()
            cursor2=connection.cursor()
            cursor2.execute("SELECT id,shtrih,markatovar FROM kassa_goods where shtrih='"+self.qle.text()+"'") 
            for row1 in cursor2:sigaret.append(row1)
            if sigaret==[] or sigaret[0].get("markatovar")==0:

                self.marka_nevern_vvod()
            else:
                cursor2=connection.cursor()
                check=[]
                cursor2.execute("SELECT kassa_check_id FROM kassa_check_positions where marka='"+str(qle1)+"'")                                                                                                 
                for row1 in cursor2:check.append(row1)
                if check!=[]:
                    check_data=[]
                    cursor2.execute("SELECT dt_close FROM kassa_check where id="+str(check[0].get("kassa_check_id")) )                                                                                                
                    for row1 in cursor2:check_data.append(row1)
                    self.error(" ДАННАЯ МАРКА БЫЛА ПРОДАНА "+str(chek_data[0].get(dt_close)))
                else:
                    self.opredel_sh(sigaret[0].get("id"),qle1,qle1,3)
                
        else:
            self.marka_nevern_vvod()
            
                
                        

    def opredel_sh(self,kassa_good_id,qle1,pole,fl):
        if len(qle1)!=68 and len(qle1)!=150 and fl!=3: 
            
            self.marka_ots()
        else:
                
            quantity=[]
            #берём данные о покупке
            #print(kassa_good_id)
            connection.commit()
            cursor=connection.cursor()
            info_pokupka=[]
            cursor.execute("SELECT id,fullname,fullname2,alc,shtrih,edizm_id,marka,markatovar FROM kassa_goods where id="+str(kassa_good_id))
            for row1 in cursor: info_pokupka.append(row1)
                
            price=[]
            cursor1=connection.cursor()
            cursor1.execute("SELECT id,price FROM kassa_price where kassa_goods_id="+str(kassa_good_id))
            for row1 in cursor1: price.append(row1)

            cursor2=connection.cursor()
            cursor2.execute("SELECT id,quantity,kassa_ulonsaleplace_id FROM kassa_rests where kassa_goods_id="+str(info_pokupka[0].get('id')))
            for row1 in cursor2:quantity.append(row1)

                  
            cursor2=connection.cursor()
            korz=[]
            cursor2.execute("SELECT marka FROM kassa_basket where marka='"+str(qle1)+"'")                                                                                                   
            for row1 in cursor2:korz.append(row1)
                    
            times=[]
            cursor2=connection.cursor()   
            cursor2.execute("SELECT begintime,endtime FROM egais_config")
            for row1 in cursor2:times.append(row1)
            time = datetime.datetime.now().time()
            value=times[0].get("begintime")
            time_morning=(datetime.datetime.min + value).time()
            value=times[0].get("endtime")
            time_evn=(datetime.datetime.min + value).time()

            #развлетвление если марка старого и нового образца (скорее всего не нужно)
            if fl==3:
                if info_pokupka==[] or int(info_pokupka[0].get("shtrih"))=='':
                    self.shtrih_ne_naznach()
  
                #цена неназначена
                elif int(quantity[0].get("quantity"))<=0:
                    self.marka_nalich()

                #есть в корзине
                elif korz!=[]:
                    self.marka_korz()
                        
                else:    
                    pole=info_pokupka[0].get("shtrih")
                    if price!=[]:
                        self.new_stroka(info_pokupka,quantity,pole,str(price[0].get('price')),price[0].get("id"),qle1,price[0].get("price"),[])

                    else:
                        self.new_stroka(info_pokupka,quantity,pole,"0",'0',qle1,"0",[])
                    self.qle.clear()
                    self.qle.setDisabled(False)
                    self.qle.setFocus(0)                        
                    
            elif fl==1 or fl==0:

                if info_pokupka==[] or int(info_pokupka[0].get("shtrih"))=='':
                        
                    self.shtrih_ne_naznach()
                elif time<time_morning or time>time_evn :
                    self.tovar_alc_time()   
                #цена неназначена
                elif int(quantity[0].get("quantity"))<=0:                        
                    self.marka_nalich()

                #есть в корзине
                elif korz!=[]:
                    self.marka_korz()

                #проверки пройдены, заполняем таблицу и записывааем в бд
                else:
                    pole=info_pokupka[0].get("shtrih")
                    if price!=[]:
                        self.new_stroka(info_pokupka,quantity,pole,str(price[0].get('price')),price[0].get("id"),qle1,price[0].get("price"),[])
                            
                    else:
                        self.new_stroka(info_pokupka,quantity,pole,"0",'0',qle1,"0",[])
                                                            
                    self.qle.clear()
                    self.qle.setDisabled(False)
                    self.qle.setFocus(0)

                                    
    def rozliv(self,qle1,alccode,rozliv):
            
        connection.commit()
        cursor=connection.cursor()
        kassa_good_id=[]
        cursor.execute("""
        SELECT kassa_goods_id 
        FROM  kassa_goods_alc 
        WHERE  AlcCode LIKE '"""+alccode+"'ORDER BY  kassa_goods_alc. id ASC ")

        for row1 in cursor:kassa_good_id.append(row1)
                                    
               
        if len(kassa_good_id)==1:
            quantity=[]
            #берём данные о покупке
            #print(kassa_good_id)
            connection.commit()
            cursor=connection.cursor()
            info_pokupka=[]
            cursor.execute("SELECT id,fullname,fullname2,alc,shtrih,edizm_id,marka,markatovar FROM kassa_goods where id="+str(kassa_good_id[0].get("kassa_goods_id")))
            for row1 in cursor: info_pokupka.append(row1)
                    
            times=[]
            cursor2=connection.cursor()   
            cursor2.execute("SELECT begintime,endtime FROM egais_config")
            for row1 in cursor2:times.append(row1)
            time = datetime.datetime.now().time()
            value=times[0].get("begintime")
            time_morning=(datetime.datetime.min + value).time()
            value=times[0].get("endtime")
            time_evn=(datetime.datetime.min + value).time()
                  
            cursor2=connection.cursor()
            cursor2.execute("SELECT id,quantity,kassa_ulonsaleplace_id FROM kassa_rests where kassa_goods_id="+str(info_pokupka[0].get('id')))
            for row1 in cursor2:quantity.append(row1)                                    
                                    
            if info_pokupka==[] or int(info_pokupka[0].get("shtrih"))=='':
                        
                self.shtrih_ne_naznach()
            elif time<time_morning or time>time_evn :
                self.tovar_alc_time()   
            elif quantity==[]:
                self.error("КОЛИЧЕСТВО НЕ НАЗНАЧЕНО!")
                  

                #проверки пройдены, заполняем таблицу и записывааем в бд
            else:

                self.new_stroka(info_pokupka,quantity,qle1,"0",'0',qle1,"0",rozliv)                                            
                self.qle.clear()
                self.qle.setDisabled(False)
                self.qle.setFocus(0)


        elif len(kassa_good_id)==0: 
            self.error("ИНФОРМАЦИЯ ПО МАРКЕ НЕ НАЙДЕНА! ОБРАТИТЕСЬ В ТЕХ.ПОДДЕРЖКУ")
        else:
            self.error("НАРУШЕНИЕ СТРУКТУРЫ ТАБЛИЦ! ОБРАТИТЕСЬ В ТЕХ.ПОДДЕРЖКУ")
                                    
    def error(self,stroka):
        self.label_8.show()

        self.label_8.setText(stroka)
        QTimer.singleShot(5000, self.skr2)

        if self.qle.hasFocus()==True:
            self.qle.clear()
        self.qle1.clear()                                    
                                    
    def marka_ots(self):
        self.label_8.show()

        self.label_8.setText("Марка не обнаружена!")
        QTimer.singleShot(5000, self.skr2)

        if self.qle.hasFocus()==True:
            self.qle.clear()
        self.qle1.clear()
        #self.qle.setDisabled(False)
        #self.qle.setFocus(0)

    def marka_spisana(self):
        #print("функция 6")
        self.label_8.show()
        self.label_8.setText("Марка списана!")
        QTimer.singleShot(5000, self.skr2)

        if self.qle.hasFocus()==True:
            self.qle.clear()
        self.qle1.clear()

        
    def marka_data(self):
        #print("функция 7")
        self.label_8.show()  

        self.label_8.setText("Покупка была совершена!")
        QTimer.singleShot(5000, self.skr2)
        self.qle1.clear()
        if self.qle.hasFocus()==True:
            self.qle.clear()

        
        
    def marka_korz(self):
        #print("функция 8")
        self.label_8.show()
        self.label_8.setText("Товар уже в коризне!!!")
        QTimer.singleShot(5000, self.skr2)
        if self.qle.hasFocus()==True:
            self.qle.clear()
        self.qle1.hide()
        self.qle1.clear()



        self.qle.clear()
        self.qle.setDisabled(False)
        self.qle.setFocus(0)
    def marka_cena(self):
        #print("функция 9")
        self.label_8.show()
        self.label_8.setText("Цена не назначена!")
        QTimer.singleShot(5000, self.skr2)
        if self.qle.hasFocus()==True:
            self.qle.clear()
        self.qle1.clear()
        
    def marka_nalich(self):
        print("функция 10")
        self.label_8.show()
        self.label_8.setText("Товара нет в наличии!")
        QTimer.singleShot(5000, self.skr2)
        if self.qle.hasFocus()==True:
            self.qle.clear()
        self.qle1.clear()

        
    def otskan_marka(self):
        #print("функция 11")
        self.label_8.show()
        self.label_8.setText("Алкокод не найден!")
        QTimer.singleShot(3000, self.skr2)
        if self.qle.hasFocus()==True:
            self.qle.clear()
        self.qle1.clear()

    def marka_nevern_vvod(self):
        #print("функция 12")
        self.label_8.show()
        self.label_8.setText("Неверный ввод!")
        QTimer.singleShot(5000, self.skr2)
        if self.qle.hasFocus()==True:
            self.qle.clear()
        self.qle.setDisabled(False)
        self.qle1.clear()
        self.qle1.hide()

        
        #очистка полей при отмене воода   
        
    def shtrih_ne_naznach(self):
        #print("функция 12")
        self.label_8.show()
        self.label_8.setText("Штрих-код не назначен!")
        QTimer.singleShot(5000, self.skr2)
        self.qle1.clear()
        if self.qle.hasFocus()==True:
            self.qle.clear()
                
    def udal(self):
        if self.lbl9 != None:
            self.verticalLayout.removeWidget(self.lbl9)
            sip.delete(self.lbl9)
            self.lbl9 = None
            
    def otmena_vvoda(self):
        self.label_8.show()
        self.label_8.setText("Марка не обнаружена!")
        QTimer.singleShot(5000, self.skr2)
        if self.qle.hasFocus()==True:
            self.qle.clear()
        self.qle.clear()
        self.qle.setDisabled(False)
        self.qle.setFocus(0)
    '''
    def keyPressEvent(self, e):
        if e.type() == 6:
            start_time = time.time()
            #print("--- %s seconds ---" % (time.time() - start_time))

            
            
            ##self.summa()

    def mousePressEvent(self, e):
        if e.type() == 2:
            pass
            ##self.summa()
     
    '''    


    def skr2(self):
        self.label_8.hide()
            
        
    #удаление строки     
    def delete_stroka(self): 

        id_pok=[]
        indices = self.table.selectionModel().currentIndex().row()
        if indices!=-1:

            cursor=connection.cursor()
            cursor.execute("""update kassa_rests set quantity=quantity+1 where quantity!=-1 and kassa_goods_id in (select kassa_goods_id from kassa_basket where id="""+str(int(self.table.item(indices ,0).text()))+")")
            connection.commit()
            cursor=connection.cursor()
            cursor.execute("""
            DELETE FROM kassa_basket WHERE  id="""+str(int(self.table.item(indices ,0).text())))
            connection.commit()
            self.table.removeRow(indices)
            self.qle.setFocus(0)
            #пересёт итьоговой суммы

            

            self.itogo()


    #поиск изменений в таблицу
    def onCellChanged(self, row, column):
        #выделенная строка
        indices = self.table.selectionModel().currentIndex().row()

        
        if indices!=-1 :
            item = self.table.item(row, column)
            lastState = item.data(LastStateRole)
            currentState = item.checkState()
            kassa_price_id=[]
            #если тпблица изменилась
            #print(str(self.table.cellWidget(indices,2)))
            if str(self.table.cellWidget(indices,2)).find("QComboBox")!=-1:
                a=self.table.cellWidget(indices,2).currentText()
                
                b=self.table.item(indices,4).text()
            else: 
                a=self.table.cellWidget(indices,2).text()
                b=self.table.cellWidget(indices,4).text()
                
            if currentState != lastState and a!='' and b!='':
                #обновляется колво и цена
                
                rowPosition = self.table.rowCount()
                cursor=connection.cursor()
                cursor.execute(r"UPDATE  kassa_basket SET quantity="+a+
                " WHERE id="+self.table.item(indices,0).text())
                connection.commit()
                cursor.execute(r"UPDATE  kassa_basket SET price="+b+
                " WHERE id="+self.table.item(indices,0).text())
                connection.commit()
                cursor.execute(r"SELECT  kassa_price_id,kassa_goods_id FROM KASSA_BASKET WHERE id="+self.table.item(indices,0).text())
                for row1 in cursor: kassa_price_id.append(row1)
                if kassa_price_id[0].get("kassa_price_id")!=0:
                    cursor.execute(r"UPDATE  kassa_price SET price="+b+
                    " WHERE id="+str(kassa_price_id[0].get("kassa_price_id")))
                
                
                else:
                    print(b,str(kassa_price_id[0].get("kassa_goods_id")))
                    cursor=connection.cursor()
                    cursor.execute(
                    r"""INSERT INTO kassa_price (dt,kassa_wb_id,price,kassa_goods_id)
                    values("2019-11-04 00:00:00",0,"""+b+','+str(kassa_price_id[0].get("kassa_goods_id"))+")")
                
                
                connection.commit()
                #self.table.setItem(indices, 6, QTableWidgetItem(str(float(self.table.cellWidget(indices,2).text())*float(self.table.cellWidget(indices,4).text()))))
                
              
    def on_combobox_changed_fio(self):
        #print("FGGDFGFHGFDH")
        #print(self.comboBox.currentText())
        ##print("идекс",self.table.item(indices,2))

        connection.commit()
        cursor.execute(r"UPDATE  kassa_kassir SET current="+'0')
        cursor.execute(r"UPDATE  kassa_kassir SET current="+'1'+" WHERE fio='"+self.comboBox.currentText()+"'")              
        connection.commit()  
        self.qle.setFocus(0)
    def on_combobox_changed(self,rozliv,combo_v):
        indices = self.table.selectionModel().currentIndex().row()
        ##print("идекс",self.table.item(indices,2))
        for i in rozliv:
            if str(i.get("volume"))==combo_v.currentText():
                price=i.get("price")
                self.table.setItem(indices, 4, QTableWidgetItem(str(price)))
                self.table.setItem(indices, 6, QTableWidgetItem(str(price)))
            else:
                
                price=rozliv[0].get("price")                
        

        
    '''
    def onChanged(self):
        self.keyReleaseEvent()
    '''
    def regim_vozvrat(self):
        self.zakr_okno()
        self.new_kassa_chek_butt()
        self.pushButton_6.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        #self.pushButton_24.hide()
        #self.pushButton_25.hide()
        self.pushButton_26.setEnabled(False)
        self.pushButton_27.setEnabled(False)
        self.pushButton_28.setEnabled(False)
        self.pushButton_29.setEnabled(False)
        self.pushButton_30.setEnabled(False)
        self.pushButton_31.setEnabled(False)
        self.pushButton_23.setEnabled(False)
        self.pushButton_10.show()
        self.pushButton_32.show()
        self.pushButton_23.hide()
        self.label_6.show()
        self.regim_vozvr=True
    
    def otmena_vozvr(self):
        a=self.label_number_chek.text()
        a=a[5:]
        cursor=connection.cursor()
        cursor.execute("""
        DELETE FROM kassa_basket WHERE  number_kassa="""+str(a))
        connection.commit()
        #self.zakr_okno()
        self.new_kassa_chek_butt()
        self.pushButton_6.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        #self.pushButton_24.hide()
        #self.pushButton_25.hide()
        self.pushButton_26.setEnabled(True)
        self.pushButton_27.setEnabled(True)
        self.pushButton_28.setEnabled(True)
        self.pushButton_29.setEnabled(True)
        self.pushButton_30.setEnabled(True)
        self.pushButton_31.setEnabled(True)
        self.pushButton_23.setEnabled(True)
        self.pushButton_10.hide()
        self.pushButton_32.hide()
        self.pushButton_23.show()
        self.label_6.hide()
        self.regim_vozvr=False
        
            
                                      
    def regim_vozvr_shtrih(self,pole):
        cursor=connection.cursor()
        connection.commit()
        info_pokupka=[]
        quantity=[]
        if len(pole)>17:
            self.regim_vozvr_marka(pole)


        elif len(pole)!=0 and len(pole)<3 or pole.isdigit()==False:
            self.tovar_never_vvod()


        else:
                                      
            cursor=connection.cursor()                       
            if cursor.execute("SELECT id,kassa_goods_id,kassa_rests_id,kassa_price_id,fullname,quantity,shtrih,price,edizm_id,marka,markatovar FROM kassa_check_positions where shtrih='"+str(pole)+"'")==0:
                self.error("Товар не числится проданным! Обратитесь в тех.поддержку.")
            else:
                for row1 in cursor: info_pokupka.append(row1)
            
                if len(info_pokupka)>1:
                    self.open_dialog_vozvat(info_pokupka)
                else:
                    self.alon_vozvrat(info_pokupka)
                                      
    def alon_vozvrat(self,info_pokupka):
        cursor2=connection.cursor()
        if info_pokupka[0].get("marka")=='':
            cursor2.execute("SELECT id,quantity,kassa_ulonsaleplace_id FROM kassa_rests where id="+str(info_pokupka[0].get("kassa_rests_id")))
            for row1 in cursor2:quantity.append(row1)
            self.new_stroka(info_pokupka,quantity,info_pokupka[0].get("shtrih"),'-'+str(info_pokupka[0].get("price")),
                            info_pokupka[0].get("kassa_price_id")," ",'-'+info_pokupka[0].get("price"),[])
        else:
                              
            self.lineEdit_2.show()

            self.qle1=self.lineEdit_2

            self.qle.setDisabled(True)
            self.qle1.setFocus(0)
                                    
        
    def regim_vozvr_marka(self,pole):
        info_pokupka=[]
        quantity=[]
        if len(pole)>17:
            cursor=connection.cursor()
            cursor2=connection.cursor()
            if cursor.execute("SELECT id,kassa_goods_id,kassa_rests_id,kassa_price_id,fullname,quantity,shtrih,price,edizm_id,marka,markatovar FROM kassa_check_positions where marka='"+str(pole)+"'")==0:
                self.error("Товар не числится проданным! Обратитесь в тех.поддержку.")
            
            elif cursor2.execute("SELECT marka FROM kassa_basket where marka='"+str(pole)+"'")!=0 :
                self.error("Товар находится в коризне!")

            else:
                cursor2=connection.cursor()
                for row1 in cursor: info_pokupka.append(row1)
                
                cursor2.execute("SELECT id,quantity,kassa_ulonsaleplace_id FROM kassa_rests where id="+str(info_pokupka[0].get("kassa_rests_id")))
                for row1 in cursor2:quantity.append(row1)
                self.new_stroka(info_pokupka,quantity,info_pokupka[0].get("shtrih"),'-'+str(info_pokupka[0].get("price")),
                                info_pokupka[0].get("kassa_price_id"),pole,'-'+str(info_pokupka[0].get("price")),[])
                self.qle.setDisabled(False)
        else:
            self.error("Неверный ввод!")
    
                  
                                      
    #функция, срабатывающая при не пустой корзине при открытии приложения
    def zapolnenie(self,number_shek):
        
        desktop=QtWidgets.QApplication.desktop()
        w=desktop.width()/2
        h=desktop.height()



        self.table.setHorizontalHeaderLabels(["","НАИМЕНОВАНИЕ", "КОЛ-ВО","","   ЦЕНА   "," ОСТАТОК ","   СУММА   "," "])
        fnt = self.table.font()
        
        for i in range(0,8):
            self.table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)

        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        #колонки по размерности текста
        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #колонка названия товара растягивается максимально
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for i in range(2,8):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        indices = int(self.table.selectionModel().currentIndex().row())

            
        info_pokupka=[]
        connection.commit()
        cursor1=connection.cursor()
        
        cursor1.execute("SELECT kassa_goods_id,pos,quantity,fullname, edizm_id,price,kassa_rests_id,shtrih,marka,rozliv FROM kassa_basket WHERE NUMBER_kassa="+str(number_shek))
        for row1 in cursor1: info_pokupka.append(row1)
        info_pokupka.reverse()
        

        id_pok=[]
        cursor=connection.cursor()
        cursor.execute("SELECT id FROM kassa_basket where NUMBER_kassa="+str(number_shek))
        for row1 in cursor: id_pok.append(row1)
        id_pok.reverse()

        
        quantity=[]
        ed_izm=[]
        alc_harakter=[]
        for i in range (0,len(info_pokupka)):

            cursor1=connection.cursor()
            cursor1.execute("SELECT quantity FROM kassa_rests where kassa_goods_id="+str(info_pokupka[i].get('kassa_goods_id')))
            for row1 in cursor1:quantity.append(row1)
        #quantity.reverse()
        alc_id=[]
                  
        for i in range (0,len(info_pokupka)):

            cursor1=connection.cursor()
            cursor1.execute("SELECT PRODUCTVCODE,CAPACITY,ALCVOLUME,KASSA_GOODS_ID FROM kassa_GOODS_ALC where kassa_goods_id="+str(info_pokupka[i].get('kassa_goods_id')))
            for row1 in cursor1:alc_harakter.append(row1)
        print(alc_harakter)
        for i in alc_harakter:
            alc_id.append(i.get("KASSA_GOODS_ID"))
        print(alc_id)
        alc_mrc=[]
        for i in alc_harakter:
            cursor1=connection.cursor()
            cursor1.execute("SELECT price FROM egais_mrc where PRODUCTVCODE="+str(i.get('PRODUCTVCODE')))
            for row1 in cursor1:alc_mrc.append(row1)
        print(alc_mrc)

        for i in range (0,len(info_pokupka)):
            if info_pokupka[i].get('edizm_id')=="ed":
                ed_izm.append("шт    ")
                
            if info_pokupka[i].get('edizm_id')=="l":
                ed_izm.append("л    ")
            if info_pokupka[i].get('edizm_id')=="kg":
                ed_izm.append("кг    ")
            if info_pokupka[i].get('edizm_id')=="ml":
                ed_izm.append("мл    ")
                
        #self.table.doubleClicked.connect(self.click_clear)
        c=0
        for i in range (0,len(info_pokupka)):
            self.table.insertRow(i) 
            btnkn = QPushButton()
            pole_vv_kolvo = QLineEdit(self)
            pole_vv_kolvo.setMaxLength(7)
            pole_vv_text = QTextEdit(self)
            pole_vv_text.setMaximumHeight(90)
            pole_vv_text.setReadOnly(True)
            
            val_kolvo=QtGui.QRegExpValidator(QtCore.QRegExp("[0-9][0-9][0-9]") )
            val_kolvo_decimal=QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+(\.[0-9][0-9][0-9]?)?") )
            val_price = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+(\.[0-9][0-9]?)?") )
            #val.setNotation(QtGui.QDoubleValidator.StandardNotation)
            #val.setRange(0.00,10000.00,2)
            pole_vv_kolvo.setValidator(val_kolvo) 
           
            
            pole_vv_price = QLineEdit(self)   
            pole_vv_price.setMaxLength(7)
            pole_vv_price.setText(str(info_pokupka[i].get('price')))
            if(int(info_pokupka[i].get('price')))==0:
                pole_vv_price.setStyleSheet("border: 1px solid red;")
            pole_vv_kolvo.setAlignment(QtCore.Qt.AlignCenter)
            
            pole_vv_kolvo.textChanged.connect(self.summa_kolvo)
            pole_vv_price.textChanged.connect(self.summa_price)
            pole_vv_price.setValidator(val_price)
            pole_vv_price.setAlignment(QtCore.Qt.AlignCenter)
            
            
            
            #btnkn.setText('удалить')
            btnkn.clicked.connect(self.delete_stroka)
            #self.table.setRowHeight(i,120) 
                  
            icon_b = QtGui.QIcon()
            icon_b.addPixmap(QtGui.QPixmap("delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            btnkn.setIcon(icon_b)
            btnkn.setIconSize(QtCore.QSize(60, 60))
                
            pole_vv_kolvo.setStyleSheet("border: 0px solid red;")
            #pole_vv_price.setStyleSheet("border: 0px solid red;")
                  
           
            pole_vv_text.setStyleSheet("border: 0px solid red;")
            if info_pokupka[i].get('edizm_id')=="ed" and info_pokupka[i].get('shtrih')!='00000011111':
                pole_vv_kolvo.setText(str(int(info_pokupka[i].get('quantity'))))
                pole_vv_kolvo.setValidator(val_kolvo) 
                if(int(info_pokupka[i].get('quantity')))==0:
                   pole_vv_kolvo.setStyleSheet("border: 1px solid red;")
                   

            else:
                pole_vv_kolvo.setText(str(info_pokupka[i].get('quantity')))
                pole_vv_kolvo.setValidator(val_kolvo_decimal) 
                if(str(info_pokupka[i].get('quantity')))=='0.0':
                   pole_vv_kolvo.setStyleSheet("border: 1px solid red;")
                
            #заполняем все стобцы
            print(int(info_pokupka[i].get('price')))
            
            self.table.setCellWidget(i, 7, btnkn)   
            a="""
                <html><head>
                  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                  <title>Текст</title>  <style>colortext {color: Grey;  font-size: 10pt;}</head><body> <p>"""
            b="</p> </body></html>"
            if info_pokupka[i].get('kassa_goods_id') in alc_id:
                print(c)
                if info_pokupka[i].get("rozliv")==0:
                    price_mrc=alc_mrc[c].get('price')
                    pvp=pole_vv_price
                  
                  
                  
                    self.proverka_mrc(price_mrc,pvp)
                    pole_vv_price.textChanged.connect(lambda:self.proverka_mrc(price_mrc,pvp))

                    pole_vv_text.setText(a+info_pokupka[i].get('fullname')+" "+str(alc_harakter[c].get("ALCVOLUME"))+"% "+
                            str(alc_harakter[c].get("CAPACITY"))+"<br/>"+'<colortext>'+
                        info_pokupka[i].get('shtrih')+"<br/>"+
                                         info_pokupka[i].get('marka')+"</colortext>"+b)
                else:

                    pole_vv_text.setText(a+"РОЗЛИВ: "+info_pokupka[i].get('fullname')+" "+str(alc_harakter[c].get("ALCVOLUME"))+"% "+
                            str(alc_harakter[c].get("CAPACITY"))+"<br/>"+'<colortext>'+
                        info_pokupka[i].get('shtrih')+"<br/>"+
                                         info_pokupka[i].get('marka')+"</colortext>"+b)                  
                  
                  
                c+=1
            #self.table.setItem(i, 0, QTableWidgetItem("№"+str(info_pokupka[i].get('pos'))))
            else:
                
                pole_vv_text.setText(a+info_pokupka[i].get('fullname')+"<br/>"+'<colortext>'+
                                     info_pokupka[i].get('shtrih')+"<br/>"+
                                     info_pokupka[i].get('marka')+"</colortext>"+b)
            #self.table.setItem(i, 1, QTableWidgetItem(info_pokupka[i].get('fullname')+'n'+info_pokupka[i].get('shtrih')+'n'+info_pokupka[i].get('marka')))
            self.table.setCellWidget(i,1, pole_vv_text) 
            self.table.setCellWidget(i, 2, pole_vv_kolvo) 
            #self.table.setItem(i, 2, QTableWidgetItem(str(info_pokupka[i].get('quantity'))))
            self.table.setItem(i, 3, QTableWidgetItem(ed_izm[i]))
            self.table.setCellWidget(i, 4, pole_vv_price) 
            #self.table.setItem(i, 4, QTableWidgetItem(str(info_pokupka[i].get('price'))))
            if str(quantity[i].get('quantity'))=='-1.0':
                self.table.setItem(i, 5, QTableWidgetItem('---'))
            else:
                self.table.setItem(i, 5, QTableWidgetItem(str(quantity[i].get('quantity'))))
            if  info_pokupka[i].get("rozliv")!=1:
                a= self.toFixed(float(self.table.cellWidget(i,2).text())*float(self.table.cellWidget(i,4).text()),2)   
                self.table.setItem(i, 6, QTableWidgetItem(str(a)))
            else:
                a= self.toFixed(float(self.table.cellWidget(i,4).text()),2)
                self.table.setItem(i, 6, QTableWidgetItem(str(a)))
                  
            self.table.setItem(i, 0, QTableWidgetItem(str(id_pok[i].get("id"))))
            
            
            self.table.item(i, 0).setFlags(QtCore.Qt.ItemIsEnabled)
            #self.table.item(i, 1).setFlags(QtCore.Qt.ItemIsEnabled)
            if info_pokupka[i].get("marka")!=' ':
                pole_vv_kolvo.setReadOnly(True)
                #self.table.item(i,2).setFlags(QtCore.Qt.ItemIsEnabled)
                
            self.table.item(i,3).setFlags(QtCore.Qt.ItemIsEnabled)    
            self.table.item(i,5).setFlags(QtCore.Qt.ItemIsEnabled)
            self.table.item(i,6).setFlags(QtCore.Qt.ItemIsEnabled)
            self.table.item(i, 0).setBackground(QtGui.QColor(250, 239, 214))
                  
            self.table.item(i, 0).setForeground(QBrush(QColor(250, 239, 214)))
            
        #self.table.cellChanged.connect(self.onCellChanged)
        self.table.resizeRowsToContents () 

        self.itogo()

        k=0     
        if info_pokupka!=[]:
            if info_pokupka[i].get('kassa_goods_id') in alc_id:

                if info_pokupka[i].get("rozliv")==0:
                    price_mrc=alc_mrc[k].get('price')
                    pvp=pole_vv_price

                    self.proverka_mrc(price_mrc,pvp)

            k+=1
        
        
    def click_clear(self):
        indices1 = int(self.table.selectionModel().currentIndex().row())
        indices2 = int(self.table.selectionModel().currentIndex().column())
        #print(indices1,indices2)
        if indices2==2 or indices2==4:
            self.table.setItem(indices1, indices2, QTableWidgetItem(''))
    #перевод из 36 системы в 10 (марка старого образца)
    def convert_base(self,num, to_base=10, from_base=36):
        to_base=10
        from_base=36
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return self.convert_base(n // to_base, to_base) + alphabet[n % to_base] 
    #открыть окно для ввода нового товара
    def open_dialog (self,info_pokupka ) :
        dialog = dop_okno(self,info_pokupka)
        dialog .setWindowModality(Qt.ApplicationModal)
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            self.qle.setFocus(0)

            info_pokupka1=[]
            i=dialog.table1.selectionModel().currentIndex().row()
            #print(info_pokupka[i])
            info_pokupka1.append(info_pokupka[i])
            
            self.alone_shtrich(info_pokupka1)
            
        else:
            self.qle.clear()
                  
                  
    def open_dialog_vozvat (self,info_pokupka ) :
        dialog = dop_okno_vozvrat(self,info_pokupka)
        dialog .setWindowModality(Qt.ApplicationModal)
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            self.qle.setFocus(0)

            info_pokupka1=[]
            i=dialog.table1.selectionModel().currentIndex().row()
            #print(info_pokupka[i])
            info_pokupka1.append(info_pokupka[i])
            
            self.alon_vozvrat(info_pokupka1)
            
        else:
            self.qle.clear()       
                
    def open_dialog2 (self) :
        dialog = dop_okno_podbor(self)
        result = dialog.exec_()
        
        #self.dialog.setWindowModality(Qt.ApplicationModal)
        if result == QtWidgets.QDialog.Accepted:
            self.qle.setFocus(0)
            i=dialog.table1.selectionModel().currentIndex().row()
            a=dialog.table1.item(i,0).text()
            connection.commit()
            info_pokupka=[]
            cursor2=connection.cursor()
            cursor2.execute("SELECT id,fullname,shtrih,edizm_id,fullname2,marka,markatovar FROM kassa_goods where id="+str(a))
            for row1 in cursor2: info_pokupka.append(row1)
            #print(info_pokupka)
            #print(a)
            self.alone_shtrich(info_pokupka)        


    def open_dialog_3 (self ) :
        dialog = Vvod_new_tovar(self)
        dialog.setWindowModality(Qt.ApplicationModal)
        result = dialog.exec_()
        

        # Здесь получаем данные из диалогового окна
        if result == QtWidgets.QDialog.Accepted:
            self.qle.setFocus(0)
            #print("Нажата кнопка Cancel")
            connection.commit()
            cursor2=connection.cursor()
            cursor2.execute("SELECT MAX(id) FROM kassa_GOODS ")
            number_id=[]
            for row1 in cursor2: number_id.append(row1) 
            info_pokupka1=[]
            cursor2=connection.cursor()    
            cursor2.execute("SELECT id,fullname,shtrih,edizm_id,fullname2,marka,markatovar FROM kassa_goods where id="+str(number_id[0].get('MAX(id)')))
            for row1 in cursor2: info_pokupka1.append(row1) 
                    

            self.alone_shtrich(info_pokupka1)  

            
    def open_dialog_4 (self ) :
        cursor1=connection.cursor()
        a=self.label_number_chek.text()
        a=a[len(a)-1]
        if cursor1.execute("SELECT* FROM kassa_basket")==0:                
            self.btn_delete_chek.setEnabled(False)
        else:
            self.btn_delete_chek.setEnabled(True)
            dialog = dop_okno_korz(self)
            dialog.setWindowModality(Qt.ApplicationModal)
            result = dialog.exec_()
            kassa=[]
            connection.commit()
            for i in range(0,len(ul)):
                cursor2=connection.cursor()
                cursor2.execute("SELECT price,number_kassa FROM kassa_basket")
            for row1 in cursor2: kassa.append(row1)
            a=0


            kassa_number=[]
            for i in kassa:
                kassa_number.append(i.get("number_kassa"))


            c = Counter(kassa_number)

            c=list(c)


            # Здесь получаем данные из диалогового окна
            if result == QtWidgets.QDialog.Accepted:
                self.qle.setFocus(0)
                i=dialog.table1.selectionModel().currentIndex().row()
                #print("ИДЕКС СТРОКИ",i,kassa_number)
                self.label_number_chek.setText("Чек №"+str(c[i]))

                position=[]


                connection.commit()
                cursor1=connection.cursor()
                cursor1.execute("SELECT COUNT(*) FROM kassa_basket WHERE NUMBER_KASSA="+str(c[i]))
                for row1 in cursor1: position.append(row1)
                if position[0].get('COUNT(*)')!=0:
                        self.table.setRowCount(0)
                        self.zapolnenie(c[i])
                        #self.table.cellChanged.connect(self.onCellChanged)                

                else: 


                    self.table.setRowCount(0)
                    #self.table.cellChanged.connect(self.onCellChanged) 
                

    def open_dialog_5 (self,vozvrat ) :
                
        cursor1=connection.cursor()
        b=self.label_number_chek.text()
        a=b[len(b)-1]
        if cursor1.execute("SELECT* FROM kassa_basket WHERE NUMBER_KASSA="+a)==0:                
            self.btn_opl.setEnabled(False)
        else:
            self.btn_opl.setEnabled(True)
                  
            dialog = dop_okno_opl(self,b,vozvrat)
            dialog.setWindowModality(Qt.ApplicationModal)
            result = dialog.exec_()                
            if result == QtWidgets.QDialog.Accepted:

                try:  

                    a=self.label_number_chek.text()
                    a=a[5:] #номер чеа из лэйбла (надпись над таблицей)
                    self.table.clear()
                    self.table.setRowCount(0)
                    self.zapolnenie(a)
                    info_pokupka=[]
                    oplata=[]
                    cursor1=connection.cursor()
                    cursor1.execute("SELECT id,price,fullname,number_kassa,quantity,shtrih,kassa_ulonsaleplace_id,kassa_goods_id,marka FROM kassa_basket where number_kassa="+str(a))
                    for row1 in cursor1: oplata.append(row1)
                    if oplata!=[]:
                        organizac_opl=[]
                        kolvo_kassa_ulonsaleplace_id=[]
                        for i in oplata:
                            kolvo_kassa_ulonsaleplace_id.append(i.get("kassa_ulonsaleplace_id"))
                        c = Counter(kolvo_kassa_ulonsaleplace_id)

                        spis_pok=c.values()

                        spis_pok=list(spis_pok)
                        c=list(c)

                        dialog.oplata_nalich(c,fl=1)
                        a=self.label_number_chek.text()
                        a=a[5:] #номер чеа из лэйбла (надпись над таблицей)
                except Exception as e:
                    print('Ошибка:\n', traceback.format_exc())
        
        
    def open_dialog_6 (self):
        if not self.gurnal_prWin:
            self.gurnal_prWin = gurnal_pr()
        self.gurnal_prWin.show()
        
                  
                  
    def open_win7(self) :
        dialog = dop_okno_vnesenie(self)
        result = dialog.exec_()
        
        #self.dialog.setWindowModality(Qt.ApplicationModal)
        if result == QtWidgets.QDialog.Accepted:
            
                      
            if self.number_driver==1:
                self.driver.vnesenie(dialog.lineEdit.text())
            elif self.number_driver==2:
                self.driver.vnesenie(dialog.lineEdit.text(),self.comboBox.currentText())
            elif self.number_driver==3:
                self.driver.vnesenie(int(dialog.lineEdit.text())*100)
                  
            self.qle.setFocus(0)
                  
                  
       
    def open_win8(self) :
        dialog = dop_okno_viemka(self)
        result = dialog.exec_()
        
        #self.dialog.setWindowModality(Qt.ApplicationModal)
        if result == QtWidgets.QDialog.Accepted:
            if self.number_driver==1:
                self.driver.vipl(dialog.lineEdit.text())
            elif self.number_driver==2:
                self.driver.vipl(dialog.lineEdit.text(),self.comboBox.currentText())
            elif self.number_driver==3:
                self.driver.vipl(int(dialog.lineEdit.text())*100)
            self.qle.setFocus(0)
            
    def quitApp(self): 
        QtCore.QCoreApplication.instance().quit() 
        
        
    
    def closeEvent(self, e):
        
        result = QtWidgets.QMessageBox.question(self,
        "Подтверждение закрытия окна",
        "Вы действительно хотите закрыть ОБЛАКО?",
         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
         QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
        else:
            e.ignore()
                  


                  

# In[30]:


class Controller:

    def __init__(self):
        pass

    def open_win1(self):
        self.window_two = Example()
        self.window_two.show() 
        #if not self.vvodnewtovarWin:
        #self.vvodnewtovarWin = Vvod_new_tovar(self)
        #self.vvodnewtovarWin.setWindowModality(Qt.ApplicationModal)

def main():
    #appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    if QApplication.instance() != None: 
        app = QApplication.instance() 
    else: 
        app = QApplication(sys.argv) 
                  
 
    controller = Controller()
    controller.open_win1()
    sys.exit(app.exec_())
    #exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    #sys.exit(exit_code)    
if __name__ == '__main__':  # Если мы з файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

