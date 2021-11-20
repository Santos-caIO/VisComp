import cv2

img = cv2.imread('lena.png',1)
cv2.imshow('normal', img)

#cria a seta
cv2.arrowedLine(img, (0,0), (100,100), (255,0,0), 5)
cv2.imshow('seta', img)

#cria o retângulo
cv2.rectangle(img, (100,0), (225,200), (10,50,100), 1)
cv2.imshow('retângulo', img)

#cria o círculo
cv2.circle(img, (80,100), 10, (0,255,0),2)
cv2.imshow('circle',img)

cv2.waitKey()
cv2.destroyAllWindows()