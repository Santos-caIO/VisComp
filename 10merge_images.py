import cv2

img = cv2.imread('leao_raiva.jpg', 1)
img2 = cv2.imread('leao_rindo.jpg', 1)

img = cv2.resize(img, (250,250))
cv2.imshow('leao com raiva', img)
img2 = cv2.resize(img2, (250,250))
cv2.imshow('leao rindo', img2)

#Mescla as imagens
Mescla = cv2.addWeighted(img, 0.1, img2, 1.2,0)
cv2.imshow('Imagens mescladas', Mescla)

cv2.waitKey()
cv2.destroyAllWindows()
