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
    clientSocketB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print( "Connecting...")
    serverAddress = (host, port)
    notConnected = True

    while notConnected:
        try:
            clientSocketB.connect(serverAddress)
            notConnected = False
        except socket.error as msg:
            print( "No connection to: {0}".format(serverAddress))
            time.sleep(2)

    print( "Connected!")

    return clientSocketB
# end connectToSever


def handle_data(data, clientSocketB):
    global secret
    data=data.decode('ASCII')
    if len(data) > 0:
        #print( "Data Received: " + str(data))

        if int(data[0]) == SEND_SECRET:
            print( "Aquiring Shares")
            tmp = data.split("::")
            secret = tmp[1]
            print( "Secret is: {0}".format(secret))
        elif int(data[0]) == GET_SECRET:
            print( "Sending My Secret: {0}".format(secret))
            if secret != "":
                clientSocketB.sendall(bytes(secret,'utf-8'))
                print("Sent")
            else:
                print( "Secret is null")
                clientSocketB.sendall(bytes("I have no secret",'utf-8'))
        elif int(data[0]) == STOP_RECEIVING:
            print("Ending Client")
            clientSocketB.close()
            sys.exit()
        else:
            clientSocketB.sendall(bytes("Unknown Command",'utf-8'))
# end handleData


def main():
    clientSocketB = connect_to_sever()
    print("Waiting for Instruction")
    
    threadInputCmds = input("Enter Command ([s,g,e], h for help): ")
    threadInputCmds =bytes(threadInputCmds,'utf-8')
    #clientSocketB.send(threadInputCmds)
    while threadInputCmds != b'e':
        time.sleep(2)
        #print("Listening...")
        clientSocketB.send(threadInputCmds)
        data = clientSocketB.recv(SOCKET_SIZE)
        if(data==b'0'):
            sec=input("Enter your share")
        #print("Data in main "+str(data.decode('ASCII')))
        handle_data(data, clientSocketB)
        threadInputCmds = input("Enter Command ([s,g,e], h for help): ")
        threadInputCmds =bytes(threadInputCmds,'utf-8')
    
    # end while

    print( "Closing Client Socket")
    clientSocketB.close()
# end main


init()
main()


