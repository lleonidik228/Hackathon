import cv2 as cv
import consts


# __________________________________________________________recognizing__________________________________________________________

letters = []
letter_counter = 0
sentence_in_list = []
is_clear_sentence = False

def persons_input(hand_cordinates):
    global is_clear_sentence
    def distance(x1, y1, x2, y2):
        distance = int((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2))
        # print(distance)
        return distance

    persons_input = ""

    if is_clear_sentence:
        sentence_in_list.clear()
        is_clear_sentence = False
    # Consider pawn is Vertical
    hand_horz = False
    # Consider all fingure are Down
    thumbs_up = False
    index_up = False
    middel_up = False
    ring_up = False
    littel_up = False

    # Here I am using Hand Cordinates(HC) values , which we got from video input.
    # With the help of HC values , I can determine wither the fingure is UP or DOWN
    # In "hand_cordinate[12][1]" , "12" is the index and "1" is X_cordinate (and "2" for Y_cordinate)
    # For more information, refer the "HAND_CORD" image (to understand the HC)

    if distance(hand_cordinates[0][2], 0, hand_cordinates[12][2], 0) < distance(hand_cordinates[0][1], 0,
                                                                                hand_cordinates[12][1], 0):
        hand_horz = True

    if distance(hand_cordinates[0][1], hand_cordinates[0][2], hand_cordinates[3][1], hand_cordinates[3][2]) < distance(
            hand_cordinates[0][1], hand_cordinates[0][2], hand_cordinates[4][1], hand_cordinates[4][2]):
        thumbs_up = True

    if distance(hand_cordinates[0][1], hand_cordinates[0][2], hand_cordinates[6][1], hand_cordinates[6][2]) < distance(
            hand_cordinates[0][1], hand_cordinates[0][2], hand_cordinates[8][1], hand_cordinates[8][2]):
        index_up = True

    if distance(hand_cordinates[0][1], hand_cordinates[0][2], hand_cordinates[10][1],
                hand_cordinates[10][2]) < distance(hand_cordinates[0][1], hand_cordinates[0][2], hand_cordinates[12][1],
                                                   hand_cordinates[12][2]):
        middel_up = True

    if distance(hand_cordinates[0][1], hand_cordinates[0][2], hand_cordinates[14][1],
                hand_cordinates[14][2]) < distance(hand_cordinates[0][1], hand_cordinates[0][2], hand_cordinates[16][1],
                                                   hand_cordinates[16][2]):
        ring_up = True

    if distance(hand_cordinates[0][1], hand_cordinates[0][2], hand_cordinates[18][1],
                hand_cordinates[18][2]) < distance(hand_cordinates[0][1], hand_cordinates[0][2], hand_cordinates[20][1],
                                                   hand_cordinates[20][2]):
        littel_up = True

    # Get persons_input according to HC values

    if index_up == False and middel_up == False and ring_up == False and littel_up == False and thumbs_up == True and hand_horz == False:
        if distance(hand_cordinates[4][1], hand_cordinates[4][2], hand_cordinates[16][1],
                    hand_cordinates[16][2]) < distance(hand_cordinates[4][1], hand_cordinates[4][2],
                                                       hand_cordinates[13][1], hand_cordinates[13][2]):
            persons_input = "_O"

        elif distance(hand_cordinates[4][1], hand_cordinates[4][2], hand_cordinates[18][1],
                      hand_cordinates[18][2]) < distance(hand_cordinates[14][1], hand_cordinates[14][2],
                                                         hand_cordinates[18][1], hand_cordinates[18][2]):
            persons_input = "_M"

        elif distance(hand_cordinates[4][1], hand_cordinates[4][2], hand_cordinates[18][1],
                      hand_cordinates[18][2]) < distance(hand_cordinates[10][1], hand_cordinates[10][2],
                                                         hand_cordinates[18][1], hand_cordinates[18][2]):
            persons_input = "_N"

        elif distance(hand_cordinates[4][1], hand_cordinates[4][2], hand_cordinates[18][1],
                      hand_cordinates[18][2]) < distance(hand_cordinates[6][1], hand_cordinates[6][2],
                                                         hand_cordinates[18][1], hand_cordinates[18][2]):
            persons_input = "_T"

        else:
            persons_input = "_A"

    elif index_up == True and middel_up == True and ring_up == True and littel_up == True and thumbs_up == True and hand_horz == False:

        persons_input = " "

        if distance(hand_cordinates[4][1], hand_cordinates[4][2], hand_cordinates[12][1],
                    hand_cordinates[12][2]) < distance(hand_cordinates[4][1], hand_cordinates[4][2],
                                                       hand_cordinates[11][1], hand_cordinates[11][2]):
            persons_input = "_C"

        elif distance(hand_cordinates[4][1], hand_cordinates[4][2], hand_cordinates[17][1],
                      hand_cordinates[17][2]) < distance(hand_cordinates[4][1], hand_cordinates[4][2],
                                                         hand_cordinates[5][1], hand_cordinates[5][2]):
            persons_input = "_B"



    elif index_up == False and middel_up == False and ring_up == False and littel_up == False and thumbs_up == False and hand_horz == False:
        if distance(hand_cordinates[20][1], hand_cordinates[20][2], hand_cordinates[4][1],
                    hand_cordinates[4][2]) < distance(hand_cordinates[19][1], hand_cordinates[19][2],
                                                      hand_cordinates[4][1], hand_cordinates[4][2]):
            persons_input = "_E"

        else:
            persons_input = "_S"

    elif index_up == False and middel_up == True and ring_up == True and littel_up == True and thumbs_up == True and hand_horz == False:
        persons_input = "_F"

    elif index_up == True and middel_up == False and ring_up == False and littel_up == False and thumbs_up == True and hand_horz == True:
        if distance(hand_cordinates[8][1], hand_cordinates[8][2], hand_cordinates[4][1],
                    hand_cordinates[4][2]) < distance(hand_cordinates[6][1], hand_cordinates[6][2],
                                                      hand_cordinates[4][1], hand_cordinates[4][2]):
            persons_input = "_Q"

        elif distance(hand_cordinates[12][1], hand_cordinates[12][2], hand_cordinates[4][1],
                      hand_cordinates[4][2]) < distance(hand_cordinates[10][1], hand_cordinates[10][2],
                                                        hand_cordinates[4][1], hand_cordinates[4][2]):
            persons_input = "_P"

        else:
            persons_input = "_G"

    elif index_up == True and middel_up == True and ring_up == False and littel_up == False and thumbs_up == True and hand_horz == True:
        if distance(hand_cordinates[12][1], hand_cordinates[12][2], hand_cordinates[4][1],
                    hand_cordinates[4][2]) < distance(hand_cordinates[10][1], hand_cordinates[10][2],
                                                      hand_cordinates[4][1], hand_cordinates[4][2]):
            persons_input = "_P"

        else:
            persons_input = "_H"

    elif index_up == False and middel_up == False and ring_up == False and littel_up == True and thumbs_up == False and hand_horz == False:
        persons_input = "_I"

    elif index_up == False and middel_up == False and ring_up == False and littel_up == True and thumbs_up == False and hand_horz == True:
        persons_input = "_J"

    elif index_up == True and middel_up == True and ring_up == False and littel_up == False and thumbs_up == True and hand_horz == False:
        if hand_cordinates[8][1] < hand_cordinates[12][1]:
            persons_input = "_R"

        elif distance(hand_cordinates[4][1], hand_cordinates[4][2], hand_cordinates[14][1],
                      hand_cordinates[14][2]) < distance(hand_cordinates[9][1], hand_cordinates[9][2],
                                                         hand_cordinates[14][1], hand_cordinates[14][2]):
            if 2 * distance(hand_cordinates[5][1], hand_cordinates[5][2], hand_cordinates[9][1],
                            hand_cordinates[9][2]) < distance(hand_cordinates[8][1], hand_cordinates[8][2],
                                                              hand_cordinates[12][1], hand_cordinates[12][2]):
                persons_input = "_V"

            else:
                persons_input = "_U"

        elif distance(hand_cordinates[4][1], hand_cordinates[4][2], hand_cordinates[14][1],
                      hand_cordinates[14][2]) < distance(hand_cordinates[5][1], hand_cordinates[5][2],
                                                         hand_cordinates[14][1], hand_cordinates[14][2]):
            persons_input = "_K"

    elif index_up == True and middel_up == False and ring_up == False and littel_up == False and thumbs_up == True and hand_horz == False:
        if distance(hand_cordinates[3][1], hand_cordinates[3][2], hand_cordinates[14][1],
                    hand_cordinates[14][2]) < distance(hand_cordinates[14][1], hand_cordinates[14][2],
                                                       hand_cordinates[4][1], hand_cordinates[4][2]):
            persons_input = "_L"

        elif distance(hand_cordinates[8][1], hand_cordinates[8][2], hand_cordinates[10][1],
                      hand_cordinates[10][2]) < distance(hand_cordinates[6][1], hand_cordinates[6][2],
                                                         hand_cordinates[10][1], hand_cordinates[10][2]):
            persons_input = "_X"

        else:
            persons_input = "_D"

    elif index_up == True and middel_up == True and ring_up == False and littel_up == False and thumbs_up == False and hand_horz == False:
        if hand_cordinates[8][1] < hand_cordinates[12][1]:
            persons_input = "_R"

        elif 2 * distance(hand_cordinates[5][1], hand_cordinates[5][2], hand_cordinates[9][1],
                          hand_cordinates[9][2]) < distance(hand_cordinates[8][1], hand_cordinates[8][2],
                                                            hand_cordinates[12][1], hand_cordinates[12][2]):
            persons_input = "_V"

        else:
            persons_input = "_U"

    elif index_up == True and middel_up == True and ring_up == True and littel_up == False and thumbs_up == True and hand_horz == False:
        persons_input = "_W"

    elif index_up == False and middel_up == False and ring_up == False and littel_up == True and thumbs_up == True and hand_horz == False:
        if distance(hand_cordinates[3][1], hand_cordinates[3][2], hand_cordinates[18][1],
                    hand_cordinates[18][2]) < distance(hand_cordinates[4][1], hand_cordinates[4][2],
                                                       hand_cordinates[18][1], hand_cordinates[18][2]):
            persons_input = "_Y"

        else:
            persons_input = "_I"

    elif index_up and middel_up and ring_up and littel_up and not thumbs_up and not hand_horz:
        persons_input = "stop"

    # print(thumbs_up)
    letters.append(persons_input)
    if len(letters) == consts.LIMIT_OF_LETTERS:
        print(letters)
        for letter in letters:
            if letters.count(letter) >= consts.MIN_LIMIT_FOR_ACCEPT_LETTER and letter != "":
                sentence_in_list.append(letter)
                print("the sentence is :", sentence_in_list)
                break
        letters.clear()

    if "stop" in sentence_in_list:
        sentence_in_list.pop(-1)
        is_clear_sentence = True
        sentence = "".join(sentence_in_list)
        # count_of_spases = 0
        # finished_sentence = 0
        # for i in sentence:
        #     if i == " ":
        #         count_of_spases += 1
        #
        #     finished_sentence += i
        sentence = "".join(sentence.split("_"))
        print("finished sentence:", sentence)
        return persons_input, sentence
    else:
        return persons_input, False


