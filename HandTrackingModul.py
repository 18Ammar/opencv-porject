import cv2
import mediapipe as mp


class HandDetector():
    def __init__(self,mode=False ,maxHand=2 ,detectionCon=0 ,trackCon=0.5):
        self.mode = mode
        self.maxHand = maxHand
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode,self.maxHand,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []

    def FindHands(self ,img ,Draw = True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
       #print(result)
        if self.result.multi_hand_landmarks:
            for handlms in self.result.multi_hand_landmarks:
                if Draw:
                    self.mpDraw.draw_landmarks(img, handlms, self.mphands.HAND_CONNECTIONS)

        return img

    def fingersUp(self, myHand):
        """
        Finds how many fingers are open and returns in a list.
        Considers left and right hands separately
        :return: List of which fingers are up
        """
        myHandType = myHand["type"]
        myLmList = myHand["lmList"]
        if self.results.multi_hand_landmarks:
            fingers = []
            # Thumb
            if myHandType == "Right":
                if myLmList[self.tipIds[0]][0] > myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if myLmList[self.tipIds[0]][0] < myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if myLmList[self.tipIds[id]][1] < myLmList[self.tipIds[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers

    def findPostion(self ,img ,noHand=0 ,Draw=True):
        lmList = []
        if self.result.multi_hand_landmarks:
            myhand= self.result.multi_hand_landmarks[noHand]
            for id,lm in enumerate(myhand.landmark):
               h, w ,c = img.shape
               cx,cy = int (lm.x * w) , int(lm.y * h)
               lmList.append([id,cx,cy])
               if Draw:
                   cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
        return lmList

def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = cap.read()
        img = detector.FindHands(img)
        lmList = detector.findPostion(img)
        print(lmList)
        cv2.imshow("app", img)
        cv2.waitKey(1)

if __name__=="__main__":
    main()