import cv2 as cv
import numpy as np

imagen = cv.imread('girasoles_g.jpg')
alto, largo = imagen.shape[:2]

img2 = cv.imread('girasoles_g.jpg')

b_max, g_max, r_max = 0,0,0        

for y in range(alto):
    for x in range(largo):
        b,g,r = imagen[y,x]
        if b>b_max:
            b_max = b
        if g>g_max:
            g_max = g
        if r>r_max:
            r_max = r
        try:
            b = int((int(b*255))/int(b_max))
            g = int((int(g*255))/int(g_max))
            r = int((int(r*255))/int(r_max))
        except ZeroDivisionError:
            b = 0
            g = 0
            r = 0
        img2[y,x] = b,g,r

img3 = np.zeros((alto, largo))

for y in range(alto):
    for x in range(largo):
        b,g,r = img2[y,x]
        if r>=239 and r<=255 and g>=149 and g<=223 and b>=23 and b<=94:
            img3[y,x] = 255
        else:
            img3[y,x] = 0        
        

cv.imshow('Original',imagen)
cv.imshow('White Patch', img2)
cv.imshow('Imagen binaria',img3)

cv.waitKey(0)
cv.destroyAllWindows()