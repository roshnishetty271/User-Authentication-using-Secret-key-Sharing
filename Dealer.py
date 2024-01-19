import socket
from _thread import *
#from threading import thread
import sys
from Codes import *
#import time
#import ClientThread
import ShamirScheme
from socketserver import ThreadingMixIn
from sslib import shamir

'''-----------------------------------'''
import threading

import socket
global connection
sh=[]
class ClientThread(threading.Thread):
    def __init__(self, ip,port, cmd):
        threading.Thread.__init__(self)
        self.ip= ip
        #(connection, (ip,port)) = tcpServer.accept()
        self.port = port
        self.cmd=cmd
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
        #print("I am inside send_to_clients")
        
        
        lenSending = len(self.secret)
        protocolTx = str(SEND_SECRET) + SEPERATOR
        #protocolTx=" Share-->"
        msg = protocolTx + self.secret
        #print("Message: "+msg)
        #print("2")
        connection.send(bytes(msg,'utf-8'))
        #print("3")
        print( "Secret Shared...")


    def recv_secret_from_clients(self):
        gets=str(GET_SECRET)
        connection.send(bytes(gets,'utf-8'))
        data = connection.recv(SOCKET_SIZE)
        data=data.decode('ASCII')
        self.secretPart = str(data)
        print( "Secret Recieved...")
        sh.append(data)
        print(sh)
        return sh



    def has_secret_part(self):
        return not self.secretPart == None


'''------------------------------------'''








global num_shares
global connection
numClientsOnline=0

host = ''
port = 5252
secret = ""
num_shares = -1
threads = []
threadInputCmds = "X"
threshold = -1
global serverSocket
def goto(linenum):
    global line
    line = linenum

line = 1
def init():
    pass

''' def init():
    global host, port, serverAddress

    # print socket.geta
    if len(sys.argv) == 1:
        host = "localhost"
        port = 5252
    elif not len(sys.argv) == 3:
        print( "Arguments are: [host] [port], leave as blank for localhost")
        sys.exit()
    elif len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2]) '''


def get_arguments(allArgs=True):
    global secret, threshold

    print( "Leave all Blank for default values")
    print("Enter a Secret (String): ")
    secret = input()
    f = open("C:\\Users\\Hp\\Documents\\pwd.txt", "w")
    f.write(secret)
    f.close()
    if secret == "":
        secret = "thisisasharedsecretvaluethatwillbesharedwithNusersandaTthreshold"

    if allArgs:
        print( "Enter Max Number of Clients: ")
        num_shares = -1

        while num_shares < 0:
            num_shares = get_user_input()

            try:
                if num_shares == "":
                    num_shares = "2"
                elif int(num_shares) <= 1:
                    num_shares = -1
                    print( "Number of Clients must be greater than 1: ")

                num_shares = int(num_shares)
            except:
                num_shares = -1
                print( "Number of Clients must be a number: ")
        # end while

        print( "Enter a Threshold Size (Integer, <= # Clients, > 1): ")

        threshold = -1
        while threshold < 0:
            threshold = get_user_input()

            try:
                if threshold == "":
                    threshold = "2"

                threshold = int(threshold)

                if threshold <= 1:
                    threshold = -1
                    print( "Threshold must be greater than 1: ")
                elif threshold > num_shares:
                    threshold = -1
                    print( "Threshold must be smaller or equal to the number of Clients, {0}: ".format(num_shares))
            except:
                threshold = -1
                print("Threshold must be a number: ")

        threshold = int(threshold)
    print (secret, num_shares, threshold)


def bind_server_socket(sock):
    successful = False
    print( "Host: {0} Port: {1}".format(host, port))
    serverAddress = (host, port)

    while not successful:
        try:
            sock.bind(serverAddress)
            successful = True
        except socket.error as msg:
            print( "Bind failed. Error Code: {0} Message: {1}".format(msg[0], msg[1]))
            time.sleep(2)


