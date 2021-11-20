import cv2

#carrega, redimensiona e mostra a imagem
img = cv2.imread('estradacurva.jpg', 0)
img = cv2.resize(img, (250,250))
cv2.imshow('normal', img)

#aplica o filtro gaussiano na imagem e mostra
img = cv2.GaussianBlur(img, (9,9), 0)
cv2.imshow('gaussiano', img)

#aplica o detector de bordas Canny na imagem e mostra
estrada_canny = cv2.Canny(img, 30, 150)
cv2.imshow('canny', estrada_canny)

cv2.waitKey()
cv2.destroyAllWindows()