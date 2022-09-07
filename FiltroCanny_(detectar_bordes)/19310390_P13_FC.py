import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo abrir la camara.")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo recibir el frame. Saliendo...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(frame,100,100)

    cv.imshow('Original', frame)
    cv.imshow('Canny', canny)
    
    if cv.waitKey(1) == ord('s'):
        break

cap.release()
cv.destroyAllWindows()