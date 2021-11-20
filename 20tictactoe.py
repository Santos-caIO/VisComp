import cv2
import numpy as np
from matplotlib import pyplot as plt
#Desenhando o jogo na folha
folha= np.empty([400,400,3],dtype=np.uint8)
folha.fill(255)
cv2.line(folha,(150,50),(150,350),(0,0,0),4)
cv2.line(folha,(250,50),(250,350),(0,0,0),4)
cv2.line(folha,(50,150),(350,150),(0,0,0),4)
cv2.line(folha,(50,250),(350,250),(0,0,0),4)

#Criando o X
X = np.empty([50,50,3], dtype=np.uint8)
X.fill(255)
cv2.line(X,(0,0),(50,50),(0,0,0),3)
cv2.line(X,(0,50),(50,0),(0,0,0),3)

#Elemento circulo deve ser colocado levando em conta o centro do local e com raio 25

#Elemento X deve ser colocado de acordo com a variação dos pixels horizontais e dos verticais no local

#Jogadas
#parâmetros do circulo: local, centro, raio, cor, espessura
cv2.circle(folha, (100,200), 25, (0,0,0), 3)

#parâmetros do X: escolher o quadrado onde o X vai ser inserido
folha[75:125, 75:125] = X #varre primeiro a dimensão vertical

cv2.circle(folha, (200,200), 25, (0,0,0), 3)
folha[275:325, 275:325] = X
cv2.circle(folha, (300,200), 25, (0,0,0), 3)
folha[275:325, 175:225] = X



#mostrar o jogo
plt.imshow(folha)
plt.title("Jogo da velha")
plt.show()