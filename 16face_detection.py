import cv2

#importa as características pré-processadas da vista frontal de uma face
caracteristicas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#carrega a imagem e põe em tons de cinza
img = cv2.imread('elenco_theboys.jpg', 0)
#img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Aplica o detector
faces = caracteristicas.detectMultiScale(img)

#Desenha um retângulo em cada face detectada
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 4)

#mostra a imagem
cv2.imshow('faces detectadas', img)

cv2.waitKey()
cv2.destroyAllWindows()