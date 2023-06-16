import numpy as np
import cv2

confidenceThreshold = 0.5
NMSThreshold = 0.3

modelConfiguration = 'cfg/yolov3.cfg'
modelWeights = 'yolov3.weights'
classFile = 'coco.names'
classNames = []

with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split("\n")

print(classNames)    


