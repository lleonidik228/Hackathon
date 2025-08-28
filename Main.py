import numpy as np
import mediapipe as mp
import Function
import say_speech
import draw_text
import sys

holy_hands = mp.solutions.hands
cap = Function.cv.VideoCapture(0)
video_bytes = []
with holy_hands.Hands(
        max_num_hands=1
        # Here only one hand is going to be detect (You can change it if you want more hands to be detected)
) as hands:
    index_cord = []  # This list stores values for pointer
    while cap.isOpened():
        sentence = False
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # To improve performance, optionally mark the image as not writeable
        image.flags.writeable = False
        image = Function.cv.cvtColor(image, Function.cv.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = Function.cv.cvtColor(image, Function.cv.COLOR_RGB2BGR)

        # Images shape
        imgH, imgW = image.shape[:2]
        string = ''
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get Hand Cordinates (HC values)
                hand_cordinate = []
                for index, landmark in enumerate(hand_landmarks.landmark):
                    x_cordinate, y_cordinate = int(landmark.x * imgW), int(landmark.y * imgH)
                    hand_cordinate.append([index, x_cordinate, y_cordinate])
                hand_cordinate = np.array(hand_cordinate)
                # Working on image
                string, sentence = Function.persons_input(hand_cordinate)
                image = Function.get_fram(image, hand_cordinate, string)
        # For pointer
        if string == "_D":
            index_cord.append([15, hand_cordinate[8][1], hand_cordinate[8][2]])
        if string == "_I" or string == "_J":
            index_cord.append([15, hand_cordinate[20][1], hand_cordinate[20][2]])
        for val in index_cord:
            image = Function.cv.circle(image, (val[1], val[2]), val[0], (255, 255, 255), 1)
            val[0] = val[0] - 1
            if val[0] <= 0:
                index_cord.remove(val)
        # Flip the image horizontally for a selfie-view display.
        Function.cv.imshow('Sign Language detection', Function.cv.flip(image, 1))
        # print("the sentence is ", sentence)
        draw_text.draw_screen(Function.list_to_string(Function.sentence_in_list))
        # print(1, image)
        x = np.array(image, dtype='<u2').tobytes()
        # print(sys.getsizeof(x))
        video_bytes.clear()
        video_bytes.append(x)
        # print(video_bytes)
        if sentence:
            say_speech.create_pm3_file(sentence)
        if Function.cv.waitKey(5) & 0xFF == ord('x'):
            break


cap.release()
