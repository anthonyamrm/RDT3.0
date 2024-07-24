import socket
import threading
import pickle
import hashlib

PORT = 5555
SERVER = socket.gethostbyname(socket.SOCK_DGRAM)
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def calculo_checksum(data):
    return hashlib.md5(data.encode()).hexdigest()

def h_sender():
    num_seq = 0
    print(f"[LISTENING] Servidor ouvindo em {SERVER}")
    while 1:
        msg, addr = server.recvfrom(1024)
        package = pickle.loads(msg)
        num_seq, msg, checksum, dest_addr = package 

        