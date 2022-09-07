import cv2 as cv
import numpy as np
import random
from skimage.util import random_noise

def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

#Lectura de imagen e implementación de ruidos
img = cv.imread('girasoles.jpg', 1)
gauss = random_noise(img, mode='gaussian', seed=None, clip=True)
gauss = np.array(255*gauss, dtype = 'uint8')
sp = cv.imread('girasoles_sp.jpg')
#sp = sp_noise(img, 0.05)
#sp = random_noise(img, mode='salt', seed=None, clip=True)
#sp = random_noise(img, mode='pepper', seed=None, clip=True)
#sp = np.array(255*sp, dtype = 'uint8')
imgs = cv.hconcat([img, gauss, sp])

#Aplicado de filtro promedio (de la media)
prom_norm = cv.blur(img, (4,4))
prom_gauss = cv.blur(gauss,(4,4))
prom_sp = cv.blur(sp, (4,4))
prom_fil = cv.hconcat([prom_norm, prom_gauss, prom_sp])

#Aplicado de filtro Gaussiano
gauss_norm = cv.GaussianBlur(img,(5,5),0)
gauss_gauss = cv.GaussianBlur(gauss,(5,5),0)
gauss_sp = cv.GaussianBlur(sp,(5,5),0)
gauss_fil = cv.hconcat([gauss_norm, gauss_gauss, gauss_sp])


cv.imshow('Imagen original y con ruido', imgs)
cv.waitKey(0)
cv.imshow('Filtro promedio (de la media)', prom_fil)
cv.waitKey(0)
cv.imshow('Filtro Gaussiano', gauss_fil)
cv.waitKey(0)
cv.destroyAllWindows()