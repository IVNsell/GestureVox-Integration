import cv2
import mediapipe as mp
import pyautogui as pg
# import autopy
import mouse
import time
import threading
import py_win_keyboard_layout
import json
import ctypes
from Python.Tect_OpenCV_for_project import Hotkey_press
import webbrowser
import os

start_time = time.time()
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

screen_width, screen_height = pg.size()

prev_x = 0
prev_thumb_y = 0
prev_index_y = 0

min_movement_pra = 0.15
min_movement = 0.13
min_movement_static = 0.03

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_tracking_confidence=0.7,
                       min_detection_confidence=0.7)

avg_cursor_x = screen_width // 2
avg_cursor_y = screen_height // 2
avg_factor = 0.97

mode = "waiting"
def post_get_keyboard_layout():
    layout_id = ctypes.windll.user32.GetKeyboardLayout(0)
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x0409)
    return layout_id & 0xFFFF

def post_back_keyboard_layout(language):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(language)
def calculate_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

gesture_performed_svipe_levo_pravo = False
def delayed_action_with_svipe_levo_pravo(index_x, middle_x, right_swipe_act, left_swipe_act):
    global mode
    global gesture_performed_svipe_levo_pravo
    if not gesture_performed_svipe_levo_pravo:
        gesture_performed_svipe_levo_pravo = True
        time.sleep(0.7)
        index_x = index_x
        middle_x = middle_x
        thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
        prev_thumb_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
        prev_index_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
        prev_middle_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
        Result_min_thumb_x = thumb_x - prev_thumb_x
        Result_min_index_x = index_x - prev_index_x
        Result_min_middle_x = middle_x - prev_middle_x
        if ((Result_min_middle_x > 0.025 and Result_min_index_x > 0.025) or (Result_min_thumb_x > 0.025 and Result_min_index_x > 0.025) or (Result_min_middle_x > 0.025 and Result_min_thumb_x > 0.025)) and thumb_y < prev_index_y and left_swipe_act == True:
            Hotkey_press.press_win_left()
            print("Swipe from right to left detected!")
            time.sleep(0.3)
        if ((Result_min_middle_x < -0.025 and Result_min_index_x < -0.025) or (Result_min_thumb_x < -0.025 and Result_min_index_x < -0.025) or (Result_min_middle_x < -0.025 and Result_min_thumb_x < -0.025)) and thumb_y < prev_index_y and right_swipe_act == True:
            Hotkey_press.press_win_right()
            print("Swipe left to right detected!")
            time.sleep(0.3)
        gesture_performed_svipe_levo_pravo = False
gesture_performed1 = False
def delayed_action_with_args_wait():
    global mode
    global gesture_performed1
    time.sleep(0.5)
    if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y < hand_landmarks.landmark[
                        mp_hands.HandLandmark.INDEX_FINGER_TIP].y:
        if not gesture_performed1:
            gesture_performed1 = True
            time.sleep(0.7)
            mode = "waiting"
            print("Mode waiting activated.")
            gesture_performed1 = False

gesture_performed = False
def delayed_action_with_args_cont(thump_act):
    global mode
    global gesture_performed
    time.sleep(0.5)
    print(1)
    if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y < hand_landmarks.landmark[
                        mp_hands.HandLandmark.INDEX_FINGER_TIP].y and thump_act == True:
        print(2)
        if not gesture_performed:
            print(3)
            gesture_performed = True
            time.sleep(0.5)
            mode = "control_mouse"
            print("Mode control_mouse activated.")
            gesture_performed = False

gesture_performed_scroll = False
def delayed_action_with_scroll(pinky_act):
    global mode
    global gesture_performed_scroll
    time.sleep(0.5)
    if pinky_act:
        if not gesture_performed_scroll:
            print(1)
            gesture_performed_scroll = True
            time.sleep(0.5)
            mode = "scrolling"
            print("Mode scrolling activated.")
            gesture_performed_scroll = False
