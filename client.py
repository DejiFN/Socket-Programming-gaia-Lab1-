# Import socket module
from socket import *
import os

# local host IP
host = '192.168.56.1'

# Define the port on which you want to connect
port = 7000

serverSocket = socket(AF_INET, SOCK_STREAM)

# connect to server on local computer
serverSocket.connect((host,port))

# message you send to server

while True:
    answer = input("Please select what you want to send:\n1 GET HelloWorld.html\n2 GET custom file name\n3 custom command\n")

    if answer == '1':
        message = "GET /HelloWorld.html"
        break
    elif answer == '2':
        message = "GET /" + input("Please enter filename with extension:\n")
        break
    elif answer == '3':
        message = input("Please enter your message:\n")
        if len(message) == 0:
            print("Please select an item from the list\n")
            continue 
        break
    else:
        print("Please select an item from the list\n")

while True:
    # message sent to server
    serverSocket.send(message.encode())
    # message received from server
    data = serverSocket.recv(1024)
    # print the received message
    # here it would be a reverse of sent message
    print('Received from the server :',str(data.decode('ascii')))
    # ask the client whether he wants to continue,
    print("Client will exit now")
    os.system('pause')
    break
# close the connection
serverSocket.close()