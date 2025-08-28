import socket
import cv2
import pickle
import struct
import threading
import consts
import sys


# Socket Create
# family = socket.AF_INET
# protocol = socket.SOCK_STREAM
# serv = socket.socket(family, protocol)

# binding ip address with the port
# serv.bind((consts.ip_server, 9647))
# serv.listen(1)

sockUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sockUDP.bind((consts.ip_server, consts.port_server))


def send_data(message):
    # print(sys.getsizeof(message))
    # num = sys.getsizeof(message) // 921806
    with open("timed_file.txt", "wb") as file:
        file.write(message)

    with open("timed_file.txt", "rb")as file:
        data = file.read(4096)
        print("send data")
        sockUDP.sendto(data, (consts.ip_server, consts.port_server))


# sending photo as a video to the client
while True:
    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        img, frame = cap.read()
        a = pickle.dumps(frame)
        message = struct.pack("Q", len(a)) + a
        # threading.Thread(target=send_data, args=(message,)).start()
        send_data(message)
        cv2.imshow('Video from Server', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            sockUDP.close()