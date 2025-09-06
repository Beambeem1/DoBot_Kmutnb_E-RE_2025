#----------------------------------------------------------------------------Do_Bot-----------------------------------------------------------------------------#

from pydobot import Dobot 
import time 

dev = Dobot(port= "/dev/ttyUSB0")

F1 = -45
F2 = -20 
F3 = 4
F4 = 28


def centerDrop_1(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_2(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)
    

def centerDrop_3(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_4(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_5(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_6(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_7(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_8(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_9(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def Home():
    dev.move_to(x=200,y =0 ,z = 100 ,r =0)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#((x,y,z,r ), (j1,j2,j3,j4)) = dev.get_pose()
#print(dev.get_pose())
#dev.move_to(x=200,y=0,z=-45)
#dev.suck(False)

#def test_autocenterDrop(cx,cy,H):
    #gap = 6 

    #dev.move_to(x =cx , y=cy , z = z+gap,r=r)
    #dev.move_to(x =cx , y =cy , z=z , r=r)
    #dev.suck(True)
    #dev.move_to(x=x1 , y= y1, z=H ,r=r)
    #dev.move_to(230,44,H,r=r)
    #dev.move_to(230,44,z1,r)
    #dev.suck(False)
    #dev.move_to(230,44,H,r=r)




#def SD(x1,y1,x2,y2):
    #r = 0 
    #z =-45
    #gap  = 6
    #dev.move_to(x=x1 , y = y1 , z= z+gap ,r=r)
    #dev.move_to(x =x1 , y =y1 , z=z , r=r)
    #dev.suck(True)
    #dev.move_to(x=x1 , y= y1, z=z+gap ,r=r)
    #dev.move_to(x=x2 , y = y2 , z= z+gap ,r=r)
    #dev.move_to(x =x2 , y =y2 , z=z , r=r)
    #dev.suck(False)
    #dev.move_to(x=x2 , y= y2, z=z+gap ,r=r)















import numpy as np
import cv2 as cv


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
                        centerDrop_1(71,75,76,77)  #ค่าทั้งหมดนั้นเป็นค่าสมมุติ
                        

               
       

    cv.imshow("Original", frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()






