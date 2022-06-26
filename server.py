#import socket module 
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM) 
import os
#Prepare a sever socket
#Fill in start
serverPort = 7000
serverSocket.bind(("",serverPort))  
serverSocket.listen(5)

myHostName = gethostname()

print("Name of the localhost is {}".format(myHostName))

myIP = gethostbyname(myHostName)

print("IP address of the localhost is {}".format(myIP))
#bind the server with  portnumber 7000
serverSocket.listen(5)
#wait and listen for some client 
#Fill in end
while True:
    #Establish the connection 
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print("message: \n", message)
        message = message.decode()

        if len(message) < 1:
            continue    
        if message.split()[0] != 'GET':
                connectionSocket.send("HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>400 Bad Request<h1> <h2><h2></body></html>".encode())
                connectionSocket.close()
                continue
        filename = message.split()[1]
        f = open(os.path.dirname(__file__) + '\\' + filename[1:])
        outputdata = f.read()
        print("outputdata: \n", outputdata)
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-type:text/html;charset=utf8\r\n\r\n".encode())
        #Fill in start 
        #Fill in end
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode())
        connectionSocket.close() 
    except IOError:
        #Send response message for file not found 
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1> <h2><h2></body></html>".encode())
        print("the file was not found ")
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
    except IndexError:
        connectionSocket.send("HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>400 Bad Request<h1> <h2><h2></body></html>".encode())
        connectionSocket.close()
        continue
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data