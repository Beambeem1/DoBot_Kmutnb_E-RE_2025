import numpy as np
import cv2 as cv
#import Dobot_def

color1 = input("กรอกสีที่ 1 (Red/Green/Yellow/Blue): ").capitalize()
color2 = input("กรอกสีที่ 2 (Red/Green/Yellow/Blue): ").capitalize()
target_colors = [color1, color2]


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()


color_ranges = {
    "Green": ([45, 100, 100], [75, 255, 255]),
    "Yellow": ([25, 130, 130], [35, 255, 255]),
    "Blue": ([100, 150, 100], [130, 255, 255]),
    "Red1": ([0, 150, 150], [10, 255, 255]),
    "Red2": ([160, 150, 150], [180, 255, 255]) 
}

def get_red_mask(hsv_img):
    lower1, upper1 = color_ranges["Red1"]
    lower2, upper2 = color_ranges["Red2"]
    mask1 = cv.inRange(hsv_img, np.array(lower1), np.array(upper1))
    mask2 = cv.inRange(hsv_img, np.array(lower2), np.array(upper2))
    return cv.bitwise_or(mask1, mask2)

while True:
    ret, frame = cap.read()
    if not ret:
        print(" Exiting ...")
        break

    kernel = np.ones((5, 5), np.uint8)
    frame = cv.convertScaleAbs(frame, alpha=1.2, beta=10)
    hsv_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    used_contours = {} 

    for idx, color in enumerate(target_colors):  
        if color == "Red":
            mask = get_red_mask(hsv_image)
        else:
            lower, upper = color_ranges[color]
            mask = cv.inRange(hsv_image, np.array(lower), np.array(upper))

        # Clean noise
        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

        # หา contours
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        if contours:
            # เรียงจากใหญ่ → เล็ก
            contours = sorted(contours, key=cv.contourArea, reverse=True)

            # ดึงจำนวนที่ใช้ไปแล้วสำหรับสีนี้
            used = used_contours.get(color, 0)

            if len(contours) > used:
                cnt = contours[used] 
                area = cv.contourArea(cnt)
                if area > 500:
                    x, y, w, h = cv.boundingRect(cnt)
                    cx = x + w // 2
                    cy = y + h // 2
                    cv.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
                    cv.circle(frame, (cx, cy), 5, (255, 255, 255), -1)
                    cv.putText(frame, f"{color} #{used+1}", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                    cv.putText(frame, f"({cx}, {cy})", (x, y + h + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    print(cx, cy, f"{color} #{used+1}")

                    used_contours[color] = used + 1
                    if 170 <= cx <= 180 and 150 <= cy <= 160:
                        print("Dobot connect")
                        break
                        

               
       

    cv.imshow("Original", frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()