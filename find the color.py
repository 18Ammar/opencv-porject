import cv2
import numpy as np
import cvzone
from ttsp import AI


   
    # def empty(a):
    #    pass
# cv2.namedWindow("TrackBar")
# cv2.resizeWindow("TrackBar",650,220)
# mySerial = SerialObject("COM15",9600,1)

# cv2.createTrackbar("Hue min","TrackBar",0,179,empty)
# cv2.createTrackbar("Hue max","TrackBar",179,179,empty)
# cv2.createTrackbar("set min","TrackBar",0,255,empty)
# cv2.createTrackbar("set max","TrackBar",2550,255,empty)
# cv2.createTrackbar("val min","TrackBar",0,255,empty)
# cv2.createTrackbar("val max","TrackBar",255,255,empty)


class findColor:
    def __init__(self) -> None:
        pass
    
    
 

    def TheColor(img):

        imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        color = ""
        
        #detect yollow color
        lower1 = np.array([25, 70, 120])
        upper1 = np.array([30, 255, 255])

        # detect the green color
        lower2 = np.array([40, 70, 80])
        upper2 = np.array([70, 255, 255])

        # detect the Red color
        lower3 = np.array([0, 50, 120])
        upper3 = np.array([10, 255, 255])


        # detect the blue color
        lower4 = np.array([90, 60, 0])
        upper4 = np.array([121, 255, 255])

        mask1 = cv2.inRange(imghsv, lower1, upper1)

        mask2 = cv2.inRange(imghsv, lower2, upper2)

        mask3 = cv2.inRange(imghsv, lower3, upper3)

        mask4 = cv2.inRange(imghsv, lower4, upper4)

        ## finding the contours for yellow color

        count1, hiarchy = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for c in count1:
            area1 = cv2.contourArea(c)
            if area1 <= 5000 and area1 >= 3000:
                cv2.drawContours(img, [c], -1, (150, 255, 150), 3)
    
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(img, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(img, "yellow", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)
                color = "yellow"
                # mySerial.sendData([1, 0, 0, 0, 0])

        ## finding the contours for green color
        count2, hiarchy = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for c in count2:
            area2 = cv2.contourArea(c)
            if area2 <= 5000 and area2 >= 500:
                cv2.drawContours(img, [c], -1, (0, 255, 0), 3)

                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(img, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(img, "Green", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                color = "green"
                # mySerial.sendData([0, 1, 0, 0, 0])

        ## finding the contours for RED color
        count3, hiarchy = cv2.findContours(mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for c in count3:
            area3 = cv2.contourArea(c)
            if area3 <= 5000 and area3 >= 500:
                cv2.drawContours(img, [c], -1, (0, 0, 255), 3)

                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(img, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(img, "RED", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                color = "red"
                # mySerial.sendData([0, 0, 0, 0, 1])

        ## finding the contours for yellow color
        count4, hiarchy = cv2.findContours(mask4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for c in count4:
            area4 = cv2.contourArea(c)

            if area4 <= 10000 and area4 >= 200:
                cv2.drawContours(img, [c], -1, (255, 0, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(img, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(img, "BLUE", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                color = "blue"
                # mySerial.sendData([0, 0, 0, 1, 0])
        return color

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3,750)
    cap.set(4,750)
    while True:
        success,img = cap.read()


        # h_min = cv2.getTrackbarPos("Hue min","TrackBar")
        # h_max = cv2.getTrackbarPos("Hue max","TrackBar")
        # s_min = cv2.getTrackbarPos("set min", "TrackBar")
        # s_max = cv2.getTrackbarPos("set max", "TrackBar")
        # v_min = cv2.getTrackbarPos("val min", "TrackBar")
        # v_max = cv2.getTrackbarPos("val max", "TrackBar")

        # lower = np.array([h_min,s_min,v_min])
        # upper = np.array([h_max,s_max,v_max])
        # mask = cv2.inRange(imghsv,lower,upper)

        # detect the yellow color

        # cv2.imshow("mask1",mask)

        fd = findColor()
        color = fd.TheColor(img)
        print(color)

        cv2.flip(img,-1,img)
        cv2.imshow("img", img)
        cv2.waitKey(1)

if __name__ == "mian":
    main()