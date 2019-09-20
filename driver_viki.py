#!/usr/bin/env python
# coding: utf-8

# In[1]:


import serial
import time
import operator
from functools import reduce
ser = serial.Serial()
ser.port='COM6'
ser.baudrate=57600
ser.parity=serial.PARITY_EVEN
ser.stopbits=serial.STOPBITS_ONE
ser.bytesize=serial.EIGHTBITS
ser.timeout=5
if ser.isOpen()==True:
    ser.close()
    ser.open()
    print("установлено")

else:
    pass
    

       
    
    
    
startbyte=b'\x02'
endByte = b'\x03'
packetId = b'\x28'
razd = bytes([0x1C])
password="PIRI"

class Driver_Viki:
    def proverka_podkl(self):
        if ser.isOpen()==True:
            return True
        else: return False
    
    def lrc(self,buff):
        """
        Расчет контрольной суммы.
        """
        return reduce(operator.xor, buff)


    def bytearray_cast(self,arg):
        if not isinstance(arg, bytearray):
            return bytearray(arg)
        return arg


    def bytearray_concat(self,*args):
        """
        Функция конкатенирования нескольких bytearray в один.
        """

        return self.bytearray_cast(reduce(operator.concat, args))
    
    
    def comanda(self,command,*args):
        command=command.encode('cp866')

        #a=[password.encode('cp866'),packetId,command,data1,razd,endByte]

        podsch_crc=self.bytearray_concat(password.encode('cp866'),packetId,command,*args,endByte)
        print(podsch_crc)
        b=self.bytearray_concat(startbyte,password.encode('cp866'),packetId,command,*args,endByte,hex(self.lrc(podsch_crc))[2:].encode('cp866'))
        
        
        #b=self.bytearray_concat(startbyte,password.encode('cp866'),packetId,command,endByte,hex(self.lrc(podsch_crc))[2:].encode('cp866'))
        
        ser.write(serial.to_bytes(self.bytearray_concat(b)))
        print("вывод",ser.read(20))


        
    def open_KKT(self,data,time):
        self.comanda('10',data.encode('cp866'),razd,time.encode('cp866'),razd)
    
    def close_KKT(self):
        ser.close()        
        
    #X-отчет
    def X_otchet(self,fio):
        self.comanda('20',fio.encode('cp866'),razd)
        
    #ЗАКРЫТЬ СМЕНУ    
    def closed_smen(self,fio,number):
        self.comanda('21',fio.encode('cp866'),razd,number.encode('cp866'),razd)
        
        
    #ОТКРЫТЬ СМЕНУ 
    def open_smena(self,fio):
        self.comanda('21',fio.encode('cp866'),razd)
    '''
    ОПЕРАЦИИ С ЧЕКОМ
    '''
    #открытие чека 
    def open_check(self,fio):
        self.comanda('30','2'.encode('cp866'),razd,'1'.encode('cp866'),razd,fio.encode('cp866'),razd)
        
        
    #открытие чека ВОЗВРАТА 
    def open_check_vozvr(self,name,number):
        self.comanda('30','3'.encode('cp866'),razd,'1'.encode('cp866'),razd,fio.encode('cp866'),razd)
        
        
    #РЕГИСТРАЦИЧ ПОЗИЦИИ В ЧЕКЕ 
    def registration_pos(self,name,shtrih,price,quantity):
        self.comanda('42',name.encode('cp866'),razd,shtrih.encode('cp866'),razd,quantity.encode('cp866'),razd,price.encode('cp866'),razd,'3'.encode('cp866'),razd,'1'.encode('cp866'),razd,'3'.encode('cp866'),razd)
    
    #подитог
    def itog(self):
        self.comanda('44')
        
    #оплата чека наличуой
    def oplata_nalich(self,summa):
        self.comanda('47','0'.encode('cp866'),razd,summa.encode('cp866'),razd,'ggg'.encode('cp866'),razd)
        
    #оплата чека по карте
    def oplata_karta(self,summa):
        self.comanda('47','1'.encode('cp866'),razd,summa.encode('cp866'),razd,'ggg'.encode('cp866'),razd)
        
    def annulir(self):
        self.comanda('32')
        
    def recvisit(self,text):
        self.comanda('49',"0".encode("cp866"),razd,"0".encode("cp866"),razd,text.encode("cp866"),razd)
        
    def qrcod(self,text):
        self.comanda('41',"0".encode("cp866"),razd,"8".encode("cp866"),razd,"8".encode("cp866"),razd,"8".encode("cp866"),razd,text.encode("cp866"),razd)
        
        
    #Закрытие полностью оплаченного чека
    def close_check(self):
        self.comanda('31','0'.encode('cp866'),razd,''.encode('cp866'),razd)
        
    #Внесение
    def vnesenie(self,summ,fio):
        self.comanda('30','4'.encode('cp866'),razd,'1'.encode('cp866'),razd,fio.encode('cp866'),razd)
        self.comanda('48','рубли'.encode('cp866'),razd,summ.encode('cp866'),razd)
        self.itog()
        self.close_check()
        
    #Внесение
    def vipl(self,summ,fio):
        self.comanda('30','5'.encode('cp866'),razd,'1'.encode('cp866'),razd,fio.encode('cp866'),razd)
        self.comanda('48','рубли'.encode('cp866'),razd,summ.encode('cp866'),razd)
        self.itog()
        self.close_check()
        
    #Внесение
    def beep(self):
        self.comanda('82','1000'.encode('cp866'),razd)
    




