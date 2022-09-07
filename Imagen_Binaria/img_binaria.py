import cv2

imagen2 = cv2.imread('girasoles2.jpg')

alto, largo = imagen2.shape[:2]

for y in range(100,300):
    for x in range(100,300):
        b,g,r = imagen2[y,x]
        if r>182 and r<=255 and g>115 and g<247 and b>=0 and b<50:
            imagen2[y,x] = 255,255,255
        else:
            imagen2[y,x] = 0,0,0
        
imagen = cv2.imread('girasoles2.jpg')
cv2.imshow('Girasoles',imagen)
cv2.imshow('Girasoles binario',imagen2)

cv2.waitKey(0)
cv2.destroyAllWindows()

