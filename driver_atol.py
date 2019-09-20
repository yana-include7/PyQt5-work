#!/usr/bin/env python
# coding: utf-8

# In[4]:


from libfptr10 import IFptr
import os



location="C:/Users/yana.timofeeva/Downloads/10.5.1.0/10.5.1.0/nt-x64-msvc2015"
LIBRARY_PATH = os.path.dirname(os.path.abspath(location))
fptr = IFptr(os.path.join(LIBRARY_PATH, "fptr10.dll"))
port="COM8"
LIBRARY_PATH = os.path.dirname(os.path.abspath("C:/Users/yana.timofeeva/Downloads/10.5.1.0/10.5.1.0/nt-x64-msvc2015"))

fptr = IFptr(os.path.join(LIBRARY_PATH,"fptr10.dll"))

version = fptr.version()
print(version)


#НАСТРОЙКА ДРЙВЕРА
fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))
fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, "COM8")
fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))
fptr.applySingleSettings()

settings = fptr.getSettings() #выгрузка настроек

fptr.open() #установка соединения с ККТ оно -1
isOpened = fptr.isOpened() #установка логического соед возвращает 0

print(settings)

class Driver_Atol:
    location="C:/Users/yana.timofeeva/Downloads/10.5.1.0/10.5.1.0/nt-x64-msvc2015"
    
    def proverka_podkl(self):
        if fptr.open()==0: return True
        else:return False
    
    def open_KKT(self):
        LIBRARY_PATH = os.path.dirname(os.path.abspath("C:/Users/yana.timofeeva/Downloads/10.5.1.0/10.5.1.0/nt-x64-msvc2015"))

        fptr = IFptr(os.path.join(LIBRARY_PATH, "fptr10.dll"))

        version = fptr.version()
        print(version)
        #НАСТРОЙКА ДРЙВЕРА
        fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
        fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))
        fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, "COM4")
        fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))
        fptr.applySingleSettings()

        settings = fptr.getSettings() #выгрузка настроек

        print(fptr.open()) #установка соединения с ККТ оно -1
        isOpened = fptr.isOpened() #установка логического соед возвращает 0

        print(settings)
    
    def close_KKT(self):
        fptr.close()
    
    #регистрация кассы
    def registration_kassa(self,address,inn,name_org,email,addres1,inn_ofd,name_ofd):
        fptr.setParam(IFptr.LIBFPTR_PARAM_FN_OPERATION_TYPE, IFptr.LIBFPTR_FNOP_REGISTRATION)

        fptr.setParam(1060, "www.nalog.ru")

        fptr.setParam(1009, address)
        fptr.setParam(1018, inn) #ИНН организации
        fptr.setParam(1048,name_org)
        fptr.setParam(1062, IFptr.LIBFPTR_TT_OSN | IFptr.LIBFPTR_TT_PATENT)
        fptr.setParam(1117, email)
        fptr.setParam(1057, IFptr.LIBFPTR_AT_BANK_PAYING_AGENT | IFptr.LIBFPTR_AT_PAYING_AGENT | IFptr.LIBFPTR_AT_ATTORNEY)

        fptr.setParam(1187, address1)#Адрес места расчетов
        fptr.setParam(1037, "12345678900987654321")#Регистрационный номер устройства
        fptr.setParam(1209, IFptr.LIBFPTR_FFD_1_0_5)
        fptr.setParam(1001, False)
        fptr.setParam(1036, "513")
        fptr.setParam(1002, False)
        fptr.setParam(1056, False)
        fptr.setParam(1108, False)
        fptr.setParam(1109, False)
        fptr.setParam(1110, False)
        fptr.setParam(1126, False)
        fptr.setParam(1193, True)
        fptr.setParam(1207, False)
        fptr.setParam(1221, False)

        fptr.setParam(1017, inn_ofd) #	ИНН ОФД
        fptr.setParam(1046, name_ofd) #Название ОФД

        fptr.fnOperation()
    #переррегистрация кассы    
    def peregistration_kassa(self,address,inn,name_org,email,addres1,inn_ofd,name_ofd):
        fptr.setParam(IFptr.LIBFPTR_PARAM_FN_OPERATION_TYPE, IFptr.LIBFPTR_FNOP_REGISTRATION)

        fptr.setParam(1060, "www.nalog.ru")

        fptr.setParam(1009, address)
        fptr.setParam(1018, inn) #ИНН организации
        fptr.setParam(1048,name_org)
        fptr.setParam(1062, IFptr.LIBFPTR_TT_OSN | IFptr.LIBFPTR_TT_PATENT)
        fptr.setParam(1117, email)
        fptr.setParam(1057, IFptr.LIBFPTR_AT_BANK_PAYING_AGENT | IFptr.LIBFPTR_AT_PAYING_AGENT | IFptr.LIBFPTR_AT_ATTORNEY)

        fptr.setParam(1187, address1)#Адрес места расчетов
        fptr.setParam(1037, "12345678900987654321")#Регистрационный номер устройства
        fptr.setParam(1209, IFptr.LIBFPTR_FFD_1_0_5)
        fptr.setParam(1001, False)
        fptr.setParam(1036, "513")
        fptr.setParam(1002, False)
        fptr.setParam(1056, False)
        fptr.setParam(1108, False)
        fptr.setParam(1109, False)
        fptr.setParam(1110, False)
        fptr.setParam(1126, False)
        fptr.setParam(1193, True)
        fptr.setParam(1207, False)
        fptr.setParam(1221, False)

        fptr.setParam(1017, inn_ofd) #	ИНН ОФД
        fptr.setParam(1046, name_ofd) #Название ОФД

        fptr.fnOperation()    
        
        
        fptr.setParam(IFptr.LIBFPTR_PARAM_FN_OPERATION_TYPE, IFptr.LIBFPTR_FNOP_CHANGE_PARAMETERS)
        fptr.setParam(1101, 3)
        fptr.fnOperation() 
    #узнать сумму наличных в денежном ящике   
    def summa_nalich(self):
        
        fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_CASH_SUM)
        fptr.queryData()

        cashSum = fptr.getParamDouble(IFptr.LIBFPTR_PARAM_SUM)
        return cashSum  
        
    #сумма выручки
    def summa_v(self):
        fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_REVENUE)
        fptr.queryData()

        revenue = fptr.getParamDouble(IFptr.LIBFPTR_PARAM_SUM)
        
    #запрос колва чеков прихода
    def chek_pr(self):
        fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_RECEIPT_COUNT)
        fptr.setParam(IFptr.LIBFPTR_PARAM_RECEIPT_TYPE, IFptr.LIBFPTR_RT_SELL)
        fptr.queryData()

        count = fptr.getParamInt(IFptr.LIBFPTR_PARAM_DOCUMENTS_COUNT)
        
        
    #регистрация кассира ДЕЛАТЬ ПЕРЕД КАЖДОЙ ФИСКАЛЬНОЙ ОПЕРАЦИЕЙ    
    def kassir_registration(self,fio,number):
        fptr.setParam(1021, fio)
        fptr.setParam(1203, number) #id кассира
        fptr.operatorLogin()

        
    #ОТКРЫТЬ СМЕНУ 
    def open_smena(self,fio,number):
        fptr.setParam(1021, fio)
        fptr.setParam(1203, number) #id кассира
        fptr.operatorLogin()    
        fptr.openShift()
        print(fptr.openShift())
        fptr.checkDocumentClosed()
        
        
    #ЗАКРЫТЬ СМЕНУ    
    def closed_smen(self,fio,number):
        fptr.setParam(1021, fio)
        fptr.setParam(1203, number) #id кассира
        fptr.operatorLogin()            
        fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_CLOSE_SHIFT)
        fptr.report()
        print(fptr.report())
        fptr.checkDocumentClosed()
        
        
    '''
    ОПЕРАЦИИ С ЧЕКОМ
    '''
    #открытие чека 
    def open_check(self,name,number):
        fptr.setParam(1021, name)
        fptr.setParam(1203, number)
        fptr.operatorLogin()

        fptr.setParam(IFptr.LIBFPTR_PARAM_RECEIPT_TYPE, IFptr.LIBFPTR_RT_SELL)
        print(fptr.openReceipt())
        
    #открытие чека ВОЗВРАТА с автоматическим расчётом НДС18
    def open_check_vozvr(self,name,number):
        fptr.setParam(1021, name)
        fptr.setParam(1203, number)
        fptr.operatorLogin()

        fptr.setParam(IFptr.LIBFPTR_PARAM_RECEIPT_TYPE, IFptr.LIBFPTR_RT_SELL_RETURN)
        fptr.setParam(IFptr.LIBFPTR_PARAM_USE_VAT18, True)
        fptr.openReceipt()    
        
    #открытие ЭЛЕКТРОННОГО чека
    def open_elekrt_check(self,mail_or_number): 
        fptr.setParam(IFptr.LIBFPTR_PARAM_RECEIPT_TYPE, IFptr.LIBFPTR_RT_SELL)
        fptr.setParam(IFptr.LIBFPTR_PARAM_RECEIPT_ELECTRONICALLY, True)
        fptr.setParam(1008, mail_or_number)
        fptr.openReceipt()        
        
        
    #отмена чека
    def otmena_check(self):
        fptr.cancelReceipt()
        
    #регистрация позиции БЕЗ указания суммы налога
    def registration_pos(self,name,price,quantity):
        fptr.setParam(IFptr.LIBFPTR_PARAM_COMMODITY_NAME,name)
        fptr.setParam(IFptr.LIBFPTR_PARAM_PRICE, price)
        fptr.setParam(IFptr.LIBFPTR_PARAM_QUANTITY, quantity)
        fptr.setParam(IFptr.LIBFPTR_PARAM_TAX_TYPE, IFptr.LIBFPTR_TAX_VAT0)
        fptr.registration()
        
        
    #оплата чека наличуой
    def oplata_nalich(self,summa):
        fptr.setParam(IFptr.LIBFPTR_PARAM_PAYMENT_TYPE, IFptr.LIBFPTR_PT_CASH)
        fptr.setParam(IFptr.LIBFPTR_PARAM_PAYMENT_SUM, summa)
        fptr.payment()
        
        
    #оплата чека по карте
    def oplata_karta(self,summa):
        fptr.setParam(IFptr.LIBFPTR_PARAM_PAYMENT_TYPE, IFptr.LIBFPTR_PT_ELECTRONICALLY)
        fptr.setParam(IFptr.LIBFPTR_PARAM_PAYMENT_SUM, summa)
        fptr.payment()
    # Закрытие частично оплаченного или неоплаченного чека  
    def close_check_bez_opl(self):
        fptr.setParam(IFptr.LIBFPTR_PARAM_PAYMENT_TYPE, IFptr.LIBFPTR_PT_ELECTRONICALLY)
        fptr.closeReceipt()
        
    #Закрытие полностью оплаченного чека
    def close_check(self):
        fptr.closeReceipt()
        
    def QR_code(self,inf):
        fptr.setParam(IFptr.LIBFPTR_PARAM_SCALE, 5)
        fptr.setParam(IFptr.LIBFPTR_PARAM_ALIGNMENT,IFptr.LIBFPTR_ALIGNMENT_CENTER)
        fptr.setParam(IFptr.LIBFPTR_PARAM_BARCODE, inf)
        fptr.setParam(IFptr.LIBFPTR_PARAM_BARCODE_TYPE, IFptr.LIBFPTR_BT_QR)
        fptr.printBarcode()
        
    def stroka(self,inf):
        fptr.setParam(IFptr.LIBFPTR_PARAM_TEXT_WRAP , IFptr.LIBFPTR_TW_WORDS )
        fptr.setParam(IFptr.LIBFPTR_PARAM_TEXT, inf)
        fptr.printText()
        
    #Проверка закрытия документа (на примере закрытия фискального чека)
    def proverka_closed(self):
        fptr.closeReceipt()

        while fptr.checkDocumentClosed() < 0:
          # Не удалось проверить состояние документа. Вывести пользователю текст ошибки, попросить устранить неполадку и повторить запрос
          print(fptr.errorDescription())
          continue

        if not fptr.getParamBool(IFptr.LIBFPTR_PARAM_DOCUMENT_CLOSED):
          # Документ не закрылся. Требуется его отменить (если это чек) и сформировать заново
          fptr.cancelReceipt()
          return

        if not fptr.getParamBool(IFptr.LIBFPTR_PARAM_DOCUMENT_PRINTED):
          # Можно сразу вызвать метод допечатывания документа, он завершится с ошибкой, если это невозможно
          while fptr.continuePrint() < 0:
            # Если не удалось допечатать документ - показать пользователю ошибку и попробовать еще раз.
            print('Не удалось напечатать документ (Ошибка "%s"). Устраните неполадку и повторите.', fptr.errorDescription())
            continue
            
            
    #Допечатывание документа
    def dopechat(self):
        fptr.continuePrint()
        

    #Внесение
    def vnesenie(self,summ):
        fptr.setParam(IFptr.LIBFPTR_PARAM_SUM, summ)
        fptr.cashIncome()
        
    #Выплата
    def vipl(self,summ):
        fptr.setParam(IFptr.LIBFPTR_PARAM_SUM, summ)
        fptr.cashOutcome()        
        
    #X-отчет
    def X_otchet(self):
        fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_X)
        fptr.report()
        
    #Копия последнего документа
    def cope_doc_check(self):
        fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_LAST_DOCUMENT)
        fptr.report()
        
        
    # Демо-печать       
    def demo_pechat(self):
        fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_KKT_DEMO)
        fptr.report()
        
    #   Диагностика соединения с ОФД
    def diagn_ofd(self):
        fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_OFD_TEST)
        fptr.report()

