import socket
import consts
import numpy as np
import cv2


def get_local_ip():
    return socket.gethostbyname(socket.gethostname())


"""
connect to server
"""

local_ip = get_local_ip()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((local_ip, consts.port_server))

print(f"Server listen in address {local_ip}")
server.listen(1)
connection, address = server.accept()

print("connection - ", connection, "address - ", address)

"""
send video
"""

s=""
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.flip(frame, 1)
    # d = frame.flatten()
    # s = d.tostring()
    # print(s)

    # for i in range(20):
    #     connection.send(s)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break