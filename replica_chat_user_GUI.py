# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:03:12 2020

@author: user
"""
from tkinter import *
import socket
import threading


opening_msg=u'''\n                 (주)레플리카 SW,   2020-11-02,   Developer: Kang Junho
            
                                                    REPLICA SW\n\n\n'''
          
#HOST = input(u'호스트 IP주소를 써주세요: ')
#PORT = int(input(u'호스트의 PORT번호를 써주세요: '))


def sendMsg(event):
    global sock
    global entry1
    msg = entry1.get()
    entry1.delete(0, END)
    #if not msg:
    try:
        sock.send(msg.encode())
    except:
        text1.insert(END,'[ERROR] 서버와의 연결이 끊겼습니다!\n')
        text1.see(END)
    
def rcvMsg(sock):
    global text1
    while True:
        data = sock.recv(1024)
        if not data:
            break
        text1.insert(END,data.decode()+'\n')
        text1.see(END)
    

def select(self):
    value=scale1.get()/100
    window.attributes('-alpha', value)
   
    
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',9000))
#sock.connect(('4.tcp.ngrok.io',13266))

window = Tk()
window.title("REPLICA Chatting Program")
window.geometry("680x550")
window.resizable(0,0)

frame1 = Frame(window)
frame1.place(x=20, y=15)
        
text1 = Text(frame1, width=70,height=25,bg="black",font=('Raavi',-17,'bold'), fg='white')
text1.insert(1.0, opening_msg)
text1.pack(side='left')
#text1.configure(state='disabled')  
    
scroll1 = Scrollbar(frame1)
scroll1.pack(side='right',fill="y")
scroll1.configure(command=text1.yview)
text1.configure(yscrollcommand=scroll1.set)

        
entry1 = Entry(window, width=70, font=('Raavi',-17,'bold'), bg="white")

thread1 = threading.Thread(target=rcvMsg,args=(sock,))
thread1.daemon = True
thread1.start() 

var=IntVar()   
scale1 = Scale(window, variable=var, command=select, orient="horizontal", showvalue=False, tickinterval=100, from_=15, to=100, length=300)
scale1.place(x=350, y=525)
scale1.set(100)
entry1.place(x=20, y=500)
  
window.bind('<Return>', sendMsg)  
window.mainloop()
try:
    sock.send('/name'.encode())
    sock.send('/quit'.encode())
    sock.close()
except:
    pass
