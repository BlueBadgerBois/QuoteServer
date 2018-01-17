import socket

s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 3333))
s.send("stockSymbol,userID")
data = s.recv(1024)
print data
s.close()
