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

def calculo_checksum(msg):
    return hashlib.md5(msg.encode()).hexdigest()

def fazer_package(num_seq, msg):
    pacote = (num_seq, msg, calculo_checksum(msg))
    return pacote 

def menu():
    while True:            
            msg, addr = server.recvfrom(1024)
            package = pickle.loads(msg)
            num_seq, msg, checksum, dest_addr = package
            menu()
    
            print("Menu de debbuging")
            print("-- Opção 1 -- no loss")
            print("-- Opção 2 -- lost packet")
            print("-- Opção 3 -- lost ACK")
            print("-- Opção 4 -- premature timeout") 
            
            escolha = input("Escolha uma opção: ")

            # Implementar a lógica no receiver
            if escolha == "1":
                server.sendto(fazer_package(num_seq, msg), dest_addr)

            elif escolha == "2":
                #Timeout porque o pacote não foi enviado - Logo, não enviaremos NADA para o receiver
                continue

            elif escolha == "3":
                #Perda de ACK
                continue
            
            elif escolha == "4":
                #Timeout prematuro
                continue

def start():
    print("Servidor ouvindo")
    menu()

if __name__ == "__main__":
    start()
