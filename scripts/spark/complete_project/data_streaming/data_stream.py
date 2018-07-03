import sys
import socket
import time

# variable
host = "localhost"
port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

content = "Hello world saaaathish\n".encode()
conn, addr = sock.accept()
for i in range(0,100):
    try:
        conn.send(content)
        time.sleep(3)
    except socket.error:
        print ('Error Occured.\n\nClient disconnected.\n')
conn.close()