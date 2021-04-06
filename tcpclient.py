import socket

ClientSocket = socket.socket()

# Get the assigned container IP Address
hostName = socket.gethostname()
ipAddress = socket.gethostbyname(hostName)
print('Container IP: ' + ipAddress)

host = input(
    "What is the Server IP Address or Hostname? (default: '172.100.0.2') ") or "172.100.0.2"
port = int(input("What is the Server Port? (default: 1223) ") or "1223")

print('Waiting for connection')

try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()
