#import socket module 
from http import server
from socket import *
import sys # In order to terminate the program
import os

#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverPort = 6789
serverSocket.bind(("",serverPort))  
serverSocket.listen(5)

myHostName = gethostname()

#print("Name of the localhost is {}".format(myHostName))

myIP = gethostbyname(myHostName)

print("Connection address is {}:{}".format(myIP, serverPort))
#bind the server with  portnumber 7000
serverSocket.listen(5)
#wait and listen for some client 
#Fill in end
print('Ready to serve...')
while True:
    #Establish the connection 
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print('Busy...')
        if not message:
                connectionSocket.close()
                continue    
        message = message.decode()
        print("message: \n", message)
        if message.split()[0] != 'GET':
                connectionSocket.send("HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>400 Bad Request<h1> <h2><h2></body></html>".encode())
                connectionSocket.close()
                continue
        filename = message.split()[1]
        f = open(os.path.dirname(__file__) + '\\' + filename[1:])
        outputdata = "HTTP/1.1 200 OK\r\nContent-type:text/html;charset=utf8\r\n\r\n"
        filedata = f.read()
        filedata += "\r\n"
        outputdata +=filedata
        print("outputdata: \n", outputdata)
        #Send one HTTP header line into socket
        connectionSocket.send(outputdata.encode())
        connectionSocket.close() 
        continue
    except IOError:
        #Send response message for file not found 
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1> <h2><h2></body></html>".encode())
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
