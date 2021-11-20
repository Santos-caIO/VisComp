import cv2

cap = cv2.VideoCapture('pessoas_andando.mp4')

#criando a máscara de background
mask = cv2.createBackgroundSubtractorMOG2(detectShadows = True)

while True:
    ret, frame = cap.read()

    #verifcar se o frame é nulo
    if frame is None:
        break

    fgmask = mask.apply(frame)

    cv2.imshow("frame",frame)
    cv2.imshow("maskframe", fgmask)

    #Tempo de delay para o laço ocorrer
    keyboard = cv2.waitKey(10)

    #Teclas q ou esc para sair do loop
    if keyboard == ord('q') or keyboard == 27:
        break
cap.release()
cv2.destroyAllWindows()