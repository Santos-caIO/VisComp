import cv2

img = cv2.imread('lena.png',1)#carrega a imagem em escala de cinza

cv2.imshow('image',img) #mostra a imagem em uma nova janela
cv2.waitKey(0) #duração em milissegundos que a janela vai ficar aberta
cv2.destroyAllWindows() #fecha todas as janelas abertas durante a execução do código

cv2.imwrite('lena_copia.png',img) #salva a imagem na pasta do projeto

