import socket
import sys

global s

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" %(err))

host_ip = '159.89.172.14'   # DigitalOcean Droplet instance
# host_ip = '10.15.1.129'
# host_ip = '192.168.43.70'

port = 9999
s.connect((host_ip, port))
cmd = 'hi'
s.send(str.encode(cmd))
while True:
# connecting to the server
    data= str(s.recv(1024))
    if 'hello' in data:
        s.send(str.encode('quit'))
    elif 'invalid' in data:
        print("invalid cmd", end="")
        cmd = input()
        s.send(str.encode(cmd))
        continue
    else:
        print("closing connection")
        s.close()
        break

