# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv

imagen = cv.imread('girasoles_osc.jpg')
alto, largo = imagen.shape[:2]

crom = []
img2 = cv.imread('girasoles_osc.jpg')

for y in range(alto):
    for x in range(largo):
        crom = []
        b,g,r = imagen[y,x]
        bgr = [b,g,r]
        try:
            for i in bgr:
                crom.append(int((int(i)/(int(r)+int(g)+int(b)))*255))
        except ZeroDivisionError:
            crom = [0,0,0]
        img2[y,x] = crom

img3 = np.zeros((alto, largo))

for y in range(alto):
    for x in range(largo):
        b,g,r = img2[y,x]
        if r>=117 and r<=155 and g>=81 and g<=111 and b>=13 and b<=30:
            img3[y,x] = 255
        else:
            img3[y,x] = 0        
        
imagen = cv.imread('girasoles_osc.jpg')
cv.imshow('Original',imagen)
cv.imshow('Cromaticas', img2)
cv.imshow('Imagen binaria',img3)

cv.waitKey(0)
cv.destroyAllWindows()