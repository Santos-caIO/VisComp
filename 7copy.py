import cv2

#carrega e mostra a imagem
img = cv2.imread('sol.jpg')
cv2.imshow('normal', img)

#copia parte da imagem para a variável sol
sol = img[56:106, 110:160]

#coloca a parte extraída na própria imagem
img[40:90, 50:100] = sol

#mostra a imagem
cv2.imshow('com_copia', img)

cv2.waitKey()
cv2.destroyAllWindows()