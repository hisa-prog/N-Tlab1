import socket, base64, ssl
from socket import *

from models import Mail

def send_message(mail:Mail):
    mailserver1 = 'smtp.mail.ru'
    cSock = socket(AF_INET, SOCK_STREAM)
    cSock.connect((mailserver1, 465))
    cSockSSL = ssl.wrap_socket(cSock)
    recv = cSockSSL.recv(1024)
    print(recv)

    cSockSSL.send("EHLO host\r\n".encode())
    recv = cSockSSL.recv(1024)
    cSockSSL.send('AUTH LOGIN\r\n'.encode())
    recv = cSockSSL.recv(1024)
    cSockSSL.send((base64.b64encode('sitmailtest@mail.ru'.encode()).decode() + '\r\n').encode())
    recv = cSockSSL.recv(1024)
    print(recv)
    cSockSSL.send((base64.b64encode('q6NSTqBwvPrd7HBiTPsP'.encode()).decode() + '\r\n').encode())
    recv = cSockSSL.recv(1024)
    print(recv)
    cSockSSL.send("MAIL FROM:sitmailtest@mail.ru\r\n".encode())
    recv = cSockSSL.recv(1024)
    print(recv)
    cSockSSL.send(f"RCPT TO:{mail.address}\r\n".encode())
    recv = cSockSSL.recv(1024)
    print(recv)
    cSockSSL.send("DATA\r\n".encode())
    recv = cSockSSL.recv(1024)
    print(recv)
    cSockSSL.send(f"Subject: {mail.subject}\r\n".encode())
    cSockSSL.send('MIME-Version: 1.0\r\n'.encode())
    cSockSSL.send('Content-Type: multipart/mixed; boundary="MixedBoundaryString"\r\n'.encode())

    cSockSSL.send("\r\n".encode())
    cSockSSL.send("--MixedBoundaryString\r\n".encode())
    cSockSSL.send("Content-Type: text/plain\r\n".encode())
    cSockSSL.send("\r\n".encode())
    cSockSSL.send(f"{mail.body}\r\n".encode())

    cSockSSL.send("\r\n".encode())
    cSockSSL.send("--MixedBoundaryString\r\n".encode())
    cSockSSL.send(f'Content-Type: application/audio; name="{mail.audio_name}"\r\n'.encode())
    cSockSSL.send("Content-Transfer-Encoding: base64\r\n".encode())
    cSockSSL.send("\r\n".encode())
    cSockSSL.send(mail.audio.split(',')[-1].encode())
    cSockSSL.send("\r\n".encode())

    cSockSSL.send("\r\n--MixedBoundaryString--\r\n".encode())
    cSockSSL.send("\r\n".encode())
    cSockSSL.send(".\r\n".encode())
    recv = cSockSSL.recv(1024)

    cSockSSL.close()
    cSock.close()

def get_list():
    mailserver2 = 'pop.mail.ru'
    pSock = socket(AF_INET, SOCK_STREAM)
    pSock.connect((mailserver2, 995))
    pSockSSL = ssl.wrap_socket(pSock)
    recv = pSockSSL.recv(1024)
    print(recv)

    pSockSSL.send('USER sitmailtest@mail.ru\r\n'.encode())
    recv = pSockSSL.recv(1024)
    print(recv)

    pSockSSL.send('PASS q6NSTqBwvPrd7HBiTPsP\r\n'.encode())
    recv = pSockSSL.recv(1024)
    print(recv)


    pSockSSL.send('list 1\r\n'.encode())
    recv = pSockSSL.recv(1024)
    print(recv)

    pSockSSL.send('RETR 2\r\n'.encode())
    recv = pSockSSL.recv(1024)
    print(recv.decode())
    sleep(6)
    recv = pSockSSL.recv(1024)
    for s in recv.decode().splitlines():
        print(s)

def delete_message():
    mailserver2 = 'pop.mail.ru'
    pSock = socket(AF_INET, SOCK_STREAM)
    pSock.connect((mailserver2, 995))
    pSockSSL = ssl.wrap_socket(pSock)
    recv = pSockSSL.recv(1024)
    print(recv)
    print(recv)

    pSockSSL.send('USER sitmailtest@mail.ru\r\n'.encode())
    recv = pSockSSL.recv(1024)
    print(recv)

    pSockSSL.send('PASS q6NSTqBwvPrd7HBiTPsP\r\n'.encode())
    recv = pSockSSL.recv(1024)
    print(recv)


    pSockSSL.send('stat\r\n'.encode())
    recv = pSockSSL.recv(1024)
    print(recv)

    recv = recv.decode('utf-8')
    lis = recv[4:7]

    message_del = "dele "+ lis + "\r\n"
    pSockSSL.send(message_del.encode())
    recv = pSockSSL.recv(1024)
    print("DELE: ", recv)

    pSockSSL.send('QUIT\r\n'.encode())
    rec = pSockSSL.recv(1024)
    print('QUIT: ', rec.decode() )

    pSockSSL.close()
    pSock.close()

# send_message()
# sock = socket()
# sock.bind(('', 9090))
# sock.listen(1)

# conn, addr = sock.accept()
# print('connected:', addr)
# while True:
    
#     data = conn.recv(1024)
#     if data.decode('utf-8') == 'quit':
#         break
#     if data.decode('utf-8') == 'del':
#         delete_message()
#     if data.decode('utf-8') == 'send':
#         send_message()
#     print(data.decode('utf-8'))


# conn.close()
# sock.close()


