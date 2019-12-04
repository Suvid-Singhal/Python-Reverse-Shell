import socket

    
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Enter the port to listen on: ")
port=int(input())
s.bind(('', port))
print("Listening on port "+str(port))




print("Enter the Commands: ")


    

while True:
    s.listen(5)
    clientsocket,address = s.accept()
    print("[+] Connection from "+str(address) +"has been established!")
    cmd = input()
    if cmd == 'quit':
        clientsocket.close()
        s.close()
        sys.exit()
    if len(str.encode(cmd)) > 0:
        clientsocket.send(str.encode(cmd))
        response = str(clientsocket.recv(1024), "utf-8")
        print(response, end="")

clientsocket.close()
