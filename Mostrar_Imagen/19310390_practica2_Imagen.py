import cv2
import numpy as np

imagen = cv2.imread('RGB.png',1)
cv2.imshow('Prueba de imagen', imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()

video = cv2.VideoCapture('Minecraft.mp4')
while(video.isOpened()):
    ret, frame = video.read()
    if(ret==True):
        cv2.imshow('Video', frame)
        if(cv2.waitKey(15) & 0xFF == ord('s')):
            break
    else:
        break
video.release()
cv2.destroyAllWindows    
