import socket 
import pickle
import hashlib

PORT = 5556
SERVER = "192.168.4.10"
ADDR = (SERVER, PORT)
WAIT = 3

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(WAIT)

def calculo_checksum(msg):
    return hashlib.md5(msg.encode()).hexdigest()

def fazer_package(num_seq, msg, destino):
    package = (num_seq, msg, destino, calculo_checksum)
    return package

def rdt(msg, destino):
    num_seq = 0
    while 1:
        package = fazer_package(num_seq, msg, destino)
        client.sendto(package, ADDR)
        

    