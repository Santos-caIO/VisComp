import cv2
import numpy as np

#carrega, redimensiona e mostra a imagem
img = cv2.imread('estradacurva.jpg', 0)
img = cv2.resize(img ,(250,250))
cv2.imshow('normal', img)

#aplica o filtro de laplace utilizando uma matriz de double
estrada_lap = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('laplacian', estrada_lap)

#transforma os pixels da matriz filtrada em tipo inteiro de 8 bits e mostra a imagem
estrada_lap = np.uint8(np.absolute(estrada_lap))
cv2.imshow('laplace', estrada_lap)

cv2.waitKey()
cv2.destroyAllWindows()