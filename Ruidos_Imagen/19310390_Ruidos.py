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
sp = sp_noise(img, 0.05)
#sp = random_noise(img, mode='salt', seed=None, clip=True)
#sp = random_noise(img, mode='pepper', seed=None, clip=True)
#sp = np.array(255*sp, dtype = 'uint8')
imgs = cv.hconcat([img, gauss, sp])

#Aplicado de filtro promedio
prom_norm = cv.blur(img, (4,4))
prom_gauss = cv.blur(gauss,(4,4))
prom_sp = cv.blur(sp, (4,4))
prom_fil = cv.hconcat([prom_norm, prom_gauss, prom_sp])

#Aplicado de filtro Gaussiano
gauss_norm = cv.GaussianBlur(img,(5,5),0)
gauss_gauss = cv.GaussianBlur(gauss,(5,5),0)
gauss_sp = cv.GaussianBlur(sp,(5,5),0)
gauss_fil = cv.hconcat([gauss_norm, gauss_gauss, gauss_sp])

#Aplicado de filtro Mediano
med_norm = cv.medianBlur(img,5)
med_gauss = cv.medianBlur(gauss,5)
med_sp = cv.medianBlur(sp,5)
med_fil = cv.hconcat([med_norm, med_gauss, med_sp])

#Aplicado de filtro máximo
    #creación del kernel
size = (4, 4)
shape = cv.MORPH_RECT
kernel = cv.getStructuringElement(shape, size)

max_norm = cv.dilate(img, kernel)
max_gauss = cv.dilate(gauss, kernel)
max_sp = cv.dilate(sp, kernel)
max_fil = cv.hconcat([max_norm, max_gauss, max_sp])

#Aplicado de filtro minimo
    #creación del kernel
size = (4, 4)
shape = cv.MORPH_RECT
kernel = cv.getStructuringElement(shape, size)

min_norm = cv.erode(img, kernel)
min_gauss = cv.erode(gauss, kernel)
min_sp = cv.erode(sp, kernel)
min_fil = cv.hconcat([min_norm, min_gauss, min_sp])



cv.imshow('Imagen original y con ruido', imgs)
cv.waitKey(0)
cv.imshow('Filtro promedio', prom_fil)
cv.waitKey(0)
cv.imshow('Filtro Gaussiano', gauss_fil)
cv.waitKey(0)
cv.imshow('Filtro Mediana', med_fil)
cv.waitKey(0)
cv.imshow('Filtro Maximo', max_fil)
cv.waitKey(0)
cv.imshow('Filtro Minmo', min_fil)
cv.waitKey(0)
cv.destroyAllWindows()
