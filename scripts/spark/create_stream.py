# import socket
# from time import sleep
#
# host = 'localhost'
# port = 12345
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((host, port))
# s.listen(1)
# while True:
#     print('\nListening for a client at',host , port)
#     conn, addr = s.accept()
#     print('\nConnected by', addr)
#     try:
#         print('\nReading file...\n')
#         with open('iris_test.csv') as f:
#             for line in f:
#                 out = line.encode('utf-8')
#                 print('Sending line',line)
#                 conn.send(out)
#                 sleep(10)
#             print('End Of Stream.')
#     except socket.error:
#         print ('Error Occured.\n\nClient disconnected.\n')
# conn.close()
#
#
# import socket
# from time import sleep
#
# host = 'localhost'
# port = 9997
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((host, port))
# s.listen(1)
# while True:
#     print('\nListening for a client at',host , port)
#     conn, addr = s.accept()
#     print('\nConnected by', addr)
#     try:
#         line = "hello,hello"
#         out = line.encode('utf-8')
#         print('Sending line',line)
#         conn.send(out)
#         sleep(10)
#         print('End Of Stream.')
#     except socket.error:
#         print ('Error Occured.\n\nClient disconnected.\n')
# conn.close()


import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
print(dir(asyncio))
# asyncio.run(tcp_echo_client('Hello World!'))