# ____________________________________________________________geting_in_frame________________________________________________________
def get_fram(image, hand_cordinate, string):
    def x_max(hand_cordinate):
        max_val = 0
        for cordinate_list in hand_cordinate:
            if max_val < cordinate_list[1]:  # 1 is x-cord value
                max_val = cordinate_list[1]
        return max_val

    def y_max(hand_cordinate):
        max_val = 0
        for cordinate_list in hand_cordinate:
            if max_val < cordinate_list[2]:  # 2 is y-cord value
                max_val = cordinate_list[2]
        return max_val

    def x_min(hand_cordinate):
        min_val = hand_cordinate[0][1]
        for cordinate_list in hand_cordinate:
            if min_val > cordinate_list[1]:
                min_val = cordinate_list[1]
        return min_val

    def y_min(hand_cordinate):
        min_val = hand_cordinate[0][2]
        for cordinate_list in hand_cordinate:
            if min_val > cordinate_list[2]:
                min_val = cordinate_list[2]
        return min_val

    def show_holy_rect(image, start_point, end_point, string):
        maxX = image.shape[1]
        # To create farme which contain hand
        image = cv.rectangle(image, start_point, end_point, (0, 0, 255), 1)
        # To create frame for letter
        image = cv.rectangle(image, (start_point[0], start_point[1] + 23), (end_point[0], start_point[1] + 3),
                             (0, 0, 255), -1)

        # Write letter in the frame
        image = cv.putText(cv.flip(image, 1), string, (maxX - end_point[0], start_point[1] + 20),
                           cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv.LINE_AA)
        return cv.flip(image, 1)

    image = show_holy_rect(image, (x_min(hand_cordinate) - 7, y_max(hand_cordinate) + 7),
                           (x_max(hand_cordinate) + 7, y_min(hand_cordinate) - 7), string)

    return image
