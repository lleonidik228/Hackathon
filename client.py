import socket
import consts



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((consts.ip_server, consts.port_server))


print("Ill gert connection to server")


"""
get video
"""

while True:
    print("Wait data")