gesture_performed_scroll_vert = False
def delayed_action_with_scroll_vert():
    global mode
    global gesture_performed_scroll_vert
    time.sleep(0.5)
    if not gesture_performed_scroll_vert:
        print(1)
        gesture_performed_scroll_vert = True
        time.sleep(0.5)
        mode = "waiting"
        print("Mode waiting activated.")
        gesture_performed_scroll_vert = False
gesture_performed_levo = False
def delayed_action_levo(left_act):
    global gesture_performed_levo
    time.sleep(0.5)
    if (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x) and \
    (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y) and \
    (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y) and \
    (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y) and \
            left_act == True:
        if not gesture_performed_levo:
            gesture_performed_levo = True
            Hotkey_press.press_win_e()
            time.sleep(0.9)
            gesture_performed_levo = False

gesture_performed_pravo = False
def delayed_action_pravo(pravo_act):
    global gesture_performed_pravo
    time.sleep(0.7)
    if pravo_act:
        if not gesture_performed_pravo:
            gesture_performed_pravo = True
            time.sleep(0.3)
            Hotkey_press.press_win_i()
            gesture_performed_pravo = False

gesture_performed_win_g = False
def delayed_action_win_g(hand_act):
    global gesture_performed_win_g
    time.sleep(0.5)
    if (index_thump_y < 0.3 and middle_index < 0.1 and ring_middle < 0.04 and pinky_ring < 0.08 and index_pinky < 0.085 and middle_pip_thump > 0.05 and
        thump_pinky_x > 0.06 and index_tip[1] < pinky) and distance_mid_x_y < 0.07 and index_tip[0] > thump_ip_x and hand_act == True:
        if not gesture_performed_win_g:
            gesture_performed_win_g = True
            Hotkey_press.press_win_g()
            time.sleep(0.9)
            gesture_performed_win_g = False

gesture_performed_win_d = False
def delayed_action_win_d(cul_act):
    global gesture_performed_win_d
    time.sleep(0.5)
    if cul_act:
        if not gesture_performed_win_d:
            gesture_performed_win_d = True
            Hotkey_press.press_win_d()
            time.sleep(0.9)
            gesture_performed_win_d = False
gesture_performed_weather = False
def delayed_action_weather(okey_act):
    global gesture_performed_weather
    time.sleep(0.6)
    if okey_act:
        if not gesture_performed_weather:
            gesture_performed_weather = True
            webbrowser.open("https://www.amazon.com/", 1, True)
            time.sleep(0.6)
            gesture_performed_weather = False

gesture_performed_bluetooth = False
def delayed_action_bluetooth(Fix_act):
    global gesture_performed_bluetooth
    time.sleep(0.6)
    if Fix_act:
        if not gesture_performed_bluetooth:
            gesture_performed_bluetooth = True
            bthprops_path = r"C:\Windows\System32\bthprops.cpl"
            os.startfile(bthprops_path)
            time.sleep(0.4)
            gesture_performed_bluetooth = False

gesture_performed_anime = False
def delayed_action_anime(Gojo_act):
    global gesture_performed_anime
    time.sleep(0.6)
    if Gojo_act:
        if not gesture_performed_anime:
            gesture_performed_anime = True
            webbrowser.open("https://www.anime-planet.com/anime/jujutsu-kaisen/videos", 1, True)
            time.sleep(0.5)
            gesture_performed_anime = False


gesture_performed_screan = False
def delayed_action_screan(keys, thump_up_act):
    global gesture_performed_screan
    time.sleep(0.5)
    thumb_tip = (hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x,
                 hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y)
    index_tip = (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
                 hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y)
    if distance >= 0.15 and thumb_tip[0] < index_tip[0] and thumb_tip[1] > index_tip[
                        1] and distance_mid > 0.23 and distance_RING > 0.23 and distance_pinky > 0.25 and thump_up_act == True:
        if not gesture_performed_screan:
            gesture_performed_screan = True
            time.sleep(0.5)
            pg.screenshot(keys)
            print("Screanshot succesed.")
            gesture_performed_screan = False

