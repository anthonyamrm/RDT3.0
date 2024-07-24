import socket 
import pickle
import hashlib

PORT = 5556
SERVER = "192.168.4.10"
ADDR = (SERVER, PORT)
WAIT = 3

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.settimeout(WAIT)

def calculo_checksum(msg):
    return hashlib.md5(msg.encode()).hexdigest()

def fazer_package(num_seq, msg):
    package = (num_seq, msg, calculo_checksum(msg))
    return package

def rdt(msg, destino):
    num_seq = 0
    while 1:
        package = fazer_package(num_seq, msg)
        server.sendto(package, destino)
        try:
            resposta, addr = server.recvfrom(1024)
            pacote_ack = pickle.loads(resposta)
            ack, num_ack = pacote_ack
            if ack == "ACK" and num_ack == num_seq:
                num_seq = 1 - num_seq
                break
        except socket.timeout:
            print("Demorou demais -> Reenviando pacote.")
            rdt(msg, destino)

if __name__ == '__main__':
    
    
    print("Você está conectado ao servidor.")
    mensagem = "blabla"
    while mensagem != "Desconectar":
        mensagem = input("Digite a mensagem a ser enviada!")
        ip_destino = input("Digite o IP do receiver")
        porta_destino = input("Digite a PORTA do receiver")
        destino = (ip_destino,porta_destino)
        rdt(mensagem, destino)



    