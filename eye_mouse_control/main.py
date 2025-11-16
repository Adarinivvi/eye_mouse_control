import cv2
import mediapipe as mp
import pyautogui
import sys

# Print instructions
print("\nWelcome to Hands-Free Mouse Control Using Eye Movement!")
print("Make sure your webcam is connected and permissions are granted.")
print("Press 'q' to quit the preview window.\n")

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)
mp_drawing = mp.solutions.drawing_utils

# Webcam setup
try:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Webcam not accessible")
except Exception as e:
    print("Could not access webcam — check if another app is using it.")
    sys.exit()

# Screen size
screen_w, screen_h = pyautogui.size()

# Calibration toggle
SMOOTHING = True
prev_x, prev_y = 0, 0

def get_eye_landmarks(landmarks, frame_w, frame_h):
    left_eye = landmarks[474]
    right_eye = landmarks[475]
    x = int(left_eye.x * frame_w)
    y = int(left_eye.y * frame_h)
    return x, y

def detect_blink(landmarks):
    left_top = landmarks[159]
    left_bottom = landmarks[145]
    vertical_distance = abs(left_top.y - left_bottom.y)
    return vertical_distance < 0.015

while True:
    ret, frame = cap.read()
    if not ret:
        print("Could not read frame from webcam.")
        break

    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    try:
        results = face_mesh.process(rgb_frame)
    except Exception as e:
        print("Mediapipe error — try reinstalling the package.")
        break

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark

            # Eye tracking
            x, y = get_eye_landmarks(landmarks, frame_w, frame_h)
            screen_x = screen_w * x / frame_w
            screen_y = screen_h * y / frame_h

            if SMOOTHING:
                screen_x = (screen_x + prev_x) / 2
                screen_y = (screen_y + prev_y) / 2
                prev_x, prev_y = screen_x, screen_y

            try:
                pyautogui.moveTo(screen_x, screen_y)
            except Exception:
                print("Permission denied — allow Accessibility and Camera permissions.")
                break

            # Blink detection
            if detect_blink(landmarks):
                pyautogui.click()

            # Optional preview window
            mp_drawing.draw_landmarks(
                frame, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS,
                mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
                mp_drawing.DrawingSpec(color=(0,0,255), thickness=1)
            )

    cv2.imshow("Eye Mouse Control - Press 'q' to Quit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()