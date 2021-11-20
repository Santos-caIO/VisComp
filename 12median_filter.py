import cv2
import numpy as np

#carrega a imagem
img = cv2.imread('macaco_rindo.jpg', 1)

#redimensiona a imagem
img = cv2.resize(img, (240,320))

#cria uma matriz de imagens suavizadas por mediana com kernels de tamanhos diferentes
suavizadas = np.vstack([
np.hstack([img, cv2.medianBlur(img, 3), cv2.medianBlur(img, 5)]),
np.hstack([cv2.medianBlur(img, 7), cv2.medianBlur(img, 9), cv2.medianBlur(img, 11)]),
])

#mostra a imagem
cv2.imshow("Imagens suavizadas por mediana", suavizadas)
cv2.waitKey()