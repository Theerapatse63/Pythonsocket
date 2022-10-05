#chat.server.py

from pickle import TRUE
from pydoc import cli
import socket
import datetime
import threading

PORT = 7400
BUFSIZE = 4096
SERVERIP = ' localhost'

clist = [] #clientlist

def client_handler(client,addr):
    while True:
        try:
            data = client.recv(BUFSIZE)
        except:
            clist.remove(client)
            break

        if(not data) or (data.decode('utf-8') == 'q'):
            clist.remove(client)
            print('OUT',client)
        msg = str(addr) + '>>>> ' +data.decode('utf-8')
        print("USER: ",msg)
        print("-------------")
        for C in clist:
            C.sendall(msg.encode('utf-8')) #ส่งข้อความให้ทุกคนเห็น

    client.close()



server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.bind((SERVERIP,PORT))
server.listen(5)

while True:
    client,addr = server.accept()
    clist.append(client)
    print("ALL CLIENT",clist)


    Task = threading.Thread(target=client_handler , args= (client, addr))
    Task.start()
