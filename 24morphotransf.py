import cv2
import numpy as np

#carrega, redimensiona e mostra a imagem
img = cv2.imread('images/scoobydoo.jpg', 0)
edges = cv2.Canny(img, 150, 200)
cv2.imshow('normal', edges)

#definindo o kernel e aplicando a dilatação
kernelDil = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
dilation = cv2.dilate(edges, kernelDil, iterations= 2)
cv2.imshow('dilate', dilation)

#definindo o kernel e aplicando a erosão
kernelEro = cv2.getStructuringElement(cv2.MORPH_RECT, (2,1))
image_1 = cv2.erode(edges, kernelEro)
cv2.imshow('eroded', image_1)

cv2.waitKey()
cv2.destroyAllWindows()