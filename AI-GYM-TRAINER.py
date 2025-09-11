import cv2
import numpy as np
import time
import PoseModule as pm
ptime=0


cap=cv2.VideoCapture(0)

detectorPose=pm.poseDetector()
count=0
countright=0
dir=0
dirright=0


while True:
    success,img=cap.read()

    img=detectorPose.findPose(img,draw=False)
    lmlist=detectorPose.findPosition(img,draw=False)

    if len(lmlist)!=0:
        #Right arm
        angleright=detectorPose.findAngle(img,12,14,16)
        perright = np.interp(angleright, (160, 320), (0, 100))
        barright = np.interp(angleright, (160, 320), (400,100))
        #print(angleright,perright)
        # check for the right dumbell curls
        colorr=(0,0,255)
        if perright == 100:
            colorr = (0, 255, 0)
            if dirright == 0:
                countright += 0.5
                dirright = 1
        if perright == 0:
            colorr = (0, 0, 255)
            if dirright == 1:
                countright += 0.5
                dirright = 0
        cv2.putText(img, f'RIGHT CURLS:{countright}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.rectangle(img, (10, 100), (50, 400), colorr, 2)
        cv2.rectangle(img, (10, int(barright)), (50, 400), colorr, cv2.FILLED)
        cv2.putText(img, f'{abs(int(perright))}%', (10, 430), cv2.FONT_HERSHEY_SIMPLEX, 1, colorr, 2)

        #Left arm
        angleleft=detectorPose.findAngle(img,11,13,15)
        perleft=np.interp(angleleft,(40,190),(0,100))
        barleft=np.interp(angleleft,(40,190),(100,400))
        #print(angleleft, perleft)

        #check for the left dumbell curls
        colorl=(0,0,255)
        if perleft==0:
            colorl = (0, 255, 0)
            if dir==0:
                count+=0.5
                dir=1
        if perleft==100:
            colorl = (0, 0,255)
            if dir==1:
                count+=0.5
                dir=0
        cv2.putText(img,f'LEFT CURLS:{count}',(450,70),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        cv2.rectangle(img,(550,100),(600,400),colorl,2)
        cv2.rectangle(img,(550,int(barleft)),(600,400),colorl,cv2.FILLED)
        cv2.putText(img,f'{abs(int(perleft-100))}%',(550,430),cv2.FONT_HERSHEY_SIMPLEX,1,colorl,2)


    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,str(int(fps)),(200,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)




    cv2.imshow('frame',img)
    cv2.waitKey(1)