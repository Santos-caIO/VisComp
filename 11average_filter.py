import cv2
import numpy as np

#carrega a imagem
img = cv2.imread('macaco_rindo.jpg', 1)

#redimensiona a imagem
img = cv2.resize(img, (240,320))

#cria uma matriz de imagens suavizadas por média com kernels de tamanhos diferentes
suavizadas = np.vstack([
np.hstack([img, cv2.blur(img, (3, 3)), cv2.blur(img, (5,5))]),
np.hstack([cv2.blur(img, (7,7)), cv2.blur(img, (9,9)), cv2.blur(img, (11,11))]),
])

#mostra as imagens
cv2.imshow("Imagens suavizadas por media", suavizadas)
cv2.waitKey()