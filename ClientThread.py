import threading
from Codes import *
import socket
global connection
class ClientThread(threading.Thread):
    def __init__(self, tcpServer, cmd):
        threading.Thread.__init__(self)
        #self.connection = connection
        #(connection, (ip,port)) = tcpServer.accept()
        self.cmd = cmd
        self.secretPart = None


    def run(self):
        try:
            if self.cmd == "s":
                print("1")
                self.send_to_clients()
            elif self.cmd == "g":
                self.recv_secret_from_clients()
        except:
            print("Error")


    def send_to_clients(self):
        print("I am inside send_to_clients")
        global connection
        print("Connection: "+connection)
        lenSending = len(self.secret)
        protocolTx = str(SEND_SECRET) + SEPERATOR
        msg = protocolTx + self.secret
        print("Message: "+msg)
        print("2")
        connection.send(bytes(msg,'utf-8'))
        print("3")
        print( "Secret Shared...")


    def recv_secret_from_clients(self):
        self.connection.send(str(GET_SECRET))
        data = self.connection.recv(SOCKET_SIZE)
        self.secretPart = data
        print( "Secret Recieved...")


    def has_secret_part(self):
        return not self.secretPart == None
