import cv2
from matplotlib import pyplot as plt

#carregando a imagem
img = cv2.imread('lena.png', 1)
#cv2.imshow("cv2", img)

#pondo os canais de cores em ordem
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
"""""
# plotar imagem
plt.imshow(img)
plt.title('plot da lena')
plt.show()
"""

#conversão de canais de cor
img1 = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ)
img3 = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

#nomes para cada imagem
titulos = ['RGB', 'YCrCb', 'XYZ', 'HSV' ]

#vetor com as imagens
imagens = [img, img1, img2, img3]

#organizando a plotagem
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(imagens[i])
    plt.title(titulos[i])
    plt.xticks([]), plt.yticks([])

#mostrando o plot
plt.show()