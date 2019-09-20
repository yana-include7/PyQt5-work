#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pyshtrih
def discovery_callback(port, baudrate):
    print(port, baudrate)
devices = pyshtrih.discovery(discovery_callback)
print(devices)
if devices!=[]:
    device = devices[0]
    device.connect()
class Driver_Shtrih():
    def proverka_podkl(self):
        if devices==[]:
            return False
        else: return True
    def vnesenie(self,summ):
        device.income(summ)
    def vipl(self,summ):
        device.outcome(summ)
    def closed_smen(self):
        device.z_report()
    def X_otchet(self):
        device.x_report()
    def open_check_dr(self):
        device.open_check(0)
    def registration_pos(self,m,tax1):
        device.sale(m,tax1)
    def close_check_dr(self,summ):
        device.close_check(summ)
    def cut_dr(self):
        device.cut(True)
    def annulir(self):
        device.cancel_check()
    def info_check(self):
        a=str(device.state())
        print(a)
        
        
        b=a.find("'Режим ФР':")+len("'Режим ФР':")
        c=a.find(", 'Подрежим ФР'")
        print(a[b:c])
        if a[b:c]==" 'Открытая смена, 24 часа не кончились.'":
            return True
        elif a[b:c]=="'Открытый документ.'":
            device.cancel_check()
        elif a[b:c]==" 'Открытая смена, 24 часа кончились.'":
            device.z_report()
            device.open_shift()
        elif a[b:c]==" 'Закрытая смена.'":
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            device.open_shift()
            
    def info_smena_open(self):
        
        a=str(device.state())
        print(a)
        
        b=a.find("'Режим ФР':")+len("'Режим ФР':")
        c=a.find(", 'Подрежим ФР'")
        print(print(a[b:c]))
        if a[b:c]==" 'Открытая смена, 24 часа не кончились.'":
            return True
        elif a[b:c]==" 'Открытый документ.'":
            device.cancel_check()
        elif a[b:c]==" 'Открытая смена, 24 часа кончились.'":
            device.z_report()
        elif a[b:c]==" 'Закрытая смена.'":
            return False
      
            
            
            
        
    

