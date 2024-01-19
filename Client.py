import socket
import sys
from Codes import *
import time

host = socket.gethostname()
port = 5252
secret = ""


def init():
    #global serverURL, port

    if len(sys.argv) == 1:
        host = 'localhost'
        port = 5252
    elif not len(sys.argv) == 3:
        raise "Arguments are: [host] [port], leave as blank for localhost"
    elif len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
    print( "Host: {0} Port: {1}".format(host, port))


def connect_to_sever():
    clientSocketA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print( "Connecting...")
    serverAddress = (host, port)
    notConnected = True

    while notConnected:
        try:
            clientSocketA.connect(serverAddress)
            notConnected = False
        except socket.error as msg:
            print( "No connection to: {0}".format(serverAddress))
            time.sleep(2)

    print( "Connected!")

    return clientSocketA
# end connectToSever


def handle_data(data, clientSocketA):
    #print("I am in handle data")
    data=data.decode('ASCII')
    if len(data) > 0:
        #print( "Data Received: " + str(data))

        if int(data[0]) == SEND_SECRET:
            print( "Aquiring Share")
            tmp = data.split("::")
            secret = tmp[1]
            print( "Share is: {0}".format(secret))
        elif int(data[0]) == GET_SECRET:
            secret=input( "Enter given Share")
            if secret != "":
                clientSocketA.sendall(bytes(secret,'utf-8'))
                print("Sent")
            else:
                print( "Secret is null")
                clientSocketA.sendall(bytes("I have no secret",'utf-8'))
        elif int(data[0]) == STOP_RECEIVING:
            print("Ending Client")
            clientSocketA.close()
            sys.exit()
        else:
            clientSocketA.sendall(bytes("Unknown Command",'utf-8'))
# end handleData


def main():
    clientSocketA = connect_to_sever()
    print("Waiting for Instruction")

    threadInputCmds = input("Enter Command ([s,g,e], h for help): ")
    threadInputCmds =bytes(threadInputCmds,'utf-8')
    #clientSocketB.send(threadInputCmds)
    while threadInputCmds != b'e':
        time.sleep(2)
        #print("Listening...")
        clientSocketA.send(threadInputCmds)
        data = clientSocketA.recv(SOCKET_SIZE)
        #print(data)
        #if(data==b'0'):
            #sec=input("Enter your share")
        '''    sec=bytes(sec,'utf-8')
            clientSocketA.send(sec)
            data = clientSocketA.recv(SOCKET_SIZE)
            print(data)'''
        #print("Data[0]")
        dat=data.decode('ASCII')
        #print(dat[0])
        #print("data length")
        #print(len(data))
        handle_data(data, clientSocketA)
        threadInputCmds = input("Enter Command ([s,g,e], h for help): ")
        threadInputCmds =bytes(threadInputCmds,'utf-8')
    
    # end while

    print( "Closing Client Socket")
    clientSocketA.close()
# end main


init()
main()


