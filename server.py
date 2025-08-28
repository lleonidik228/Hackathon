# import socket
# import consts
# import numpy as np
# import cv2
#
#
# def get_local_ip():
#     return socket.gethostbyname(socket.gethostname())
#
#
# """
# connect to server
# """
#
# local_ip = get_local_ip()
#
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((local_ip, consts.port_server))
#
# print(f"Server listen in address {local_ip}")
# server.listen(1)
# connection, address = server.accept()
#
# print("connection - ", connection, "address - ", address)
#
# """
# send video
# """
#
# s=""
# cap = cv2.VideoCapture(0)
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     cv2.flip(frame, 1)
#     # d = frame.flatten()
#     # s = d.tostring()
#     # print(s)
#
#     # for i in range(20):
#     #     connection.send(s)
#     #     if cv2.waitKey(1) & 0xFF == ord('q'):
#     #         break


import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here

    frame.flags.writeable = True
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()