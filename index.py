import cv2, math, os, json
import numpy as np
import pyautogui as pg

width_img = 480
height_img = 640

# Cap init
cap = cv2.VideoCapture(0)
cap.set(3, width_img)
cap.set(4, height_img)


# Load config
if os.path.exists('./config/config.json'):
    print('Config found, loading...')
    with open('./config/config.json', 'r') as f:
        config = json.load(f)
else:
    print('Config file not found, setting default params...')
    config = {"h_min": 0, "h_max": 179, "s_min": 0, "s_max": 255, "v_min": 30,
              "v_max": 101, "rois": [[358, 358, 80, 71], [251, 359, 83, 75]]}


# Mask params setup
lower = np.array([config['h_min'], config['s_min'], config['v_min']])
upper = np.array([config['h_max'], config['s_max'], config['v_max']])


# ROI setup
rl = config['rois'][0]
rr = config['rois'][1]


# Timers setup
max_timer = 25
current_timer = 25


# Row gap setup
row_gap = 5


def checkRoi(roi):
    height, width, _ = roi.shape
    for row in range(math.floor(height/row_gap)):
        for col in range(math.floor(width)):
            if roi[row*row_gap, col][0] >= 220:
                return True
    return False

while(True):
    _, frame = cap.read()
    HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(HSV_frame, lower, upper)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    rr_frame = mask[int(rr[1]):int(rr[1]+rr[3]),
                    int(rr[0]):int(rr[0]+rr[2])]
    rl_frame = mask[int(rl[1]):int(rl[1]+rl[3]),
                    int(rl[0]):int(rl[0]+rl[2])]

    
    if(current_timer == max_timer):
        if(checkRoi(rl_frame)):
            print('left click')
            pg.press('left')
            current_timer = 0

        if(checkRoi(rr_frame)):
            print('right click')
            pg.press('right')
            current_timer = 0

    # It works only when rois have same heights :(
    # possible fix is to take one, wider roi instead of two
    # and divide it

    # roi_stack = np.hstack([rl_frame, rr_frame])
    # cv2.imshow('roi stack', roi_stack)

    if(current_timer < max_timer):
        current_timer += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