gesture_performed_LClick = False
def delayed_action_LCLick():
    global gesture_performed_LClick
    time.sleep(0.5)
    if not gesture_performed_LClick:
        gesture_performed_LClick = True
        print("LClick")
        pg.leftClick()
        time.sleep(0.5)
        gesture_performed_LClick = False
min_finger_distance = 0.1



print("Write a system of activate gester like this:  right_swipe_act = x\n"
      "left_swipe_act = x\nright_act = x\nleft_act = x\n"
      "thump_act = x\npinky_act = x\nthump_up_act = x\n"
      "hand_act = x\ncul_act = x\nokey_act = x\nGojo_act = x\n~~~x = True of False(T, F)~~~")

# right_swipe_act = input("Right_swipe_act = ")
# left_swipe_act = input("Left_swipe_act = ")
# right_act = input("Right_act = ")
# left_act = input("Left_act = ")
# thump_act = input("Thump_act = ")
# pinky_act = input("Pinky_act = ")
# thump_up_act = input("Thump_up_act = ")
# hand_act = input("Hand_act = ")
# cul_act = input("Cul_act = ")
# okey_act = input("Okey_act = ")
# Gojo_act = input("Gojo_act = ")
# Fix_act = input("Fix_act = ")

# left_act = data["Gesture_1"]
# thump_act = data["Gesture_2"]
# right_act = data["Gesture_3"]
# okey_act = data["Gesture_4"]
# thump_up_act = data["Gesture_5"]
# Gojo_act = data["Gesture_6"]
# hand_act = data["Gesture_7"]
# cul_act = data["Gesture_8"]
# pinky_act = data["Gesture_9"]
# Fix_act = data["Gesture_10"]
# right_swipe_act = data["Gesture_11"]
# left_swipe_act = data["Gesture_12"]
#
# variables = [right_swipe_act, left_swipe_act, right_act, left_act, thump_act, pinky_act, thump_up_act, hand_act, cul_act, okey_act, Gojo_act]
#
#
# for i in range(len(variables)):
#     if variables[i].lower() in ['true', 't']:
#         variables[i] = True
#     elif variables[i].lower() in ['false', 'f']:
#         variables[i] = False
#     else:
#         variables[i] = True
#
# right_swipe_act, left_swipe_act, right_act, left_act, thump_act, pinky_act, thump_up_act, hand_act, cul_act, okey_act, Gojo_act = variables
#
#
# print(right_swipe_act, left_swipe_act, right_act, left_act, thump_act, pinky_act, thump_up_act, hand_act, cul_act, okey_act, Gojo_act)


