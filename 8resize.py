import cv2

#carrega e mostra a imagem
img = cv2.imread('lena.png',1)
cv2.imshow('normal', img)

#aumenta e mostra a imagem
img = cv2.resize(img, (500, 500))
cv2.imshow('redimensionada para maior', img)

#diminui e mostra a imagem
img = cv2.resize(img, (150,190))
cv2.imshow('redimensionada para menor', img)

cv2.waitKey()
cv2.destroyAllWindows()