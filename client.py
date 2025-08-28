import socket
import consts


sockUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sockUDP.bind((consts.ip_server, consts.port_server))


while True:
    sockUDP.sendto("hello".encode(), (consts.ip_server, consts.port_server))