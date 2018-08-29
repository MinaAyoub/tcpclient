import socket

host = '127.0.0.1'
port= 23

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

message = input("->  ")


while message != 'q':
    s.send(message.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print ("feedback from server: " + data)
    message = input("-> ")