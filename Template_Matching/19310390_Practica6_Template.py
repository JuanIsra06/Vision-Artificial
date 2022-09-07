import cv2 as cv
from matplotlib import pyplot as plt


#img = cv.resize(cv.imread('perro.jpg',0), (0,0), fx=0.35, fy=0.35)
#temp = cv.resize(cv.imread('temp_perro.jpg',0), (0,0), fx=0.35, fy=0.35)

img = cv.imread('abeja.jpg')
temp = cv.imread('temp_abeja.jpg')

#img = cv.imread('girasoles.jpg')
#temp = cv.imread('temp_girasoles2.jpg')

#img = cv.imread('personas.jpg')
#temp = cv.imread('temp_personas.jpg')

alto, largo = temp.shape[:2]

methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
            cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]



for method in methods:
    img2 = img.copy()
    res = cv.matchTemplate(img, temp, method)
    v_min, v_max, l_min, l_max = cv.minMaxLoc(res)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        ubi = l_min
    else:
        ubi = l_max

    inf_der = (ubi[0] + largo, ubi[1] + alto)
    cv.rectangle(img2, ubi, inf_der, (255, 0, 150), 3)

    plt.figure(figsize=(8,4))
    plt.imshow(res, cmap='gray')

    cv.imshow('Imagen', img2)
    cv.imshow('Template', temp)
    plt.show()

    cv.waitKey(0)
    cv.destroyAllWindows()