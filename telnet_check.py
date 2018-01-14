import socket
ip='172.31.31.54'
port=24
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
result = sock.connect_ex((ip,port))
print result