while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    result = hands.process(img)
    image_height, image_width, _ = img.shape

    with open('settings.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    left_act = data["Gesture_1"]
    thump_act = data["Gesture_2"]
    right_act = data["Gesture_3"]
    okey_act = data["Gesture_4"]
    thump_up_act = data["Gesture_5"]
    Gojo_act = data["Gesture_6"]
    hand_act = data["Gesture_7"]
    cul_act = data["Gesture_8"]
    pinky_act = data["Gesture_9"]
    Fix_act = data["Gesture_10"]
    right_swipe_act = data["Gesture_11"]
    left_swipe_act = data["Gesture_12"]

    variables = [right_swipe_act, left_swipe_act, right_act, left_act, thump_act, pinky_act, thump_up_act, hand_act,
                 cul_act, okey_act, Gojo_act]

    for i in range(len(variables)):
        if variables[i].lower() in ['true', 't']:
            variables[i] = True
        elif variables[i].lower() in ['false', 'f']:
            variables[i] = False
        else:
            variables[i] = True

    right_swipe_act, left_swipe_act, right_act, left_act, thump_act, pinky_act, thump_up_act, hand_act, cul_act, okey_act, Gojo_act = variables

    # print(right_swipe_act, left_swipe_act, right_act, left_act, thump_act, pinky_act, thump_up_act, hand_act, cul_act,
    #       okey_act, Gojo_act)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
            index_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y

            if (abs(prev_thumb_y - thumb_y) < min_movement_static) and (abs(prev_index_y - index_y) < min_movement_static):
                is_static_hand = True
            else:
                is_static_hand = False

            prev_thumb_y = thumb_y
            prev_index_y = index_y

            if mode == "waiting":
                if is_static_hand:
                    thumb_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                    index_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                    middle_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
                    threading.Thread(target=delayed_action_with_svipe_levo_pravo, args=(index_x, middle_x, right_swipe_act, left_swipe_act)).start()
                else:
                    print("5")
                    thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                    index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                    pinky_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
                    thumb_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                    index_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                    index_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
                    ring_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                    middle_fin_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                    middle_pip_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x
                    middle_fin_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
                    pinky_x = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x
                    ring_x = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x
                    ring_pip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x
                    ring_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
                    pinky_pip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x
                    ind_thu = abs(index_tip_y - thumb_tip_y)
                    ind_mid_fon = abs(index_tip_x - middle_fin_x)
                    index_thump_x = abs(index_tip_x - thumb_tip_x)
                    middle_ring_pip = abs(middle_fin_x - ring_pip)
                    middle_ring = abs(middle_fin_y - ring_y)
                    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                    print(f"Index_tip_x: {index_tip_x} --- Thumb_tip_x: {thumb_tip_x}")
                    print(f"index_tip_y: {index_tip_y} --- middle_fin_y: {middle_fin_y}")
                    print(f"index_tip_y: {index_tip_y} --- thumb_tip_y: {thumb_tip_y}")
                    print(f"index_tip_y: {index_tip_y} --- middle_fin_y: {middle_fin_y}")
                    print(f"index_tip_y: {index_tip_y} --- pinky_tip_y: {pinky_tip_y}")
                    print(f"index_tip_y: {index_tip_y} --- ring_y: {ring_y}")
                    print(f"ind_mid_fon: {ind_mid_fon} --- > 0.001")
                    print(f"index_thump_x: {index_thump_x} --- > 0.11")
                    if (index_tip_x > thumb_tip_x and middle_fin_x > index_tip_x and pinky_pip > ring_pip and ring_y > index_tip_y and ring_y > middle_fin_y
                            and middle_ring_pip < 0.05 and middle_ring > 0.05 and ring_x > index_tip_x and pinky_x > index_tip_x):
                        threading.Thread(target=delayed_action_bluetooth, args=(Fix_act,)).start()
                        print("Open bluetooth Settins.")
                    if (((index_tip_x < thumb_tip_x) or (index_tip_y < middle_fin_y)) and index_tip_y < thumb_tip_y and index_tip_y < middle_fin_y
                            and (index_tip_y < pinky_tip_y) and (index_tip_y < ring_y) and ind_mid_fon > 0.001):#0.1
                        threading.Thread(target=delayed_action_levo, args=(left_act,)).start()
                        print(5555)

                    if (index_tip_x > thumb_tip_x) and (index_tip_x > middle_fin_x) and (index_tip_y < thumb_tip_y) and (index_tip_y < middle_fin_y) and (index_tip_y < ring_y) and ind_thu < 0.23 and ind_mid_fon > 0.013 and index_tip_x > middle_pip_x and thumb_tip_y < ring_pip_y:#1
                        print(1234)
                        threading.Thread(target=delayed_action_pravo, args=(right_act,)).start()

                    distance_between_fingers = abs(thumb_tip_x - index_tip_x)
                    distance_between_fingers_pinky = abs(pinky_tip_y - thumb_tip_y)
                    distance_between_fingers_pinky_and_ring = abs(pinky_tip_y - ring_y)

                    desired_distance = 10.01

                    if thumb_tip_y < index_tip_y and abs(thumb_tip_x - index_tip_x) < 0.085 and abs(
                            distance_between_fingers - desired_distance) < 10 and abs(distance_between_fingers_pinky > 0.30):
                        print("Ok")
                        threading.Thread(target=delayed_action_with_args_cont, args=(thump_act,)).start()

                    if abs(distance_between_fingers_pinky < 0.3) and (pinky_tip_y < index_tip_y) and distance_between_fingers_pinky_and_ring > 0.2:
                        print("NON")
                        threading.Thread(target=delayed_action_with_scroll, args=(pinky_act,)).start()
                    thumb_tip = (hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x,
                                 hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y)
                    index_tip = (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
                                 hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y)
                    thump_ip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
                    thump_mcp_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x
                    middle_pip_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x
                    middle_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
                    index_pip_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x
                    middle_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
                    middle = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                    RING_x = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x
                    RING = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                    pinky_x = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x
                    pinky_x_pip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x
                    pinky = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
                    middle_tip = (hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,
                                 hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y)

                    distance = calculate_distance(thumb_tip, index_tip)
                    distance_mid = abs(middle - index_tip[1])
                    distance_RING = abs(index_tip[1] - RING)
                    distance_pinky = abs(index_tip[1] - pinky)
                    distance_mid_x_y = calculate_distance(index_tip, middle_tip)
                    distance_indpip_middle_x = abs(index_tip[0] - index_pip_x)
                    if distance >= 0.15 and thumb_tip[0] < index_tip[0] and thumb_tip[1] > index_tip[
                        1] and distance_mid > 0.23 and distance_RING > 0.23 and distance_pinky > 0.25 and RING > index_tip[1]:
                        threading.Thread(target=delayed_action_screan, args=(("screenshot.png"), thump_up_act)).start()
                    index_thump_x = abs(index_tip[0] - thumb_tip[0])
                    index_thump_y = abs(index_tip_y - thumb_tip_y)
                    middle_index = abs(middle - index_tip[1])
                    ring_middle = abs(RING - middle)
                    pinky_ring = abs(pinky - RING)
                    index_pinky = abs(index_tip_y - pinky)
                    thump_pinky = abs(thumb_tip_y - pinky)
                    thump_pinky_x = abs(thumb_tip[0]- pinky_x )
                    middle_pip_thump = abs(thumb_tip[1] - middle_pip_y)
                    if ((index_thump_y < 0.3 and middle_index < 0.1 and ring_middle < 0.04 and pinky_ring < 0.082 and
                            index_pinky < 0.088 and middle_pip_thump > 0.05 and thump_pinky_x > 0.06 and index_tip[1] < pinky) and
                            distance_mid_x_y < 0.07 and index_tip[0] > thump_ip_x and index_tip[0] > thump_mcp_x):
                        threading.Thread(target=delayed_action_win_g, args=(hand_act,)).start()
                        print("Hand up.")
                    if (index_thump_y < 0.18 and middle_index < 0.27 and ring_middle < 0.04 and pinky_ring < 0.08 and
                            index_pinky < 0.07 and middle_pip_thump < 0.04 and ring_y > thumb_tip[1] and index_tip[1] > thumb_tip[1]):
                        threading.Thread(target=delayed_action_win_d, args=(cul_act,)).start()
                        print("Hand over.")
                    if (pinky_x_pip > RING_x and RING_x > middle_x and middle_x > index_tip[0] and middle_x > thumb_tip[0] and pinky > RING and RING < middle
                            and index_thump_x < 0.11 and index_thump_y < 0.5 ): #and index_tip[1] < thumb_tip[1]and index_tip[1] > middle_tip[1]
                        threading.Thread(target=delayed_action_weather, args=(okey_act,)).start()
                        print("Okey let's go!!!!!!!!!!!")
                    if (middle_pip_x > index_tip[0] and pinky_x < index_tip[0] and pinky_x > thumb_tip[0]):
                        print("Open anime Gojo.")
                        threading.Thread(target=delayed_action_anime, args=(Gojo_act,)).start()
            elif mode == "control_mouse":
                index_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                thumb_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                middle_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
                distance_between_fingers_x = abs(index_tip_x - thumb_tip_x)
                distance_between_fingers_y = abs(index_tip_y - thumb_tip_y)
                distance_between_fingers_mid_y = abs(index_tip_y - middle_tip_y)
                distance_between_fingers_thumb_mid_y = abs(middle_tip_y - thumb_tip_y)
                ser_width = screen_width // image_width
                ser_hight = screen_height // image_height
                for lm in hand_landmarks.landmark:
                    if index_tip_x > 0.5 and index_tip_y < 0.5:
                        ind_x = (index_tip_x - 0.5) / 0.5 * 100 * 2
                        ind_y = (0.5 - index_tip_y) / 0.5 * 100 * 3.5
                        cx, cy = int(lm.x * screen_width + ind_x), int(lm.y * screen_height - ind_y)

                        avg_cursor_x = int(avg_cursor_x * avg_factor + cx * (1 - avg_factor))
                        avg_cursor_y = int(avg_cursor_y * avg_factor + cy * (1 - avg_factor))

                        avg_cursor_x = min(max(avg_cursor_x, 0), screen_width - 0.1)
                        avg_cursor_y = min(max(avg_cursor_y, 0), screen_height - 0.1)
                        mouse.move(avg_cursor_x, avg_cursor_y)
                        distance_between_fingers_ind_mid_y = abs(index_tip_y - middle_tip_y)
                        distance_between_fingers_ind_mid_x = abs(index_tip_x - middle_tip_x)
                        if abs(distance_between_fingers_y < 0.05) and abs(distance_between_fingers_mid_y > 0.04) and abs(distance_between_fingers_x < 0.02):
                            threading.Thread(target=delayed_action_LCLick).start()
                            print("LClick")
                        if thumb_tip_y < index_tip_y and distance_between_fingers_ind_mid_x < 0.01 and distance_between_fingers_ind_mid_y > 0.04:
                            print("Leave")
                            threading.Thread(target=delayed_action_with_args_wait).start()
                    if index_tip_x > 0.5 and index_tip_y > 0.5:
                        ind_x = (index_tip_x - 0.5) / 0.5 * 100 * 2
                        ind_y = (0.5 - index_tip_y) / 0.5 * 100 * 1.3
                        cx, cy = int(lm.x * screen_width + ind_x), int(lm.y * screen_height - ind_y)

                        avg_cursor_x = int(avg_cursor_x * avg_factor + cx * (1 - avg_factor))
                        avg_cursor_y = int(avg_cursor_y * avg_factor + cy * (1 - avg_factor))

                        avg_cursor_x = min(max(avg_cursor_x, 0), screen_width - 0.1)
                        avg_cursor_y = min(max(avg_cursor_y, 0), screen_height - 0.1)

                        mouse.move(avg_cursor_x, avg_cursor_y)
                        distance_between_fingers_ind_mid_y = abs(index_tip_y - middle_tip_y)
                        distance_between_fingers_ind_mid_x = abs(index_tip_x - middle_tip_x)
                        if abs(distance_between_fingers_y < 0.05) and abs(distance_between_fingers_mid_y < 0.05) and abs(distance_between_fingers_x < 0.02):
                            threading.Thread(target=delayed_action_LCLick).start()
                            print("LClick")
                        if thumb_tip_y < index_tip_y and distance_between_fingers_ind_mid_x < 0.01 and distance_between_fingers_ind_mid_y > 0.04:
                            print("Leave")
                            threading.Thread(target=delayed_action_with_args_wait).start()
                    if index_tip_x < 0.5 and index_tip_y < 0.5:
                        ind_x = (index_tip_x - 0.5) / 0.5 * 100 * 4
                        ind_y = (0.5 - index_tip_y) / 0.5 * 100 * 3.5
                        cx, cy = int(lm.x * screen_width + ind_x), int(lm.y * screen_height - ind_y)

                        avg_cursor_x = int(avg_cursor_x * avg_factor + cx * (1 - avg_factor))
                        avg_cursor_y = int(avg_cursor_y * avg_factor + cy * (1 - avg_factor))

                        avg_cursor_x = min(max(avg_cursor_x, 0), screen_width - 0.1)
                        avg_cursor_y = min(max(avg_cursor_y, 0), screen_height - 0.1)

                        mouse.move(avg_cursor_x, avg_cursor_y)
                        distance_between_fingers_ind_mid_y = abs(index_tip_y - middle_tip_y)
                        distance_between_fingers_ind_mid_x = abs(index_tip_x - middle_tip_x)
                        if abs(distance_between_fingers_y < 0.05) and abs(distance_between_fingers_mid_y > 0.04) and abs(distance_between_fingers_x < 0.02):
                            threading.Thread(target=delayed_action_LCLick).start()
                            print("LClick")
                        if thumb_tip_y < index_tip_y and distance_between_fingers_ind_mid_x < 0.01 and distance_between_fingers_ind_mid_y > 0.04:
                            print("Leave")
                            threading.Thread(target=delayed_action_with_args_wait).start()
                    if index_tip_x < 0.5 and index_tip_y > 0.5:
                        ind_x = (index_tip_x - 0.5) / 0.5 * 100 * 4
                        ind_y = (0.5 - index_tip_y) / 0.5 * 100 * 1.3
                        cx, cy = int(lm.x * screen_width + ind_x), int(lm.y * screen_height - ind_y)

                        avg_cursor_x = int(avg_cursor_x * avg_factor + cx * (1 - avg_factor))
                        avg_cursor_y = int(avg_cursor_y * avg_factor + cy * (1 - avg_factor))

                        avg_cursor_x = min(max(avg_cursor_x, 0), screen_width - 0.1)
                        avg_cursor_y = min(max(avg_cursor_y, 0), screen_height - 0.1)
                        mouse.move(avg_cursor_x, avg_cursor_y)
                        distance_between_fingers_ind_mid_y = abs(index_tip_y - middle_tip_y)
                        distance_between_fingers_ind_mid_x = abs(index_tip_x - middle_tip_x)

                        if abs(distance_between_fingers_y < 0.05) and abs(distance_between_fingers_mid_y > 0.04) and abs(distance_between_fingers_x < 0.03):
                            threading.Thread(target=delayed_action_LCLick).start()
                            print("LClick")
                        if thumb_tip_y < index_tip_y and distance_between_fingers_ind_mid_x < 0.01 and distance_between_fingers_ind_mid_y > 0.04:
                            print("Leave")
                            threading.Thread(target=delayed_action_with_args_wait).start()
            elif mode == "scrolling":
                middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                con_y = 0
                thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                pinky_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
                ring_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                distance_between_fingers_pinky = abs(pinky_tip_y - thumb_tip_y)
                distance_between_fingers_mid = abs(middle_tip_y - index_tip_y)
                distance_between_fingers_ring = abs(pinky_tip_y - ring_y)
                if abs(distance_between_fingers_pinky < 0.31) and abs(pinky_tip_y < index_tip_y) and abs(distance_between_fingers_ring > 0.15):
                    threading.Thread(target=delayed_action_with_scroll_vert).start()
                def scroll_page(y):
                    global con_y
                    if y > 250:
                        con_y = (y - 250) // 2 * 2
                        pg.scroll(-con_y)
                    elif y < 250:
                        con_y = abs((y - 250) // 2 * 2)
                        pg.scroll(con_y)



                index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                x, y = int(index_finger.x * img.shape[1]), int(index_finger.y * img.shape[0])
                index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                if abs(distance_between_fingers_mid < 0.05):
                    scroll_page(y)

    # cv2.imshow("Hand tracking", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
