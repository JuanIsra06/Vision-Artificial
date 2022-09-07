import cv2 as cv
import numpy as np

def trasladar (img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    tam = (img.shape[1], img.shape[0]) 
    return cv.warpAffine(img, transMat, tam)

def rotar(img, ang, puntoRot=None):
    (alto,ancho) = img.shape [:2] 
    if puntoRot is None:
        puntoRot = (alto//2,ancho//2)
    rotMat = cv.getRotationMatrix2D(puntoRot, ang, 1.0)
    tam = (ancho,alto)
    return cv.warpAffine(img, rotMat, tam)


img = cv.imread('Bodoque.jpg')
img_trasl = trasladar(img, 100, 100)
img_rot = rotar(img, 15)
img_esc = cv.resize(img,(200,200), interpolation=cv.INTER_CUBIC)
img_flip = cv.flip(img, 1)

cv.imshow('Imagen Original',img)
cv.waitKey(0)
cv.imshow('Imagen Trasladada',img_trasl)
cv.waitKey(0)
cv.imshow('Imagen Rotada',img_rot)
cv.waitKey(0)
cv.imshow('Imagen Escalada',img_esc)
cv.waitKey(0)
cv.imshow('Imagen Escalada',img_flip)
cv.waitKey(0)
cv.destroyAllWindows()