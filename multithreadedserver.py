#import socket module
from socket import *
import sys # In order to terminate the program
from _thread import *
import threading
import os

#Prepare a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('',serverPort))  
serverSocket.listen(5)

myHostName = gethostname()
#print("Name of the localhost is {}".format(myHostName))

myIP = gethostbyname(myHostName)

print("Connection address is {}:{}".format(myIP, serverPort))
print("Ready to serve...")

def Socket(connectionSocket):   
    while True:
        try:
            message = connectionSocket.recv(1024)
            print("message: \n", message)
            message = message.decode()
            if not message:
                #print_lock.release()
                break
            if message.split()[0] != 'GET':
                connectionSocket.send("HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>400 Bad Request<h1> <h2><h2></body></html>".encode())
                connectionSocket.close()
                break
            filename = message.split()[1]
            f = open(os.path.dirname(__file__) + '\\' + filename[1:])
            outputdata = "HTTP/1.1 200 OK\r\nContent-type:text/html;charset=utf8\r\n\r\n"
            filedata = f.read()
            filedata += "\r\n"
            outputdata +=filedata
            print("outputdata: \n", outputdata)
            #Send one HTTP header line into socket
            connectionSocket.send(outputdata.encode())
            #Fill in start 
            #Fill in end
            #Send the content of the requested file to the client 
            connectionSocket.close()
            #print_lock.release()
            break
        except IOError:
            #Send response message for file not found 
            #Fill in start
            connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1> <h2><h2></body></html>".encode())
            #Fill in end
            #Close client socket
            #Fill in start
            connectionSocket.close()
            #print_lock.release()
            break
            #Fill in end
        except IndexError:
            connectionSocket.send("HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>400 Bad Request<h1> <h2><h2></body></html>".encode())
            connectionSocket.close()
            break
    connectionSocket.close()

while True:
    # establish connection with client
    connectionSocket, addr = serverSocket.accept()

    # lock acquired by client
    #print_lock.acquire()
    print('Connected to {}:{} {}'.format(addr[0], serverPort, addr[1]))

    # Start a new thread and return its identifier
    start_new_thread(Socket, (connectionSocket,))
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data