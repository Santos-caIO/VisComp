from PIL import Image

img = Image.open('lena.png') #comando que carrega a imagem em escala de cinza para a variável img
print(img.format) #tipo da imagem
print(img.mode) #sistema de cores da imagem
print(img.getbands()) #retorna o sistema de cores
print(img.size) #tamanho da imagem
print(img.info) #dados sobre o sistema de cores, relação claro-escuro, resolução da imagem(pontos por polegadas)
print(img.getextrema()) #extremos dos valores dos pixels em cada cor do sistema de cores da imagem

coordenadas = x, y = 10, 2 #fixando as coordenadas dos pixels
print(img.getpixel(coordenadas)) #pixel referente aquelas coordenadas em relação a cada canal de cor