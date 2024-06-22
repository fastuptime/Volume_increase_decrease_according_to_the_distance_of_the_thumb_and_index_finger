import cv2
import mediapipe as mp
import numpy as np
import time
import keyboard
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

def volume_control():
    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Kamera açilamadi. Yazilim kapatiliyor.")
                continue

            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    x1 = hand_landmarks.landmark[4].x
                    y1 = hand_landmarks.landmark[4].y
                    x2 = hand_landmarks.landmark[8].x
                    y2 = hand_landmarks.landmark[8].y
                    length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                    if length < 0.1:
                        pyautogui.press('volumedown')
                        cv2.putText(image, 'Ses Azaltiliyor', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    elif length > 0.2:
                        pyautogui.press('volumeup')
                        cv2.putText(image, 'Ses Arttiriliyor', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    cv2.circle(image, (int(x1 * 640), int(y1 * 480)), 5, (255, 0, 0), cv2.FILLED)
                    cv2.circle(image, (int(x2 * 640), int(y2 * 480)), 5, (255, 0, 0), cv2.FILLED)


            cv2.imshow('Ses Kontrol', image)
            if cv2.waitKey(5) & 0xFF == 27:
                break

volume_control()
cap.release()
cv2.destroyAllWindows()
