import cv2
#carrega e mostra a imagem
img = cv2.imread('lena.png',1)
cv2.imshow('start', img)

#define a fonte e o texto
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'Lena', (0,150), font, 2, (255,0,0), 1)




#mostra a imagem com o texto
cv2.imshow('texto', img)
cv2.waitKey()
cv2.destroyAllWindows()