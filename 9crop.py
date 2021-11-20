import cv2

#carrega e mostra a imagem
img = cv2.imread('lena.png', 1)
cv2.imshow('normal', img)

#recorta e mostra o recorte da imagem
corte = img[105:160, 105:170]
cv2.imshow('imagem cortada', corte)

cv2.waitKey()
cv2.destroyAllWindows()
