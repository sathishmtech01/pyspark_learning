import sys
import socket
import time

# variable
hostname = "0.0.0.0"
port = 9999

def netcat(host,port,content):
    """

    :param host:
    :param port:
    :param content:
    :return:
    """
    # initialize the connection
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(sock)
    sock.connect((host,port))
    print("Hello")
    # send content
    for i in range(0,100):
        print(i)
        sock.sendall(content)
        time.sleep(0.5)

    sock.shutdown(socket.SHUT_WR)
    #sock.shutdown(socket.SHUT_WR)
    sock.close()
    # res = ""
    #
    # while True:
    #     data = sock.recv(1024)
    #     if(not data):
    #         break
    #     res += data.decode()
    # print(res)
    # print("connection closed")
    # sock.close()

content = "Hello world jmhjklkj \n"

netcat(hostname,port,content.encode())
