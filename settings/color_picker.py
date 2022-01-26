import cv2, json, os
import numpy as np

if not os.path.exists('./config'):
    os.makedirs('./config')

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
#cap.set(10, 130) #Brigthness

if os.path.exists('./config/config.json'):
    with open('./config/config.json', 'r') as f:
        config = json.load(f)
else:
    config = {}

def empty(a):
    pass

cv2.namedWindow('HSV')
cv2.resizeWindow('HSV', 640, 240)
cv2.createTrackbar('HUE Min', 'HSV', 0, 179, empty)
cv2.createTrackbar('SAT Min', 'HSV', 0, 255, empty)
cv2.createTrackbar('VAL Min', 'HSV', 0, 255, empty)
cv2.createTrackbar('HUE Max', 'HSV', 179, 179, empty)
cv2.createTrackbar('SAT Max', 'HSV', 255, 255, empty)
cv2.createTrackbar('VAL Max', 'HSV', 255, 255, empty)

while True:
    _, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('HUE Min', 'HSV')
    h_max = cv2.getTrackbarPos('HUE Max', 'HSV')
    s_min = cv2.getTrackbarPos('SAT Min', 'HSV')
    s_max = cv2.getTrackbarPos('SAT Max', 'HSV')
    v_min = cv2.getTrackbarPos('VAL Min', 'HSV')
    v_max = cv2.getTrackbarPos('VAL Max', 'HSV')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    h_stack = np.hstack([img, mask])

    cv2.imshow('Horizontal stack', h_stack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # press Q to quit
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # press S to save mask params in config
        config['h_min'] = h_min
        config['h_max'] = h_max
        config['s_min'] = s_min
        config['s_max'] = s_max
        config['v_min'] = v_min
        config['v_max'] = v_max
        with open('./config/config.json', 'w') as f:
            json.dump(config, f)
        break

cap.release()
cv2.destroyAllWindows()