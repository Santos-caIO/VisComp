import cv2
import numpy as np

#cria o método para o evento de clique
def click_event(event, x, y, flags, param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print(x,' , ', y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = str(x) + ' , ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 0.8, (0,255,0), 2)
        cv2.imshow('imagem', img)

#cria e mostra uma imagem escura
img = np.zeros((500,500,3), np.uint8)
cv2.imshow('imagem', img)

#recebe o retorno do mouse
cv2.setMouseCallback('imagem', click_event)

cv2.waitKey()
cv2.destroyAllWindows()