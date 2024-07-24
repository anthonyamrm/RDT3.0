import socket
import pickle
import hashlib

PORT = 5557
SERVER = "192.168.4.10"
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind(ADDR)

def calculo_checksum(msg):
    return hashlib.md5(msg.encode()).hexdigest()

def h_server():
    seq_esperado = 0
    while 1:
        msg, addr = receiver.recvfrom(1024)
        package = pickle.loads(msg)
        num_seq, msg, checksum, addr = package

