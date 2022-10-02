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

def get_message():
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
    decoded_data = recv.decode().splitlines()
    while decoded_data[-1] is not '.':
        recv = pSockSSL.recv(1024)
        decoded_data = recv.decode().splitlines()
        print(recv.decode())


get_message()


