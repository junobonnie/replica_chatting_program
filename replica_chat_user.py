# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:27:06 2020

@author: user
"""

import socket
from threading import Thread

print(u'(주)레플리카 SW, 2020-11-02, Developer: Kang Junho')
print(u'''
          ______  _____ ______  _     _____  _____   ___       _____  _    _ 
          | ___ \|  ___|| ___ \| |   |_   _|/  __ \ / _ \     /  ___|| |  | |
          | |_/ /| |__  | |_/ /| |     | |  | /  \// /_\ \    \ `--. | |  | |
          |    / |  __| |  __/ | |     | |  | |    |  _  |     `--. \| |/\| |
          | |\ \ | |___ | |    | |_____| |_ | \__/\| | | |    /\__/ /\  /\  /
          \_| \_|\____/ \_|    \_____/\___/  \____/\_| |_/    \____/  \/  \/ \n\n''')
          
HOST = input(u'호스트 IP주소를 써주세요: ')
PORT = int(input(u'호스트의 PORT번호를 써주세요: '))
#HOST = '4.tcp.ngrok.io'#'localhost'
#PORT = 14198#10361


def rcvMsg(sock):
   while True:
      try:
         data = sock.recv(1024)
         if not data:
            break
         print(data.decode())
      except:
         pass

def runChat():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((HOST, PORT))
      t = Thread(target=rcvMsg, args=(sock,))
      t.daemon = True
      t.start()

      while True:
         msg = input()
         if msg == '/quit':
            sock.send(msg.encode())
            break

         sock.send(msg.encode())
            
runChat()