def serv():
    global recievedSecrets,numClientsOnline
    global serverSocket
    global connection
    global p
    shamirScheme = ShamirScheme.ShamirScheme()
    splitSecrets,p = shamirScheme.split_secret(secret, num_shares, threshold)
    print(splitSecrets)
    #print(p)

    keepRunning = True
    TCP_IP='0.0.0.0'
    TCP_PORT=5252
    BUFFER_SIZE=20
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #serverSocket.setsockopt(socket.SQL_SOCKET,socket.SO_REUSEADDR,1)
    serverSocket.bind((TCP_IP,TCP_PORT))
    
        #bind_server_socket(serverSocket)
        
    
    
    #wait_for_all_clients()

    try:
        share = iter(splitSecrets)
        
        fl=0

        while True:
            serverSocket.listen(4)

            #start_new_thread(connection_thread, (serverSocket,))

            (connection, (ip,port)) = serverSocket.accept()
            
            newthread = ClientThread(ip,port,"X") 
            newthread.start() 
            threads.append(newthread) 
            numClientsOnline=numClientsOnline+1
            print("Connected to client no. ",numClientsOnline)
                #print( "Enter Command ([s,g,e], h for help): ")
            #threadInputCmds = input()
            for t in threads:
                threadInputCmds=connection.recv(SOCKET_SIZE)
                threadInputCmds=threadInputCmds.decode('ASCII')
                print("Data: "+threadInputCmds)
                        
                if threadInputCmds == SEND_MSG:
                    ''' Send shares to clients '''
                
                    msg = next(share)
                    t.cmd = threadInputCmds
                    t.secret = msg
                        #t.send_to_clients()
                    t.run()
                elif threadInputCmds == GET_MSG:
                    ''' Sends the tx secret command to each client, and they send their part                    back to the server, the server waits for the threshold number of clients
                            to respond, and then will recombine the secret and print it out'''
                    #for i in range(2):
                    fl=fl+1
                    t.cmd = threadInputCmds
                    receivedMsg=t.recv_secret_from_clients()
                    if(fl==2):
                        receivedSecret = []
                        #print("2 secrets are :")
                        #print(receivedMsg)
                            #t.run()
                            #receivedMsg = wait_for_threshold_responses()
                            
                        for msg in receivedMsg:
                            #print(msg)
                            t=msg
                            #t = recover_message(msg)
                            #print(t)

                            if not t == None:
                                receivedSecret.append(t)

                        try:    
                            data={'required_shares': 2, 'prime_mod':p, 'shares':receivedSecret}
                            #combinedSecret = shamirScheme.recover_secret(data)
                            combinedSecret=shamir.recover_secret(shamir.from_base64(data)).decode('ascii')
                            print("The Recovered Secret is: {0}".format(combinedSecret))
                            ###
                            f = open("C:\\Users\\Hp\\Documents\\recovery.txt", "w")
                            f.write(combinedSecret)
                            f.close()
                        except:
                            f = open("C:\\Users\\Hp\\Documents\\recovery.txt", "w")
                            f.write("None")
                            f.close()
                            print("Oops! You have entered wrong shares")
        
                elif threadInputCmds == HELP:
                    print("s - Split and Send Secret\ng - Get and Recombine Secret\ne - Exit")
                elif threadInputCmds == EXIT:
            
                    break
                else:
                    print("Unknown Command")
                # end while
            
                
        
        
    except socket.error as msg:
        print( "Bind failed. Error Code: {0} Message: {1}".format(msg[0], msg[1]))
        serverSocket.close()
        sys.exit()
    except:
        print( "Error: {0}".format(error))
    finally:
        print( "Closing Server")
        serverSocket.close()
        for t in threads:
            t.join()
        connection.close()
    
        #close_clients()
        sys.exit()
    # end try



    # end serv


# this accepts a connection and adds it to the thread pool, as long as the connection amount isn't
# greater than the num_shares


def connection_thread(serverSocket):
    global numClientsOnline, threshold
    global connection



    while True:
        serverSocket.listen(4)
        (connection, (ip,port)) = serverSocket.accept()
        numClientsOnline = numClientsOnline + 1
        print( "Client connected, Accepted From: {0}, minimum number left to connect: {1}".format(clientAddress, num_shares - numClientsOnline))
        clientThread = ClientThread(ip,port, "X")
        #clientThread.start()
        threads.append(clientThread)

        for t in threads:
            t.join()
        connection.close()

def get_user_input():
    return input()


def close_clients():
    global connection
    for t in threads:
        try:
            t.join()
            #t.connection.send(bytes(STOP_RECEIVING,'utf-8'))
            serverSocket.send(bytes(STOP_RECEIVING,'utf-8'))
            time.sleep(1)
        
        except IOError:
            pass
    connection.close()

def wait_for_all_clients():
    print( "Waiting for {0} Clients".format(num_shares))

    while numClientsOnline < num_shares:
        time.sleep(1)
    print( "All Clients Connected")


def wait_for_threshold_responses():
    recievedSecrets = []
    timeout = 5

    for t in threads:
        i = 0

        while not t.has_secret_part():
            print( "Waiting... {0}".format(i))
            i = i + 1
            time.sleep(1)

            if i == threshold:
                # wait a lot less if we have enough secrets
                timeout = 5

            if i > timeout:
                print("Timed out waiting for responses")
                break
        # end while

        if t.has_secret_part():
            recievedSecrets.append(t.secretPart)
            t.secretPart = ""

    return recievedSecrets
# end waitForThresholdResponses


def build_message(indexMsgTuple):
    index = indexMsgTuple[0]
    share = indexMsgTuple[1]
    msg = index + ";;" + share

    return msg


def recover_message(msgReceived):
    if msgReceived == "":
        return None

    tokens = msgReceived.split("-")
    index = tokens[0]
    share = tokens[1]
    print("Index"+str(index))
    print("Share"+str(share))
    return (index, share)


init()
get_arguments()
serv()
