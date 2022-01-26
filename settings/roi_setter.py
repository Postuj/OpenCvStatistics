import cv2, json, os
# import numpy as np

if not os.path.exists('./config'):
    os.makedirs('./config')

vid = cv2.VideoCapture(0)

width_img = 480
height_img = 640

vid.set(3, width_img)
vid.set(4, height_img)

if os.path.exists('./config/config.json'):
    with open('./config/config.json', 'r') as f:
        config = json.load(f)
else:
    config = {}


def getRois():
    try:
        roi_left = cv2.selectROI('roi left', frame)
        print(roi_left)
        roi_right = cv2.selectROI('roi right', frame)
        print(roi_right)
        rois = [roi_left, roi_right]
        config['rois'] = rois
    except:
        print('exception')


while(True):
    _, frame = vid.read()

    cv2.imshow('Config', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # press Q to quit
        break
    if cv2.waitKey(1) & 0xFF == ord('r'):
        # press S to save roi positions in config
        getRois()
        with open('./config/config.json', 'w') as f:
            json.dump(config, f)
        break
    


vid.release()
cv2.destroyAllWindows()
