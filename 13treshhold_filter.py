import cv2

#carrega e mostra a imagem
img = cv2.imread('lena.png', 0)
cv2.imshow('normal', img)

#aplica e mostra as limiarizações normal e inversa
ret, t1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
cv2.imshow('limiar',t1)
ret, t2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('limiar inverso', t2)


cv2.waitKey()
cv2.destroyAllWindows()