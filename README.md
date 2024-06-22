# Volume Control with Thumb and Index Finger 📶👍☝️

![Untitled video - Made with Clipchamp](https://github.com/fastuptime/Volume_increase_decrease_according_to_the_distance_of_the_thumb_and_index_finger/assets/63351166/78226809-5439-4adb-938e-898521bb3600)

## Overview 🌟

Welcome to the **Volume Control with Thumb and Index Finger** repository! This project leverages OpenCV and MediaPipe to adjust your computer's volume based on the distance between your thumb and index finger. When the fingers are close together, the volume decreases; when they are further apart, the volume increases.

## Features 🚀

- **Real-Time Hand Gesture Recognition**: Adjust the volume using the distance between your thumb and index finger.
- **Visual Feedback**: Provides on-screen indicators for volume adjustments.
- **Intuitive and Natural**: No additional hardware required, just your webcam.

## Installation and Setup 🛠️

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/fastuptime/Volume_increase_decrease_according_to_the_distance_of_the_thumb_and_index_finger.git
   cd Volume_increase_decrease_according_to_the_distance_of_the_thumb_and_index_finger
   ```

2. **Install Dependencies**:
   - Ensure you have Python installed.
   - Install required packages:
     ```sh
     pip install opencv-python mediapipe numpy pyautogui
     ```

3. **Run the Program**:
   - Execute the Python script:
     ```sh
     python volume_control.py
     ```

## Usage 💻

1. **Launch the Program**:
   - Run the script. The webcam will start, and the program will begin detecting hand gestures.

2. **Volume Control**:
   - Bring your thumb and index finger close together to decrease the volume.
   - Move your thumb and index finger apart to increase the volume.
   - Visual feedback will be displayed on the screen indicating the current action.

3. **Exit the Program**:
   - Press the 'Esc' key to quit the program.

## Code Explanation 📝

### `volume_control.py`

- **Import Libraries**:
  ```python
  import cv2
  import mediapipe as mp
  import numpy as np
  import pyautogui
  ```

- **Initialize MediaPipe and OpenCV**:
  ```python
  mp_drawing = mp.solutions.drawing_utils
  mp_hands = mp.solutions.hands

  cap = cv2.VideoCapture(0)
  ```

- **Volume Control Function**:
  ```python
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
  ```

## Contributing 🤝

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
