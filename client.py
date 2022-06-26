# Import socket module
from socket import *
import os
import sys

if len(sys.argv) == 1:
    while True:
        try:
            while True:
                host = input("Please give the IP to connect:\n")
                if len(host) > 0:
                    break

            while True:
                port = input("Please give the port to connect:\n")
                if len(port) > 0:
                    break

            print("Testing Connection...")

            port = int(port)

            serverSocket = socket(AF_INET, SOCK_STREAM)

            # connect to server on local computer
            serverSocket.connect((host,port))
            break
        except Exception:
            print("There is a problem with your IP or Host. Please try again.")

    print("Connection OK.")

    while True:
        answer = input("Please select what you want to send:\n1 GET HelloWorld.html\n2 GET custom file name\n3 custom command\n")
        if answer == '1':
            message = "GET /HelloWorld.html"
            break
        elif answer == '2':
            message = "GET /" + input("Please enter filename with extension (ex: Helloworld.html):\n")
            break
        elif answer == '3':
            message = input("Please enter your message:\n")
            if len(message) == 0:
                print("Please select an item from the list\n")
                continue 
            break
        else:
            print("Please select an item from the list\n")

elif len(sys.argv) == 4:
    host = sys.argv[1]
    port = int(sys.argv[2])
    message = "GET /" + sys.argv[3]
    # connect to server on local computer
    try:
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.connect((host,port))
    except Exception:
        print("There is a problem with your IP or Host. Please try again.")
        exit()

else:
    print("Please check your arguments and try again.\nUsage: ip port file_to_request")
    exit()

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