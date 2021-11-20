import cv2

##importa as características pré-processadas da vista frontal de uma face
caracteristicas_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#carrega o vídeo
cap = cv2.VideoCapture('pessoas_parque.mp4')

while cap.isOpened():
    (retorno, video) = cap.read() #lista com uma variável de sucesso e com cada frame do video
    video = cv2.resize(video,(480,360)) #redimensiona para acelerar o processamento
    video_cinza = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY) #atribui a uma variável os frames em tons de cinza
    faces = caracteristicas_face.detectMultiScale(video_cinza) #aplica o detector de faces

    #desenha um retângulo em cada face detectada
    for(x,y,w,h) in faces:
        cv2.rectangle(video, (x,y), (x+w,y+h), (0,0,255),4)

        quantidade = str( faces.shape[0])
        cv2.putText(video, "Quantidade de faces:" + quantidade, (20, 350), cv2.FONT_HERSHEY_COMPLEX, 1,(255,0,0),2)

    #mostra o vídeo
    cv2.imshow('faces detectadas', video)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
