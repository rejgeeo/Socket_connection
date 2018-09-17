import socket
import sys

# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as msg:
        print("Socket creation error: " + str(msg))



# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))
        s.bind((host, port))
        s.listen(5)
        print("Socket listing")

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


def accept_connections():
    while True:
        try:
            conn, address = s.accept()
            conn.setblocking(1)  # prevents timeout
            print("Connection has been established :" + address[0])
            while True:
                data = str(conn.recv(1024), "utf-8")
                if 'quit' in data:
                    print("received quit cmd")
                    conn.close()
                    break
                elif 'hi' in data:
                    print("received hi, sending hello")
                    conn.send(str.encode('hello'))
                elif 'ip_addr' in data:
                    conn.send(str.encode('my ip is: '))
                else:
                    conn.send(str.encode('invalid command'))
        except:
            print("Error accepting connections")

# def send_data(conn):
#     conn.send(str.encode('thank you for connecting'))
#     data = str(conn.recv(1024),"utf-8")
#     print("data from client: " + data)
#     conn.close()

if __name__ == '__main__':
    create_socket()
    bind_socket()
    accept_connections()
    # send_data(conn)
